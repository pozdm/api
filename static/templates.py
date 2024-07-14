stats_day_form = """\
<strong><a href="https://analytics.spb.yazzh.ru/d/F6JYhx64z/vk-dashboard?orgId=1&refresh=1m">📈
Ежедневная статистика по аудитории ЯЗЖ за {td}:</a></strong>

<strong>Всего пользователей (с декабря 2022): {} {user_d[1]}</strong>

<strong>Пользователей: {uniqe_u[0]} {uniqe_u[1]}</strong>
<strong>Просмотров: {user_day[0]} {user_day[1]}</strong>

<strong>UTM term:</strong>
{utm}

<strong>Просмотры по сервисам:</strong>
{result_change}

<strong>Подписки на уведомления: </strong>
Telegram: {subscribers_tg[0]} ({subscribers_tg[1]})
VK: {subscribers_vk[0]} ({subscribers_vk[1]})
Всего (уникальных): {subscribers_total[0]} ({subscribers_total[1]})

<strong>Домовые чаты (пилот):</strong>
Всего чатов: {chats_count}
Всего участников: {chats_users_sum}
Всего сообщений: {chats_mes_sum}

<a href="https://disk.yandex.ru/i/IJ5zJCq9SjwchA">❓\
Если возникли вопросы "как считали?", пожалуйста, ознакомьтесь со справкой</a>"""