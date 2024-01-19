from django.urls import path
from .views import fortune_form, enfj_detail, enfp_detail, entj_detail, entp_detail, esfj_detail, esfp_detail, estj_detail, estp_detail, infj_detail, infp_detail, intj_detail, intp_detail, isfj_detail, isfp_detail, istj_detail, istp_detail


urlpatterns = [
    path('', fortune_form, name='home'),  # 루트 URL
    path('fortune/', fortune_form, name='fortune_form'),
    path('enfj/', enfj_detail, name='enfj_detail'),
    path('enfp/', enfp_detail, name='enfp_detail'),
    path('entj/', entj_detail, name='entj_detail'),
    path('entp/', entp_detail, name='entp_detail'),
    path('esfj/', esfj_detail, name='esfj_detail'),
    path('esfp/', esfp_detail, name='esfp_detail'),
    path('estj/', estj_detail, name='estj_detail'),
    path('estp/', estp_detail, name='estp_detail'),
    path('infj/', infj_detail, name='infj_detail'),
    path('infp/', infp_detail, name='infp_detail'),
    path('intj/', intj_detail, name='intj_detail'),
    path('intp/', intp_detail, name='intp_detail'),
    path('isfj/', isfj_detail, name='isfj_detail'),
    path('isfp/', isfp_detail, name='isfp_detail'),
    path('istj/', istj_detail, name='istj_detail'),
    path('istp/', istp_detail, name='istp_detail'),
]