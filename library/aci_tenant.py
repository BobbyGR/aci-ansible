#!usr/bin/python

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: aci_tenant
short_description: Manage tenants on Cisco ACI fabrics
description:
- Manage tenants on a Cisco ACI fabric.
author:
- Swetha Chunduri (@schunduri)
- Dag Wieers (@dagwieers)
version_added: '2.4'
requirements:
- ACI Fabric 1.0(3f)+
options:
  tenant_name:
    description:
    - The name of the tenant.
    required: yes
  descr:
    description:
    - Description for the AEP.
  state:
    description:
    - present, absent, query
    default: present
    choices: [ absent, present, query ]
extends_documentation_fragment: aci
'''

EXAMPLES = '''
- name: Add a new tenant
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant_name: Name of the tenant
    description: Description for the tenant
    state: present

- name: Remove a tenant
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant_name: Name of the tenant
    state: absent

- name: Query a tenant
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    tenant_name: Name of the tenant
    state: query

- name: Query all tenants
  aci_tenant:
    hostname: apic
    username: admin
    password: SomeSecretPassword
    state: query
'''

RETURN = '''
status:
  description: The status code of the http request
  returned: upon making a successful GET, POST or DELETE request to the APIC
  type: int
  sample: 200
response:
  description: Response text returned by APIC
  returned: when a HTTP request has been made to APIC
  type: string
  sample: '{"totalCount":"0","imdata":[]}'
'''

from ansible.module_utils.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = aci_argument_spec
    argument_spec.update(
        tenant_name=dict(type='str', aliases=['name'], required=False),
        description=dict(type='str', aliases=['descr'], required=False),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        method=dict(type='str', choices=['delete', 'get', 'post'], aliases=['action'], removed_in_version='2.6'),  # Deprecated starting from v2.6
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    tenant_name = module.params['tenant_name']
    description = module.params['description']
    state = module.params['state']

    aci = ACIModule(module)

    if tenant_name is not None:
        # Work with a specific tenant
        path = 'api/mo/uni/tn-%(tenant_name)s.json' % module.params
    elif state == 'query':
        # Query all tenants
        path = 'api/class/fvTenant.json'
    else:
        module.fail_json(msg="Parameter 'tenant_name' is required for state 'absent' or 'present'")

    aci.result['url'] = '%(protocol)s://%(hostname)s/' % aci.params + path

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(aci_class='fvTenant', class_config=dict(name=tenant_name, descr=description))

        # generate config diff which will be used as POST reqest body
        aci.get_diff(aci_class='fvTenant')

        # submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
