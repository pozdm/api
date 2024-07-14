import uvicorn
from fastapi import APIRouter

from utils import general_stats, utm_stats, views_stats, subscribers_stats, chats_stats

router = APIRouter(prefix="/statistics", tags=["statistics"])


@router.get("/general_stats/")
async def get_general_stats(date: str) -> dict:
    total_users = await general_stats.get_users_before_date(date)
    users = await general_stats.get_users_for_date(date)
    views = await general_stats.get_views_for_date(date)

    return {
        "total_users": total_users,
        "users_for_day": users,
        "views_for_day": views
    }


@router.get("/utm_stats/")
async def get_utm_stats(date: str) -> dict:
    utm = await utm_stats.get_utm_stats_for_date(date)
    return utm


@router.get("/views_stats/")
async def get_views_stats(date: str) -> dict:
    views = await views_stats.get_views_by_services(date)
    return views


@router.get("/subscribers_stats/")
async def get_subscribers_stats(date: str) -> dict:
    subscriptions = await subscribers_stats.get_subscriptions_for_date(date)
    return subscriptions


@router.get("/chats_stats/")
async def get_chats_stats(date: str) -> dict:
    chats = await chats_stats.get_chats_stats_for_date(date)
    return chats
