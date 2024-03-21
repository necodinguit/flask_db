"""APP"""

from flask import jsonfy







if __name__ == "__main__":
    api = Api(app)

    api.add_resource(DbFullApi, '/<string:tablename>')
    api.add_resource(DbApiPk, '/<string:tablename>')
    api.add_resource(DbApi, '/<string:tablename>')
