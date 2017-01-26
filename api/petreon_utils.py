from sqlalchemy.orm import class_mapper, ColumnProperty

def toDict(modelObj):
    """Returns a dict representation of a SQLAlchemy model object.

    Keyword arguments:
    modelObj -- a SQLAlchemy model object or a list of them
    """
    if isinstance(modelObj, list):
        return [toDict(o) for o in modelObj]
    else:
        props = [prop.key for prop in class_mapper(type(modelObj)).iterate_properties
            if isinstance(prop, ColumnProperty)]
        d = {}
        for prop in props:
            d[prop] = getattr(modelObj, prop)

        return d

