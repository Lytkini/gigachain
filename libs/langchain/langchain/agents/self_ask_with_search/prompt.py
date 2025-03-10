# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

_DEFAULT_TEMPLATE = """Вопрос: Кто прожил дольше, Мухаммед Али или Алан Тьюринг?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Сколько лет было Мухаммеду Али, когда он умер?
Промежуточный ответ: Мухаммед Али умер в возрасте 74 лет.
Дополнительный вопрос: Сколько лет было Алану Тьюрингу, когда он умер?
Промежуточный ответ: Алан Тьюринг умер в возрасте 41 года.
Итак, окончательный ответ: Мухаммед Али

Вопрос: Когда родился основатель craigslist?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Кто был основателем craigslist?
Промежуточный ответ: Craigslist был основан Крейгом Ньюмарком.
Дополнительный вопрос: Когда родился Крейг Ньюмарк?
Промежуточный ответ: Крейг Ньюмарк родился 6 декабря 1952 года.
Итак, окончательный ответ: 6 декабря 1952 года

Вопрос: Кто был материнским дедом Джорджа Вашингтона?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Кто была мать Джорджа Вашингтона?
Промежуточный ответ: Мать Джорджа Вашингтона была Мэри Болл Вашингтон.
Дополнительный вопрос: Кто был отцом Мэри Болл Вашингтон?
Промежуточный ответ: Отцом Мэри Болл Вашингтон был Джозеф Болл.
Итак, окончательный ответ: Джозеф Болл

Вопрос: Оба ли режиссера фильмов "Челюсти" и "Казино Рояль" из одной страны?
Нужны ли здесь дополнительные вопросы: Да.
Дополнительный вопрос: Кто является режиссером фильма "Челюсти"?
Промежуточный ответ: Режиссером фильма "Челюсти" является Стивен Спилберг.
Дополнительный вопрос: Откуда Стивен Спилберг?
Промежуточный ответ: Соединенные Штаты.
Дополнительный вопрос: Кто является режиссером фильма "Казино Рояль"?
Промежуточный ответ: Режиссером фильма "Казино Рояль" является Мартин Кэмпбелл.
Дополнительный вопрос: Откуда Мартин Кэмпбелл?
Промежуточный ответ: Новая Зеландия.
Итак, окончательный ответ: Нет

Вопрос: {input}
Нужны ли здесь дополнительные вопросы:{agent_scratchpad}"""
PROMPT = PromptTemplate(
    input_variables=["input", "agent_scratchpad"], template=_DEFAULT_TEMPLATE
)
