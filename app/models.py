from app import db

# 국가 정보
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    languages = db.Column(db.JSON)

# 역 정보
class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

# 노선 정보
class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

class RouteStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))
    station_order = db.Column(db.Integer)

# 교통 패스 정보
class TravelPass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    valid_days = db.Column(db.Integer)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

class PassRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass_id = db.Column(db.Integer, db.ForeignKey('travel_pass.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))

# 관광지 정보
class TouristSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    # distance_from_station = db.Column(db.Float)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))

# 즐겨찾기 기능
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)  # 임시로 사용자 ID
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    pass_id = db.Column(db.Integer, db.ForeignKey('travel_pass.id'))