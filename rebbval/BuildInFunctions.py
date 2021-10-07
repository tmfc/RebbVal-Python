import calendar
import datetime
import re

from rebbval.RebbValConfig import RebbValConfig
from rebbval.RebbValHelper import RebbValHelper
from rebbval.RebbValParser import RebbValParser


class BuildInFunctions:
    def __init__(self, config):
        self.__config = config
        self.__function_map = dict()
        self.error = ""
        self.__init_function_map()

    def __init_function_map(self):
        self.__function_map[str(RebbValParser.TRUE)] = self.check_true
        self.__function_map[str(RebbValParser.FALSE)] = self.check_false
        self.__function_map[str(RebbValParser.LEAPYEAR)] = self.check_leap_year
        self.__function_map[str(RebbValParser.LEAPDAY)] = self.check_leap_day
        self.__function_map[str(RebbValParser.IMEI)] = self.check_imei
        self.__function_map[str(RebbValParser.IMEISV)] = self.check_imeisv
        self.__function_map[str(RebbValParser.ISBN)] = self.check_isbn
        self.__function_map[str(RebbValParser.UUID)] = self.check_uuid
        self.__function_map[str(RebbValParser.MAC)] = self.check_mac
        self.__function_map[str(RebbValParser.ID)] = self.check_id
        self.__function_map[str(RebbValParser.DOMAIN)] = self.check_domain
        self.__function_map[str(RebbValParser.EMAIL)] = self.check_email
        self.__function_map[str(RebbValParser.IPV4)] = self.check_ipv4
        self.__function_map[str(RebbValParser.IPV6)] = self.check_ipv6
        self.__function_map[str(RebbValParser.PRIVATEIP)] = self.check_private_ip
        self.__function_map[str(RebbValParser.URL)] = self.check_url

    def check(self, check_type, obj):
        return self.__function_map[str(check_type)](obj)

    def check_true(self, obj):
        if isinstance(obj, bool):
            return obj is True
        elif isinstance(obj, str):
            return obj in self.__config[RebbValConfig.TRUE_STRING]
        elif RebbValHelper.is_numeric(obj):
            return RebbValHelper.parse_number(obj) == 1
        else:
            self.error = "ObjectTypeNotSupport"
            return False

    def check_false(self, obj):
        return not self.check_true(obj)

    def check_leap_year(self, obj):
        if RebbValHelper.is_date(obj):
            return calendar.isleap(obj.year)
        else:
            self.error = "ObjectTypeNotDate"
            return False

    def check_leap_day(self, obj):
        if RebbValHelper.is_date(obj):
            return calendar.isleap(obj.year) and obj.month == 2 and obj.day == 29
        else:
            self.error = "ObjectTypeNotDate"
            return False

    def check_imei(self, obj):
        regex = r'^(\d{15})|^(\d{2}\-\d{6}\-\d{6}\-\d)'
        result = self.__check_regex(obj, regex)
        if result:
            imei = obj.replace("-", "")

            check = imei[14]
            imei = imei[0:14]
            check_sum = 0

            for i in range(len(imei)):
                _weight = 1
                if i % 2 == 1:
                    _weight = 2

                _char_int = int(imei[i]) * _weight
                if _char_int >= 10:
                    _char_int = _char_int - 9

                check_sum += _char_int
            
            check_sum %= 10
            check_sum = 0 if check_sum == 0 else (10 - check_sum)

            return check_sum == int(check)
        
        return False

    def check_imeisv(self, obj):
        regex = r'^(\d{16})|^(\d{2}\-\d{6}\-\d{6}\-\d{2})'
        return self.__check_regex(obj, regex)

    def check_isbn(self, obj):
        regex = r"^(?:ISBN(?:-1[03])?:?●)?(?=[-0-9●]{17}$|[-0-9X●]{13}$|[0-9X]{10}$)(?:97[89][-●]?)?[0-9]{1,5}[-●]?(?:[0-9]+[-●]?){2}[0-9X]$"
        result = self.__check_regex(obj, regex)
        if result:
            isbn = obj.replace("-", "")

            checksum = 0
            for i in range(len(isbn)):
                weight = 1
                if i % 2 == 1:
                    weight = 3
                char_int = int(isbn[i])
                a = char_int * weight
                checksum += a
            return checksum % 10 == 0
        return False

    def check_uuid(self, obj):
        regex = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
        return self.__check_regex(obj, regex)

    def check_id(self, obj):
        regex = r"(^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])"
        regex_result = self.__check_regex(obj, regex)
        if not regex_result:
            return False

        id = obj
        # check area code
        areas = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 61, 62, 63, 64, 65, 71, 81, 82, 91]
        area = int(id[0:2])
        if area not in areas:
            return False

        # check birthday
        birthday = id[6:14]
        try:
            dt = datetime.datetime.strptime(birthday, '%Y%m%d')
        except ValueError as error:
            self.error = str(error)
            return False

        # checksum
        checksum = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        for i in range(17):
            char_int = int(id[i])
            a = char_int * weight[i]
            checksum += a

        checksum_char_list = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        checksum_char = checksum_char_list[checksum % 11]
        return str(checksum_char) == id[-1]

    def check_mac(self, obj):
        regex = "^((?:[a-fA-F0-9]{2}[:-]){5}[a-fA-F0-9]{2})"
        return self.__check_regex(obj, regex)

    def check_domain(self, obj):
        regex = r'^(?:(?:(?:[\w\-]*)(?:\.))?(?:[\w\-]*))\.(?:\w*)(?:\:(?:\d*))?$'
        return self.__check_regex(obj, regex)

    def check_email(self, obj):
        regex = r'^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$'
        return self.__check_regex(obj, regex)

    def check_ipv4(self, obj):
        regex = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return self.__check_regex(obj, regex)

    def check_ipv6(self, obj):
        regex = r'^([\da-fA-F]{1,4}(?::[\da-fA-F]{1,4}){7}|::|:(?::[\da-fA-F]{1,4}){1,6}|[\da-fA-F]{1,4}:(?::[\da-fA-F]{1,4}){1,5}|(?:[\da-fA-F]{1,4}:){2}(?::[\da-fA-F]{1,4}){1,4}|(?:[\da-fA-F]{1,4}:){3}(?::[\da-fA-F]{1,4}){1,3}|(?:[\da-fA-F]{1,4}:){4}(?::[\da-fA-F]{1,4}){1,2}|(?:[\da-fA-F]{1,4}:){5}:[\da-fA-F]{1,4}|(?:[\da-fA-F]{1,4}:){1,6}:)$'
        return self.__check_regex(obj, regex)

    def check_private_ip(self, obj):
        if RebbValHelper.is_string(obj):
            regex_ipv4 = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
            regex_ipv6 = r'^([\da-fA-F]{1,4}(?::[\da-fA-F]{1,4}){7}|::|:(?::[\da-fA-F]{1,4}){1,6}|[\da-fA-F]{1,4}:(?::[\da-fA-F]{1,4}){1,5}|(?:[\da-fA-F]{1,4}:){2}(?::[\da-fA-F]{1,4}){1,4}|(?:[\da-fA-F]{1,4}:){3}(?::[\da-fA-F]{1,4}){1,3}|(?:[\da-fA-F]{1,4}:){4}(?::[\da-fA-F]{1,4}){1,2}|(?:[\da-fA-F]{1,4}:){5}:[\da-fA-F]{1,4}|(?:[\da-fA-F]{1,4}:){1,6}:)$'

            if self.__check_regex(obj, regex_ipv4):
                regex_ipv4_private = r'^(10(\.(([0-9]?[0-9])|(1[0-9]?[0-9])|(2[0-4]?[0-9])|(25[0-5]))){3})|(172\.((1[6-9])|(2[0-9])(3[0-1]))(\.(([0-9]?[0-9])|(1[0-9]?[0-9])|(2[0-4]?[0-9])|(25[0-5]))){2})|(192\.168(\.(([0-9]?[0-9])|(1[0-9]?[0-9])|(2[0-4]?[0-9])|(25[0-5]))){2})|(127(\.(([0-9]?[0-9])|(1[0-9]?[0-9])|(2[0-4]?[0-9])|(25[0-5]))){3})$'
                return self.__check_regex(obj, regex_ipv4_private)
            elif self.__check_regex(obj, regex_ipv6):
                return obj.startswith("FEC0:")
            else:
                return False
        else:
            self.error = "ObjectTypeNotString"
            return False

    def check_url(self, obj):
        regex = r'^((https?:)(\/\/\/?)([\w]*(?::[\w]*)?@)?([\d\w\.-]+)(?::(\d+))?)?([\/\\\w\.()-]*)?(?:([?][^#]*)?(#.*)?)*$'
        return self.__check_regex(obj, regex)

    def __check_regex(self, obj, regex):
        if RebbValHelper.is_string(obj):
            p = re.compile(regex)
            m = p.search(obj)
            return m is not None
        else:
            self.error = "ObjectTypeNotSupport"
            return False
