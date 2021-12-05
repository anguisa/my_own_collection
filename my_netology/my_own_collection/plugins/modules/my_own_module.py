#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create text file and write to it

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Create text file on remote host by specified path with specified content. If file already exists, do nothing

options:
    path:
        description: Path to new file with name and extension
        required: true
        type: str
    content:
        description: Content that should be written to file
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_netology.my_own_collection.my_own_module

author:
    - Olga Ivanova (https://github.com/anguisa)
'''

EXAMPLES = r'''
# Pass in a message
- name: Create and populate file
  my_netology.my_own_collection.my_own_module:
    path: /tmp/1.txt
    content: 'hello world'
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original content that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the module generates.
    type: str
    returned: always
    sample: 'file was created'
'''

from ansible.module_utils.basic import AnsibleModule
import os.path

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    result['original_message'] = module.params['content']

    if module.params['path'] == "":
        result['changed'] = False
        result['failed'] = True
        result['message'] = 'path is empty'
    elif not os.path.exists(module.params['path']):
        with open(module.params['path'], 'w') as my_file:
            my_file.write(module.params['content'])
            result['changed'] = True
            result['message'] = 'file was created'
    elif not os.path.isfile(module.params['path']):
        result['changed'] = False
        result['failed'] = True
        result['message'] = 'is directory'
    else:
        result['changed'] = False
        result['message'] = 'file already exists'

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()