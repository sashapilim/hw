from marshmallow import Schema, fields, validates_schema, ValidationError

cmd = ("filter",
       "map",
       "unique",
       "sorted",
       "limit")



class Params(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema()
    def valid_cmd(self, values, *args, **kwargs):
        if values["cmd"] not in cmd:
            raise ValidationError(f"cmd not valid")


# [{"cmd":"",
# "value":""},
# {"cmd":"",
# # "value":""},
# ]
class SeveralParams(Schema):
    qeuries = fields.Nested(Params, many=True)
