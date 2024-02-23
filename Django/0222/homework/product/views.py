from django.shortcuts import render

product_db = [
    {
        "id": 1,
        "name": "product1",
        "price": 1000,
        "description": "This is product1",
        "image": "product1.jpg",
        "sale_count": 100,
        "star_rating": 4,
    },
    {
        "id": 2,
        "name": "product2",
        "price": 2000,
        "description": "This is product2",
        "image": "product2.jpg",
        "sale_count": 200,
        "star_rating": 3,
    },
    {
        "id": 3,
        "name": "product3",
        "price": 3000,
        "description": "This is product3",
        "image": "product3.jpg",
        "sale_count": 300,
        "star_rating": 5,
    },
    {
        "id": 4,
        "name": "product4",
        "price": 4000,
        "description": "This is product4",
        "image": "product4.jpg",
        "sale_count": 400,
        "star_rating": 4,
    },
    {
        "id": 5,
        "name": "product5",
        "price": 5000,
        "description": "This is product5",
        "image": "product5.jpg",
        "sale_count": 500,
        "star_rating": 3,
    },
    {
        "id": 6,
        "name": "product6",
        "price": 6000,
        "description": "This is product6",
        "image": "product6.jpg",
        "sale_count": 600,
        "star_rating": 5,
    },
    {
        "id": 7,
        "name": "product7",
        "price": 7000,
        "description": "This is product7",
        "image": "product7.jpg",
        "sale_count": 700,
        "star_rating": 4,
    },
    {
        "id": 8,
        "name": "product8",
        "price": 8000,
        "description": "This is product8",
        "image": "product8.jpg",
        "sale_count": 800,
        "star_rating": 3,
    },
    {
        "id": 9,
        "name": "product9",
        "price": 9000,
        "description": "This is product9",
        "image": "product9.jpg",
        "sale_count": 900,
        "star_rating": 5,
    },
]


def product_index(request):
    # DB 쿼리 최적화를 나중에 알려드릴 예정입니다.
    # 기본적으로는 DB 쿼리를 최소화하는 것이 좋습니다.
    # 결과 값 자체도 최소화를 해야 합니다.

    # filter => select * from product where sale_count > 100 # 먼저 최소화를 시키고
    # order_by => select * from product order by sale_count desc # 정렬을 시키고
    # limit => select * from product limit 6 # 결과값

    sorted_product = sorted(product_db, key=lambda x: x["sale_count"], reverse=True)[:6]

    # sorted_product에 star_rating은 3 => [0, 1, 2]와 같은 형태로 변경하여 context로 함께 전달합니다.
    for product in sorted_product:
        product["star_rating"] = list(range(product["star_rating"]))

    context = {"product_db": sorted_product}
    return render(request, "product/index.html", context)


def product_detail(request, pk):
    context = {"product": product_db[pk - 1]}
    return render(request, "product/detail.html", context)
