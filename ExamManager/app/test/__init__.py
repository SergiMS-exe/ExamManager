SQLALCHEMY_MIGRATE_TEST_REPO = os.path.join(basedir, 'db_test_repository')
 
if not os.path.exists(SQLALCHEMY_MIGRATE_TEST_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
    pass
db = SQLAlchemy(app=test)
db.create_all()