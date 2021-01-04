
def PulsePerHZ(r, x, v, ppr, f) :
    # Pulse Per HZ
    # Velcity[m/s] -> Pulse per HZ 
    # 제어주기 당 펄스가 얼마나 나오는지 확인할 때 사용하는 함수
    # 목표 속도 v[m/s], 바퀴반지름 r[m], 축 한바퀴당 펄스 수 ppr, 체배 x, 제어주파수 f [
 
    return v*1/(2*3.141592*r) * ppr * x / f


def vel2rpm(v, r) :
    # r은 바퀴 반지름 [m]
    # velocity -> RPM
    # Velocity [m/s] -> RPM
    # v 속도는 몇 rpm일까?

    return v / (2 * 3.141592 * r) * 60 

def rpm2vel(rpm, r) : 
    # R은 m
    # RPM -> vel [m/s]
    # rpm은 몇 vel일까?
    return rpm * 2 * PI * r / 60 
