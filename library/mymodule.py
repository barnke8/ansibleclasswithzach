#!/usr/bin/pythons3

ANSIBLE_METADATA = {
        'metadata+version': '1.1',
        'status': ['preview'],
        'supported_by': 'kellybarnett'
        }

DOCUMENTATION = '''
---
module: mymodule
short_description: This module is bing designed so we can observe the minum required config for an Ansible module
version_added = "2.8"
description:
    - this module is being designed so we can observethe minimum required config for an ansible module
    - user passes a parameter called "name:" <str> <required>
    - user passws a parameter called "augment: " <bool> <required>
    - if augment: true then ansible returns the name value and additonal string as well as indicates a yello chnge on teh play recap
    - if augment: false then ansible returns name string and indicates a green ok on play recap
    - if name: fail me then ansible returns failed in play recap
author: 
    kelly.barnett@vzw.com
'''

EXAMPLE = '''
- name: this sould get a green ok
  mymodule:
    name: Kelly
    augment: true

- name: this would get a red fail
  mymodule:
    name: fail me
'''

RETURN = '''
original_message:
    description: the name param that was passed in by the suer
    type: str
message:
    description: the name param the same way it was passed in or the new augmented name param
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    ## define the parameters that the user is allowed to pass in
    module_args = dict(
            name=dict(type='str',required=Tru),
            augment=dict(type='bool',default=False)
            )
    
    ## seed the return object
    result = dict(
            changed=False,
            original_message='',
            message=''
            )

    module = AnsibleModule(
            argument_spec=module_args,
            support_check_mode=True
            )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']

    if module.params['augment'] == False:
        result['message'] = module.params['name']
    else:
        result['message'] = moudle.params['name'] + " is a wild and crazy guy!!! -- Dan Akroyd"

    if module.params['name'] == 'fail me':
        module.fail_json(msg"You requested this to fail", **result)

    module.exit_json(**result)
def main():
        run_module()

if __name__ == "__main__":
            main()
