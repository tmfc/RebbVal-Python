from datetime import datetime


class RebbValHelper:
    @staticmethod
    def is_bool(value):
        return isinstance(value, bool)

    @staticmethod
    def is_date(value):
        return isinstance(value, datetime)

    @staticmethod
    def is_list(value):
        return isinstance(value, list)

    @staticmethod
    def is_numeric(value):
        if value is None:
            return False

        try:
            num = float(value)
            # check for "nan" floats
            is_number = num == num  # or use `math.isnan(num)`
        except ValueError:
            is_number = False
        except TypeError:
            is_number = False
        return is_number

    @staticmethod
    def parse_number( value):
        if not RebbValHelper.is_numeric(value):
            return None
        else:
            try:
                return int(value)
            except ValueError:
                return float(value)

    @staticmethod
    def is_string(value):
        return isinstance(value, str)
