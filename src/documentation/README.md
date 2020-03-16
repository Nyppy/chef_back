Сераер Chief Street предоставляет услуги заказа еды.

Для того чтобы оформить зазказ с клиентской части програмного обеспечения, необходимо:

- Отправить HTTP запрос, методом POST
- относительный url - api/order/
- тело запроса:

    ```
    {
            'address', 'apartment',
            'price', 'phone', 'food'
     }
     ```

- статус ответа - 201

Пример запроса:

```
{
    'address': "г. Пермь ул. Фрунзе д. 9",
    'apartment': "кв. 105",
    'price': "1259.00",
    'phone': "+79520392260",
    'food': "Ризотто"
}
```

Пример ответа:

```
{
    "id": 6,
    "price": "1259.00",
    "food": "Ризотто"
}
```