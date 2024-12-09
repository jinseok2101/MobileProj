from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 데이터베이스 객체 초기화
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # SQLite 사용
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'supersecretkey'  # CSRF 보호를 위한 키

    # DB와 Flask 앱 연결
    db.init_app(app)
    migrate.init_app(app, db)

    # 라우트 등록
    from app.routes import main
    app.register_blueprint(main)

    return app