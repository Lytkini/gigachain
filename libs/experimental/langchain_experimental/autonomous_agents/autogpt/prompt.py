import time
from typing import Any, Callable, List

from langchain.prompts.chat import (
    BaseChatPromptTemplate,
)
from langchain.schema.messages import BaseMessage, HumanMessage, SystemMessage
from langchain.schema.vectorstore import VectorStoreRetriever
from langchain.tools.base import BaseTool

from langchain_experimental.autonomous_agents.autogpt.prompt_generator import get_prompt
from langchain_experimental.pydantic_v1 import BaseModel


class AutoGPTPrompt(BaseChatPromptTemplate, BaseModel):
    """Prompt for AutoGPT."""

    ai_name: str
    ai_role: str
    tools: List[BaseTool]
    token_counter: Callable[[str], int]
    send_token_limit: int = 4196

    def construct_full_prompt(self, goals: List[str]) -> str:
        prompt_start = (
            "Ваши решения всегда должны приниматься независимо, "
            "без привлечения помощи пользователя.\n"
            "Играйте на своих сильных сторонах как LLM и преследуйте простые "
            "стратегии без юридических сложностей.\n"
            "Если вы выполнили все свои задачи, обязательно "
            'используйте команду "завершить".'
        )
        # Construct full prompt
        full_prompt = f"Вы {self.ai_name}, {self.ai_role}\n{prompt_start}\n\nЦЕЛИ:\n\n"
        for i, goal in enumerate(goals):
            full_prompt += f"{i+1}. {goal}\n"

        full_prompt += f"\n\n{get_prompt(self.tools)}"
        return full_prompt

    def format_messages(self, **kwargs: Any) -> List[BaseMessage]:
        system_content = self.construct_full_prompt(kwargs["goals"])
        system_content += f"\n\nТекущее время и дата {time.strftime('%c')}"

        # base_prompt =
        #   SystemMessage(content=self.construct_full_prompt(kwargs["goals"]))
        # time_prompt = SystemMessage(
        #     content=f"Текущее время и дата {time.strftime('%c')}"
        # )
        # used_tokens = self.token_counter(base_prompt.content) + self.token_counter(
        #     time_prompt.content
        # )
        used_tokens = self.token_counter(system_content)

        memory: VectorStoreRetriever = kwargs["memory"]
        previous_messages = kwargs["messages"]
        relevant_docs = memory.get_relevant_documents(str(previous_messages[-10:]))
        relevant_memory = [d.page_content for d in relevant_docs]
        relevant_memory_tokens = sum(
            [self.token_counter(doc) for doc in relevant_memory]
        )
        while used_tokens + relevant_memory_tokens > 2500:
            relevant_memory = relevant_memory[:-1]
            relevant_memory_tokens = sum(
                [self.token_counter(doc) for doc in relevant_memory]
            )
        if len(relevant_memory) > 0:
            content = (
                "\n\n"
                f"Это напоминает тебе о следующих событиях "
                f"из вашего прошлого:\n{relevant_memory}\n\n"
            )
            # memory_message = SystemMessage(content=content_format)
            system_content += content
            used_tokens += self.token_counter(content)
        historical_messages: List[BaseMessage] = []
        for message in previous_messages[-10:][::-1]:
            message_tokens = self.token_counter(message.content)
            if used_tokens + message_tokens > self.send_token_limit - 1000:
                break
            historical_messages = [message] + historical_messages
            used_tokens += message_tokens
        input_message = HumanMessage(content=kwargs["user_input"])
        messages: List[BaseMessage] = [SystemMessage(content=system_content)]
        messages += historical_messages
        messages.append(input_message)
        return messages
