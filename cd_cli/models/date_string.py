import pprint


class DateString(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"_date": "date"}

    attribute_map = {"_date": "date"}

    def __init__(self, _date=None):
        """DateString"""

        self.__date = None

        if _date is not None:
            self._date = _date

    @property
    def _date(self):
        """Gets the _date of this DateString.

        Time with format: 'yyyy-MM-dd'

        :return: The _date of this DateString.
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DateString.

        Time with format: 'yyyy-MM-dd'

        :param _date: The _date of this DateString.
        :type: date
        """

        self.__date = _date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in iter(self.attribute_types.items()):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(DateString, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DateString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateString):
            return True

        return self.to_dict() != other.to_dict()
