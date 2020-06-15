# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from tb_rest_client.models.models_ce import Asset


class Asset(Asset):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {**Asset.swagger_types, "owner_id": "EntityId"}
    attribute_map = {**Asset.attribute_map, "owner_id": "ownerId"}

    def __init__(self, additional_info=None, created_time=None, customer_id=None, id=None, label=None, name=None, owner_id=None, tenant_id=None, type=None):  # noqa: E501
        """Asset - a model defined in Swagger"""  # noqa: E501

        super().__init__(additional_info, created_time, customer_id, id, label, name, tenant_id, type)
        self._owner_id = owner_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Asset.  # noqa: E501


        :return: The owner_id of this Asset.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Asset.


        :param owner_id: The owner_id of this Asset.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id