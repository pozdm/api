from fastapi import APIRouter, Response, Query

from utils import users_stats, utm_stats, views_stats, subscribers_stats, chats_stats
from utils.other import sorted_dict

router = APIRouter(prefix="/statistics", tags=["statistics"])


def return_json(start_result: dict, end_result: dict) -> dict:
    keys = set()
    delta = dict()

    if isinstance(start_result, dict) and isinstance(end_result, dict):
        keys.update(start_result.keys())
        keys.update(end_result.keys())

        for key in keys:
            if key not in start_result:
                delta[key] = end_result[key]
            elif key not in end_result:
                delta[key] = -start_result[key]
            else:
                delta[key] = end_result[key] - start_result[key]

    return {
        "result_for_start_day": sorted_dict(start_result),
        "result_for_end_day": sorted_dict(end_result),
        "delta": sorted_dict(delta)
    }


@router.get("/users_stats/")
async def get_users_stats(start_date: str, end_date: str) -> dict:
    users_stat_for_start_date = await users_stats.get_users_for_date(start_date)
    users_stat_for_end_date = await users_stats.get_users_for_date(end_date)

    return return_json(users_stat_for_start_date, users_stat_for_end_date)


@router.get("/utm_stats/")
async def get_utm_stats(start_date: str, end_date: str):
    utm_for_start_date = await utm_stats.get_utm_stats_for_date(start_date)
    utm_for_end_date = await utm_stats.get_utm_stats_for_date(end_date)

    if utm_for_start_date is None or utm_for_end_date is None:
        return Response(status_code=204)

    return return_json(utm_for_start_date, utm_for_end_date)


@router.get("/views_stats/")
async def get_views_stats(start_date: str, end_date: str):
    views_for_start_date = await views_stats.get_views_by_services(start_date)
    views_for_end_date = await views_stats.get_views_by_services(end_date)

    if views_for_start_date is None or views_for_end_date is None:
        return Response(status_code=204)

    return return_json(views_for_start_date, views_for_end_date)


@router.get("/subscribers_stats/")
async def get_subscribers_stats(start_date: str, end_date: str):
    subscriptions_for_start_date = await subscribers_stats.get_subscriptions_for_date(start_date)
    subscriptions_for_end_date = await subscribers_stats.get_subscriptions_for_date(end_date)

    if subscriptions_for_start_date is None or subscriptions_for_end_date is None:
        return Response(status_code=204)

    return return_json(subscriptions_for_start_date, subscriptions_for_end_date)


@router.get("/chats_stats/")
async def get_chats_stats(start_date: str, end_date: str):
    chats_for_start_date = await chats_stats.get_chats_stats_for_date(start_date)
    chats_for_end_date = await chats_stats.get_chats_stats_for_date(end_date)

    if chats_for_start_date is None or chats_for_end_date is None:
        return Response(status_code=204)

    return return_json(chats_for_start_date, chats_for_end_date)
