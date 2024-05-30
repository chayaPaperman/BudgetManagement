from app.services import user_service, operation_service
import matplotlib.pyplot as plt
import io
from fastapi.responses import StreamingResponse


async def get_users_balance():
    """
    A function that returns a bar graph describing the users' balances
    :return:A picture of the graph
    """
    users = await user_service.get_all_users()
    users_names = []
    users_balance = []
    for u in users:
        users_names.append(u['name'])
        users_balance.append(await operation_service.get_balance(u['id']))
    plt.bar(users_names, users_balance, color='red')
    plt.title('Users Balance Bar Graph')
    plt.xlabel('Users')
    plt.ylabel('Balance')
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()
    return StreamingResponse(io.BytesIO(img_bytes.read()), media_type="image/png")


async def get_user_balance(user_id):
    """
    A function that returns a bar graph describing the user's budget according to months
    :param user_id: the id of the user
    :return:A picture of the graph
    """

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = []
    for i in x:
        y.append(await operation_service.get_user_balance_by_month(user_id, i))
    plt.style.use('fast')
    plt.plot(x, y)
    plt.title('User Balance Graph')
    plt.xlabel('Users')
    plt.ylabel('Balance')
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()
    return StreamingResponse(io.BytesIO(img_bytes.read()), media_type="image/png")
