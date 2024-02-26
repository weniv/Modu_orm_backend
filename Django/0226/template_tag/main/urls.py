from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print("index호출")
    print(f"request: {request}")
    print(f"request: {dir(request)}")
    print(f"request.GET: {request.GET}")
    print(f'request.GET.get("q"): {request.GET.get("q")}')
    print(f'request.GET.get("test"): {request.GET.get("test")}')
    return HttpResponse("Hello, world!")


# get test
# http://127.0.0.1:8000/?q=hello
# http://127.0.0.1:8000/?q=hello&test=world
# http://127.0.0.1:8000/?q=hello&test=world&test2=world2


def template_tag(request):
    mock_data = [
        {
            "_id": "40ed5f5d-1479-4cff-A8db-50cd925358d1",
            "index": "1",
            "name": "탁민재",
            "email": "user-okckofi@molestie.net",
            "phone": "010-3275-8617",
            "country": "감비아",
            "address": "용두동 86-3",
            "job": "메이크업아티스트",
            "age": "29",
        },
        {
            "_id": "c802171f-5661-43d8-C146-29d60cb097ab",
            "index": "2",
            "name": "류정민",
            "email": "user-98i0esc@Ornare.com",
            "phone": "010-7740-8505",
            "country": "칠레",
            "address": "성동로 89-4",
            "job": "메이크업아티스트",
            "age": "61",
        },
        {
            "_id": "8f605ef8-98fe-43ab-A234-e7882745254e",
            "index": "3",
            "name": "대재은",
            "email": "user-rj5sqf1@finibus.com",
            "phone": "010-2930-6436",
            "country": "가나",
            "address": "공덕로 9-3",
            "job": "은행출납사무원",
            "age": "30",
        },
        {
            "_id": "63d288ca-81ee-4689-Af9d-e3d20e8a8b2e",
            "index": "4",
            "name": "등예건",
            "email": "user-0crjbbk@montes.io",
            "phone": "010-6523-7033",
            "country": "세인트루시아",
            "address": "행운동 87-5",
            "job": "국제회의전문가",
            "age": "57",
        },
        {
            "_id": "acb7bc4b-b99e-4cff-Cd1f-ce14b4572773",
            "index": "5",
            "name": "담누리",
            "email": "user-ay8ycrv@Nam.co.kr",
            "phone": "010-6276-4787",
            "country": "수리남",
            "address": "잠원로 25-9",
            "job": "영화감독",
            "age": "47",
        },
        {
            "_id": "488f4267-3f06-432f-B3bd-7f9f5f793a5e",
            "index": "6",
            "name": "동진성",
            "email": "user-k285yz7@sagittis.biz",
            "phone": "010-4826-4141",
            "country": "그레나다",
            "address": "서소문로 76-7",
            "job": "심리학연구원",
            "age": "53",
        },
        {
            "_id": "ba473db8-1d12-4241-Ce5c-66348452eec9",
            "index": "7",
            "name": "근승리",
            "email": "user-a1txn3z@tempus.io",
            "phone": "010-2148-4195",
            "country": "앤티가 바부다",
            "address": "대림로 35-6",
            "job": "로봇연구원",
            "age": "20",
            "contents": "각급 선거관리위원회의 조직·직무범위 기타 필요한 사항은 법률로 정한다. 국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다. 국회의원의 수는 법률로 정하되, 200인 이상으로 한다.\n\n\n대통령이 임시회의 집회를 요구할 때에는 기간과 집회요구의 이유를 명시하여야 한다. 이 헌법공포 당시의 국회의원의 임기는 제1항에 의한 국회의 최초의 집회일 전일까지로 한다.",
        },
    ]
    context = {"mock_data": mock_data}
    return render(request, "template_tag.html", context)


urlpatterns = [
    path("", index),
    path("template/", template_tag),
]
