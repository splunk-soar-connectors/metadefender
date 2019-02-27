# File: metadefender_connector.py
# Copyright (c) 2016-2019 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.

# Phantom imports
import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# THIS Connector imports
from metadefender_consts import *

# Required library imports
import simplejson as json
import requests


class MetadefenderConnector(BaseConnector):

    ACTION_ID_IP_REPUTATION = "ip_reputation"
    ACTION_ID_FILE_REPUTATION = "file_reputation"
    ACTION_ID_TEST_ASSET_CONNECTIVITY = "test_connectivity"

    def __init__(self):

        super(MetadefenderConnector, self).__init__()

    def _make_rest_call(self, endpoint, headers):

        full_url = METADEFENDER_API_BASE_URL + endpoint

        try:

            r = requests.get(full_url, headers=headers)

        except Exception as e:

            return (phantom.APP_ERROR, "Could not complete rest call. {}".format(e))

        if (r.status_code == 403):
            return (phantom.APP_ERROR, "API call limit reached.  See Metadefender's Portal for more information")

        if (400 <= r.status_code):
            return (phantom.APP_ERROR, "Response failed. {}".format(r.reason))
        try:
            resp_json = r.json()
        except Exception as e:
            return (phantom.APP_ERROR, "Could not convert response to JSON. {}", format(e))

        return (phantom.APP_SUCCESS, resp_json)

    def _ip_reputation(self, params):

        action_result = self.add_action_result(ActionResult(params))

        ip = params[METADEFENDER_JSON_IP]

        endpoint = METADEFENDER_API_IP_REPUTATION.format(ip=ip)

        config = self.get_config()

        headers = {'Authorization': "apikey {0}".format(config[METADEFENDER_CONFIG_API_KEY])}

        ret_val, response = self._make_rest_call(endpoint, headers)

        if (phantom.is_fail(ret_val)):
            return (action_result.set_status(phantom.APP_ERROR, "Could not complete rest call", response))

        action_result.add_data(response)

        action_result.set_summary({'detected_by': response['data']['detected_by']})
        return action_result.set_status(phantom.APP_SUCCESS)

    def _file_reputation(self, params):

        action_result = self.add_action_result(ActionResult(params))

        file = params[METADEFENDER_JSON_HASH]

        config = self.get_config()

        headers = {'apikey': config[METADEFENDER_CONFIG_API_KEY]}

        headers.update({'file_metadata': "1"})

        endpoint = METADEFENDER_API_FILE_REPUTATION.format(file=file)

        ret_val, response = self._make_rest_call(endpoint, headers)

        if (phantom.is_fail(ret_val)):
            return (action_result.set_status(phantom.APP_ERROR, "Could not complete rest call", response))

        action_result.add_data(response)
        if 'scan_results' in response:
            action_result.set_summary({"file_result": response['scan_results']['scan_all_result_a']})
        else:
            action_result.set_summary({"file_result": "Clean"})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _test_connectivity(self):

        # set the endpoint
        endpoint = METADEFENDER_API_IP_REPUTATION.format(ip="8.8.8.8")

        # Action result to represent the call
        action_result = ActionResult()

        # Progress message, since it is test connectivity, it pays to be verbose
        self.save_progress("Querying Metadefender...")

        config = self.get_config()

        headers = {'Authorization': "apikey {0}".format(config[METADEFENDER_CONFIG_API_KEY])}

        ret_val, response = self._make_rest_call(endpoint, headers)

        # Process errors
        if (phantom.is_fail(ret_val)):
            # Dump error messages in the log
            self.debug_print(action_result.get_message())

            # Set the status of the complete connector result
            self.set_status(phantom.APP_ERROR, action_result.get_message())

            # Append the message to display
            self.append_to_message(response)

            # return error
            return phantom.APP_ERROR

        # Set the status of the connector result
        return self.set_status_save_progress(phantom.APP_SUCCESS, "Test Connectivity succeeded")

    def handle_action(self, params):

        action = self.get_action_identifier()

        ret_val = phantom.APP_SUCCESS

        if (action == self.ACTION_ID_IP_REPUTATION):
            ret_val = self._ip_reputation(params)
        elif (action == self.ACTION_ID_FILE_REPUTATION):
            ret_val = self._file_reputation(params)
        if (action == self.ACTION_ID_TEST_ASSET_CONNECTIVITY):
            ret_val = self._test_connectivity()
        return ret_val


if __name__ == '__main__':
    # Imports
    import sys
    import pudb

    # Breakpoint at runtime
    pudb.set_trace()

    # The first param is the input json file
    with open(sys.argv[1]) as f:
        # Load the input json file
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=' ' * 4))

        # Create the connector class object
        connector = MetadefenderConnector()

        # Se the member vars
        connector.print_progress_message = True

        # Call BaseConnector::_handle_action(...) to kickoff action handling.
        ret_val = connector._handle_action(json.dumps(in_json), None)

        # Dump the return value
        print ret_val

    exit(0)
