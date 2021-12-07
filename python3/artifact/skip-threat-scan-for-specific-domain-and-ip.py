# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

# A script to skip scan artifacts which contains company domain or IP addresses

import re

COMPANY_IP = re.compile('^9\.9\.')
COMPANY_DOMAIN = re.compile('^ibm\.com$')
COMPANY_DOMAINS = re.compile('.*\.ibm\.com$')

if COMPANY_IP.match(artifact.value):
	artifact.global_info.scan_option = "off"
	artifact.global_info.summary = "This artifact belongs to company IP, skip threat scanning"

if COMPANY_DOMAIN.match(artifact.value) or COMPANY_DOMAINS.match(artifact.value):
	artifact.global_info.scan_option = "off"
	artifact.global_info.summary = "This artifact belongs to company domain, skip threat scanning"
