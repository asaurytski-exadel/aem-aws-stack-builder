#!/usr/bin/python

from ansible.module_utils.basic import *
import random
import string

def generate_facts(params):
    return """proxy_enabled=%s
proxy_protocol=%s
proxy_host=%s
proxy_port=%s
aem_orchestrator_version=%s
""" % (
            str(params['proxy_enabled']).lower(),
            params['proxy_protocol'],
            params['proxy_host'],
            params['proxy_port'],
            params['aem_orchestrator_version']
        )

def main():

    module = AnsibleModule(
      argument_spec = dict(
        proxy_enabled            = dict(required=True, type='bool'),
        proxy_protocol           = dict(required=True, type='str'),
        proxy_host               = dict(required=True, type='str'),
        proxy_port               = dict(required=True, type='str'), # string type to allow empty value when proxy is irrelevant
        aem_orchestrator_version = dict(required=True, type='str'),
      )
    )
    response = generate_facts(module.params)
    module.exit_json(changed = False, meta = response)

if __name__ == '__main__':
    main()