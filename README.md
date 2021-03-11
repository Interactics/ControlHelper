# ControlHelper
Motor Control Design Helper
모터 제어할때 도움이 되는 함수들 정리


# 모터 제어 도우미들
Pulse Per HZ

Velcity[m/s] -> Pulse per HZ

제어주기 당 펄스가 얼마나 나오는지 확인할 때 사용하는 함수,

    목표 속도 v[m/s], 바퀴반지름 r[m], 축 한바퀴당 펄스 수 ppr, 체배 x, 제어주기 f
    PulsePerHZ(r, x, v, ppr, f)

# 도움이 되는 상수

- rad2deg : 57.29578049

- deg2rad : 0.01745329222 
