from sqlalchemy.orm import class_mapper, ColumnProperty

def to_dict(model_obj):
    """Returns a dict representation of a SQLAlchemy model object.

    Keyword arguments:
    model_obj -- a SQLAlchemy model object or a list of them
    """
    if isinstance(model_obj, list):
        return [to_dict(o) for o in model_obj]
    else:
        props = [prop.key for prop in class_mapper(type(model_obj)).iterate_properties
            if isinstance(prop, ColumnProperty)]
        d = {}
        for prop in props:
            d[prop] = getattr(model_obj, prop)

        return d
