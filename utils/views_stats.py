from sqlalchemy import select, func

from db.models import VKModel
from db.session import open_session


services_names = {
    "/my_home":           "Мой дом",
    "/monument_building": "Мой дом / Дом-памятник",
    "/falsification":     "Мой дом / Фальсификация",
    "/our_spb":           "Сообщения по ЖКХ",
    "/beautiful_places":  "Красивые места",
    "/billboard_event":   "Афиша событий",
    "/kindergartens":     "Детские сады",
    "/i_parent":          "Я родитель",
    "/road_cleaning":     "Уборка дорог",
    "/ecology":           "Раздельный сбор",
    "/blockade":          "Блокада Ленинграда",
    "/sports_ground":     "Спортивный город",
    "/pets":              "Мой питомец",
    "/news":              "Новости",
    "/street_vending":    "Торговля и услуги",
    "/":                  "Главная страница",
    "/pensioners":        "Активное долголетие",
    "/about_us":          "О нас",
    "/chat_bot":          "Чат-бот",
    "/profile":           "Профиль",
    "/reference":         "Cправочная",
    "/section":           "Я родитель / Развитие",
    "/city_development":  "Развитие территорий",
}


@open_session
async def get_views_by_services(session, date: str, developers: list = []) -> dict[str: int] | None:
    query = select(
        VKModel.event_name, func.count(VKModel.user_id)
    ).filter(
        VKModel.user_id.not_in(developers)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    ).group_by(
        VKModel.event_name
    )

    result = await session.execute(query)
    result = result.mappings()

    res = {}

    for service in result:
        if (name := service["event_name"]) in services_names:
            res[services_names[name]] = service["count"]

    if not res:
        return None

    return res



