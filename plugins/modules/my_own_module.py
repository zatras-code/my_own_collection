#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create text file with content

version_added: "1.0.0"

description:
  - Module creates file with given content.

options:
  path:
    description:
      - Path to target file.
    required: true
    type: str

  content:
    description:
      - File content.
    required: true
    type: str

author:
  - Your Name
'''

EXAMPLES = r'''
- name: Create file
  my_own_module:
    path: /tmp/test.txt
    content: "hello world"
'''

RETURN = r'''
msg:
  description: Result message
  type: str
  returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():

    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        msg=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    if os.path.exists(path):
        with open(path, 'r') as f:
            current_content = f.read()

        if current_content == content:
            result['msg'] = 'File already exists'
            module.exit_json(**result)

    if module.check_mode:
        result['changed'] = True
        module.exit_json(**result)

    with open(path, 'w') as f:
        f.write(content)

    result['changed'] = True
    result['msg'] = 'File created'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

