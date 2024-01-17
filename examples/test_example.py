# Copyright (c) 2024 Petro-Logistics S.A., All rights reserved.
# 
# This work is licensed under the terms of the MIT license.  
# For a copy, see <https://opensource.org/licenses/MIT>.

from plapi.client import PLAPIClient

# Initialize object "PLAPIClient" to be executed.
#
# Provide your credentials ("api_key", "api_hash", "http_user", "http_pass").
# !!! If you don't find your credentials, please contact our support!
#
# Provide your "desired_report_type"
# !!! If you don't know what the **desired_report_type**, please contact our support
# !!! e.g. of "desired_report_type": "/aggregatemovementsdata", "/movementsdata", etc.
plapiclient = PLAPIClient(
            api_url="https://secure.petro-logistics.com/api/v4/aggregatemovementsdata",
            api_key="37rspm6j39td23nh0o2v0h78",
            api_hash="d1Npusz7BrVDauza7b7v5swgV20uiXQwiCG6nxiPseWRda6mTfJBeByKZsvp5sNX",
            http_user="testuser_http_kRQNk5878ezA",
            http_pass="F268DBvvPCBV83eT1vIeTpBGrJD604K2"
        )

print("Executing PLAPIClient Query")

# Execute function "execute" to request and get the results.
#
# provide the "query_name".
# !!! If you don't find your **query_name**, please contact our support!
result = plapiclient.execute("Angola_Test_Data")

print(result["envelope"]["header"])

# [ EXECUTING MORE THAN 1 QUERY ]
# To execute more than one query/api, you can use 1 of the following proposals:
#   1. Creating copies of this example file for each desired query (By filling in the corresponding parameters on each file)
#
#   2. By repeating a part of the code in this same file to execute other queries for the same api_url, like this:
#
#      result = plapiclient.execute("query_2")
#      print(result["envelope"]["header"])
#
#   3. By repeating corresponding code in this same file to execute other queries for another api_url, like this:
#
#      plapiclient = PLAPIClient(
#                  api_url="https://secure.petro-logistics.com/api/v4/other_desired_api",
#                  api_key="37rspm6j39td23nh0o2v0h78",
#                  api_hash="P0iwW39qaMvTjFRdcmsiKmD9OxGEquHNXapwbSQr8gbuV2ssqjbt0Vy7Yelyi4C1",
#                  http_user="testuser_http_CuH68Omfx17R",
#                  http_pass="X9PV5EmJPr88lEyjD2I2IE26b9ElQCX0"
#              )
#
#      result = plapiclient.execute("other_desired_query")
#      print(result["envelope"]["header"])
