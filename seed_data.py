from app import create_app, db
from app.models import Country, Station, Route, RouteStation, TravelPass, PassRoute, TouristSpot, Favorite

app = create_app()

with app.app_context():
    # 국가 데이터 추가
    korea = Country(id=1, name='South Korea', languages=["Korean", "English"])
    japan = Country(id=2, name='Japan', languages=["Japanese", "English"])
    db.session.add_all([korea, japan])

    # 역 데이터 추가
    seoul_station = Station(id=1, name='서울역', latitude=37.554722, longitude=126.970833, country_id=1)
    tokyo_station = Station(id=2, name='도쿄역', latitude=35.681236, longitude=139.767125, country_id=2)
    sapporo_station = Station(id=3, name='삿포로역', latitude=43.068661, longitude=141.350755, country_id=2)
    db.session.add_all([seoul_station, tokyo_station, sapporo_station])

    # 노선 데이터 추가
    gyeongbu_line = Route(id=1, name='경부선', country_id=1)
    tozai_line = Route(id=2, name='도자이선', country_id=2)
    shinkansen_line = Route(id=3, name='신칸센', country_id=2)
    db.session.add_all([gyeongbu_line, tozai_line, shinkansen_line])

    # 노선-역 관계 추가
    db.session.add(RouteStation(id=1, route_id=1, station_id=1, station_order=1))
    db.session.add(RouteStation(id=2, route_id=2, station_id=2, station_order=1))
    db.session.add(RouteStation(id=3, route_id=3, station_id=3, station_order=1))

    # 교통 패스 데이터 추가
    kr_pass = TravelPass(id=1, name='코리아 레일 패스', description='한국에서 기차를 무제한 이용 가능', price=80.0, valid_days=7, country_id=1)
    jp_pass = TravelPass(id=2, name='재팬 레일 패스', description='일본에서 기차를 무제한 이용 가능', price=250.0, valid_days=14, country_id=2)
    db.session.add_all([kr_pass, jp_pass])

    # 패스-노선 관계 추가
    db.session.add(PassRoute(id=1, pass_id=1, route_id=1))
    db.session.add(PassRoute(id=2, pass_id=2, route_id=2))
    db.session.add(PassRoute(id=3, pass_id=2, route_id=3))

    # 관광지 데이터 추가
    db.session.add(TouristSpot(id=1, name='경복궁', description='서울의 대표적인 역사적 궁궐', station_id=1))
    db.session.add(TouristSpot(id=2, name='도쿄 타워', description='도쿄의 상징적인 랜드마크', station_id=2))
    db.session.add(TouristSpot(id=3, name='오도리 공원', description='삿포로의 유명한 공원', station_id=3))

    # 즐겨찾기 데이터 추가
    db.session.add(Favorite(id=1, user_id=1, station_id=1, route_id=1, pass_id=1))
    db.session.add(Favorite(id=2, user_id=1, station_id=2, route_id=2, pass_id=2))
    db.session.add(Favorite(id=3, user_id=2, station_id=3, route_id=3, pass_id=2))

    db.session.commit()

    print("샘플 데이터 삽입 완료")