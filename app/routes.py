from flask import Blueprint, render_template, request
from app.models import db, Station

# Blueprint 설정
main = Blueprint('main', __name__)

# 홈 페이지 라우트
@main.route('/')
def home():
    return render_template('index.html')

# 모든 역(stations)을 조회하는 라우트
@main.route('/stations')
def stations():
    stations = Station.query.all()
    return render_template('stations.html', stations=stations)

# 검색 기능 라우트
@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # 검색어 쿼리
    stations = Station.query.filter(Station.name.ilike(f'%{query}%')).all()
    return render_template('search.html', stations=stations)