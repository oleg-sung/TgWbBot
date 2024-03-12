from pprint import pprint

import requests


async def get_item_by_articyl(articyl: int) -> dict | str:
    response = requests.get(
        f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={articyl}"
    )
    if response.status_code == 200:
        response_data = response.json()
        if not response_data["data"]["products"]:
            return f"⚠ Товар по артилем {articyl} не найден ⚠.\nПроверте корректность артикль!"
        data = response.json()["data"]["products"][0]
        qty = 0
        for size in data["sizes"]:
            qty += sum([stock["qty"] for stock in size["stocks"]])
        return {
            "name": data["name"],
            "id": data["id"],
            "price": data["salePriceU"],
            "rating": data["reviewRating"],
            "qty": qty,
        }


async def validate_articyl(atr: str):
    if not atr.isnumeric():
        return "❌ Артикул должен состоять только из цифр ❌"
    if len(atr) != 9:
        return "❌ Артикул тавара должен состоять из 9 цифр ❌"
    return atr
