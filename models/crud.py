from constants import db as db_consts


class Crud:
    @classmethod
    def get_table_sql_fields(cls):
        sql_fields = []
        foreign_key_constraints = []
        for field_name, field_params in cls.get_table_attributes().items():
            sql_field_query = f'{field_name} {field_params[0]}'
            if 'pk' in field_params:
                sql_field_query += f' {db_consts.PRIMARY_KEY}'
            elif 'fk' in field_params:
                foreign_key_constraints.append(
                    db_consts.FOREIGN_KEY.format(field_name, field_params[2], field_params[3]))
            sql_fields.append(sql_field_query)
        return sql_fields + foreign_key_constraints

    @classmethod
    def create_table_query(cls):
        return f"CREATE TABLE IF NOT EXISTS {cls.__tablename__} ( {','.join(cls.get_table_sql_fields())} )"

    @classmethod
    def create_query(cls, columns):
        values = ['?']*(len(columns))
        return f"INSERT INTO {cls.__tablename__} ({','.join(columns)}) VALUES ({','.join(values)})"

    @classmethod
    def read(cls, filters):
        query = db_consts.SELECT_ALL.format(cls.__tablename__)
        if not filters:
            return query
        query += f' WHERE '
        for index,filter in enumerate(filters):
            if index < len(filters) -1:
                query += f' {filter}=:{filter} and '
            else:
                query += f' {filter}=:{filter}'
        return query
