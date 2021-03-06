.. _aci_intf_policy_port_channel:


aci_intf_policy_port_channel - Manage port channel interface policies on Cisco ACI fabrics (lacp:LagPol)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage port channel interface policies on Cisco ACI fabrics.
* More information from the internal APIC class *lacp:LagPol* at https://developer.cisco.com/media/mim-ref/MO-lacpLagPol.html.


Requirements (on host that executes module)
-------------------------------------------

  * ACI Fabric 1.0(3f)+


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>

    <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The description for the port channel.</div>
        </br><div style="font-size: small;">aliases: descr</div>
    </td>
    </tr>

    <tr>
    <td>fast_select<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Determines if Fast Select is enabled for Hot Standby Ports.</div>
        <div>This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.</div>
        <div>The APIC defaults new LACP Policies to <code>true</code>.</div>
    </td>
    </tr>

    <tr>
    <td>graceful_convergence<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Determines if Graceful Convergence is enabled.</div>
        <div>This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.</div>
        <div>The APIC defaults new LACP Policies to <code>true</code>.</div>
    </td>
    </tr>

    <tr>
    <td>hostname<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>IP Address or hostname of APIC resolvable by Ansible control host.</div>
        </br><div style="font-size: small;">aliases: host</div>
    </td>
    </tr>

    <tr>
    <td>load_defer<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Determines if Load Defer is enabled.</div>
        <div>This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.</div>
        <div>The APIC defaults new LACP Policies to <code>false</code>.</div>
    </td>
    </tr>

    <tr>
    <td>max_links<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>16</td>
    <td><ul><li>Ranges from 1 to 16</li></ul></td>
    <td>
        <div>Maximum links (range 1-16).</div>
        <div>The APIC defaults new Port Channel Policies to <code>16</code>.</div>
    </td>
    </tr>

    <tr>
    <td>min_links<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1</td>
    <td><ul><li>Ranges from 1 to 16</li></ul></td>
    <td>
        <div>Minimum links (range 1-16).</div>
        <div>The APIC defaults new Port Channel Policies to <code>1</code>.</div>
    </td>
    </tr>

    <tr>
    <td>mode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>active</li><li>mac-pin</li><li>mac-pin-nicload</li><li>False</li><li>passive</li></ul></td>
    <td>
        <div>Port channel interface policy mode.</div>
        <div>Determines the LACP method to use for forming port-channels.</div>
        <div>The APIC defaults new Port Channel Polices to <code>off</code>.</div>
    </td>
    </tr>

    <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>The password to use for authentication.</div>
    </td>
    </tr>

    <tr>
    <td>port_channel<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the port channel.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>absent</li><li>present</li><li>query</li></ul></td>
    <td>
        <div>Use <code>present</code> or <code>absent</code> for adding or removing.</div>
        <div>Use <code>query</code> for listing an object or multiple objects.</div>
    </td>
    </tr>

    <tr>
    <td>suspend_individual<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Determines if Suspend Individual is enabled.</div>
        <div>This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.</div>
        <div>The APIC defaults new LACP Policies to <code>true</code>.</div>
    </td>
    </tr>

    <tr>
    <td>symmetric_hash<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Determines if Symmetric Hashing is enabled.</div>
        <div>This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.</div>
        <div>The APIC defaults new LACP Policies to <code>false</code>.</div>
    </td>
    </tr>

    <tr>
    <td>timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>30</td>
    <td></td>
    <td>
        <div>The socket level timeout in seconds.</div>
    </td>
    </tr>

    <tr>
    <td>use_proxy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <code>no</code>, it will not use a proxy, even if one is defined in an environment variable on the target hosts.</div>
    </td>
    </tr>

    <tr>
    <td>use_ssl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <code>no</code>, an HTTP connection will be used instead of the default HTTPS connection.</div>
    </td>
    </tr>

    <tr>
    <td>username<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>admin</td>
    <td></td>
    <td>
        <div>The username to use for authentication.</div>
        </br><div style="font-size: small;">aliases: user</div>
    </td>
    </tr>

    <tr>
    <td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <code>no</code>, SSL certificates will not be validated.</div>
        <div>This should only set to <code>no</code> used on personally controlled sites using self-signed certificates.</div>
    </td>
    </tr>

    </table>
    </br>



Examples
--------

 ::

    
    - aci_intf_policy_port_channel:
        hostname: '{{ inventory_hostname }}'
        username: '{{ username }}'
        password: '{{ password }}'
        port_channel: '{{ port_channel }}'
        description: '{{ description }}'
        min_links: '{{ min_links }}'
        max_links: '{{ max_links }}'
        mode: '{{ mode }}'


Notes
-----

.. note::
    - By default, if an environment variable ``<protocol>_proxy`` is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see `setting the environment <http://docs.ansible.com/playbooks_environment.html>`_), or by using the ``use_proxy`` option.
    - HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.



Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.

For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/testing` and :doc:`dev_guide/developing_modules`.
