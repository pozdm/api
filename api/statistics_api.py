import datetime
from fastapi import APIRouter, Response, Query
from starlette.responses import Response

from utils import users_stats, utm_stats, views_stats, subscribers_stats, chats_stats
from utils.other import return_json

router = APIRouter(prefix="/statistics", tags=["statistics"])


yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = yesterday - datetime.timedelta(days=1)

start_date_q = Query(day_before_yesterday, min_length=10, max_length=10, example="yyyy-mm-dd")
end_date_q = Query(yesterday, min_length=10, max_length=10, example="yyyy-mm-dd")


@router.get("/users_stats/")
async def get_users_stats(start_date: str = start_date_q,
                          end_date: str = end_date_q):

    users_stat_for_start_date = await users_stats.get_users_for_date(start_date)
    users_stat_for_end_date = await users_stats.get_users_for_date(end_date)

    if users_stat_for_start_date is None or users_stat_for_end_date is None:
        return Response(status_code=204)

    return return_json(users_stat_for_start_date, users_stat_for_end_date)


@router.get("/utm_stats/")
async def get_utm_stats(start_date: str = start_date_q,
                        end_date: str = end_date_q):

    utm_for_start_date = await utm_stats.get_utm_stats_for_date(start_date)
    utm_for_end_date = await utm_stats.get_utm_stats_for_date(end_date)

    if utm_for_start_date is None or utm_for_end_date is None:
        return Response(status_code=204)

    return return_json(utm_for_start_date, utm_for_end_date)


@router.get("/views_stats/")
async def get_views_stats(start_date: str = start_date_q,
                          end_date: str = end_date_q):

    views_for_start_date = await views_stats.get_views_by_services(start_date)
    views_for_end_date = await views_stats.get_views_by_services(end_date)

    if views_for_start_date is None or views_for_end_date is None:
        return Response(status_code=204)

    return return_json(views_for_start_date, views_for_end_date)


@router.get("/subscribers_stats/")
async def get_subscribers_stats(start_date: str = start_date_q,
                                end_date: str = end_date_q):

    subscriptions_for_start_date = await subscribers_stats.get_subscriptions_for_date(start_date)
    subscriptions_for_end_date = await subscribers_stats.get_subscriptions_for_date(end_date)

    if subscriptions_for_start_date is None or subscriptions_for_end_date is None:
        return Response(status_code=204)

    return return_json(subscriptions_for_start_date, subscriptions_for_end_date)


@router.get("/chats_stats/")
async def get_chats_stats(start_date: str = start_date_q,
                          end_date: str = end_date_q):

    chats_for_start_date = await chats_stats.get_chats_stats_for_date(start_date)
    chats_for_end_date = await chats_stats.get_chats_stats_for_date(end_date)

    if chats_for_start_date is None or chats_for_end_date is None:
        return Response(status_code=204)

    return return_json(chats_for_start_date, chats_for_end_date)
