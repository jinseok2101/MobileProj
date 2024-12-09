import logging
from logging.config import fileConfig

from flask import current_app

from alembic import context

# 이 객체는 Alembic의 Config 객체로,
# 사용 중인 .ini 파일 내의 값에 접근할 수 있도록 함.
config = context.config

# .ini 파일의 설정을 해석하여 로깅 설정
# 이 라인은 기본적으로 로거 설정
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')


def get_engine():
    try:
        # Flask-SQLAlchemy<3 및 Alchemical과 호환되는 방식
        return current_app.extensions['migrate'].db.get_engine()
    except (TypeError, AttributeError):
        # Flask-SQLAlchemy>=3와 호환되는 방식
        return current_app.extensions['migrate'].db.engine


def get_engine_url():
    try:
        return get_engine().url.render_as_string(hide_password=False).replace(
            '%', '%%')
    except AttributeError:
        return str(get_engine().url).replace('%', '%%')


# 모델의 MetaData 객체를 추가하여
# 'autogenerate'(자동 생성) 기능 지원.
# 예: from myapp import mymodel
# target_metadata = mymodel.Base.metadata
config.set_main_option('sqlalchemy.url', get_engine_url())
target_db = current_app.extensions['migrate'].db

# env.py의 필요에 따라 정의된 config의 다른 값을 가져올 수도 있음.
# 예: my_important_option = config.get_main_option("my_important_option")


def get_metadata():
    if hasattr(target_db, 'metadatas'):
        return target_db.metadatas[None]
    return target_db.metadata


def run_migrations_offline():
    """'오프라인' 모드에서 마이그레이션을 실행.

    이 함수는 URL만을 사용하여 컨텍스트를 구성하며,
    엔진(Engine)은 필요하지 않음.
    이로 인해 DBAPI를 사용할 필요가 없음.

    이 함수에서 context.execute()를 호출하면
    제공된 문자열이 스크립트 출력으로 출력.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=get_metadata(), literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """'온라인' 모드에서 마이그레이션을 실행.

    이 시나리오에서는 엔진(Engine)을 생성하고
    컨텍스트와 연결을 연결해야함.
    """

    # 스키마에 변경 사항이 없을 때 자동 마이그레이션이 생성되지 않도록 콜백 설정
    # 참고: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('스키마에서 변경 사항이 감지되지 않았습니다.')

    conf_args = current_app.extensions['migrate'].configure_args
    if conf_args.get("process_revision_directives") is None:
        conf_args["process_revision_directives"] = process_revision_directives

    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=get_metadata(),
            **conf_args
        )

        with context.begin_transaction():
            context.run_migrations()


# 현재 모드가 '오프라인'인지 확인한 뒤 적절한 함수 실행
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()