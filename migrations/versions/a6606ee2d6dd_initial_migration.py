"""초기 마이그레이션

Revision ID: a6606ee2d6dd
Revises: 
Create Date: 2024-11-20 20:35:53.349170

"""
from alembic import op
import sqlalchemy as sa


# Alembic에 의해 사용되는 리비전 식별자.
revision = 'a6606ee2d6dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """데이터베이스 스키마를 업그레이드하는 함수.

    Alembic이 자동으로 생성한 명령들을 포함하며,
    필요한 경우 수정하여 사용할 수 있음.
    """
    # ### Alembic에 의해 자동 생성된 명령 - 필요에 따라 조정 필요 ###
    op.create_table('country',  # 국가 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('name', sa.String(length=100), nullable=False),  # 국가 이름 (문자열, 필수)
    sa.Column('languages', sa.JSON(), nullable=True),  # 사용 언어 정보 (JSON 형식)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('route',  # 노선 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('name', sa.String(length=100), nullable=False),  # 노선 이름 (문자열, 필수)
    sa.Column('country_id', sa.Integer(), nullable=True),  # 국가 ID (외래키)
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),  # 외래키 연결 (country 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('station',  # 역 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('name', sa.String(length=100), nullable=False),  # 역 이름 (문자열, 필수)
    sa.Column('latitude', sa.Float(), nullable=False),  # 위도 (실수형, 필수)
    sa.Column('longitude', sa.Float(), nullable=False),  # 경도 (실수형, 필수)
    sa.Column('country_id', sa.Integer(), nullable=True),  # 국가 ID (외래키)
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),  # 외래키 연결 (country 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('travel_pass',  # 교통 패스 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('name', sa.String(length=100), nullable=False),  # 패스 이름 (문자열, 필수)
    sa.Column('description', sa.Text(), nullable=True),  # 패스 설명 (텍스트, 선택)
    sa.Column('price', sa.Float(), nullable=True),  # 가격 (실수형, 선택)
    sa.Column('valid_days', sa.Integer(), nullable=True),  # 유효 기간 (정수형, 선택)
    sa.Column('country_id', sa.Integer(), nullable=True),  # 국가 ID (외래키)
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),  # 외래키 연결 (country 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('favorite',  # 즐겨찾기 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('user_id', sa.Integer(), nullable=True),  # 사용자 ID (정수형)
    sa.Column('station_id', sa.Integer(), nullable=True),  # 역 ID (외래키)
    sa.Column('route_id', sa.Integer(), nullable=True),  # 노선 ID (외래키)
    sa.Column('pass_id', sa.Integer(), nullable=True),  # 패스 ID (외래키)
    sa.ForeignKeyConstraint(['pass_id'], ['travel_pass.id'], ),  # 외래키 연결 (travel_pass 테이블)
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),  # 외래키 연결 (route 테이블)
    sa.ForeignKeyConstraint(['station_id'], ['station.id'], ),  # 외래키 연결 (station 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('pass_route',  # 패스-노선 연결 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('pass_id', sa.Integer(), nullable=True),  # 패스 ID (외래키)
    sa.Column('route_id', sa.Integer(), nullable=True),  # 노선 ID (외래키)
    sa.ForeignKeyConstraint(['pass_id'], ['travel_pass.id'], ),  # 외래키 연결 (travel_pass 테이블)
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),  # 외래키 연결 (route 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('route_station',  # 노선-역 연결 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('route_id', sa.Integer(), nullable=True),  # 노선 ID (외래키)
    sa.Column('station_id', sa.Integer(), nullable=True),  # 역 ID (외래키)
    sa.Column('station_order', sa.Integer(), nullable=True),  # 역 순서 (정수형)
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),  # 외래키 연결 (route 테이블)
    sa.ForeignKeyConstraint(['station_id'], ['station.id'], ),  # 외래키 연결 (station 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    op.create_table('tourist_spot',  # 관광지 테이블 생성
    sa.Column('id', sa.Integer(), nullable=False),  # ID 컬럼 (정수형, 기본키)
    sa.Column('name', sa.String(length=100), nullable=False),  # 관광지 이름 (문자열, 필수)
    sa.Column('description', sa.Text(), nullable=True),  # 관광지 설명 (텍스트, 선택)
    sa.Column('distance_from_station', sa.Float(), nullable=True),  # 역으로부터 거리 (실수형, 선택)
    sa.Column('station_id', sa.Integer(), nullable=True),  # 역 ID (외래키)
    sa.ForeignKeyConstraint(['station_id'], ['station.id'], ),  # 외래키 연결 (station 테이블)
    sa.PrimaryKeyConstraint('id')  # ID를 기본키로 설정
    )
    # ### Alembic에 의해 자동 생성된 명령 끝 ###


def downgrade():
    """데이터베이스 스키마를 다운그레이드하는 함수입니다.

    업그레이드에서 생성된 모든 테이블을 삭제합니다.
    """
    # ### Alembic에 의해 자동 생성된 명령 - 필요에 따라 조정 필요 ###
    op.drop_table('tourist_spot')  # 관광지 테이블 삭제
    op.drop_table('route_station')  # 노선-역 연결 테이블 삭제
    op.drop_table('pass_route')  # 패스-노선 연결 테이블 삭제
    op.drop_table('favorite')  # 즐겨찾기 테이블 삭제
    op.drop_table('travel_pass')  # 교통 패스 테이블 삭제
    op.drop_table('station')  # 역 테이블 삭제
    op.drop_table('route')  # 노선 테이블 삭제
    op.drop_table('country')  # 국가 테이블 삭제
    # ### Alembic에 의해 자동 생성된 명령 끝 ###