# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class CustomerControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_customer_using_delete(self, customer_id, **kwargs):  # noqa: E501
        """deleteCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_customer_using_delete(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_customer_using_delete_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_customer_using_delete_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def delete_customer_using_delete_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """deleteCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_customer_using_delete_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `delete_customer_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customer/{customerId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_by_id_using_get(self, customer_id, **kwargs):  # noqa: E501
        """getCustomerById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_customer_by_id_using_get(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_by_id_using_get_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_by_id_using_get_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def get_customer_by_id_using_get_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """getCustomerById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_customer_by_id_using_get_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customer/{customerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_title_by_id_using_get(self, customer_id, **kwargs):  # noqa: E501
        """getCustomerTitleById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_customer_title_by_id_using_get(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_title_by_id_using_get_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_title_by_id_using_get_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def get_customer_title_by_id_using_get_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """getCustomerTitleById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_customer_title_by_id_using_get_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_title_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/text'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customer/{customerId}/title', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customers_using_get(self, limit, **kwargs):  # noqa: E501
        """getCustomers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_customers_using_get(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataCustomer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customers_using_get_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customers_using_get_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def get_customers_using_get_with_http_info(self, limit, **kwargs):  # noqa: E501
        """getCustomers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_customers_using_get_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataCustomer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'text_search', 'id_offset', 'text_offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_customers_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'id_offset' in params:
            query_params.append(('idOffset', params['id_offset']))  # noqa: E501
        if 'text_offset' in params:
            query_params.append(('textOffset', params['text_offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customers{?textSearch,idOffset,textOffset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextPageDataCustomer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_short_customer_info_by_id_using_get(self, customer_id, **kwargs):  # noqa: E501
        """getShortCustomerInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_short_customer_info_by_id_using_get(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_short_customer_info_by_id_using_get_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_short_customer_info_by_id_using_get_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def get_short_customer_info_by_id_using_get_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """getShortCustomerInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_short_customer_info_by_id_using_get_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: customerId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_short_customer_info_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customer/{customerId}/shortInfo', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_customer_using_get(self, customer_title, **kwargs):  # noqa: E501
        """getTenantCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_customer_using_get(customer_title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_title: customerTitle (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_customer_using_get_with_http_info(customer_title, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_customer_using_get_with_http_info(customer_title, **kwargs)  # noqa: E501
            return data

    def get_tenant_customer_using_get_with_http_info(self, customer_title, **kwargs):  # noqa: E501
        """getTenantCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_customer_using_get_with_http_info(customer_title, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_title: customerTitle (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_title']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_title' is set
        if ('customer_title' not in params or
                params['customer_title'] is None):
            raise ValueError("Missing the required parameter `customer_title` when calling `get_tenant_customer_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_title' in params:
            query_params.append(('customerTitle', params['customer_title']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/customers{?customerTitle}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_customer_using_post(self, customer, **kwargs):  # noqa: E501
        """saveCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_customer_using_post(customer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Customer customer: customer (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_customer_using_post_with_http_info(customer, **kwargs)  # noqa: E501
        else:
            (data) = self.save_customer_using_post_with_http_info(customer, **kwargs)  # noqa: E501
            return data

    def save_customer_using_post_with_http_info(self, customer, **kwargs):  # noqa: E501
        """saveCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_customer_using_post_with_http_info(customer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Customer customer: customer (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer' is set
        if ('customer' not in params or
                params['customer'] is None):
            raise ValueError("Missing the required parameter `customer` when calling `save_customer_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer' in params:
            body_params = params['customer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
