# ArubaOS-CX REST API (Simplified Docs)

### `POST /boot`
**Summary**: Boot the current firmware version in use

**Parameters:**
- `image` (query, required): image type


---
### `GET /certificates`
**Summary**: Get certificates

**Parameters:**
None

---
### `POST /certificates`
**Summary**: Generate CSR or create self-signed certificate

**Parameters:**
- `certificate request` (body, required): certificate request


---
### `DELETE /certificates/{certificate_name}`
**Summary**: Delete certificate

**Parameters:**
- `certificate_name` (path, required): certificate name


---
### `GET /certificates/{certificate_name}`
**Summary**: Get certificate details

**Parameters:**
- `certificate_name` (path, required): certificate name


---
### `PUT /certificates/{certificate_name}`
**Summary**: Install signed certificate

**Parameters:**
- `certificate_name` (path, required): certificate name
- `certificate` (body, required): certificate in pem format


---
### `GET /firmware`
**Summary**: Get the current firmware version

**Description**: Get the current firmware version.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
None

---
### `POST /firmware`
**Summary**: Upload new firmware

**Parameters:**
- `fileupload` (formData, required): firmware file
- `image` (query, required): image type


---
### `PUT /firmware`
**Summary**: Copy image from remote server to switch.

**Parameters:**
- `image` (query, required): image type
- `from` (query, required): Source location. Full URL. i.e. http://{ip|host}[:port]/image-name
- `vrf` (query, optional): VRF Name.


---
### `GET /firmware/status`
**Summary**: Get the current firmware upgrade status

**Description**: Get the current firmware upgrade status

This URI is not supported by Notification feature and by NAE.

**Parameters:**
None

---
### `GET /fullconfigs`
**Summary**: Retrieve list of configurations

**Description**: Retrieve list of configurations.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
None

---
### `GET /fullconfigs/{local-config}`
**Summary**: Copy local configuration to remote

**Description**: Copy local configuration  (e.g., 'running-config', 'startup-config') to remote

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `local-config` (path, required): Configuration name. Possible values: running-config or startup-config
- `to` (query, required): Destination location. Full URL. i.e. tftp://{ip|host}[:port]/config-file-name
- `type` (query, required): Type. i.e json or cli
- `vrf` (query, required): VRF Name.


---
### `PUT /fullconfigs/{local-config}`
**Summary**: Copy remote configuration to local

**Description**: Copy remote configuration to local (e.g., 'running-config', 'startup-config')

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `local-config` (path, required): Configuration name. Possible values: running-config or startup-config
- `from` (query, required): Source location. Full URL. i.e. tftp://{ip|host}[:port]/config-file-name
- `vrf` (query, required): VRF Name.


---
### `GET /fullconfigs/{name}`
**Summary**: Retrieve configuration by name

**Description**: Retrieve configuration by name (e.g., 'running-config', 'startup-config')

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `name` (path, required): Configuration name. Possible values: running-config, startup-config, or any other checkpoint configuration name


---
### `PUT /fullconfigs/{name}`
**Summary**: Upload a new running configuration

**Description**: Upload a new running configuration.

**Parameters:**
- `name` (path, required): Configuration name. Possible values: running-config, startup-config
- `config` (body, required): Configuration content.


---
### `PUT /fullconfigs/{to}`
**Summary**: Copy a configuration to/from running-config or startup-config

**Description**: Copy a configuration.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `to` (path, required): Destination configuration name. Possible values: running-config, startup-config, or any other checkpoint configuration name
- `from` (query, required): Source configuration name. Full URL. i.e. /rest/v1/fullconfigs/startup-config


---
### `POST /login`
**Summary**: User login

**Description**: Use username and password to log user in

**Parameters:**
- `username` (formData, required): User name
- `password` (formData, required): Password


---
### `POST /logout`
**Summary**: User logout

**Description**: Log user out of the system

**Parameters:**
None

---
### `GET /logs/audit`
**Summary**: Get Audit log entries

**Description**: Get Audit log entries

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `since` (query, optional): Fetch logs since the time specified. Valid format: YYYY-MM-DD hh:mm:ss. Relative words like yesterday, today, now, recent, this-week, week-ago, this-month, this-year are accepted.
- `until` (query, optional): Fetch logs until the time specified. Valid format: YYYY-MM-DD hh:mm:ss. Relative words like yesterday, today, now, recent, this-week, week-ago, this-month, this-year are accepted.
- `username` (query, optional): The Username of the session that is generating the log entry.
- `usergroup` (query, optional): Fetch logs logged by UserGroup specified.
- `session` (query, optional): Fetch logs of session type specified. Session type, could be REST or CLI
- `isConfig` (query, optional): Fetch logs of specified configuration type. isConfig type, could be yes or no


---
### `GET /logs/event`
**Summary**: Log entries

**Description**: Get log entries

**Parameters:**
- `priority` (query, optional): Log priority levels. Valid values 0-7. The format is either integer or integer range(e.g. 1..3). Single integer option will match events with equal or lower severity than this value. Integer range option will match all events with priority in the range.
- `since` (query, optional): Fetch logs since the time specified. Valid format: YYYY-MM-DD hh:mm:ss. Relative words like yesterday, today, now,1 day ago, 10 hours ago, 12 minutes ago are accepted. Words like hour ago, minute ago and day ago must precede with a positive integer and can be in plural form too.
- `until` (query, optional): Fetch logs until the time specified. Valid format: YYYY-MM-DD hh:mm:ss. Relative words like yesterday, today, now,1 day ago, 10 hours ago, 12 minutes ago are accepted. Words like hour ago, minute ago and day ago must precede with a positive integer and can be in plural form too.
- `limit` (query, optional): Number of log entries in the response.Valid range is 1-1000
- `MESSAGE` (query, optional): Exact log message that is expected to be matched.
- `MESSAGE_ID` (query, optional): A comma separated list of 128-bit message identifiers for recognizing certain message types.  Use MESSAGE_ID 50c0fa81c2a545ec982a54293f1b1945 and 73d7a43eaf714f97bbdf2b251b21cade to query all of the events in the systemd journal.
- `EVENT_CATEGORY` (query, optional): The event category. For retrieving only the events in a specific category.
- `SYSLOG_IDENTIFIER` (query, optional): This is the module generating the log message. Use this field to filter logs by a specific module.
- `NAE_AGENT_NAME` (query, optional): The NAE agent name. This field is only included in messages sent by NAE backend when an alert happens and indicates which agent generated that alert.
- `_PID` (query, optional): The Process ID of the process that is generating the log entry.
- `_GID` (query, optional): The Group ID of the process that is generating the log entry.
- `_UID` (query, optional): The User ID of the process that is generating the log entry.


---
### `DELETE /nae/data`
**Summary**: Delete/Clear Time Series and Alerts Data

**Description**: Delete/Clear Time Series and Alerts Data.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
None

---
### `GET /ping`
**Summary**: Get ping statistics

**Description**: Get ping statistics.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `ping_target` (query, required): ping IP address
- `is_ipv4` (query, required): true if ping_target is an IPv4 address
- `ping_data_fill` (query, optional): ping dataFill pattern in hexadecimal, and maximum pattern data less than 32
- `ping_data_size` (query, optional): set the packet size to n bytes, default value 100.
- `ping_time_out` (query, optional): ping timeout, default value 2
- `ping_interval` (query, optional): set ping interval, time between packets in seconds
- `ping_repetitions` (query, optional): send n ping signals, default value 5
- `ping_type_of_service` (query, optional): ping type of service
- `include_time_stamp` (query, optional): include time stamp
- `include_time_stamp_address` (query, optional): include time stamp address
- `record_route` (query, optional): route recorded
- `mgmt` (query, optional): VRF name/Management mutually exclusive. default value false


---
### `GET /reversessh_sessions`
**Summary**: Get list of SSH sessions

**Parameters:**
None

---
### `POST /reversessh_sessions`
**Summary**: Create SSH connection to the switch

**Parameters:**
- `Create SSH connection to the switch` (body, required): SSH connection values


---
### `DELETE /reversessh_sessions/{id}`
**Summary**: Delete an SSH connection to the switch

**Parameters:**
- `id` (path, required): RSSH id


---
### `GET /reversessh_sessions/{id}`
**Summary**: Get connection parameters of an SSH session

**Parameters:**
- `id` (path, required): RSSH id


---
### `GET /system`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/aaa_accounting_attributes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `accounting_mode` (filter, optional): Indicates mode of accounting records to be generated.<br>'start-stop' : In this mode, device sends a message to the<br>               configured accounting server indicating start<br>               of the accounting process for a client when a<br>               client logs in. It sends another message to the<br>               accounting server indicating end of the accounting<br>               process after the client logs out.<br>'stop-only'  : In this mode, device sends a message to the<br>               configured accounting server indicating end of<br>               the accounting process after a client logs out.<br>               No message is sent when the client logs in.<br><br>
- `interim_update_enable` (filter, optional): Enables the device to send interim network accounting updates<br>to the configured accounting server. This is only applicable<br>when the accounting mode is set to start-stop.<br><br>Key: boolean<br>
- `interim_update_interval` (filter, optional): Specifies the time interval(in minutes) between two successive<br>accounting updates sent to the server. This is only applicable<br>when interim update is enabled.<br><br>Minimum Value: 1<br>Maximum Value: 525600<br>
- `interim_update_onreauth_enable` (filter, optional): Enables the device to send interim network accounting updates<br>to the configured accounting server on client successful<br>reauthentication. This is only applicable when the accounting<br>mode is set to start-stop.<br><br>Key: boolean<br>
- `session_type` (filter, optional): Channel through which user is logging in:<br>'port-access'  : dot1x and mac-auth.<br><br>


---
### `POST /system/aaa_accounting_attributes`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/aaa_accounting_attributes/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Channel through which user is logging in:<br>'port-access'  : dot1x and mac-auth.<br><br>Reference Resource: [AAA_Accounting_Attributes](#!/AAA95Accounting95Attributes)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/aaa_accounting_attributes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Channel through which user is logging in:<br>'port-access'  : dot1x and mac-auth.<br><br>Reference Resource: [AAA_Accounting_Attributes](#!/AAA95Accounting95Attributes)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/aaa_accounting_attributes/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Channel through which user is logging in:<br>'port-access'  : dot1x and mac-auth.<br><br>Reference Resource: [AAA_Accounting_Attributes](#!/AAA95Accounting95Attributes)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/aaa_server_group_prios`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `session_type` (filter, optional): Channel through which user is logging in:<br>'ssh'          : Secure Shell<br>'console'      : Serial cable<br>'https-server' : REST API, Web UI etc.<br>'default'      : If authentication_group_prios, authorization_group_prios and/or<br>                 accounting_group_prios per channel i.e, ssh/console/https-server<br>                 is empty, then configuration from 'default' will be applied.<br><br>


---
### `GET /system/aaa_server_group_prios/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Channel through which user is logging in:<br>'ssh'          : Secure Shell<br>'console'      : Serial cable<br>'https-server' : REST API, Web UI etc.<br>'default'      : If authentication_group_prios, authorization_group_prios and/or<br>                 accounting_group_prios per channel i.e, ssh/console/https-server<br>                 is empty, then configuration from 'default' will be applied.<br><br>Reference Resource: [AAA_Server_Group_Prio](#!/AAA95Server95Group95Prio)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/aaa_server_group_prios/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Channel through which user is logging in:<br>'ssh'          : Secure Shell<br>'console'      : Serial cable<br>'https-server' : REST API, Web UI etc.<br>'default'      : If authentication_group_prios, authorization_group_prios and/or<br>                 accounting_group_prios per channel i.e, ssh/console/https-server<br>                 is empty, then configuration from 'default' will be applied.<br><br>Reference Resource: [AAA_Server_Group_Prio](#!/AAA95Server95Group95Prio)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/aaa_server_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `group_name` (filter, optional): Name of the server group.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `group_type` (filter, optional): 'none':   System-defined group, no members.<br>          All authentication requests against this group type<br>          will be automatically authorized.<br>'local':  System-defined group, no members.<br>          All authentication requests against this group type<br>          will be locally authorized.<br>'radius': System-defined group, open exclusively to RADIUS<br>          server members.<br>          All authentication requests against this group type<br>          will be authorized via RADIUS based on configuration<br>          order<br>'tacacs': System-defined group, open exclusively to TACACS+<br>          server members.<br>          All authentication requests against this group type<br>          will be authorized via TACACS based on configuration.<br>          order<br>'123xyz': User-defined group, open exclusively to RADIUS or<br>          TACACS+ server members but not both.<br>          All authentication requests against this group type<br>          will be authorized based on configuration order.<br><br>
- `origin` (filter, optional): Indicator of whether the group is built-in(system-defined)<br>or configured by the user. Unlike user configured groups,<br>built-in groups cannot be deleted.<br><br>


---
### `POST /system/aaa_server_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/aaa_server_groups/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the server group.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/aaa_server_groups/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the server group.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/aaa_server_groups/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the server group.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/acl_object_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of 'cfg_addresses' or 'cfg_ports' which<br>should be changed to a random value each time 'cfg_addresses' or<br>'cfg_ports' are modified.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `in_progress_version` (filter, optional): The version of the in-progress Object Group.  This value is<br>copied from 'cfg_version' when Object Group processing begins.<br>This value is cleared when the Object Group status is updated<br>to 'applied' or 'rejected.'<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `name` (filter, optional): Name of the ACL Object Group.<br><br>Maximum Length: 64<br>
- `object_type` (filter, optional): Type of ACL Object Group indicating which kind of entries<br>it contains. If the type is 'ipv4' or 'ipv6', the port attributes<br>are ignored. If the type is 'l4port', the address attributes are<br>ignored.<br><br>


---
### `POST /system/acl_object_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/acl_object_groups/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Name of the ACL Object Group.<br><br>Maximum Length: 64<br>Reference Resource: [ACL_Object_Group](#!/ACL95Object95Group)
- `id2` (path, required): Type of ACL Object Group indicating which kind of entries<br>it contains. If the type is 'ipv4' or 'ipv6', the port attributes<br>are ignored. If the type is 'l4port', the address attributes are<br>ignored.<br><br>Reference Resource: [ACL_Object_Group](#!/ACL95Object95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/acl_object_groups/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Name of the ACL Object Group.<br><br>Maximum Length: 64<br>Reference Resource: [ACL_Object_Group](#!/ACL95Object95Group)
- `id2` (path, required): Type of ACL Object Group indicating which kind of entries<br>it contains. If the type is 'ipv4' or 'ipv6', the port attributes<br>are ignored. If the type is 'l4port', the address attributes are<br>ignored.<br><br>Reference Resource: [ACL_Object_Group](#!/ACL95Object95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/acl_object_groups/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Name of the ACL Object Group.<br><br>Maximum Length: 64<br>Reference Resource: [ACL_Object_Group](#!/ACL95Object95Group)
- `id2` (path, required): Type of ACL Object Group indicating which kind of entries<br>it contains. If the type is 'ipv4' or 'ipv6', the port attributes<br>are ignored. If the type is 'l4port', the address attributes are<br>ignored.<br><br>Reference Resource: [ACL_Object_Group](#!/ACL95Object95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/acls`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of 'cfg_aces' that should be changed to a<br>random value each time 'cfg_aces' is modified.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `in_progress_version` (filter, optional): The version of the 'in_progress' Access Control List.  This value is copied from<br>'cfg_version' when the ACL processing begins. This value is cleared<br>when the ACL status is updated to 'applied' or 'rejected'.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `list_type` (filter, optional): Type of an Access Control List.<br><br>
- `name` (filter, optional): Name of an Access Control List.<br><br>Maximum Length: 64<br>


---
### `POST /system/acls`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/acls/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `id2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/acls/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `id2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/acls/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `id2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/acls/{pid1}/{pid2}/cfg_aces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `pid2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): 'permit': packets will be forwarded<br>'deny':   packets will be dropped<br>ACE will only be activated when an associated action is provided<br><br>
- `comment` (filter, optional): Comment associated with the ACE<br><br>Maximum Length: 256<br>
- `count` (filter, optional): ACE attribute count action: when true, increment hit count<br>for packets that match this ACL.<br><br>Key: boolean<br>
- `dscp` (filter, optional): Differentiated Services Code Point matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 63<br>
- `dst_ip` (filter, optional): Destination IP matching attribute:<br>If no IP address is specified, the ACL Entry<br>will not match on destination IP address. The<br>following IPv4 and IPv6 address formats are accepted.<br>IPv4 format (A.B.C.D | A.B.C.D/W.X.Y.Z)<br>IPv6 format (A:B::C:D | A:B::C:D/W:X::Y:Z)<br><br>Maximum Length: 100<br>
- `dst_l4_port_max` (filter, optional): Maximum IP destination port matching attribute: Used in<br>conjunction with dst_l4_port_min and dst_l4_port_range_reverse.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `dst_l4_port_min` (filter, optional): Minimum IP destination port matching attribute: Used in<br>conjunction with dst_l4_port_max and dst_l4_port_range_reverse.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `dst_mac` (filter, optional): Destination MAC matching attribute: <br>Format (AAAA.BBBB.CCCC | AAAA.BBBB.CCCC/XXXX.YYYY.ZZZZ)<br><br>Maximum Length: 29<br>
- `ecn` (filter, optional): Explicit Congestion Notification matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 3<br>
- `ethertype` (filter, optional): Ethernet type matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `fragment` (filter, optional): Fragment matching attribute.<br><br>Key: boolean<br>
- `icmp_code` (filter, optional): ICMP code matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `icmp_type` (filter, optional): ICMP type matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `ip_precedence` (filter, optional): IP Precedence matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `log` (filter, optional): ACE attribute log action: when true, log information<br>for packets that match this ACL.<br><br>Key: boolean<br>
- `pcp` (filter, optional): Priority Code Point matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `protocol` (filter, optional): IPv4 protocol matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `src_ip` (filter, optional): Source IP matching attribute:<br>If no IP address is specified, the ACL Entry<br>will not match on source IP address. The<br>following IPv4 and IPv6 address formats are accepted.<br>IPv4 format (A.B.C.D | A.B.C.D/W.X.Y.Z)<br>IPv6 format (A:B::C:D | A:B::C:D/W:X::Y:Z)<br><br>Maximum Length: 100<br>
- `src_l4_port_max` (filter, optional): Maximum L4 port to match on the packet.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `src_l4_port_min` (filter, optional): Minimum L4 port to match on the packet.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `src_mac` (filter, optional): Source MAC matching attribute: <br>Format (AAAA.BBBB.CCCC | AAAA.BBBB.CCCC/XXXX.YYYY.ZZZZ)<br><br>Maximum Length: 29<br>
- `tcp_ack` (filter, optional): TCP ACK flag matching attribute.<br><br>Key: boolean<br>
- `tcp_cwr` (filter, optional): TCP CWR flag matching attribute.<br><br>Key: boolean<br>
- `tcp_ece` (filter, optional): TCP ECE flag matching attribute.<br><br>Key: boolean<br>
- `tcp_established` (filter, optional): TCP Established state (ACK or RST flag is set).<br><br>Key: boolean<br>
- `tcp_fin` (filter, optional): TCP FIN flag matching attribute.<br><br>Key: boolean<br>
- `tcp_psh` (filter, optional): TCP PSH flag matching attribute.<br><br>Key: boolean<br>
- `tcp_rst` (filter, optional): TCP RST flag matching attribute.<br><br>Key: boolean<br>
- `tcp_syn` (filter, optional): TCP SYN flag matching attribute.<br><br>Key: boolean<br>
- `tcp_urg` (filter, optional): TCP URG flag matching attribute.<br><br>Key: boolean<br>
- `tos` (filter, optional): IP Type of Service value matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 31<br>
- `ttl` (filter, optional): Time-to-live matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `vlan` (filter, optional): VLAN-ID matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 4095<br>


---
### `POST /system/acls/{pid1}/{pid2}/cfg_aces`
**Summary**: Create a new resource instance

**Parameters:**
- `pid1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `pid2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `data` (body, required): data


---
### `DELETE /system/acls/{pid1}/{pid2}/cfg_aces/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `pid2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `id` (path, required): ACL_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/acls/{pid1}/{pid2}/cfg_aces/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `pid2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `id` (path, required): ACL_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/acls/{pid1}/{pid2}/cfg_aces/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `pid2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `id` (path, required): ACL_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/acls/{pid1}/{pid2}/cfg_aces/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid1` (path, required): Name of an Access Control List.<br><br>Maximum Length: 64<br>Reference Resource: [ACL](#!/ACL)
- `pid2` (path, required): Type of an Access Control List.<br><br>Reference Resource: [ACL](#!/ACL)
- `id` (path, required): ACL_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/adc_lists`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `GET /system/adc_lists/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Name of Analytics Data Collection List.<br><br>Maximum Length: 64<br>Reference Resource: [ADC_List](#!/ADC95List)
- `id2` (path, required): Type of Analytics Data Collection List.<br><br>Reference Resource: [ADC_List](#!/ADC95List)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/all_user_copp_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of the 'cfg_cpes' column. It should be written a random value (signed 53 bit)<br>every time cfg_aces is modified to prevent overlaps with restored checkpoints.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `hw_default` (filter, optional): When true, this represents the hardware default CoPP policy.<br><br>Key: boolean<br>
- `in_progress_version` (filter, optional): The version of the 'in_progress' Control Plane Policing Policy.  This value is<br>copied from the cfg_version column when the policy processing begins. This value<br>is cleared when the policy status is updated to 'applied' or 'rejected.'<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `name` (filter, optional): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>


---
### `POST /system/all_user_copp_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/all_user_copp_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/all_user_copp_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/all_user_copp_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/all_user_copp_policies/{pid}/cfg_cpes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `burst` (filter, optional): The burst in units of packets. Optional parameter. If no burst is specified, the<br>entry will not use burst for policing.<br><br>Minimum Value: 0<br>Maximum Value: 9999<br>
- `hw_default` (filter, optional): When true, this represents the hardware default CoPP policy entry for this<br>class.<br><br>Key: boolean<br>
- `priority` (filter, optional): The local priority for an entry in the CoPP policy.<br><br>Minimum Value: 0<br>Maximum Value: 10<br>
- `rate` (filter, optional): The rate limit in units of packets-per-second.<br><br>Minimum Value: 0<br>Maximum Value: 99999<br>


---
### `POST /system/all_user_copp_policies/{pid}/cfg_cpes`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `data` (body, required): data


---
### `DELETE /system/all_user_copp_policies/{pid}/cfg_cpes/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `id` (path, required): CoPP_Policy_Entry class<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/all_user_copp_policies/{pid}/cfg_cpes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `id` (path, required): CoPP_Policy_Entry class<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/all_user_copp_policies/{pid}/cfg_cpes/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of a Control Plane Policing (CoPP) Policy.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [CoPP_Policy](#!/CoPP95Policy)
- `id` (path, required): CoPP_Policy_Entry class<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/aruba_central`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/aruba_central`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/bgp_aspath_filters`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `description` (filter, optional): Free form description of the filter<br><br>Maximum Length: 80<br>
- `name` (filter, optional): Name of the filter.<br><br>Maximum Length: 80<br>


---
### `POST /system/bgp_aspath_filters`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/bgp_aspath_filters/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/bgp_aspath_filters/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/bgp_aspath_filters/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/bgp_aspath_filters/{pid}/bgp_aspath_filter_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): Action to be taken if the 'regex' matches<br><br>
- `regex` (filter, optional): POSIX compliant regular expression applied against the AS Path<br><br>Maximum Length: 32<br>


---
### `POST /system/bgp_aspath_filters/{pid}/bgp_aspath_filter_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `data` (body, required): data


---
### `DELETE /system/bgp_aspath_filters/{pid}/bgp_aspath_filter_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `id` (path, required): BGP_ASPath_Filter_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/bgp_aspath_filters/{pid}/bgp_aspath_filter_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `id` (path, required): BGP_ASPath_Filter_Entry preference<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/bgp_aspath_filters/{pid}/bgp_aspath_filter_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_ASPath_Filter](#!/BGP95ASPath95Filter)
- `id` (path, required): BGP_ASPath_Filter_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/bgp_community_filters`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `description` (filter, optional): Free form description of the filter.<br><br>Maximum Length: 80<br>
- `name` (filter, optional): Name of the filter.<br><br>Maximum Length: 80<br>
- `type` (filter, optional): Filter type:<br>'extcommunity-list'       : a list that matches extended community numbers<br>'extcommunity-expanded-list' : a list that matches extended community numbers using POSIX regular expressions<br>'community-list'          : a list that matches standard community numbers <br>'community-expanded-list' : a list that matches community numbers using POSIX regular expressions<br><br>


---
### `POST /system/bgp_community_filters`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/bgp_community_filters/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/bgp_community_filters/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/bgp_community_filters/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/bgp_community_filters/{pid}/bgp_community_filter_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): Action to be taken if 'match_string' matches'<br><br>
- `match_string` (filter, optional): String to be matched with the BGP Community/extended-community string. When the 'type' <br>of community list entry is either 'community-list' or 'extcommunity-list' <br>this field should be a list of community or extended community numbers respectively.<br>Ex: '1:1 2:2 3:3'.<br>When the 'type' is 'community-expanded-list', or 'extcommunity-expanded-list',<br>this field should contain a POSIX regular expression to match the corresonding community string.<br>Ex: '[0-9]+:[0-9]+'<br><br>Maximum Length: 256<br>


---
### `POST /system/bgp_community_filters/{pid}/bgp_community_filter_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `data` (body, required): data


---
### `DELETE /system/bgp_community_filters/{pid}/bgp_community_filter_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `id` (path, required): BGP_Community_Filter_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/bgp_community_filters/{pid}/bgp_community_filter_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `id` (path, required): BGP_Community_Filter_Entry preference<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/bgp_community_filters/{pid}/bgp_community_filter_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of the filter.<br><br>Maximum Length: 80<br>Reference Resource: [BGP_Community_Filter](#!/BGP95Community95Filter)
- `id` (path, required): BGP_Community_Filter_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/captive_portal_profiles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of the captive portal profile.<br><br>Minimum Length: 2<br>Maximum Length: 128<br>
- `origin` (filter, optional): Origin of the captive portal profile, i.e., how the captive portal profile <br>is created.<br> `local`:      captive portal profile is configured locally on the switch.<br> `downloaded`: downloaded from Clearpass server.<br> `radius`:     translated from the attributes assigned by RADIUS server.<br><br>
- `url` (filter, optional): Captive portal redirect URL. Ex: http://www.testme.com/testme.cgi<br><br>Minimum Length: 1<br>Maximum Length: 1024<br>
- `url_hash_key` (filter, optional): A URL Hash key to provide security for the captive portal<br>exchange with Clearpass. The key is a shared<br>secret between Clearpass and the switch.<br><br>Minimum Length: 1<br>


---
### `POST /system/captive_portal_profiles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/captive_portal_profiles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the captive portal profile.<br><br>Minimum Length: 2<br>Maximum Length: 128<br>Reference Resource: [Captive_Portal_Profile](#!/Captive95Portal95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/captive_portal_profiles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the captive portal profile.<br><br>Minimum Length: 2<br>Maximum Length: 128<br>Reference Resource: [Captive_Portal_Profile](#!/Captive95Portal95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/captive_portal_profiles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the captive portal profile.<br><br>Minimum Length: 2<br>Maximum Length: 128<br>Reference Resource: [Captive_Portal_Profile](#!/Captive95Portal95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/classes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of 'cfg_entries' that should be changed to a<br>random value each time 'cfg_entries' is modified.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `in_progress_version` (filter, optional): The version of the 'in_progress' Class.  This value is copied from<br>'cfg_version' when Class processing begins. This value is cleared<br>when the Class status is updated to 'applied' or 'rejected.'<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `name` (filter, optional): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>
- `origin` (filter, optional): Origin of the class, i.e., how the class is provisioned:<br> `dynamic`:    class is provisioned dynamically via DUR from<br>               Clearpass server or via a NAS-Filter-Rule<br>               attribute from a RADIUS server.<br>`synthesized`: class has been dynamically synthesized<br>               by the system.<br> `static`:     class is provisioned by the administrator<br>               via CLI or REST.<br><br>
- `type` (filter, optional): Type of a Class.<br><br>


---
### `POST /system/classes`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/classes/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `id2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/classes/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `id2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/classes/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `id2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/classes/{pid1}/{pid2}/cfg_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `pid2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `comment` (filter, optional): Comment to associate with the specified class entry.<br><br>Maximum Length: 256<br>
- `count` (filter, optional): Class entry attribute count action: when true, increment hit count<br>for packets that match this Class.<br><br>Key: boolean<br>
- `dscp` (filter, optional): Differentiated Services Code Point matching attribute.<br>DSCP match is not supported when class type is gbp*<br><br>Minimum Value: 0<br>Maximum Value: 63<br>
- `dst_ip` (filter, optional): Destination IP matching attribute:<br>If no IP address is specified, the Class entry<br>will not match on destination IP address. The<br>following IPv4 and IPv6 address formats are accepted.<br>IPv4 format (A.B.C.D | A.B.C.D/W.X.Y.Z)<br>IPv6 format (A:B::C:D | A:B::C:D/W:X::Y:Z)<br>Destination IP match is not supported when class type is gbp*<br><br>Maximum Length: 100<br>
- `dst_l4_port_max` (filter, optional): Maximum IP destination port matching attribute: Used in <br>conjunction with dst_l4_port_min and dst_l4_port_range_reverse.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `dst_l4_port_min` (filter, optional): Minimum IP destination port matching attribute: Used in<br>conjunction with dst_l4_port_max and dst_l4_port_range_reverse.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `dst_mac` (filter, optional): Destination MAC matching attribute: <br>Format (AAAA.BBBB.CCCC | AAAA.BBBB.CCCC/XXXX.YYYY.ZZZZ)<br>Destination MAC match is not supported when class type is gbp*<br><br>Maximum Length: 29<br>
- `dst_role` (filter, optional): Destination role matching attribute.<br><br>Maximum Length: 128<br>
- `ecn` (filter, optional): Explicit Congestion Notification matching attribute.<br>Explicit Congestion match is not supported when class type is gbp*<br><br>Minimum Value: 0<br>Maximum Value: 3<br>
- `ethertype` (filter, optional): Ethernet type matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `fragment` (filter, optional): Fragment matching attribute. If not specified, the class entry<br>will not restrict matching to fragmented packets.<br><br>Key: boolean<br>
- `icmp_code` (filter, optional): ICMP code matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `icmp_type` (filter, optional): ICMP type matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `ip_precedence` (filter, optional): IP Precedence matching attribute.<br>IP Precedence match is not supported when class type is gbp*<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `origin` (filter, optional): Origin of the class-entry, i.e., how the class-entry is provisioned.<br> `dynamic`:     class entry is provisioned dynamically via DUR<br>                from Clearpass server or via a NAS-Filter-Rule<br>                attribute from a RADIUS server.<br> `synthesized`: class entry has been dynamically synthesized<br>                by the system.<br> `static`:      class entry is provisioned by the administrator<br>                via CLI or REST.<br><br>
- `pcp` (filter, optional): Priority Code Point matching attribute.<br>PCP match is not supported when class type is gbp*<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `protocol` (filter, optional): IPv4 protocol matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `src_ip` (filter, optional): Source IP matching attribute:<br>If no IP address is specified, the Class entry<br>will not match on source IP address. The<br>following IPv4 and IPv6 address formats are accepted.<br>IPv4 format (A.B.C.D | A.B.C.D/W.X.Y.Z)<br>IPv6 format (A:B::C:D | A:B::C:D/W:X::Y:Z)<br>Source IP match is not supported when class type is gbp*<br><br>Maximum Length: 100<br>
- `src_l4_port_max` (filter, optional): Maximum L4 port to match on the packet.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `src_l4_port_min` (filter, optional): Minimum L4 port to match on the packet.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `src_mac` (filter, optional): Source MAC matching attribute: <br>Format (AAAA.BBBB.CCCC | AAAA.BBBB.CCCC/XXXX.YYYY.ZZZZ)<br>Source MAC match is not supported when class type is gbp*<br><br>Maximum Length: 29<br>
- `src_role` (filter, optional): Source role matching attribute.<br><br>Maximum Length: 128<br>
- `tcp_ack` (filter, optional): TCP ACK flag matching attribute.<br><br>Key: boolean<br>
- `tcp_cwr` (filter, optional): TCP CWR flag matching attribute.<br><br>Key: boolean<br>
- `tcp_ece` (filter, optional): TCP ECE flag matching attribute.<br><br>Key: boolean<br>
- `tcp_established` (filter, optional): Match packets that are in an established state, (ACK or RST flag<br> is set).  If not specified, the class entry will not restrict<br>matching to established TCP connections.<br><br>Key: boolean<br>
- `tcp_fin` (filter, optional): TCP FIN flag matching attribute.<br><br>Key: boolean<br>
- `tcp_psh` (filter, optional): TCP PSH flag matching attribute.<br><br>Key: boolean<br>
- `tcp_rst` (filter, optional): TCP RST flag matching attribute.<br><br>Key: boolean<br>
- `tcp_syn` (filter, optional): TCP SYN flag matching attribute.<br><br>Key: boolean<br>
- `tcp_urg` (filter, optional): TCP URG flag matching attribute.<br><br>Key: boolean<br>
- `tos` (filter, optional): IP Type of Service value matching attribute.<br>IP Type of Service match is not supported when class type is gbp*<br><br>Minimum Value: 0<br>Maximum Value: 31<br>
- `ttl` (filter, optional): Time-to-live matching attribute.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `type` (filter, optional): Type of a class entry:<br>'match':  corresponding policy actions will be performed on<br>          the matching packets.<br>'ignore': matching packets will be processed as if<br>          no policy was applied.<br><br>
- `vlan` (filter, optional): VLAN-ID matching attribute.<br>VLAN-ID match is not supported when class type is gbp*<br><br>Minimum Value: 0<br>Maximum Value: 4095<br>


---
### `POST /system/classes/{pid1}/{pid2}/cfg_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `pid2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `data` (body, required): data


---
### `DELETE /system/classes/{pid1}/{pid2}/cfg_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `pid2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `id` (path, required): Class_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/classes/{pid1}/{pid2}/cfg_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `pid2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `id` (path, required): Class_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/classes/{pid1}/{pid2}/cfg_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid1` (path, required): Name of a Classifier Class (Class).<br><br>Maximum Length: 128<br>Reference Resource: [Class](#!/Class)
- `pid2` (path, required): Type of a Class.<br><br>Reference Resource: [Class](#!/Class)
- `id` (path, required): Class_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/cli_aliases`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `alias_definition` (filter, optional): Contains the set of commands to be executed when the shortcut name is used. Every<br>command is separated by ";". Runtime arguments can be specified using $1,<br>$2 and so on. Extra arguments, if any, are added at the end of last command. e.g:<br>Execute the command "alias mycmd hostname $1; console length $2; console width<br>$3" to configure "mycmd" as shortcut. On executing "mycmd Switch1 80 24", it<br>expands to "hostname Switch1; console length 80; console width 24" where <br>"mycmd" is stored in alias_name and "hostname $1; console length $2;<br>console width $3" will be saved in alias_definition respectively.<br>
- `alias_name` (filter, optional): Shortcut name configured by the user to execute a set of commands.<br>


---
### `POST /system/cli_aliases`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/cli_aliases/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Shortcut name configured by the user to execute a set of commands.<br>Reference Resource: [CLI_Alias](#!/CLI95Alias)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/cli_aliases/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Shortcut name configured by the user to execute a set of commands.<br>Reference Resource: [CLI_Alias](#!/CLI95Alias)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/cli_aliases/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Shortcut name configured by the user to execute a set of commands.<br>Reference Resource: [CLI_Alias](#!/CLI95Alias)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/device_profiles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `enable` (filter, optional): Enables the profile.<br><br>Key: boolean<br>
- `name` (filter, optional): The name of the profile.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>


---
### `POST /system/device_profiles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/device_profiles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The name of the profile.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Device_Profile](#!/Device95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/device_profiles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The name of the profile.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Device_Profile](#!/Device95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/device_profiles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The name of the profile.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Device_Profile](#!/Device95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/dhcp_relays`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `POST /system/dhcp_relays`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/dhcp_relays/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/dhcp_relays/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/dhcp_relays/{id1}/{id2}`
**Summary**: Create a new resource instance

**Parameters:**
- `id1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `data` (body, required): data


---
### `PUT /system/dhcp_relays/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/dhcp_relays/{pid1}/{pid2}/dhcp_relay_v6_mcast_servers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `pid2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `POST /system/dhcp_relays/{pid1}/{pid2}/dhcp_relay_v6_mcast_servers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `pid2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `data` (body, required): data


---
### `DELETE /system/dhcp_relays/{pid1}/{pid2}/dhcp_relay_v6_mcast_servers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `pid2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id` (path, required): DHCP_Relay_V6_Mcast_Server ipv6_multicast_address<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/dhcp_relays/{pid1}/{pid2}/dhcp_relay_v6_mcast_servers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `pid2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id` (path, required): DHCP_Relay_V6_Mcast_Server ipv6_multicast_address<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/dhcp_relays/{pid1}/{pid2}/dhcp_relay_v6_mcast_servers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid1` (path, required): VRF through which DHCP server is reachable.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `pid2` (path, required): Layer 3 Port on which the configuration is made.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [DHCP_Relay](#!/DHCP95Relay)
- `id` (path, required): DHCP_Relay_V6_Mcast_Server ipv6_multicast_address<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/dhcpv4_snooping_guard_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Policy name.<br><br>Maximum Length: 128<br>


---
### `POST /system/dhcpv4_snooping_guard_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/dhcpv4_snooping_guard_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [DHCPv4_Snooping_Guard_Policy](#!/DHCPv495Snooping95Guard95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/dhcpv4_snooping_guard_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [DHCPv4_Snooping_Guard_Policy](#!/DHCPv495Snooping95Guard95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/dhcpv4_snooping_guard_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [DHCPv4_Snooping_Guard_Policy](#!/DHCPv495Snooping95Guard95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/dhcpv6_snooping_guard_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Policy name.<br><br>Maximum Length: 128<br>


---
### `POST /system/dhcpv6_snooping_guard_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/dhcpv6_snooping_guard_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [DHCPv6_Snooping_Guard_Policy](#!/DHCPv695Snooping95Guard95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/dhcpv6_snooping_guard_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [DHCPv6_Snooping_Guard_Policy](#!/DHCPv695Snooping95Guard95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/dhcpv6_snooping_guard_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [DHCPv6_Snooping_Guard_Policy](#!/DHCPv695Snooping95Guard95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/dlogs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `module` (filter, optional): Name of the debug module.<br>All keyword is to enable all debug modules.<br><br>
- `severity` (filter, optional): Minimum severity for logging.<br><br>
- `sub_module` (filter, optional): Name of the sub_module of this module.<br>All keyword is to enable all sub_modules of this module.<br><br>


---
### `POST /system/dlogs`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/dlogs/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Name of the debug module.<br>All keyword is to enable all debug modules.<br><br>Reference Resource: [DLog](#!/DLog)
- `id2` (path, required): Name of the sub_module of this module.<br>All keyword is to enable all sub_modules of this module.<br><br>Reference Resource: [DLog](#!/DLog)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/dlogs/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Name of the debug module.<br>All keyword is to enable all debug modules.<br><br>Reference Resource: [DLog](#!/DLog)
- `id2` (path, required): Name of the sub_module of this module.<br>All keyword is to enable all sub_modules of this module.<br><br>Reference Resource: [DLog](#!/DLog)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/dlogs/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Name of the debug module.<br>All keyword is to enable all debug modules.<br><br>Reference Resource: [DLog](#!/DLog)
- `id2` (path, required): Name of the sub_module of this module.<br>All keyword is to enable all sub_modules of this module.<br><br>Reference Resource: [DLog](#!/DLog)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/evpn_instances`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `evi` (filter, optional): Index identifying the EVPN instance.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>
- `operational_failure_reason` (filter, optional): Operational failure reason of the EVPN instance:<br>'entity-not-up'           : EVPN entity is not up.<br>'admin-config'            : Admin status is disabled.<br>'resource-failure'        : Insufficient resources.<br>'no-if-info'              : Incomplete interface information.<br>'evi-not-up'              : EVPN instance is not up.<br>'bd-not-up'               : EVPN bridge domain is not up.<br>'no-route-distinguisher'  : No route distinguisher configured.<br>'route-dist-conflict'     : This EVPN instance's RD is the same as<br>                            another active instance's RD.<br>'no-esi'                  : No Ethernet Segment Identifier is available.<br>'bad-vni'                 : Invalid VNI.<br>'vni-conflict'            : There is another bridge domain with the<br>                            same VNI.<br>'vlan-sub-if-evi-conflict': Multiple VLAN sub-interfaces have been<br>                            configured for the same EVI on the same<br>                            Ethernet Segment.<br>'no-bgp-id'               : BGP router identifier is not yet available<br>                            to EVPN.<br>'rt-type-conflict'        : Configured route target and the auto-derived<br>                            route target have the same route target value<br>                            but different route target types.<br>'no-rt'                   : No configured route targets.<br>'ip-vrf-not-up'           : IP VRF instance is not up.<br>'no-system-mac'           : System MAC address is not known.<br>'rt-conflict'             : There is an another active route target<br>                            configured with the same route target value.<br><br>
- `operational_status` (filter, optional): Operational status of the EVPN instance:<br>'up'         : Active.<br>'down'       : Inactive.<br>'going-up'   : Activating.<br>'going-down' : Deactivating.<br>'act-failed' : Activation failed.<br><br>
- `rd` (filter, optional): Route distinguisher for this EVPN instance.<br><br>Maximum Length: 22<br>


---
### `GET /system/evpn_instances/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Index identifying the EVPN instance.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>Reference Resource: [EVPN_Instance](#!/EVPN95Instance)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/evpn_mac_ips`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `evi` (filter, optional): Index identifying the EVPN instance.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>
- `mac_address` (filter, optional): MAC address in AA:BB:CC:DD:EE:FF form.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `mac_mobility_seq_num` (filter, optional): MAC mobility sequence number associated with this MAC address<br>on this EVPN instance.<br><br>Key: integer<br>
- `mac_route_status` (filter, optional): MAC-only NLRI (no IP address associated with this NLRI) for this<br>MAC address on this EVPN instance.<br><br>Key: boolean<br>
- `nexthop` (filter, optional): EVPN next hop for the MAC/IP entry.<br><br>Maximum Length: 45<br>
- `source` (filter, optional): Source of this MAC/IP entry on this EVPN instance.<br><br>


---
### `GET /system/evpn_mac_ips/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Index identifying the EVPN instance.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>Reference Resource: [EVPN_MAC_IP](#!/EVPN95MAC95IP)
- `id2` (path, required): MAC address in AA:BB:CC:DD:EE:FF form.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [EVPN_MAC_IP](#!/EVPN95MAC95IP)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `DELETE /system/evpns`
**Summary**: Delete a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/evpns`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/evpns`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `PUT /system/evpns`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/evpns/evpn_vlans`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `rd` (filter, optional): EVPN RD in ASN:nn format or IP:nn format or 'auto'.<br><br>Maximum Length: 22<br>


---
### `POST /system/evpns/evpn_vlans`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/evpns/evpn_vlans/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): EVPN_VLAN vlan<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/evpns/evpn_vlans/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): EVPN_VLAN vlan<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/evpns/evpn_vlans/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): EVPN_VLAN vlan<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/external_storages`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address` (filter, optional): IP address or host name of the network attached storage.<br><br>Maximum Length: 255<br>
- `directory` (filter, optional): Directory to be accessed on the external storage.<br><br>Maximum Length: 128<br>
- `enable` (filter, optional): Enables access to specific storage volume.<br><br>Key: boolean<br>
- `name` (filter, optional): The name of the external storage volume.<br><br>Maximum Length: 64<br>
- `password` (filter, optional): Password to be used for SMB and SCP type storage.<br><br>Minimum Length: 8<br>Maximum Length: 192<br>
- `state` (filter, optional): Current state of external storage volume:<br><br>`operational`:           fully operational<br>`disabled`:              administratively disabled<br>`connecting`:            establishing connection to network attached storage<br>`unaccessible`:          network attached storage is not accessible due to connectivity issues<br>`invalid_credentials`:   invalid username and/or the password<br>`invalid_directory`:     directory doesn't exist or is not allowed to be accessed<br>`internal_error`:        any other error that might have happened during access to<br>                         the external storage<br><br>
- `type` (filter, optional): External storage access type:<br>'NFSv4': network attached storage, accessible through NFSv4 protocol<br>'NFSv3': network attached storage, accessible through NFSv3 protocol<br>'SMB':   network attached storage, accessible through SMB protocol (also known as CIFS or Windows Share)<br>'SCP':   network attached storage, accessible through secured shell protocol<br><br>
- `username` (filter, optional): User name to be used for SMB and SCP type storage.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>


---
### `POST /system/external_storages`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/external_storages/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The name of the external storage volume.<br><br>Maximum Length: 64<br>Reference Resource: [External_Storage](#!/External95Storage)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/external_storages/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The name of the external storage volume.<br><br>Maximum Length: 64<br>Reference Resource: [External_Storage](#!/External95Storage)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/external_storages/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The name of the external storage volume.<br><br>Maximum Length: 64<br>Reference Resource: [External_Storage](#!/External95Storage)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/gbp_role_name_id_maps`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `gbp_role_id` (filter, optional): The GBP role-id associated with this role.<br><br>Minimum Value: 0<br>Maximum Value: 8191<br>
- `gbp_role_name` (filter, optional): GBP role name.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>
- `origin` (filter, optional): <br>


---
### `POST /system/gbp_role_name_id_maps`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/gbp_role_name_id_maps/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): GBP role name.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>Reference Resource: [GBP_Role_Name_Id_Map](#!/GBP95Role95Name95Id95Map)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/gbp_role_name_id_maps/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): GBP role name.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>Reference Resource: [GBP_Role_Name_Id_Map](#!/GBP95Role95Name95Id95Map)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/gbp_role_name_id_maps/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): GBP role name.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>Reference Resource: [GBP_Role_Name_Id_Map](#!/GBP95Role95Name95Id95Map)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/hscs`
**Summary**: Delete a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/hscs`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/hscs`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `PUT /system/hscs`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/hw_default_copp_policy`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/hw_default_copp_policy`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/hw_default_copp_policy/cfg_cpes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `burst` (filter, optional): The burst in units of packets. Optional parameter. If no burst is specified, the<br>entry will not use burst for policing.<br><br>Minimum Value: 0<br>Maximum Value: 9999<br>
- `hw_default` (filter, optional): When true, this represents the hardware default CoPP policy entry for this<br>class.<br><br>Key: boolean<br>
- `priority` (filter, optional): The local priority for an entry in the CoPP policy.<br><br>Minimum Value: 0<br>Maximum Value: 10<br>
- `rate` (filter, optional): The rate limit in units of packets-per-second.<br><br>Minimum Value: 0<br>Maximum Value: 99999<br>


---
### `POST /system/hw_default_copp_policy/cfg_cpes`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/hw_default_copp_policy/cfg_cpes/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): CoPP_Policy_Entry class<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/hw_default_copp_policy/cfg_cpes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): CoPP_Policy_Entry class<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/hw_default_copp_policy/cfg_cpes/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): CoPP_Policy_Entry class<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/interfaces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `acl_init_status` (filter, optional): This enum is used to represent the initialization status<br>of an interface from the ACL feature perspective.<br>'none':    Interface is still initializing.<br>'success': ACL is successfully applied on the interface during<br>           initialization or there is no ACL on the interface<br>           or when LAG membership update succeeds.<br>'failure': ACL is not successfully applied on the interface<br>           during initialization or when LAG membership update<br>           fails.<br><br>
- `admin_state` (filter, optional): The administrative state of the physical network link.<br><br>
- `autonegotiation` (filter, optional): The autonegotiation setting of the physical network link.<br><br>
- `cdp_disable` (filter, optional): Disables reception and transmission of CDP packets on the<br>interface, regardless of the system level configuration.<br><br>Key: boolean<br>
- `cdp_pre_standard_mode` (filter, optional): Sets CDP pre standard mode in the interface :<br>'rx_only':If CDP voice VLAN query packet is received on this interface,<br>          the switch responds with the voice VLAN TLV included in its advertisements.<br>'tx_rx'  :The switch includes voice VLAN TLV in its advertisements on this interface <br>          regardless of whether it has received a query packet from the peer.<br>'disable':If CDP voice VLAN query packet is received on this interface, switch updates<br>          CDP neighbor information received from the peer, but doesn't send any CDP<br>          advertisements to it.<br><br>
- `coa_bounce` (filter, optional): Temporary shutdown is required due to Change of Authorization.<br><br>Key: boolean<br>
- `description` (filter, optional): Description for the 'system' interfaces<br><br>Minimum Length: 0<br>Maximum Length: 64<br>
- `dot1x_status` (filter, optional): Enumeration indicating the forwarding state of the interface when 802.1X<br>Authenticator is configured. * Up: The interface is eligible and should be<br>fowarding traffic according to 802.1X. * Blocked:  The interface is either not<br>eligible or should be blocked according to 802.1X. * Down:  802.1X is configured<br>on the interface, but it is either administratively or operatively down. This<br>field value will be empty if 802.1X Authenticator is not enabled on this<br>interface.<br><br>
- `duplex` (filter, optional): The duplex mode of the physical network link.<br><br>
- `error` (filter, optional): If the configuration of the [Interface](#!/Interface) failed, ArubaOS-CX sets this<br>column to an error description in human readable form.  Otherwise, ArubaOS-CX<br>clears this column.<br><br>Key: string<br>
- `error_control` (filter, optional): The status of Ethernet error control (error detection and correction) mode of<br>the physical network link. The error control can be implemented as forward error<br>correction (FEC). The FEC can be implemented using BASE-R (Firecode) or RS-FEC <br>(Reed-Solomon).<br><br>
- `evpn_force_shutdown` (filter, optional): A value of 'true' implies EVPN wants to shutdown the interface.<br><br>Key: boolean<br>
- `ifindex` (filter, optional): Unique ifindex for the interface.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `l1_current_state` (filter, optional): The current L1 state of the physical interface. This state is only valid <br>for interfaces of type `system`. <br><br>`inactive` - The interface is inactive and not enabled.<br><br>`pre_init` - The interface is prepared to begin linking.<br><br>`negotiate` - The interface is waiting for link.<br><br>`post_init` - The interface has linked and post-link configuration is done.<br><br>`ready` - The interface is ready for traffic.<br><br>`restart` - This state is deprecated and not used.<br><br>`failed` - The interface encountered a configuration error.<br><br>Key: string<br>
- `l1_next_state` (filter, optional): The requested L1 state of the physical interface. <br><br>`inactive` - The interface is inactive and not enabled.<br><br>`pre_init` - The interface is prepared to begin linking.<br><br>`negotiate` - The interface is waiting for link.<br><br>`post_init` - The interface has linked and post-link configuration is done.<br><br>`ready` - The interface is ready for traffic.<br><br>`restart` - This state is deprecated and not used.<br><br>`failed` - The interface encountered a configuration error.<br><br>Key: string<br>
- `lacp_current` (filter, optional): Boolean value indicating LACP status for this interface.  If true, this<br>interface has current LACP information about its LACP partner.  This information<br>may be used to monitor the health of interfaces in a LACP enabled port.  This<br>column will be empty if LACP is not enabled.<br><br>Key: boolean<br>
- `link_errors` (filter, optional): The number of times ArubaOS-CX has observed a link error on this [Interface](#!/Interface).<br><br>Key: integer<br>
- `link_resets` (filter, optional): The number of times ArubaOS-CX has observed the<br>[link_state](#!/Interface) of this [Interface](#!/Interface) change.<br><br>Key: integer<br>
- `link_speed` (filter, optional): The negotiated speed of the physical network link in bits per second. Valid<br>values are positive integers greater than 0.<br><br>Key: integer<br>
- `link_state` (filter, optional): The observed state of the physical network link.  This is ordinarily the link's<br>carrier status.<br><br>
- `lldp_med_loc_civic_info` (filter, optional): The civic info which includes 'country code' and 'what number' for<br>advertisements specific to LLDP-MED.<br><br>Minimum Length: 1<br>Maximum Length: 4<br>
- `lldp_med_loc_elin_info` (filter, optional): LLDP-MED Elin Location configured for this interface.<br><br>Minimum Length: 1<br>Maximum Length: 25<br>
- `lldp_mgmt_addr_list` (filter, optional): Comma separated list of local IPv4, IPv6 and MAC management addresses.<br>
- `loop_detected` (filter, optional): Indicates whether the loop is detected by Loop-protect.<br><br>Key: boolean<br>
- `mac_in_use` (filter, optional): The MAC address in use by this [Interface](#!/Interface).<br><br>Key: string<br>
- `mdi_mode` (filter, optional): The current MDI mode of the physical network link. This only applies to BASE-T<br>ports with links up, and will be empty otherwise.<br><br>
- `mstp_force_shutdown` (filter, optional): A value of 'true' implies MSTP wants to shutdown the interface.<br><br>Key: boolean<br>
- `mtu` (filter, optional): The MTU (maximum transmission unit); i.e. the largest amount of data that can<br>fit into a single Ethernet frame. The standard Ethernet MTU is 1500 bytes.  Some<br>physical media and many kinds of virtual interfaces can be configured with<br>higher MTUs.<br><br>This column will be empty for an interface that does not have an MTU as, for<br>example, some kinds of tunnels do not.<br><br>Key: integer<br>
- `name` (filter, optional): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>
- `num_clear_stats_performed` (filter, optional): Number of clear statistics performed.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `num_clear_stats_requested` (filter, optional): Number of clear statistics requested.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `origin` (filter, optional): Indicator of whether the interface is built-in (system-defined)<br>or configured.<br>Built-in interface cannot be modified or deleted by users.<br><br>
- `pause` (filter, optional): The status of the Ethernet PAUSE mode of the physical network link.<br><br>
- `pfc_priorities_applied` (filter, optional): Priority-based flow control priorities that are applied in the data path.<br>Empty if no priotity-based flow control is configured.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `pfc_priorities_config` (filter, optional): The user configured priorities for priority-based flow control.<br>This field is only valid when interface_flowcontrol_pfc capability <br>is present and the "pause" key of the user_config <br>is set to "pfc".<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `physical_interface_state` (filter, optional): The physical state of the interface.<br><br>`absent` - The state where the interface is absent and HW cannot be accessed.<br><br>`initializing` - The state where the interface is currently being initialized.<br>The interface should not be processed by any entity not involved in hardware<br>initialization and test.<br><br>`ready` - The state where the interface is considered available for the rest of<br>the system.<br><br>`failed` - The state where the interface had failed due to errors. Some examples<br>of errors are interface initialization and self-test. Normal interface<br>processing should not occur.<br><br>Key: string<br>
- `pm_state` (filter, optional): State of the pluggable module:<br>'DEFAULT': Default state when PMD is started OR.<br>           when interfaces are added to be processed.<br>'PARKED': Interface is no longer accessible.<br>'EMPTY': No transceiver is present.<br>'DETECTING_ADAPTER': QSFP-to-SFP adapter is being detected.<br>'IDENTIFYING_ADAPTER': QSFP-to-SFP adapter is being identified.<br>'INITIALIZING': Transceiver is being initialized.<br>'IDENTIFYING': Transceiver is being identified.<br>'INACTIVE': Transceiver is inactive due to failed access OR.<br>            failed identification OR incompatible type.<br>'DISALLOWED': Transceiver is not allowed to be enabled,<br>              since it is not supported.<br>'VALIDATING': Transceiver is being validated.<br>'DISABLED': Transceiver is administratively disabled.<br>'PRE_TUNING': Transceiver is checking and intializing tunings.<br>'TUNING': Transceiver is applying tunings.<br>'POST_TUNING': Transceiver has applied tunings and is enabling operation<br>'ENABLED': Transceiver is administratively enabled.<br>'ENABLING': Transceiver is being enabled (turned on).<br>'DISABLING': Transceiver is being disabled (turned off).<br><br>
- `policy_init_status` (filter, optional): This enum is used to represent the initialization status<br>of an interface from the classifier policy feature perspective.<br>'none':    Interface is still initializing.<br>'success': Policy is successfully applied on the interface<br>           during initialization or there is no policy on the<br>           interface or when LAG membership update succeeds.<br>'failure': Policy is not successfully applied on the interface<br>           during initialization or when LAG membership update<br>           fails.<br><br>
- `port_access_security_violation_shutdown` (filter, optional): A value of 'true' implies Port Access wants to shutdown the interface.<br><br>Key: boolean<br>
- `rate_interval` (filter, optional): Interval in seconds to calculate interface rate statistics.<br><br>Minimum Value: 5<br>Maximum Value: 300<br>
- `selftest_disable` (filter, optional): Specify *true* to disable and *false* to enable <br>for the respective interface<br><br>Key: boolean<br>
- `software_update_force_shutdown` (filter, optional): A value of 'true' implies that the interface should be shutdown.<br><br>Key: boolean<br>
- `split_admin_status` (filter, optional): The current administrative split status of the interface. <br>'none':     Interface cannot be split. <br>'inactive': Split interface is administratively inactive; <br>            either a parent that is configured as split or a <br>            child of a parent that is not. <br>'active':   Split interface is administratively active. <br><br>
- `split_oper_status` (filter, optional): The current operational split status of the interface. <br>This can be different from the administrative status when the <br>interface requires reinitialization to complete a split or <br>unsplit operation. Interface which can be split must be <br>administratively and operationally active to establish a link. <br><br>'none':     Interface cannot be split. <br>'inactive': Split interface is operationally inactive. <br>'active':   Split interface is operationally active. <br><br>
- `type` (filter, optional): The interface type, one of:<br><br>`system`:           Regular, physical interface of the system.<br>`internal_bridge`:  A simulated network device that represents the bridge and is used.<br>                    for providing L3 traffic to the control plane.<br>`vlan`:             Generally represents SVI - L3 Vlan interfaces.<br>`vlansubint`:       A sub-interface created for a physical interface based on dot1q encapsulation.<br>`loopback`:         A loopback interface is a virtual interface, supporting<br>                    ipv4/ipv6 address configuration, that remains up until it is deleted<br>                    by administrator. Loopback interface ip address is used as router-id<br>                    and source address by many protocols.<br>`gre_ipv4`:         ipv4 GRE tunnel.<br>`ipv6_in_ipv4`:     IPv6 in IPv4 tunnel.<br>`ipv6_in_ipv6`:     IPv6 in IPv6 tunnel.<br>`vxlan`:            VXLAN interface<br>`ubt`:              User Based Tunnel L2GRE interface<br><br>
- `udld_active` (filter, optional): The running state of the UDLD protocol on this interface.<br>For UDLD to be running, it has to be enabled and the link has to be up.<br><br>Key: boolean<br>
- `udld_arubaos_compatibility_mode` (filter, optional): Configured UDLD operation mode for ArubaOS. In `verify_then_forward` the<br>interface starts out blocked and will not forward traffic until UDLD determines<br>that the interface is bidirectional. With `forward_then_verify` the interface<br>starts out unblocked.<br><br>
- `udld_compatibility` (filter, optional): UDLD compatibility mode.<br><br>
- `udld_enable` (filter, optional): UDLD protocol is enabled or not on this interface.<br><br>Key: boolean<br>
- `udld_interface_state` (filter, optional): Reports the current interface state defined by the internal finite state machine of the UDLD protocol.<br><br>
- `udld_interface_status` (filter, optional): Reports the current interface status defined by the UDLD protocol. In `block` the<br>interface should not forward traffic. In `unblock` the interface can normally<br>forward traffic.<br><br>
- `udld_interval` (filter, optional): The time interval in milliseconds to send UDLD packets.  If 'udld_compatibility' value is 'rfc5171' and time interval is below valid range for RFC 5171 (7000 - 90000), then it will be forced to 7000.<br><br>Minimum Value: 10<br>Maximum Value: 90000<br>
- `udld_num_clear_stats_performed` (filter, optional): Number of clear statistics performed.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `udld_num_clear_stats_requested` (filter, optional): Number of clear statistics requested.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `udld_remote_interface_mac` (filter, optional): Remote interface MAC address.<br><br>Key: string<br>
- `udld_remote_interface_name` (filter, optional): Remote interface name.<br><br>Key: string<br>
- `udld_remote_system_id` (filter, optional): Remote system's ID. It corresponds to the remote bridge MAC address.<br><br>Key: string<br>
- `udld_retries` (filter, optional): Number of retries before changing the UDLD interface status to `block`.<br><br>Minimum Value: 3<br>Maximum Value: 10<br>
- `udld_rfc5171_compatibility_mode` (filter, optional): Configured UDLD operation mode for RFC5171. In `normal` mode, once the link is<br>determined to be in unidirectional state (after it was deemed bidireccional),<br>and no "Echo" is received, it is set to "undetermined" state. However, if a a<br>UDLD packet with an empty "Echo" is received the interface will be set to<br>"errDisabled". In `aggressive` , once a link is determined to be in<br>unidirectional state (after it was deemed bidirectional), and no "Echo" is<br>received, it is set to "errDisabled" state. The interface will also be set to<br>"errDisabled" if a UDLD packet with an empty "Echo" is received.<br><br>
- `vsx_force_shutdown` (filter, optional): A value of 'true' implies VSX wants to shutdown the interface.<br><br>Key: boolean<br>


---
### `POST /system/interfaces`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `GET /system/interfaces/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/interfaces/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/interfaces/{pid}/cdp_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cdpversion` (filter, optional): The CDP version that the neighbor is using.<br><br>Minimum Value: 1<br>Maximum Value: 2<br>
- `device_id` (filter, optional): Hostname of the neighbor.<br><br>Maximum Length: 256<br>
- `duplex` (filter, optional): Operating mode of the interface.<br><br>
- `last_update` (filter, optional): Time (in seconds from epoch) of the last CDP update received for this neighbor.<br>
- `mac_addr` (filter, optional): The MAC address that uniquely identifies the IEEE 802 LAN station<br>associated to the chassis of the neighboring CDP agent. This MAC<br> address is stored in the canonical format that includes six groups<br> of two hexadecimal digits separated by colons e.g. 01:23:45:AB:CD:EF<br>
- `native_vlan` (filter, optional): Native VLAN of the neighbor port.<br><br>Key: integer<br>
- `platform` (filter, optional): Hardware/model details of the neighbor.<br><br>Maximum Length: 256<br>
- `port_id` (filter, optional): Interface to which neighbor is connected.<br>
- `software_version` (filter, optional): Software version of the CDP neighbor.<br><br>Maximum Length: 1024<br>
- `voice_vlan_query` (filter, optional): Voice VLAN query value received from the neighbor.<br><br>Key: integer<br>


---
### `GET /system/interfaces/{pid}/cdp_neighbors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id` (path, required): The MAC address that uniquely identifies the IEEE 802 LAN station<br>associated to the chassis of the neighboring CDP agent. This MAC<br> address is stored in the canonical format that includes six groups<br> of two hexadecimal digits separated by colons e.g. 01:23:45:AB:CD:EF<br>Reference Resource: [CDP_Neighbor](#!/CDP95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/interfaces/{pid}/lldp_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `chassis_id` (filter, optional): The Chassis ID identifies the chassis containing the IEEE 802<br>LAN station associated with the transmitting LLDP agent.<br>
- `mac_addr` (filter, optional): The MAC address that uniquely identifies the IEEE 802 LAN station<br>associated to the chassis of the neighboring LLDP agent. This MAC<br>address is stored in the canonical format that includes six groups<br>of two hexadecimal digits separated by colons e.g. 01:23:45:AB:CD:EF.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `port_id` (filter, optional): The Port ID identifies the port component of the MSAP identifier<br>associated with the transmitting LLDP agent.<br>


---
### `GET /system/interfaces/{pid}/lldp_neighbors/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id1` (path, required): The Chassis ID identifies the chassis containing the IEEE 802<br>LAN station associated with the transmitting LLDP agent.<br>Reference Resource: [LLDP_Neighbor](#!/LLDP95Neighbor)
- `id2` (path, required): The Port ID identifies the port component of the MSAP identifier<br>associated with the transmitting LLDP agent.<br>Reference Resource: [LLDP_Neighbor](#!/LLDP95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/interfaces/{pid}/macsec_secies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cipher_suite` (filter, optional): The MACsec cipher-suite used to protect MACsec frames on this<br>SecY.<br> `gcm-aes-128`:     Use Galois/Counter mode of operation with the<br>                    AES-128 symmetric block cipher.<br> `gcm-aes-256`:     Use Galois/Counter mode of operation with the<br>                    AES-256 symmetric block cipher.<br> `gcm-aes-xpn-128`: Use Galois/Counter mode of operation with the<br>                    AES-128 symmetric block cipher with extended<br>                    packet numbering.<br> `gcm-aes-xpn-256`: Use Galois/Counter mode of operation with the<br>                    AES-256 symmetric block cipher with extended<br>                    packet numbering.<br><br>
- `confidentiality_disable` (filter, optional): Disable encryption on this SecY.<br><br>Key: boolean<br>
- `confidentiality_offset` (filter, optional): Confidentiality-offset to use on this SecY.<br> `byte_0`:  the entire Ethernet frame is sent encrypted.<br> `byte_30`: the data following the first 30 bytes of the Ethernet<br>            frame is sent encrypted.<br> `byte_50`: the data following the first 50 bytes of the Ethernet<br>            frame is sent encrypted.<br><br>
- `controlled_port_enable` (filter, optional): Enable the controlled port of this SecY.<br><br>Key: boolean<br>
- `controlled_port_state` (filter, optional): State of the controlled port (CP) associated with this SecY.<br>`init`:          The CP is initialized.<br>`secured`:       The CP is waiting for a new SAK to be generated.<br>`receive`:       A new SAK is generated and the receive SAs are<br>                 for the new SAK are created on the CP.<br>`receiving`:     The receive SAs are in use on the CP.<br>`ready`:         The CP is ready to transmit.<br>`transmit`:      The transmit SA is created on the CP.<br>`transmitting`:  The transmit SA is in use on the CP.<br>`abandon`:       The current SAs are being abandoned on the CP as<br>                 a result of a new SAK being generated.<br>`retire`:        The current SAs are being abandoned on the CP as<br>                 the SAK is use has expired.<br><br>
- `id` (filter, optional): The identifier associated with the SecY.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `include_sci_disable` (filter, optional): Disable inclusion of Secure Channel Identifier (SCI) in MACsec<br>frames on this SecY.<br><br>Key: boolean<br>
- `peer_mac` (filter, optional): MAC address of the peer that is bound to the SecY.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `replay_protect_disable` (filter, optional): Disable replay protection on this SecY.<br><br>Key: boolean<br>
- `replay_window` (filter, optional): Replay protection window associated with this SecY. When a<br>packet is received, it is processed only if the Packet Number<br>(PN) associated with this packet is within the replay window.<br>This is only applicable if the replay protection is enabled for<br>this SecY.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `type` (filter, optional): The type of the SecY.<br> `real`:    A SecY that is provisioned upfront and maps directly<br>            to the interface on which it is instantiated.<br> `virtual`: A SecY that is created on demand to provide<br>            separate secure connectivity associations over the<br>            same LAN.<br><br>


---
### `GET /system/interfaces/{pid}/macsec_secies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id` (path, required): The identifier associated with the SecY.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>Reference Resource: [MACsec_SecY](#!/MACsec95SecY)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/interfaces/{pid}/macsec_secies/{ppid}/macsec_secure_channels`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `ppid` (path, required): The identifier associated with the SecY.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>Reference Resource: [MACsec_SecY](#!/MACsec95SecY)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `channel_type` (filter, optional): The type of Secure Channel (SC).<br> `receive`:   This SC will be used to process traffic received<br>              from the peer(s).<br> `transmit`:  This SC will be used when transmitting traffic to<br>              the peer(s).<br><br>
- `create_time` (filter, optional): Time (in seconds) since system boot at which the SC was created.<br>
- `sci` (filter, optional): Unique identifier for a given secure channel. It comprises the<br>MAC address and a unique port number corresponding to the<br>interface that this secure channel is instantiated for.<br><br>Maximum Length: 16<br>
- `ssci` (filter, optional): A 32-bit value managed by the KaY. It is unique for each SCI<br>within the context of all MAC Security Entities (SecYs) using a<br>given Secure Association Key (SAK).<br>It is used in the validation functions of the GCM-AES-XPN Cipher<br>Suites.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `start_time` (filter, optional): Time (in seconds) since system boot when this SC started<br>transmitting or receiving frames.<br>
- `stop_time` (filter, optional): Time (in seconds) since system boot when this SC last received or<br>transmitted frames.<br>


---
### `GET /system/interfaces/{pid}/macsec_secies/{ppid}/macsec_secure_channels/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `ppid` (path, required): The identifier associated with the SecY.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>Reference Resource: [MACsec_SecY](#!/MACsec95SecY)
- `id1` (path, required): Unique identifier for a given secure channel. It comprises the<br>MAC address and a unique port number corresponding to the<br>interface that this secure channel is instantiated for.<br><br>Maximum Length: 16<br>Reference Resource: [MACsec_Secure_Channel](#!/MACsec95Secure95Channel)
- `id2` (path, required): The type of Secure Channel (SC).<br> `receive`:   This SC will be used to process traffic received<br>              from the peer(s).<br> `transmit`:  This SC will be used when transmitting traffic to<br>              the peer(s).<br><br>Reference Resource: [MACsec_Secure_Channel](#!/MACsec95Secure95Channel)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/interfaces/{pid}/poe_interface`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/interfaces/{pid}/poe_interface`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/interfaces/{pid}/tunnel_endpoints`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `destination` (filter, optional): IPv4 destination tunnel IP in the address format.<br>Example 192.168.1.1<br><br>Maximum Length: 15<br>
- `macs_invalid` (filter, optional): If `true`, indicates that MACs on this vtep are invalid.<br><br>Key: boolean<br>
- `origin` (filter, optional): Identifies the mechanism that is responsible for the<br>creation of the endpoint:<br>'static': user configuration<br>'evpn':   dynamically learnt via EVPN<br>'hsc':    dynamically learnt from a remote controller(e.g.NSX)<br><br>Key: string<br>
- `state` (filter, optional): Status of this tunnel endpoint:<br>'operational':         endpoint is fully provisioned in the forwarding path<br>'configuration_error': endpoint provisioning failed due to misconfiguration<br>'no_hw_resources':     endpoint provisioning failed due to insufficient resources<br>'activating':          endpoint is being provisioned<br><br>


---
### `POST /system/interfaces/{pid}/tunnel_endpoints`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `data` (body, required): data


---
### `DELETE /system/interfaces/{pid}/tunnel_endpoints/{id1}/{id2}/{id3}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id1` (path, required): VRF to be used for resolving the destination address.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id2` (path, required): Identifies the mechanism that is responsible for the<br>creation of the endpoint:<br>'static': user configuration<br>'evpn':   dynamically learnt via EVPN<br>'hsc':    dynamically learnt from a remote controller(e.g.NSX)<br><br>Key: string<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id3` (path, required): IPv4 destination tunnel IP in the address format.<br>Example 192.168.1.1<br><br>Maximum Length: 15<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/interfaces/{pid}/tunnel_endpoints/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id1` (path, required): VRF to be used for resolving the destination address.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id2` (path, required): Identifies the mechanism that is responsible for the<br>creation of the endpoint:<br>'static': user configuration<br>'evpn':   dynamically learnt via EVPN<br>'hsc':    dynamically learnt from a remote controller(e.g.NSX)<br><br>Key: string<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id3` (path, required): IPv4 destination tunnel IP in the address format.<br>Example 192.168.1.1<br><br>Maximum Length: 15<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/interfaces/{pid}/tunnel_endpoints/{id1}/{id2}/{id3}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id1` (path, required): VRF to be used for resolving the destination address.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id2` (path, required): Identifies the mechanism that is responsible for the<br>creation of the endpoint:<br>'static': user configuration<br>'evpn':   dynamically learnt via EVPN<br>'hsc':    dynamically learnt from a remote controller(e.g.NSX)<br><br>Key: string<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id3` (path, required): IPv4 destination tunnel IP in the address format.<br>Example 192.168.1.1<br><br>Maximum Length: 15<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `data` (body, required): data


---
### `PUT /system/interfaces/{pid}/tunnel_endpoints/{id1}/{id2}/{id3}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The interface name. For non-bonded ports, the interface name is the<br>same as the associated port name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Interface](#!/Interface)
- `id1` (path, required): VRF to be used for resolving the destination address.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id2` (path, required): Identifies the mechanism that is responsible for the<br>creation of the endpoint:<br>'static': user configuration<br>'evpn':   dynamically learnt via EVPN<br>'hsc':    dynamically learnt from a remote controller(e.g.NSX)<br><br>Key: string<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `id3` (path, required): IPv4 destination tunnel IP in the address format.<br>Example 192.168.1.1<br><br>Maximum Length: 15<br>Reference Resource: [Tunnel_Endpoint](#!/Tunnel95Endpoint)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ip_bindings`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the ip binding entry.<br><br>
- `clear_requested` (filter, optional): Set to `true` to delete the IP Binding entry.<br><br>Key: boolean<br>
- `from` (filter, optional): Source of the binding entry:<br>'<br>d<br>h<br>c<br>p<br>'<br>:<br> <br>b<br>i<br>n<br>d<br>i<br>n<br>g<br> <br>e<br>n<br>t<br>r<br>y<br> <br>l<br>e<br>a<br>r<br>n<br>e<br>d<br> <br>t<br>h<br>r<br>o<br>u<br>g<br>h<br> <br>D<br>H<br>C<br>P<br> <br>s<br>n<br>o<br>o<br>p<br>i<br>n<br>g<br>.<br>'static': binding is configured statically.<br>'<br>n<br>d<br>'<br>:<br> <br>b<br>i<br>n<br>d<br>i<br>n<br>g<br> <br>e<br>n<br>t<br>r<br>y<br> <br>l<br>e<br>a<br>r<br>n<br>e<br>d<br> <br>t<br>h<br>r<br>o<br>u<br>g<br>h<br> <br>N<br>D<br> <br>s<br>n<br>o<br>o<br>p<br>i<br>n<br>g<br>.<br><br>
- `ia_id` (filter, optional): Interface identifier of the client. Set only for IPv6 binding entries.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `ip_address` (filter, optional): An IP address that has been leased to or statically configured for this client.<br><br>Maximum Length: 45<br>
- `ip_binding_state` (filter, optional): State of the IP binding entry:<br>'valid':     IP binding entry is in 'valid' state.This is<br>             applicable for both DHCP snooping and ND snooping<br>             entries.<br>'tentative': IP binding entry is in 'tentative' state and DAD is <br>             in progress. This is applicable for ND snooping <br>             entries only.<br>'testing':   IP binding entry is in 'testing' state,An entry<br>             is in this state when the client is changing its<br>             its association from one port to another.<br>             This is applicable for ND snooping entries only.<br><br>
- `ip_source_lockdown_enabled` (filter, optional): Indicates whether IP Lockdown is enabled on this binding.<br>IP packets from the client are forwarded only if IP address, MAC address <br>and Port match the binding.<br><br>Key: boolean<br>
- `lease_expiration_time` (filter, optional): Lease expiration time in seconds from epoch for learned bindings.<br><br>Minimum Value: 1<br>
- `mac` (filter, optional): The MAC address of the DHCP client that this binding applies to.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `GET /system/ip_bindings/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): The VLAN ID on which this binding was learnt.<br><br>Reference Resource: [VLAN](#!/VLAN)<br>Reference Resource: [IP_Binding](#!/IP95Binding)
- `id2` (path, required): An IP address that has been leased to or statically configured for this client.<br><br>Maximum Length: 45<br>Reference Resource: [IP_Binding](#!/IP95Binding)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ipsla_responders`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `responder_ip` (filter, optional): IP address for listening for IP SLA probes.<br>If both responder_ip and responder_interface are provided responder_ip will be used.<br>If both responder_ip or responder_interface are NOT provided,<br>the responder listens on all L3 interfaces in a given VRF.<br><br>Maximum Length: 256<br>
- `responder_port_number` (filter, optional): TCP/UDP port number on which the responder needs to listen for the probes.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `status` (filter, optional): Running status of IP SLA responder:<br>`not_running_yet`:    responder is configured, but not running yet.<br>`running`:            responder is fully operational.<br>`bind_failure`:       TCP or UDP port number is being used by some other service.<br>`internal_error`:     unexpected error prevents responder operation.<br><br>
- `type` (filter, optional): Type of IP SLA:<br>`udp_echo`:         responds to UDP echo probes.<br>`tcp_connect`:      responds to TCP connect requests.<br>`udp_jitter_voip`:  responds to UDP VOIP probes.<br><br>


---
### `POST /system/ipsla_responders`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/ipsla_responders/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_responder](#!/ipsla95responder)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ipsla_responders/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_responder](#!/ipsla95responder)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/ipsla_responders/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `id` (path, required): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_responder](#!/ipsla95responder)
- `data` (body, required): data


---
### `PUT /system/ipsla_responders/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_responder](#!/ipsla95responder)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ipsla_responders/{pid}/ipsla_responder_statistics`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_responder](#!/ipsla95responder)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `last_probe_time` (filter, optional): Time (in seconds from epoch) when last probe was received from the source.<br>
- `num_of_pkts_received` (filter, optional): Number of packets received by the IP SLA responder.<br>
- `num_of_pkts_transmitted` (filter, optional): Number of packets responded back by the IP SLA responder.<br>
- `source_ip` (filter, optional): IP address of the IP SLA source from which the packets are being<br>received.<br>
- `source_port` (filter, optional): TCP/UDP port of the IP SLA source on which the session has been<br>established.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>


---
### `GET /system/ipsla_responders/{pid}/ipsla_responder_statistics/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): SLA name that uniquely identifies an IP SLA Responder.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_responder](#!/ipsla95responder)
- `id1` (path, required): IP address of the IP SLA source from which the packets are being<br>received.<br>Reference Resource: [ipsla_responder_statistics](#!/ipsla95responder95statistics)
- `id2` (path, required): TCP/UDP port of the IP SLA source on which the session has been<br>established.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [ipsla_responder_statistics](#!/ipsla95responder95statistics)
- `id3` (path, required): VRF on which the responder listens for IP SLA packets.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [ipsla_responder_statistics](#!/ipsla95responder95statistics)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ipsla_sources`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `domain_name_server` (filter, optional): IPv4/IPv6 address of the DNS server to be used for resolve destination hostnames.<br>If not provided, name server for the respective VRF will be used instead.<br><br>Maximum Length: 256<br>
- `effective_source_ip` (filter, optional): Source IP that is being used by the IP SLA outgoing probes that<br>belong to this specific session.<br><br>IP address is selected using following priority:<br>1. source_ip<br>2. source_interface<br>3. VRF.effective_source_ip.ipsla<br><br>If neither of them is populated, then regular routing rules takes place.<br><br>Minimum Length: 7<br>Maximum Length: 256<br>
- `enable` (filter, optional): Enables IP SLA session.<br><br>Key: boolean<br>
- `frequency` (filter, optional): Time gap (in seconds) between two consecutive probes of the SLA session.<br><br>Minimum Value: 5<br>Maximum Value: 604800<br>
- `name` (filter, optional): Unique identifier of the specific IP SLA session.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `payload_size` (filter, optional): Size of the payload to add to ICMP echo and UDP echo probes.<br><br>Minimum Value: 0<br>Maximum Value: 1440<br>
- `source_ip` (filter, optional): Source IPv4/IPv6 address for outgoing IP SLA packets.<br>If not specified, the address will either follow source_interface configuration<br>or if it's missing as well, will default to 'VRF.effective_source_ip.ipsla'.<br><br>Maximum Length: 256<br>
- `source_port_number` (filter, optional): In case of TCP and UDP probes, allows specification of the specific source port.<br>If not specified the port will be chosen by the system.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `tos` (filter, optional): Type of Service (TOS) to set on the packets of UDP echo, UDP VOIP and HTTP probes.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `type` (filter, optional): Type of IP SLA:<br>`icmp_echo`:         measures Round Trip Time(RTT) between source and<br>                     responder using ICMP .<br>`udp_echo`:          measures one way or RTT latency between<br>                     the source and the responder using UDP.<br>`tcp_connect`:       measures the time that it takes to perform TCP Connect<br>                     operation between the source and the responder.<br>`udp_jitter_voip`:   measures packet loss, one way delay, RTT,<br>                     Mean Opinion Scores (MOS),<br>                     (Impairment) Calculated Planning Impairment Factor (ICPIF)<br>                     between the source and the responder using VOIP traffic.<br>`http`:              measures HTTP or HTTPS response time for a web page.<br>                     This includes the time taken for DNS resolution, TCP connect,<br>                     SSL handshake(for HTTPS) and fetching of the web page.<br>'dns':               measures the time taken for DNS resolution<br>                     for the given hostname and nameserver.<br>'dhcp':              measures the time taken to perform DHCP operation<br>                     on the given source interface.<br><br>


---
### `POST /system/ipsla_sources`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/ipsla_sources/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Unique identifier of the specific IP SLA session.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_source](#!/ipsla95source)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ipsla_sources/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Unique identifier of the specific IP SLA session.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_source](#!/ipsla95source)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ipsla_sources/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Unique identifier of the specific IP SLA session.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [ipsla_source](#!/ipsla95source)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ipv6_destination_guard_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `enforcement` (filter, optional): Enforcement rule associated with this policy.<br>always : Destination guard will function always.<br>stressed : enforced only when the ND cache exceeds a certain threshold.<br><br>
- `name` (filter, optional): Policy name.<br><br>Maximum Length: 128<br>
- `nd_cache_threshold` (filter, optional): Specifies the nd-cache threshold value in the units of percentage<br>of ndmd internal cache. IPv6 destination guard, when configured with<br>stressed option, will get activated only when nd-cache exceeds this value.<br><br>Minimum Value: 1<br>Maximum Value: 90<br>


---
### `POST /system/ipv6_destination_guard_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/ipv6_destination_guard_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [IPv6_Destination_Guard_Policy](#!/IPv695Destination95Guard95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ipv6_destination_guard_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [IPv6_Destination_Guard_Policy](#!/IPv695Destination95Guard95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ipv6_destination_guard_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [IPv6_Destination_Guard_Policy](#!/IPv695Destination95Guard95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/keychains`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active_send_key` (filter, optional): Active send key corresponding to this keychain instance.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `name` (filter, optional): Name of the keychain.<br><br>Maximum Length: 32<br>


---
### `POST /system/keychains`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/keychains/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/keychains/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/keychains/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/keychains/{pid}/keys`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `accept_end` (filter, optional): Time since Epoch when the key will be de-activated.<br>The `accept_end` should be always greater than the `accept_start`.<br><br>Minimum Value: 1577836801<br>Maximum Value: 2556143999<br>
- `accept_start` (filter, optional): Time since Epoch from when the key will be active.<br><br>Minimum Value: 1577836800<br>Maximum Value: 2556143999<br>
- `auth_key` (filter, optional): Key used for authentication.<br><br>Minimum Length: 1<br>
- `auth_type` (filter, optional): The type of authentication associated with this Key.<br><br>
- `send_end` (filter, optional): Time since Epoch when the key will be de-activated.<br>The `send_end` should be always greater than the `send_start`.<br><br>Minimum Value: 1577836801<br>Maximum Value: 2556143999<br>
- `send_start` (filter, optional): Time since Epoch from when the key will be active.<br><br>Minimum Value: 1577836800<br>Maximum Value: 2556143999<br>


---
### `POST /system/keychains/{pid}/keys`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `data` (body, required): data


---
### `DELETE /system/keychains/{pid}/keys/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `id` (path, required): Key key_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/keychains/{pid}/keys/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `id` (path, required): Key key_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/keychains/{pid}/keys/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of the keychain.<br><br>Maximum Length: 32<br>Reference Resource: [Keychain](#!/Keychain)
- `id` (path, required): Key key_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/logging_filters`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>


---
### `POST /system/logging_filters`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/logging_filters/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/logging_filters/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/logging_filters/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/logging_filters/{pid}/logging_filter_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): Action applied on the selected events.<br><br>
- `match_regex` (filter, optional): Filter events using regular expression.<br><br>Minimum Length: 2<br>Maximum Length: 256<br>


---
### `POST /system/logging_filters/{pid}/logging_filter_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `data` (body, required): data


---
### `DELETE /system/logging_filters/{pid}/logging_filter_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `id` (path, required): Logging_Filter_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/logging_filters/{pid}/logging_filter_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `id` (path, required): Logging_Filter_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/logging_filters/{pid}/logging_filter_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Filter name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Logging_Filter](#!/Logging95Filter)
- `id` (path, required): Logging_Filter_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/mac_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>


---
### `POST /system/mac_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/mac_groups/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/mac_groups/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/mac_groups/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/mac_groups/{pid}/entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional):  `match`:        port access role will be applied.<br> `dont_match`:   port access role will not be applied.<br>MAC entry will be matched when an associated action is provided.<br><br>
- `mac` (filter, optional): The mac address to match. The format should match the mac_type configured.<br><br>Minimum Length: 8<br>Maximum Length: 17<br>
- `mac_type` (filter, optional): The following are the supported mac types in IEEE 802 format:<br> `mac`: mac entries are of the form AA:BB:CC:DD:EE:FF or aa:bb:cc:dd:ee:ff,<br> `mac-oui`:  mac-oui entries are of the form AA:BB:CC or aa:bb:cc,<br> `mac-mask`: mac-mask are of the form AA:BB:CC:DD/32 or aa:bb:cc:dd/32.<br><br>


---
### `POST /system/mac_groups/{pid}/entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `data` (body, required): data


---
### `DELETE /system/mac_groups/{pid}/entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `id` (path, required): MAC_Group_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/mac_groups/{pid}/entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `id` (path, required): MAC_Group_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/mac_groups/{pid}/entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The name of the mac-group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [MAC_Group](#!/MAC95Group)
- `id` (path, required): MAC_Group_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/mac_lockouts`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `from` (filter, optional): Origin of the MAC lockout entry:<br>`static`:             configured by the user.<br>`rogue_ap_isolation`: produced by Rouge AP Isolation feature.<br><br>
- `mac_addr` (filter, optional): MAC address to be locked out in the form of AA:BB:CC:DD:EE:FF.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `POST /system/mac_lockouts`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/mac_lockouts/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Origin of the MAC lockout entry:<br>`static`:             configured by the user.<br>`rogue_ap_isolation`: produced by Rouge AP Isolation feature.<br><br>Reference Resource: [MAC_Lockout](#!/MAC95Lockout)
- `id2` (path, required): MAC address to be locked out in the form of AA:BB:CC:DD:EE:FF.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [MAC_Lockout](#!/MAC95Lockout)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/mac_lockouts/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Origin of the MAC lockout entry:<br>`static`:             configured by the user.<br>`rogue_ap_isolation`: produced by Rouge AP Isolation feature.<br><br>Reference Resource: [MAC_Lockout](#!/MAC95Lockout)
- `id2` (path, required): MAC address to be locked out in the form of AA:BB:CC:DD:EE:FF.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [MAC_Lockout](#!/MAC95Lockout)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/mac_lockouts/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Origin of the MAC lockout entry:<br>`static`:             configured by the user.<br>`rogue_ap_isolation`: produced by Rouge AP Isolation feature.<br><br>Reference Resource: [MAC_Lockout](#!/MAC95Lockout)
- `id2` (path, required): MAC address to be locked out in the form of AA:BB:CC:DD:EE:FF.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [MAC_Lockout](#!/MAC95Lockout)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/macsec_kay_mka_participants`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/macsec_kay_mka_peers`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/macsec_kay_mkas`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/macsec_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `confidentiality_disable` (filter, optional): Disable encryption on the MACsec interface.<br><br>Key: boolean<br>
- `confidentiality_offset` (filter, optional): Number of octets in an Ethernet frame that are unencrypted.<br>This is only applicable when confidentiality is enabled for this<br>policy.<br> `byte_0`:  the entire Ethernet frame is sent encrypted.<br> `byte_30`: the data following the first 30 bytes of the Ethernet<br>            frame is sent encrypted.<br> `byte_50`: the data following the first 50 bytes of the Ethernet<br>            frame is sent encrypted.<br><br>
- `include_sci_disable` (filter, optional): Disable inclusion of Secure Channel Identifier (SCI) in MACsec<br>frames.<br><br>Key: boolean<br>
- `name` (filter, optional): Name of the MACsec policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `origin` (filter, optional): Origin of the MACsec policy, i.e., how the policy is provisioned:<br> `static`:  policy is provisioned by the administrator via CLI or<br>            REST.<br> `dynamic`: policy is provisioned based on attributes provided by<br>            the RADIUS server.<br><br>
- `replay_protect_disable` (filter, optional): Disable replay protection on the MACsec interface.<br><br>Key: boolean<br>
- `replay_window` (filter, optional): Replay protection window associated with this policy. When a<br>packet is received, it is processed only if the Packet Number<br>(PN) associated with this packet is within the replay window.<br>This is only applicable if the replay protection is enabled for<br>this policy.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `POST /system/macsec_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/macsec_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the MACsec policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [MACsec_Policy](#!/MACsec95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/macsec_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the MACsec policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [MACsec_Policy](#!/MACsec95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/macsec_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the MACsec policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [MACsec_Policy](#!/MACsec95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/macsec_secure_associations`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/mirrors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active` (filter, optional): The intended state of the mirror session: active or inactive. The<br>[operation_state](#!/Mirror) value contains the actual state<br>in hardware (e.g. active, inactive, or error). When missing or false, the state<br>is inactive.<br><br>Key: boolean<br>
- `comment` (filter, optional): Descriptive comment for the session.<br><br>Maximum Length: 64<br>
- `id` (filter, optional): The Mirror Session ID.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `session_type` (filter, optional): Mirror Session output/destination type.<br>'none'       : session doesn't have defined destination<br>'port'       : session mirrors to the physical interface<br>'cpu'        : session mirrors to the internal CPU<br>'tunnel'     : session mirrors into a tunnel<br><br>
- `statistics_clear_performed` (filter, optional): Number of times statistics were cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times statistics were requested to be cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `POST /system/mirrors`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/mirrors/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The Mirror Session ID.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>Reference Resource: [Mirror](#!/Mirror)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/mirrors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The Mirror Session ID.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>Reference Resource: [Mirror](#!/Mirror)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/mirrors/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The Mirror Session ID.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>Reference Resource: [Mirror](#!/Mirror)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/mka_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cak` (filter, optional): Secure Connectivity Assocation Key (CAK) associated with this<br>policy. This is only applicable when the mode is set to PSK.<br><br>
- `ckn` (filter, optional): Connectivity Association Key Name (CKN) associated with this<br>policy. This is only applicable when the mode is set to PSK.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `key_server_priority` (filter, optional): MKA participant priority used to determine which participant is<br>elected as the key server. A value of 255 indicates that this<br>participant will not become the key server.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `mode` (filter, optional): The MKA policy mode.<br> `psk`:     Policy mode is Pre-Shared Key. In this mode the CAK<br>            and CKN of the MKA policy are statically<br>            configured by the user.<br> `eap-tls`: Policy mode is EAP over Transport layer Security<br>            Protocol(TLS). In this mode, the CAK and CKN of the<br>            MKA policy are derived from EAP MSK<br>            (Master Session Key).<br><br>
- `name` (filter, optional): Name of the MKA policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `origin` (filter, optional): Origin of the MKA policy, i.e., how the policy is provisioned:<br> `static`:  policy is provisioned by the administrator via CLI or<br>            REST.<br> `dynamic`: policy is provisioned based on attributes provided by<br>            the RADIUS server.<br><br>
- `transmit_interval` (filter, optional): MKA transmit interval in seconds.<br><br>Minimum Value: 2<br>Maximum Value: 6<br>


---
### `POST /system/mka_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/mka_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the MKA policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [MKA_Policy](#!/MKA95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/mka_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the MKA policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [MKA_Policy](#!/MKA95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/mka_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the MKA policy.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [MKA_Policy](#!/MKA95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/mtraces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `group_address` (filter, optional): IP multicast group address of the stream whose path is to be traced.<br><br>Maximum Length: 45<br>
- `last_hop_router_address` (filter, optional): IP address of the gateway router to which the hosts are connected.<br><br>Maximum Length: 45<br>
- `source_address` (filter, optional): Source address of the IP multicast stream whose path is to be traced.<br><br>Maximum Length: 45<br>
- `time_to_live` (filter, optional): TTL value to be used when generating the Multicast trace packet.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `timestamp` (filter, optional): Time since epoch when this mtrace request was instantiated.<br>


---
### `GET /system/mtraces/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Source address of the IP multicast stream whose path is to be traced.<br><br>Maximum Length: 45<br>Reference Resource: [MTrace](#!/MTrace)
- `id2` (path, required): IP multicast group address of the stream whose path is to be traced.<br><br>Maximum Length: 45<br>Reference Resource: [MTrace](#!/MTrace)
- `id3` (path, required): Specifies the VRF corresponding to the stream whose path is <br>to be traced.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [MTrace](#!/MTrace)
- `id4` (path, required): Time since epoch when this mtrace request was instantiated.<br>Reference Resource: [MTrace](#!/MTrace)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/multicast_replication_portsets`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `author` (filter, optional): NAE Script author name<br><br>Key: string<br>
- `description` (filter, optional): NAE Script long description<br><br>Key: string<br>
- `expert_only` (filter, optional): Indicates whether the script requires expert level knowledge to deal with or not.<br><br>Key: boolean<br>
- `name` (filter, optional): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>
- `origin` (filter, optional): Defines the origin of the script. The script can either be user-defined or system defined.<br><br>
- `required_nae_api_version` (filter, optional): The version of NAE Script APIs required to run the NAE Script.<br><br>Key: string<br>
- `script` (filter, optional): NAE Script content in Base64.<br>The max length represents a 256KB script.<br><br>Maximum Length: 342000<br>
- `target_platform` (filter, optional): The target platform on which the NAE Script is designed to be<br>executed.<br><br>Key: string<br>
- `target_software_version` (filter, optional): The target software version on which the NAE Script is designed<br>to be executed.<br><br>Key: string<br>
- `version` (filter, optional): NAE Script version<br><br>Key: string<br>


---
### `POST /system/nae_scripts`
**Summary**: Create NAE Script

**Description**: Create nae script

**Parameters:**
- `script` (body, required): nae script entry


---
### `DELETE /system/nae_scripts/{id}`
**Summary**: Delete NAE Script

**Description**: Delete nae script

**Parameters:**
- `id` (path, required): name of nae script


---
### `GET /system/nae_scripts/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/nae_scripts/{id}`
**Summary**: Update NAE Script

**Description**: Update nae script

**Parameters:**
- `id` (path, required): name of nae script
- `script` (body, required): nae script entry


---
### `GET /system/nae_scripts/{pid}/nae_agents`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `disabled` (filter, optional): Disables the Agent, so it won't react to any alarms<br>actions, etc.<br><br>Key: boolean<br>
- `name` (filter, optional): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>
- `origin` (filter, optional): Defines the origin of the script. The script can either be user-defined or system defined.<br><br>


---
### `POST /system/nae_scripts/{pid}/nae_agents`
**Summary**: Create NAE Agent

**Parameters:**
- `pid` (path, required): name of nae script
- `agent` (body, required): nae agent


---
### `DELETE /system/nae_scripts/{pid}/nae_agents/{id}`
**Summary**: Delete NAE Agent

**Description**: Delete nae agent

**Parameters:**
- `id` (path, required): name of nae agent
- `pid` (path, required): name of nae script


---
### `GET /system/nae_scripts/{pid}/nae_agents/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `id` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/nae_scripts/{pid}/nae_agents/{id}`
**Summary**: Update NAE Agent

**Description**: Update nae agent

**Parameters:**
- `id` (path, required): name of nae agent
- `pid` (path, required): name of nae script
- `agent` (body, required): nae agent details


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_baselines`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `algorithm` (filter, optional): The algorithm used in the NAE baseline.<br>'max':                this algorithm uses the max over a period of time<br>                      to calculate the high theshold.<br>'standard_deviation': this algorithm uses the standard deviation<br>                      to calculate the high threshold.<br><br>
- `continuous_learning_window` (filter, optional): The time (in seconds) is the moving window used to smooth the data.<br>It is also the interval after which the thresholds are recalculated.<br>
- `high_threshold_factor` (filter, optional): Calculates the high threshold and depends on the algorithm<br>chosen in the NAE baseline definition.<br>
- `initial_learning_time` (filter, optional): The time (in seconds) during which NAE calculates the high and low thresholds of the baseline.<br>
- `learning_end_time` (filter, optional): Time (in seconds from Epoch) when learning ended.<br>
- `low_threshold_factor` (filter, optional): Calculate the low threshold and depends on the algorithm<br>chosen in the NAE baseline definition<br>
- `state` (filter, optional): The state of the baseline is: <br>'learning': the thresholds are still not finalized. Alerts will not be generated.<br>'active':   the baseline is operational and alerts will be generated as needed.<br>'inactive': the baseline is suspended. It generally happens when the agent is disabled.<br><br>
- `title` (filter, optional): Custom title of the NAE Baseline.<br><br>Key: string<br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_baselines/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `id` (path, required): NAE_Baseline name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_graphs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `dashboard_display` (filter, optional): Indicates whether the graph is to be displayed in dashboard <br>view of the Web UI.<br>
- `title` (filter, optional): Custom title to be used for a specific NAE Graph.<br>Here are some examples for NAE Graph custom title:<br>Averaged CPU utilization.<br>Averaged CPU utilization for CPU {}.<br>Every {} would be substituted by the value from <br>title_arguments.<br><br>Key: string<br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_graphs/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `id` (path, required): NAE_Graph name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_monitors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `aggregate_function` (filter, optional): The function used to aggregate the data of the monitored resource.<br>Empty value means that no aggregation is applied to the monitored resource.<br>The possible aggregator functions, including possible nested functions are:<br>'Rate':            When the monitored URI is wildcarded,this function finds the rate.<br>'Raw' :            Regular raw data points in the time series.<br>'Count':           This counts the number of distinct time-series that have been<br>                   generated and implicitly reflects the 'count' of data points<br>                   collected every scrape interval.<br>'Sum':             When the monitored URI is wildcarded, this function sums over the<br>                   current values of 'all' resources pointed to by expanding on the<br>                   wildcard.<br>'Min/Max':         When the monitored URI is wildcarded,these functions return the<br>                   min/max of the current value of 'all' currently present resource<br>                   pointed to by expanding on the wildcard.<br>'Average':         This function performs an average over the current value of 'all'<br>                   currently present resources pointed to by expanding on the wildcard.<br>'CountOverTime',<br>'SumOverTime',<br>'MinOverTime',<br>'MaxOverTime',<br>'AverageOverTime': When the keyword 'OverTime' follows one of the aggregators defined<br>                   above,the function behaves in a similar way but performs its<br>                   aggregation 'over' the specified time in the past instead of over<br>                   the current value only.<br>'Count_Rate',<br>'Count_CountOverTime',<br>'Count_Sum',<br>'Count_SumOverTime',<br>'Count_Min',<br>'Count_MinOverTime',<br>'Count_Max',<br>'Count_MaxOverTime',<br>'Count_Average',<br>'Count_AverageOverTime',<br>'Sum_Rate',<br>'Sum_Count',<br>'Sum_CountOverTime',<br>'Sum_SumOverTime',<br>'Sum_Min',<br>'Sum_MinOverTime',<br>'Sum_Max',<br>'Sum_MaxOverTime',<br>'Sum_Average',<br>'Sum_AverageOverTime',<br>'Min_Rate',<br>'Min_Count',<br>'Min_CountOverTime',<br>'Min_Sum',<br>'Min_SumOverTime',<br>'Min_MinOverTime',<br>'Min_Max',<br>'Min_MaxOverTime',<br>'Min_Average',<br>'Min_AverageOverTime',<br>'Max_Rate',<br>'Max_Count',<br>'Max_CountOverTime',<br>'Max_Sum',<br>'Max_SumOverTime',<br>'Max_Min',<br>'Max_MinOverTime',<br>'Max_MaxOverTime',<br>'Max_Average',<br>'Max_AverageOverTime',<br>'Average_Rate',<br>'Average_Count',<br>'Average_CountOverTime',<br>'Average_Sum',<br>'Average_SumOverTime',<br>'Average_Min',<br>'Average_MinOverTime',<br>'Average_Max',<br>'Average_MaxOverTime',<br>'Average_AverageOverTime': Nested Aggregate Functions - multiple functions are combined<br>                           to obtain the effect of the two functions.<br>                           For example, Sum_Rate initially computes the Rate,<br>                           then the Sum of the monitored resource.<br><br>
- `description` (filter, optional): NAE Monitor description<br><br>Maximum Length: 256<br>
- `multi_object_monitor` (filter, optional): Indicates whether the monitor is defined to monitor mutiple objects or single object.<br><br>Key: boolean<br>
- `name` (filter, optional): Name of the NAE Monitor<br>This has to be a CNAME starting with<br>NAE Agent name followed by<br>its own name<br>(i.e com.arubanetworks.bgp_monitor.agent1.condition1).<br>
- `time_interval` (filter, optional): The time interval used by the aggregation function<br>The format is 'number <unit>'<br>The <unit> can be: second, seconds, minute, minutes<br>day, days, hour, hours.<br>For example: '5 minutes', '1 day', '1 hour'<br><br>Key: string<br>
- `uri` (filter, optional): NAE Monitor uri that identifies the resource to be<br>monitored.<br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_monitors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `id` (path, required): NAE_Monitor name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_monitors/{pppid}/time_series`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Monitor name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of the Time Series.<br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_monitors/{pppid}/time_series/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Monitor name<br>
- `id` (path, required): Time_Series name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `description` (filter, optional): NAE Rule description<br><br>Maximum Length: 256<br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `id` (path, required): NAE_Rule name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{pppid}/nae_conditions`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Rule name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `expression` (filter, optional): Expression associated with the NAE Condition.<br>The grammar for condition language is defined as follows:<br>operand    = integer | enum<br>operator   = "<" | ">" | "==" | "!="<br>for        = "for" , integer , time<br>time       = "seconds" | "minutes" | "hours" | "days"<br>operation1 = uri , operator, operand , [ for ]<br>operation2 = "sum" , uri , operator , integer<br>operation3 = "rate" , uri , operator , float , "per" , time<br>operation4 = "transition" , uri , "from" , operand2 , "to" , operand2<br>Here are some examples:<br>transition /v1/system/vrfs/red/bgp_routers/101/bgp_neighbors/10.0.0.1/conn_state from "up" to "down<br>/v1/system/vrfs/red/bgp_routers/*/bgp_neighbors/count < 5 for 3 minutes<br>sum /v1/system/vrfs/red/bgp_routers/*/bgp_neighbors/count < 5 for 2 minutes<br>rate /v1/system/vlan/1/spanning_tree/tcn_count > 3 per hour<br>sum /v1/system/vrfs/red/bgp_routers/*/bgp_neighbors/count < {} for {} minutes<br>every {} would be substituted by the value from arguments.<br>
- `name` (filter, optional): Name of the NAE Condition.<br>This has to be a CNAME starting with<br>NAE Agent name followed by<br>its own name<br>(i.e com.arubanetworks.bgp_monitor.agent1.condition1).<br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{pppid}/nae_conditions/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Rule name<br>
- `id` (path, required): NAE_Condition name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{pppid}/nae_conditions/{ppppid}/actions`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Rule name<br>
- `ppppid` (path, required): NAE_Condition type<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `parameter` (filter, optional): Parameters to be used while executing an Action.<br>For syslog, parameter is the message to be send to the syslog<br>server.<br>For SHOW, parameter is the CLI command to be executed.<br>For CALLBACK, it will contain the script method name that will<br> be executed.<br>For SHELL, parameter is the command to be executed.<br>For ALERT_LEVEL, parameter is the alert level that the policy agent should be <br>changed to. Allowed values are "critical", "major", "minor" and "none".<br>
- `title` (filter, optional): Custom title to be used for a specific predefined NAE Action.<br><br>Key: string<br>
- `type` (filter, optional): Type of the nae action:<br>* `SYSLOG`: Send a local or remote message to a syslog server<br>* `CLI`: Executes a CLI command and stores the output so<br>   it can be accessed through an external application interface.<br>* `CALLBACK`: Executes a python callback method specified on the<br>   associated nae script. CALLBACK is only relevant<br>   for script based policy actions.<br>* `SHELL`: Executes a shell command and stores the output <br>   that can be accessed through an external application interface.<br>* `ALERT_LEVEL`: Change or remove the alert level of policy agent.<br>   Only relevant for policy actions created by the scripts.<br><br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{pppid}/nae_conditions/{ppppid}/actions/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Rule name<br>
- `ppppid` (path, required): NAE_Condition type<br>
- `id` (path, required): NAE_Action type<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{pppid}/nae_conditions/{ppppid}/nae_condition_events`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Rule name<br>
- `ppppid` (path, required): NAE_Condition type<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Unique name of the condition event.<br>
- `processed_actions_count` (filter, optional): Count of the actions that were executed for the condition event<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `status` (filter, optional): Condition Notification status:<br>* `PENDING`: The notificiation is waiting to be processed.<br>* `PROCESSING`: The notification is being processed.<br><br>


---
### `GET /system/nae_scripts/{pid}/nae_agents/{ppid}/nae_rules/{pppid}/nae_conditions/{ppppid}/nae_condition_events/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `ppid` (path, required): Name of a NAE Agent.<br>This has to be a CNAME starting with<br>NAE Script name followed by its<br>own name (i.e com.arubanetworks.bgp_monitor.agent1).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Agent](#!/NAE95Agent)
- `pppid` (path, required): NAE_Rule name<br>
- `ppppid` (path, required): NAE_Condition type<br>
- `id` (path, required): Unique name of the condition event.<br>Reference Resource: [NAE_Condition_Event](#!/NAE95Condition95Event)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/nae_scripts/{pid}/nae_parameters`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `default_value` (filter, optional): Value that should be assigned to the parameter during agent<br>instantiation if not provided.<br><br>Maximum Length: 256<br>
- `encrypt` (filter, optional): Specifies whether this parameter is encrypted when an agent is created<br><br>Key: boolean<br>
- `long_description` (filter, optional): Description of the NAE Parameter.<br><br>Maximum Length: 256<br>
- `required` (filter, optional): Specifies whether this parameter is required when an agent is created.<br>If the parameter is required and the user does not provide a value,<br>then the NAE Agent will be considered invalid and will be in an error state.<br><br>Key: boolean<br>
- `short_description` (filter, optional): Short description of the NAE Parameter.<br><br>Maximum Length: 64<br>
- `type` (filter, optional): Type of the nae parameter.<br>* `FLOAT`: Specifies a Parameter where its contents will<br>             always contain a decimal value<br>* `INTEGER`: Specifies a Parameter where its contents will<br>             always contain a signed 64 bit integer value<br>* `STRING`: Specifies a Parameter where its contents will <br>           always contain a string value<br><br>


---
### `GET /system/nae_scripts/{pid}/nae_parameters/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a NAE Script.<br>This has to be a valid canonical name (CNAME)<br>(i.e com.arubanetworks.bgp_monitor).<br><br>Minimum Length: 3<br>Maximum Length: 80<br>Reference Resource: [NAE_Script](#!/NAE95Script)
- `id` (path, required): NAE_Parameter name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/notification_subscribers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of the notification subscriber.<br>
- `type` (filter, optional): Notification transport type.<br>* `ws`: Notifications will be sent via WebSockets.<br><br>


---
### `GET /system/notification_subscribers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the notification subscriber.<br>Reference Resource: [Notification_Subscriber](#!/Notification95Subscriber)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/notification_subscribers/{pid}/notification_subscriptions`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the notification subscriber.<br>Reference Resource: [Notification_Subscriber](#!/Notification95Subscriber)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `GET /system/notification_subscribers/{pid}/notification_subscriptions/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the notification subscriber.<br>Reference Resource: [Notification_Subscriber](#!/Notification95Subscriber)
- `id` (path, required): Notification_Subscription name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ntp_keys`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `key_id` (filter, optional): Specifies a key_id which is used for NTP authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65534<br>
- `key_password` (filter, optional): Specifies an encrypted key_password which is used for NTP authentication.<br><br>Minimum Length: 8<br>Maximum Length: 128<br>
- `key_type` (filter, optional): Specifies an encrypted key_type which is used for NTP authentication.<br><br>
- `trust_enable` (filter, optional): Enables trust settings for this key_id..<br>


---
### `POST /system/ntp_keys`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/ntp_keys/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Specifies a key_id which is used for NTP authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65534<br>Reference Resource: [NTP_Key](#!/NTP95Key)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ntp_keys/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Specifies a key_id which is used for NTP authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65534<br>Reference Resource: [NTP_Key](#!/NTP95Key)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ntp_keys/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Specifies a key_id which is used for NTP authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65534<br>Reference Resource: [NTP_Key](#!/NTP95Key)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/pbr_action_lists`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of a PBR Action List.<br><br>Maximum Length: 64<br>


---
### `POST /system/pbr_action_lists`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/pbr_action_lists/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/pbr_action_lists/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/pbr_action_lists/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/pbr_action_lists/{pid}/cfg_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `ip` (filter, optional): Routing gateway address.<br>IPv4 format (A.B.C.D)<br>IPv6 format (A:B::C:D)<br><br>Maximum Length: 100<br>
- `type` (filter, optional): Type of a PBR Action List Entry.<br><br>


---
### `POST /system/pbr_action_lists/{pid}/cfg_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `data` (body, required): data


---
### `DELETE /system/pbr_action_lists/{pid}/cfg_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `id` (path, required): PBR_Action_List_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/pbr_action_lists/{pid}/cfg_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `id` (path, required): PBR_Action_List_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/pbr_action_lists/{pid}/cfg_entries/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `id` (path, required): PBR_Action_List_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/pbr_action_lists/{pid}/cfg_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of a PBR Action List.<br><br>Maximum Length: 64<br>Reference Resource: [PBR_Action_List](#!/PBR95Action95List)
- `id` (path, required): PBR_Action_List_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/pim_clear_mroute_requests`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/pim_clear_mroute_requests`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `PUT /system/pim_clear_mroute_requests`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/pki_est_profiles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `arbitrary_label` (filter, optional): The generic arbitrary label to be concatenated with the <br>EST profile URL to request EST service.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `arbitrary_label_enrollment` (filter, optional): The arbitrary label to be concatenated with the <br>EST profile URL to request enrollment operation.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `arbitrary_label_reenrollment` (filter, optional): The arbitrary label to be concatenated with the <br>EST profile URL to request re-enrollment operation.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `name` (filter, optional): Name of the profile.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `password` (filter, optional): Encrypted password of the user account for authenticating <br>the EST client with the EST service.<br><br>Minimum Length: 1<br>Maximum Length: 192<br>
- `reenrollment_lead_time` (filter, optional): The number of days before expiration certificates are reenrolled.<br><br>Minimum Value: 0<br>Maximum Value: 30<br>
- `retry_count` (filter, optional): The number of retries the switch will do<br>after a certificate enrollment fails.<br><br>Minimum Value: 0<br>Maximum Value: 32<br>
- `retry_interval` (filter, optional): The interval in seconds, over which the switch retries<br>after a certificate enrollment fails.<br><br>Minimum Value: 30<br>Maximum Value: 600<br>
- `url` (filter, optional): URL of the EST service.<br><br>Minimum Length: 1<br>Maximum Length: 192<br>
- `username` (filter, optional): Name of the user account for authenticating <br>the EST client with the EST service.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>


---
### `POST /system/pki_est_profiles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/pki_est_profiles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the profile.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [PKI_EST_Profile](#!/PKI95EST95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/pki_est_profiles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the profile.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [PKI_EST_Profile](#!/PKI95EST95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/pki_est_profiles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the profile.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [PKI_EST_Profile](#!/PKI95EST95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/pki_ta_profiles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `certificate` (filter, optional): TA certificate associated with this TA profile in PEM format. <br>This could be a root cert or an intermediate certificate.<br><br>Minimum Length: 52<br>
- `certificate_status` (filter, optional): Certificate status:<br>'valid': certificate has not been found to be malformed<br>             or missing any required fields.<br>'malformed': certificate doesn't comply to the standard format.<br>'expired':   certificate is expired.<br>'unchecked': certificate status is pending.<br>             It might have just been installed or the system just booted.<br><br>
- `name` (filter, optional): Name of the profile. Suffix *-est-taNN is reserved for <br>TA profiles whose TA certificates are downloaded from <br>EST servers. User-configured TA profiles are not allowed <br>to end with that.<br><br>Minimum Length: 1<br>Maximum Length: 41<br>
- `origin` (filter, optional): Origin of the TA profile, i.e., how profile is provisioned.<br> `user`: TA profile is provisioned by an user via CLI or REST.<br> `est` : TA profile is downloaded dynamically from an EST <br>         service.<br> `activate`: TA profile is downloaded dynamically from Activate<br><br>
- `revocation_check_mode` (filter, optional): Mode to be used for revocation status checking.<br><br>


---
### `POST /system/pki_ta_profiles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/pki_ta_profiles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the profile. Suffix *-est-taNN is reserved for <br>TA profiles whose TA certificates are downloaded from <br>EST servers. User-configured TA profiles are not allowed <br>to end with that.<br><br>Minimum Length: 1<br>Maximum Length: 41<br>Reference Resource: [PKI_TA_Profile](#!/PKI95TA95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/pki_ta_profiles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the profile. Suffix *-est-taNN is reserved for <br>TA profiles whose TA certificates are downloaded from <br>EST servers. User-configured TA profiles are not allowed <br>to end with that.<br><br>Minimum Length: 1<br>Maximum Length: 41<br>Reference Resource: [PKI_TA_Profile](#!/PKI95TA95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/pki_ta_profiles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the profile. Suffix *-est-taNN is reserved for <br>TA profiles whose TA certificates are downloaded from <br>EST servers. User-configured TA profiles are not allowed <br>to end with that.<br><br>Minimum Length: 1<br>Maximum Length: 41<br>Reference Resource: [PKI_TA_Profile](#!/PKI95TA95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of 'cfg_entries' that should be changed to a<br>random value each time 'cfg_entries' is modified.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `in_progress_version` (filter, optional): The version of the 'in_progress' Classifier Policy.  This value is copied from<br>'cfg_version' when the Policy processing begins. This value is cleared<br>when the Policy status is updated to 'applied' or 'rejected.'<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `name` (filter, optional): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>


---
### `POST /system/policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/policies/{pid}/cfg_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `comment` (filter, optional): Comment to associate with the specified policy entry.<br><br>Maximum Length: 256<br>


---
### `POST /system/policies/{pid}/cfg_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `data` (body, required): data


---
### `DELETE /system/policies/{pid}/cfg_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `id` (path, required): Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/policies/{pid}/cfg_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `id` (path, required): Policy_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/policies/{pid}/cfg_entries/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `id` (path, required): Policy_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/policies/{pid}/cfg_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `id` (path, required): Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `ppid` (path, required): Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `ppid` (path, required): Policy_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `ppid` (path, required): Policy_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of a Classifier Policy (Policy).<br><br>Maximum Length: 64<br>Reference Resource: [Policy](#!/Policy)
- `ppid` (path, required): Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_cdp_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>


---
### `POST /system/port_access_cdp_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/port_access_cdp_groups/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_cdp_groups/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_cdp_groups/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_cdp_groups/{pid}/entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional):  `match`:        port access role will be applied.<br> `ignore`:       port access role will not be applied.<br>CDP entry will be matched when an associated action is provided.<br><br>
- `platform` (filter, optional): Hardware or model details of the neighbor to match.<br><br>Maximum Length: 128<br>
- `software_version` (filter, optional): Software version of the neighbor to match.<br><br>Maximum Length: 128<br>
- `voice_vlan_query_value` (filter, optional): Voice vlan query value of the neighbor to match.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>


---
### `POST /system/port_access_cdp_groups/{pid}/entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `data` (body, required): data


---
### `DELETE /system/port_access_cdp_groups/{pid}/entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `id` (path, required): Port_Access_CDP_Group_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_cdp_groups/{pid}/entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `id` (path, required): Port_Access_CDP_Group_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_cdp_groups/{pid}/entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The name of the CDP group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_CDP_Group](#!/Port95Access95CDP95Group)
- `id` (path, required): Port_Access_CDP_Group_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_gbps`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of 'cfg_entries' that should be changed to a<br>random value each time 'cfg_entries' is modified.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `in_progress_version` (filter, optional): The version of the 'in_progress' Policy.  This value is copied from<br>'cfg_version' when the Policy processing begins. This value is cleared<br>when the Policy status is updated to 'applied' or 'rejected.'<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `name` (filter, optional): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>
- `origin` (filter, optional): Origin of the policy, i.e., how the policy is provisioned.<br>`local`:       policy is provisioned locally on the device.<br>`synthesized`: policy has been dynamically synthesized<br>               by the system.<br><br>


---
### `POST /system/port_access_gbps`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/port_access_gbps/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_gbps/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_gbps/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_gbps/{pid}/cfg_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `comment` (filter, optional): Comment to associate with the specified policy entry.<br><br>Maximum Length: 256<br>
- `origin` (filter, optional): Origin of the policy, i.e., how the policy entry is provisioned.<br> `local`:       policy entry is provisioned locally on the device.<br> `synthesized`: policy entry has been dynamically synthesized<br>                by the system.<br><br>


---
### `POST /system/port_access_gbps/{pid}/cfg_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `data` (body, required): data


---
### `DELETE /system/port_access_gbps/{pid}/cfg_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `id` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_gbps/{pid}/cfg_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `id` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/port_access_gbps/{pid}/cfg_entries/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `id` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/port_access_gbps/{pid}/cfg_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `id` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/port_access_gbps/{pid}/cfg_entries/{ppid}/gbp_action_set`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `ppid` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_gbps/{pid}/cfg_entries/{ppid}/gbp_action_set`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `ppid` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/port_access_gbps/{pid}/cfg_entries/{ppid}/gbp_action_set`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `ppid` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/port_access_gbps/{pid}/cfg_entries/{ppid}/gbp_action_set`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Port Access Group Based Policy name.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_GBP](#!/Port95Access95GBP)
- `ppid` (path, required): Port_Access_GBP_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_lldp_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>


---
### `POST /system/port_access_lldp_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/port_access_lldp_groups/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_lldp_groups/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_lldp_groups/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_lldp_groups/{pid}/entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional):  `match`:        port access role will be applied.<br> `ignore`:       port access role will not be applied.<br>LLDP entry will be matched when an associated action is provided.<br><br>
- `system_description` (filter, optional): System description TLV of the vendor to match.<br><br>Minimum Length: 2<br>Maximum Length: 256<br>
- `system_name` (filter, optional): System name TLV of the device vendor to match.<br><br>Minimum Length: 2<br>Maximum Length: 63<br>
- `vendor_oui` (filter, optional): The organization unique identifier (OUI) of the device vendor to match.<br><br>Minimum Length: 6<br>Maximum Length: 6<br>


---
### `POST /system/port_access_lldp_groups/{pid}/entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `data` (body, required): data


---
### `DELETE /system/port_access_lldp_groups/{pid}/entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `id` (path, required): Port_Access_LLDP_Group_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_lldp_groups/{pid}/entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `id` (path, required): Port_Access_LLDP_Group_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_lldp_groups/{pid}/entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The name of the lldp group.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_LLDP_Group](#!/Port95Access95LLDP95Group)
- `id` (path, required): Port_Access_LLDP_Group_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_policies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cfg_version` (filter, optional): The version of 'cfg_entries' that should be changed to a<br>random value each time 'cfg_entries' is modified.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `in_progress_version` (filter, optional): The version of the 'in_progress' Policy.  This value is copied from<br>'cfg_version' when the Policy processing begins. This value is cleared<br>when the Policy status is updated to 'applied' or 'rejected.'<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `name` (filter, optional): Name of a port-access policy.<br><br>Maximum Length: 128<br>
- `origin` (filter, optional): Origin of the policy, i.e., how the policy is provisioned.<br> `local`:      policy is provisioned locally on the device.<br> `downloaded`: policy is downloaded from ClearPass server.<br> `radius`:     policy is translated from the attributes assigned<br>               by RADIUS server.<br><br>


---
### `POST /system/port_access_policies`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/port_access_policies/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_policies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_policies/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_policies/{pid}/cfg_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `comment` (filter, optional): Comment to associate with the specified policy entry.<br><br>Maximum Length: 256<br>
- `origin` (filter, optional): Origin of the policy, i.e., how the policy entry is provisioned.<br> `local`:      policy entry is provisioned locally on the device.<br> `downloaded`: policy entry is downloaded from ClearPass server.<br> `radius`:     policy entry is translated from the attributes assigned<br>               by RADIUS server.<br><br>


---
### `POST /system/port_access_policies/{pid}/cfg_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `data` (body, required): data


---
### `DELETE /system/port_access_policies/{pid}/cfg_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `id` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_policies/{pid}/cfg_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `id` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/port_access_policies/{pid}/cfg_entries/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `id` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/port_access_policies/{pid}/cfg_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `id` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/port_access_policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `ppid` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `ppid` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/port_access_policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `ppid` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `data` (body, required): data


---
### `PUT /system/port_access_policies/{pid}/cfg_entries/{ppid}/policy_action_set`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of a port-access policy.<br><br>Maximum Length: 128<br>Reference Resource: [Port_Access_Policy](#!/Port95Access95Policy)
- `ppid` (path, required): Port_Access_Policy_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_roles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `auth_mode` (filter, optional): Indicates, whether each individual client on the port needs to be<br>authenticated separately to gain access to the network.<br>`client-mode`: every client needs to be authenticated to be<br>               granted network access.<br>`device-mode`: only one of the attached clients must be<br>               authenticated for all clients to be granted<br>               network access.<br>If empty, then port_access_auth_mode of the `Port` is used.<br><br>
- `cached_reauth_period` (filter, optional): Duration in seconds until when cached re-authentication is<br>allowed for clients on-boarded via this role.<br>If empty, then Port_Access_Auth_Configuration.cached_reauth_period of the `Port` is used.<br><br>Minimum Value: 30<br>Maximum Value: 4294967295<br>
- `client_inactivity_monitor` (filter, optional): Sets the inactivity mode<br> `configured_timeout`: value set by `client_inactivity_time` will be used for<br>                       tracking inactivity<br> `dynamic_timeout`:    client will expire after global dynamic ageout value<br> `no_timeout`:         client will never ageout and stays in system.<br>                       Example: mac-pinning<br><br>
- `client_inactivity_timeout` (filter, optional): Time in seconds after which a client will be removed from<br>the port for lack of activity. This is only applicable when<br>client_inactivity_monitor mode is set to 'configured_timeout'.<br><br>Minimum Value: 300<br>Maximum Value: 4294967295<br>
- `description` (filter, optional): Free text description of role.<br><br>Minimum Length: 1<br>Maximum Length: 256<br>
- `gateway_zone` (filter, optional): Gateway zone associated with this user role.<br><br>Key: string<br>
- `max_session_time` (filter, optional): The maximum number of seconds of service to provide to the<br>client before termination of session. If empty, the maximum<br>session time is indefinite.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `mtu` (filter, optional): The MTU (maximum transmission unit); i.e. the largest amount of<br>data that can be transmitted in an IP packet.<br>If empty, then active_ip_mtu value of the `Port` is used.<br><br>Minimum Value: 68<br>Maximum Value: 9198<br>
- `name` (filter, optional): Name of the role.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>
- `origin` (filter, optional): Origin of the access role, i.e., how the access role <br>is created.<br> `local`:      access role is configured locally on the switch.<br> `downloaded`: downloaded from Clearpass Policy Manager (CPPM) server.<br> `radius`:     translated from the attributes assigned by RADIUS server.<br><br>
- `poe_priority` (filter, optional): If the PoE demand exceeds the PoE budget, the switch will deny<br>power to some ports. PoE prioritization is the way the switch<br> determines which ports are to receive power. The priorities are:<br> `critical`: the active PoE ports at this level are provisioned<br>             before the PoE ports at any other level are provisioned.<br> `high`:     the active PoE ports at this level are provisioned<br>             before the low priority PoE ports are provisioned.<br> `low`:      the active PoE ports at this level are provisioned<br>             only if there is power available after provisioning<br>             any active PoE ports at the higher priority levels.<br>If empty, then config.priority value of the `PoE_Interface` is used.<br><br>
- `qos_trust_mode` (filter, optional): Specifies the individual port QoS Trust Mode.<br><br>`none`: no fields are inspected on arriving packets. The initial local-<br>        priority and color meta-data values are taken from PCP 0 entry of the COS Map.<br>`cos`:  will use the PCP of the outermost 802.1 VLAN tag to index the COS Map<br>        entry to initialize the local-priority and color meta-data values of the packet.<br>        For untagged packets, the initial local-priority and color meta-data values are<br>        taken from code_point 0 entry of the COS Map.<br>`dscp`: will use the DSCP value of IP packets to index the DSCP Map entry to<br>        initialize the local-priority and color meta-data values of the packet.  For<br>        non-IP packets, what meta-data values are assigned is hardware dependent.<br>If empty, then qos_config.qos_trust value of the `Port` is used.<br><br>
- `reauth_period` (filter, optional): Time period in seconds to enforce periodic re-authentication of the clients.<br>If empty, then Port_Access_Auth_Configuration.reauth_period of the `Port` is used.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `stp_admin_edge_port` (filter, optional): Specifies whether the port will operate as an STP admin_edge port.<br>If empty, then [stp_config].admin_edge_port_enable of the `Port` is used.<br><br>Key: boolean<br>
- `ubt_gateway_clearpass_role` (filter, optional): Indicates the role name that will be communicated to the UBT <br>cluster. The cluster needs to download the role definition from <br>ClearPass.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>
- `ubt_gateway_role` (filter, optional): Role to be assigned to tunneled clients on the UBT cluster side.<br><br>Minimum Length: 1<br>Maximum Length: 63<br>
- `vlan_group_name` (filter, optional): VLAN group name associated with this user role via RADIUS.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>
- `vlan_mode` (filter, optional): When empty, default mode is selected as follows:<br> `access`:           if the vlan_tag contains a value, role contains an access vlan<br>                     and the vlan_trunks will be empty.<br> `trunk`:            if the vlan_tag is empty, and the vlan_trunks is non-empty,<br>                     then role has no-native vlan specified.<br>If the mode is explicitly configured:<br> `native-tagged`:    value contained in vlan_tag refers to native vlan<br>                     and that vlan has to be tagged.<br> `native-untagged`:  value contained in vlan_tag refers to native vlan<br>                     and that vlan has to be untagged.<br><br>
- `vlan_name_tag` (filter, optional): The untagged VLAN, identified by name, to which users of this<br>access role are assigned. If empty, VLAN identifier<br>corresponding to the vlan_tag is used if set. Otherwise,<br>vlan_tag of the 'Port' is used.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `vlan_tag` (filter, optional): The untagged VLAN identifier to which users of this access<br>role are assigned. If empty, VLAN identifier corresponding<br>to the vlan_name_tag is used if set. Otherwise, vlan_tag<br>of the 'Port' is used.<br><br>Minimum Value: 1<br>Maximum Value: 4094<br>


---
### `POST /system/port_access_roles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/port_access_roles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the role.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>Reference Resource: [Port_Access_Role](#!/Port95Access95Role)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_roles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the role.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>Reference Resource: [Port_Access_Role](#!/Port95Access95Role)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_roles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the role.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>Reference Resource: [Port_Access_Role](#!/Port95Access95Role)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/port_access_vlan_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): VLAN group name.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>


---
### `POST /system/port_access_vlan_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/port_access_vlan_groups/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): VLAN group name.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_VLAN_Group](#!/Port95Access95VLAN95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/port_access_vlan_groups/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): VLAN group name.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_VLAN_Group](#!/Port95Access95VLAN95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/port_access_vlan_groups/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): VLAN group name.<br><br>Minimum Length: 2<br>Maximum Length: 32<br>Reference Resource: [Port_Access_VLAN_Group](#!/Port95Access95VLAN95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `aclmac_in_cfg_version` (filter, optional): The version of the 'aclmac_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclmac_in_cfg' value. An empty value means no ingress MAC ACL has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclmac_out_cfg_version` (filter, optional): The version of the 'aclmac_out_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclmac_out_cfg' value. An empty value means no egress MAC ACL has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv4_in_cfg_version` (filter, optional): The version of the 'aclv4_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclv4_in_cfg' value. An empty value means no ingress IPv4 ACL has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv4_out_cfg_version` (filter, optional): The version of the 'aclv4_out_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclv4_out_cfg' value. An empty value means no egress IPv4 ACL has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv4_routed_in_cfg_version` (filter, optional): The version of the 'aclv4_routed_in_cfg' column. This value is<br>changed to a random value each time any management interface<br>modifies the 'aclv4_routed_in_cfg' value. An empty value means<br>no routed ingress IPv4 ACL has been configured for the VLAN<br>interface.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv4_routed_out_cfg_version` (filter, optional): The version of the currently configured routed egress IPv4 ACL<br>that corresponds to this configuration version value. This value<br>is changed to a random value each time any management interface<br>modifies the configured routed egress IPv4 ACL value. An empty<br>value means no routed egress IPv4 ACL has been configured for<br>the VLAN interface.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv6_in_cfg_version` (filter, optional): The version of the 'aclv6_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclv6_in_cfg' value. An empty value means no ingress IPv6 ACL has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv6_out_cfg_version` (filter, optional): The version of the 'aclv6_out_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclv6_out_cfg' value. An empty value means no egress IPv6 ACL has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv6_routed_in_cfg_version` (filter, optional): The version of the 'aclv6_routed_in_cfg' column. This value is<br>changed to a random value each time any management interface<br>modifies the 'aclv6_routed_in_cfg' value. An empty value means<br>no routed ingress IPv6 ACL has been configured for the VLAN<br>interface.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv6_routed_out_cfg_version` (filter, optional): The version of the currently configured routed egress IPv6 ACL<br>that corresponds to this configuration version vlaue. This value<br>is changed to a random value each time any management interface<br>modifies the configured routed egress IPv6 ACL value. An empty<br>value means no routed egress IPv6 ACL has been configured for<br>the VLAN interface.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `active_ip4_address` (filter, optional): Reflects IPv4 address that is activated on the interface. This might be different<br>from the configured one if 'dhcp_config.enable' is not 'none' i.e. DHCP client is<br>enabled on the interface.<br><br>Maximum Length: 18<br>
- `active_ipv4_address_source` (filter, optional): Indicates the source of the active IPv4 address on this interface.<br><br>
- `active_ipv6_ll_source` (filter, optional): Indicates the source of active IPv6 Link Local address on this interface.<br><br>
- `admin` (filter, optional): The administrative state of the Interface.<br>If not configured, the default behavior depends on the 'type':<br>'mgmt':                'up'<br>'lag':                 'down'<br>'vlan':                'up'<br>'gre_ipv4 tunnel':     'down'<br>'ipv6_in_ipv4 tunnel': 'down'<br>'ipv6_in_ipv6 tunnel': 'down'<br>'loopback':            'up'<br>'system':              'down'<br>'vxlan':               'down'<br>'ubt':                 'down'<br><br>
- `applied_vlan_mode` (filter, optional): The VLAN mode applied on the port.<br><br>
- `arp_timeout` (filter, optional): Determines the time interval in seconds till when a neighbor entry is valid.<br><br>Minimum Value: 30<br>Maximum Value: 28800<br>
- `bfd_detect_multiplier` (filter, optional): The number of negotiated min_rx_intervals that can occur before<br>the BFD session is considered to be down.<br><br>Minimum Value: 1<br>Maximum Value: 5<br>
- `bfd_min_rx_interval` (filter, optional): The shortest interval, in milliseconds, at which BFD sessions<br>can receive BFD control messages. Remote endpoints may send<br>messages at a slower rate.<br>If not present, the system value is used.<br><br>Minimum Value: 100<br>Maximum Value: 20000<br>
- `bfd_min_tx_interval` (filter, optional): The shortest interval, in milliseconds, at which BFD sessions<br>can transmit BFD control messages. Messages will actually be<br>transmitted at a slower rate if the remote endpoints cannot<br>receive them as quickly as specified.<br>If not present, the system value is used.<br><br>Minimum Value: 50<br>Maximum Value: 20000<br>
- `bond_active_slave` (filter, optional): <br>Key: string<br>
- `bond_mode` (filter, optional): The type of bonding used for a bonded port. Bond mode controls the selection of<br>a interface from a group of aggregate interfaces with which to transmit a frame.<br>This selection is performed with a hash function using either source and<br>destination mac addresses (l2), ip addresses (l3) or tcp/udp ports (l4) as<br>parameters. Defaults to `l3-src-dst-hash` if not assigned.<br><br>
- `description` (filter, optional): Description for LAG, VLAN, or tunnel interface.<br><br>Minimum Length: 0<br>Maximum Length: 64<br>
- `erps_port_blocked` (filter, optional): This value will be set to `true`,if the port is blocked by ERPS.<br>Default value is `false`.<br><br>Key: boolean<br>
- `flaps_performed` (filter, optional): This value shall indicate the number of flaps performed.<br><br>Key: integer<br>
- `flaps_requested` (filter, optional): This value shall indicate the number of flap requests done by different applications.<br><br>Key: integer<br>
- `flood_block` (filter, optional): When set to &#8216;true&#8217;, all flood traffic received from and forwarded to<br>this port will be dropped. The default value is `false`.<br><br>Key: boolean<br>
- `icmp_redirect_disable` (filter, optional): Disables ICMPv4 and ICMPv6 redirect messages.<br>For the specific port, takes precedence over the same System configuration.<br><br>Key: boolean<br>
- `icmp_unreachable_disable` (filter, optional): Disables ICMPv4 and ICMPv6 unreachable messages.<br>For the specific port, takes precedence over the same System configuration.<br><br>Key: boolean<br>
- `icmp_unreachable_ratelimit` (filter, optional): Rate limit (in milliseconds per message), that should be used for ICMP Unreachable <br>messages. For the specific port, takes precedence over the same System configuration.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `ifindex` (filter, optional): unique ifindex for LAG Interfaces.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ip4_address` (filter, optional): The IPv4 address and subnet mask in the address/mask format. This is the primary<br>IP address.<br><br>Maximum Length: 18<br>
- `ip_mtu` (filter, optional): The user configured IP MTU of a port. This would be applicable for both IPv4 and IPv6.<br><br>Minimum Value: 68<br>Maximum Value: 9198<br>
- `ipv4_source_lockdown_enable` (filter, optional): Enables IP Lockdown feature on the port.<br>When set, IPv4 packets received from the clients on this port are forwarded only <br>if there is an associated IP binding entry.<br><br>Key: boolean<br>
- `ipv6_address_autoconfig_enable` (filter, optional): Enable automatic configuration of the IPv6 addresses.<br><br>Key: boolean<br>
- `ipv6_address_linklocal_enable` (filter, optional): Enables IPV6 link-local address when global unicast address is <br>not configured.<br><br>Key: boolean<br>
- `ipv6_nd_dad_attempts` (filter, optional): The number of Neighbor discovery packets to be sent for duplicate address<br>detection.<br><br>Minimum Value: 0<br>Maximum Value: 15<br>
- `ipv6_nd_icmpv6_redirects` (filter, optional): Enable sending ICMPv6 redirect messages.<br><br>Key: boolean<br>
- `ipv6_nd_mtu` (filter, optional): The MTU option is used in router advertisement messages to ensure that all nodes<br>on a link use the same MTU value.<br><br>Minimum Value: 1280<br>Maximum Value: 65535<br>
- `ipv6_nd_ns_interval` (filter, optional): The interval (in milliseconds) between neighbor solicitation messages.<br><br>Minimum Value: 1000<br>Maximum Value: 3600000<br>
- `ipv6_nd_ra_hoplimit` (filter, optional): The default value that will be used in RA message. If this value is not set,<br> then global ipv6 hoplimit value will be used in RA message.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `ipv6_nd_ra_lifetime` (filter, optional): The lifetime associated with the default router in units of seconds.<br><br>Minimum Value: 0<br>Maximum Value: 9000<br>
- `ipv6_nd_ra_managed_flag` (filter, optional): When set it indicates that addresses are available via DHCPV6.<br><br>Key: boolean<br>
- `ipv6_nd_ra_max_interval` (filter, optional): The maximum interval (in seconds) between sending router advertisements.<br><br>Minimum Value: 4<br>Maximum Value: 1800<br>
- `ipv6_nd_ra_min_interval` (filter, optional): The minimum interval (in seconds) between sending router advertisements.<br><br>Minimum Value: 3<br>Maximum Value: 1350<br>
- `ipv6_nd_ra_other_config_flag` (filter, optional): When set it indicates that other configuration information(DNS) is available via<br>DHCPV6.<br><br>Key: boolean<br>
- `ipv6_nd_ra_reachable_time` (filter, optional): The time, in milliseconds, that a node assumes a neighbor is reachable after<br>having received a reachability confirmation.<br><br>Minimum Value: 0<br>Maximum Value: 3600000<br>
- `ipv6_nd_ra_retransmit_timer` (filter, optional): The value to be placed in retransmission timer field in router advertisement messages<br>sent by router.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ipv6_nd_router_preference` (filter, optional): The preference associated with the default router.<br><br>
- `ipv6_neighbor_timeout` (filter, optional): Determines the time interval in seconds till when an IPv6 neighbor entry is valid.<br><br>Minimum Value: 30<br>Maximum Value: 28800<br>
- `ipv6_source_lockdown_enable` (filter, optional): Enables IP Lockdown feature on the port.<br>When set, IPv6 packets received from the clients on this port are forwarded only <br>if there is an associated IP binding entry.<br><br>Key: boolean<br>
- `lacp` (filter, optional): Configures LACP on this port.  LACP allows directly connected switches to<br>negotiate which links may be bonded.  LACP may be enabled on non-bonded ports<br>for the benefit of any switches they may be connected to.  `active` ports are<br>allowed to initiate LACP negotiations.  `passive` ports are allowed to<br>participate in LACP negotiations initiated by a remote switch, but not allowed<br>to initiate such negotiations themselves.  If LACP is enabled on a port whose<br>partner switch does not support LACP, the bond will be disabled. Defaults to<br>`off` if unset.<br><br>
- `loop_detect_source` (filter, optional): If the detected source is not loop-protect,then loop protect<br>should not take any action on timer expiry.<br><br>
- `loop_protect_action` (filter, optional): This determines action for the Loop-protect feature.The value is set to "tx-<br>port-disable" for disabling the sending port on detecting a loop, "tx-rx-<br>disable" disables both sending and receiving ports when loop is detected and<br>"do-not-disable" will not disable any port. Default value is `tx-port-disable`.<br><br>
- `loop_protect_enable` (filter, optional): When set to `true`, Loop-protect is enabled on this port. Default value is<br>`false`.<br><br>Key: boolean<br>
- `loop_protect_port_disabled` (filter, optional): This value will be set to `true`,if the port is disabled by Loop-protect.<br>Default value is `false`.<br><br>Key: boolean<br>
- `loop_protect_stagger_count` (filter, optional): This determines the number of loop protect PDUs to be received<br> before taking a receiver action.<br><br>Minimum Value: 0<br>
- `mac` (filter, optional): The MAC address to use for this port for the purpose of choosing the bridge's<br>MAC address.  This column does not necessarily reflect the port's actual MAC<br>address, nor will setting it change the port's actual MAC address.<br><br>Key: string<br>
- `mac_learn_disable` (filter, optional): When set to 'true', mac learning will be disabled on the port. The default value<br>is `false`.<br><br>Key: boolean<br>
- `macs_invalid` (filter, optional): If `true`, indicates that MACs on this port are invalid. This might be set by<br>any agent of the system that decides that MACs are indeed invalid. Eventually<br>those MACs will be cleared from the system and macs_invalid will revert to<br>`false`.<br><br>Key: boolean<br>
- `mgmd_igmp_version` (filter, optional): The IGMP protocol version to use.  When IGMP is disabled, this field would be<br>empty. If there is a version mismatch between L2 and L3 VLAN, it will pick the<br>lowest version.<br><br>Minimum Value: 2<br>Maximum Value: 3<br>
- `mgmd_mld_version` (filter, optional): The MLD protocol version to use.  When MLD is disabled, this field would be<br>empty. If there is a version mismatch between L2 and L3 VLAN, it will pick the<br>lowest version.<br><br>Minimum Value: 1<br>Maximum Value: 2<br>
- `mvrp_enable` (filter, optional): The value `true` indicates MVRP is enabled on this port.<br><br>Key: boolean<br>
- `mvrp_last_pdu_src_mac` (filter, optional): The source MAC address of the last MVRP message received on this port.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `mvrp_registration` (filter, optional): Defines the mode of operation of all the registrar state machines associated<br>with the port. The different mode of operations are In "normal" mode, the<br>Registrar responds to incoming MRP messages. In "fixed" mode, the Registrar<br>ignores all MRP messages, and remains in the registered state. In "forbidden"<br>mode, the Registrar ignores all MRP messages, and remains in the unregistered<br>state.<br><br>
- `name` (filter, optional): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>
- `num_clear_sflow_stats_performed` (filter, optional): Number of clear sFlow statistics performed.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `num_clear_sflow_stats_requested` (filter, optional): Number of clear sFlow statistics requested.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `origin` (filter, optional): Indicator of whether the port is built-in (system-defined)<br>or configured.<br>Built-in ports cannot be modified or deleted by users.<br><br>
- `ospf_auth_text_key` (filter, optional): The authentication key for OSPFv2 authentication type "text".<br><br>Minimum Length: 1<br>
- `ospf_auth_type` (filter, optional): The type of OSPFv2 authentication. If not set, then parent area level<br>authentication holds for the port.<br><br>
- `ospf_bfd` (filter, optional): Specifies whether OSPF router global BFD mode should be overridden for this particular interface:<br>'enable':  Enables BFD, regardless of OSPF router bfd_all_interfaces_enable.<br>'disable': Disables BFD, regardless of OSPF router bfd_all_interfaces_enable.<br>'default': Keeps BFD disabled or enabled according to OSPF router bfd_all_interfaces_enable.<br><br>
- `ospf_if_out_cost` (filter, optional): The output cost configured on the corresponding OSPFv2 interface.<br>If not set, OSPF will calculate cost for this interface based<br>on link speed and reference bandwidth. Any configured value will<br>override the automatic cost calculation.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `ospf_if_shutdown` (filter, optional): Shut OSPF down on this interface.<br><br>Key: boolean<br>
- `ospf_if_type` (filter, optional): The type of the OSPFv2 network interface. The default value is the type of the<br>interface from the Interface table.<br><br>
- `ospf_neighbor_clear_performed` (filter, optional): Number of times that OSPF neighbors on this port were cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ospf_neighbor_clear_requested` (filter, optional): Number of times a request was made to clear OSPF neighbors learned on this port.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ospf_priority` (filter, optional): The router with the highest priority will be more eligible to become Designated<br>Router. Setting the value to 0, makes the router ineligible to become Designated<br>Router.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `ospfv3_bfd` (filter, optional): Specifies whether OSPFv3 router global BFD mode should be overridden for this particular interface:<br>'enable':  Enables BFD, regardless of OSPFv3 router bfd_all_interfaces_enable.<br>'disable': Disables BFD, regardless of OSPFv3 router bfd_all_interfaces_enable.<br>'default': Keeps BFD disabled or enabled according to OSPFv3 router bfd_all_interfaces_enable.<br><br>
- `ospfv3_dead_interval` (filter, optional): The time duration, in seconds, that a neighbor should wait for a Hello packet<br>before tearing down adjacencies with the local router.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `ospfv3_hello_interval` (filter, optional): The Hello packet will be sent every hello interval timer value seconds. This<br>value must be the same for all routers attached to a common network.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `ospfv3_if_cost` (filter, optional): The output cost configured on the corresponding OSPFv3 interface.<br>If not set, OSPFv3 will calculate cost for this interface<br>based on link speed and reference bandwidth. Any configured value<br>will override the automatic cost calculation.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `ospfv3_if_priority` (filter, optional): The router with the highest priority will be more eligible to become Designated<br>Router. Setting the value to `0`, makes the router ineligible to become<br>Designated Router.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `ospfv3_if_shutdown` (filter, optional): Shutdown OSPFv3 on this interface.<br><br>Key: boolean<br>
- `ospfv3_if_type` (filter, optional): The type of the OSPFv3 network interface. The default value is the type of the<br>interface from the Interface table.<br><br>
- `ospfv3_neighbor_clear_performed` (filter, optional): Number of times that OSPFv3 neighbors on this port were cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ospfv3_neighbor_clear_requested` (filter, optional): Number of times a request was made to clear OSPFv3 neighbors learned on this port.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ospfv3_retransmit_interval` (filter, optional): The number of seconds between LSA retransmissions. It is also used when<br>retransmitting Database Description and Link State Request Packets.<br><br>Minimum Value: 1<br>Maximum Value: 1800<br>
- `ospfv3_transmit_delay` (filter, optional): The estimated time in seconds to transmit an LSA to a neighbor. The transmit<br>delay timer increments the age of LSAs in the update packets to accommodate<br>transmission and propagation delays for the interface. The timer is more<br>important on very low speed links where the transmission delay is more<br>significant.<br><br>Minimum Value: 1<br>Maximum Value: 1800<br>
- `policy_in_cfg_version` (filter, optional): The version of 'policy_in_cfg'. This value is changed to a<br>random value each time any management interface modifies the<br>'policy_in_cfg' value. An empty value means no ingress policy has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `policy_routed_in_cfg_version` (filter, optional): The version of 'policy_routed_in_cfg'. This value is changed to a<br>random value each time any management interface modifies the<br>'policy_routed_in_cfg' value. An empty value means no routed ingress policy has been<br>configured for the port.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `port_access_allow_flood_traffic` (filter, optional): Enables transmission of flood-traffic (broadcast, multicast and<br>unknown unicast) out ports that are security blocked.<br>A port is security blocked when authentication is enabled for<br>that port and no client has yet been authenticated on this port.<br><br>Key: boolean<br>
- `port_access_auth_mode` (filter, optional): Indicates, whether each individual client on the port needs to be<br>authenticated separately to gain access to the network.<br>`client-mode`: every client needs to be authenticated to be<br>               granted network access.<br>`device-mode`: only one of the attached clients must be<br>               authenticated for all clients to be granted<br>               network access.<br><br>
- `port_access_clients_limit` (filter, optional): Maximum number of clients that can be authenticated on this port.<br><br>Minimum Value: 1<br>Maximum Value: 256<br>
- `port_access_concurrent_onboarding` (filter, optional): Enable authentication methods to start concurrently for faster<br>onboarding. If not set, clients are onboarded based on the order<br>specified by `port_access_onboarding_precedence`.<br><br>Key: boolean<br>
- `port_access_disable_cdp_auth` (filter, optional): Disable BPDU triggered authentication for CDP.<br> This is only applicable when port access authentication is<br> enabled for this port.<br><br>Key: boolean<br>
- `port_access_disable_lldp_auth` (filter, optional): Disable BPDU triggered authentication for LLDP.<br> This is only applicable when port access authentication is<br> enabled for this port.<br><br>Key: boolean<br>
- `port_access_operational_auth_mode` (filter, optional): Indicates port-access operational auth mode of this port. It <br>will be same as configured auth mode if not dynamically updated <br>by any one of the port access client's role attributes.<br>`client-mode`: Operational auth-mode on the port is client-mode.<br>`device-mode`: Operational auth-mode on the port is device-mode.<br><br>
- `port_access_qos_trust` (filter, optional): Policy based assignment of port QoS trust mode. When set, this will override user<br>configured 'qos_config.qos_trust' of this port:<br>`none`: no fields are inspected on arriving packets. The initial local-priority<br>        and color meta-data values are taken from PCP 0 entry of the COS Map<br>        table.<br>`cos`:  will use the PCP of the outermost 802.1 VLAN tag to index the COS Map<br>        entry to initialize the local-priority and color meta-data values of the packet.<br>        For untagged packets, the initial local-priority and color meta-data values are<br>        taken from code_point 0 entry of the COS Map table.<br>`dscp`: will use the DSCP value of IP packets to index the DSCP Map entry to<br>        initialize the local-priority and color meta-data values of the packet.  For<br>        non-IP packets, what meta-data values are assigned is hardware dependent.<br><br>
- `port_access_reauthentication_performed` (filter, optional): Number of times re-authentication is performed.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `port_access_reauthentication_requested` (filter, optional): Number of times re-authentication is requested.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `port_access_stp_admin_edge` (filter, optional): Policy based assignment on Port's STP mode. When set to 'true', <br>this port will operate as an STP admin-edge port overriding <br>the configured value of STP admin_edge for this port.<br>If empty, then [stp_config].admin_edge_port_enable of the `Port` is used.<br><br>Key: boolean<br>
- `port_access_vlan_mode` (filter, optional): The VLAN mode of the port derived by port access security.<br><br>
- `process_grat_arp` (filter, optional): Disable processing gratituous ARP packets received on this port.<br>This is only applicable to Layer-3 interfaces (SVIs, Routed ports or L3 LAG).<br><br>Key: boolean<br>
- `q_profile` (filter, optional): References queue profile for this port. If this is unspecified, then the queue<br>profile referenced in [System](#!/System)) table q_profile will be used.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `qos` (filter, optional): References schedule profile for this port. If this is unspecified, then the<br>schedule profile referenced in [System](#!/System)) table qos will be used.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `rdisc_irdp_broadcast` (filter, optional): Specifies whether router advertisements should be sent using broadcast,<br>255.255.255.255 address. If the value is false (which is a default) the packets<br>would be sent to multicast 224.0.0.1 address.<br><br>Key: boolean<br>
- `rdisc_irdp_enable` (filter, optional): When set to `true`, IRDP is enabled on the port. The default value is `false`.<br><br>Key: boolean<br>
- `rdisc_irdp_preference` (filter, optional): Specifies the preference level of this routing switch. Higher value indicates<br>higher router preference. The default preference value is `0`.<br><br>Minimum Value: -4294967296<br>Maximum Value: 4294967295<br>
- `routing` (filter, optional): Indicates whether the interface is routing or Layer 2.<br>For routing interfaces, 'vrf' has to be properly populated.<br>If not configured, default behavior depends on interface 'type':<br>'vlan':                  'true'<br>'gre_ipv4 tunnel':       'true'<br>'ipv6_in_ipv4 tunnel':   'true'<br>'ipv6_in_ipv6 tunnel':   'true'<br>'loopback':              'true'<br>'system':              'true'<br>'lag':                 'true'<br>'vxlan':                'false'<br>'ubt':                  'false'<br><br>Key: boolean<br>
- `urpf_check` (filter, optional): Mode of unicast reverse path forwarding verification:<br>'loose':   drop packets that are destined to the device itself and that have source IP that is not reachable.<br>'strict':  drop packets that are destined to the device and that have source IP that is not reachable through the interface that the packet arrived on.<br>'disable': no reverse path verification.<br><br>
- `virtual_gw_l3_src_mac_enable` (filter, optional): Enables the interface to use the virtual gateway MAC address as the source MAC for routed traffic.<br>This is only applicable for SVI interfaces.<br><br>Key: boolean<br>
- `virtual_gw_operational_l3_src_mac` (filter, optional): The operational source MAC address for routed traffic associated with this interface.<br>This will be either the system MAC address or the IPv4 or IPv6 virtual gateway MAC address <br>depending on the configuration on this interface.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `vlan_mode` (filter, optional): VLAN mode for ports with 'routing' being 'false'.<br>For those ports, it has to be set, otherwise the port will be held down.<br> `access`: Port can carry traffic for only one VLAN and the VLAN<br>           is specified as part of vlan_tag. Packets ingressing<br>           and egressing this port will not have an 802.1Q VLAN tag.<br><br>When the port is trunked, mode must be either native-tagged or<br>native-untagged, value contained in vlan_trunks refers to the<br>list of VLANs which have to be trunked, if it is<br>empty then all VLANs have to be trunked.<br> `native-tagged`:    Port can carry traffic for multiple VLANs.<br>                     One of the VLANs is designated as native<br>                     and is specified as part of vlan_tag.<br>                     Traffic for all VLANs on this port<br>                     including the native VLAN will be 802.1Q<br>                     VLAN tagged.<br> `native-untagged`:  Port can carry traffic for multiple VLANs.<br>                     One of the VLANs is designated as native<br>                     and the VLAN ID is specified as part of<br>                     vlan_tag. Traffic for all VLANs except the<br>                     native VLAN will be 802.1Q VLAN tagged<br>                     Traffic for the native VLAN will not have<br>                     an 802.1Q tag.<br><br>
- `vsx_active_forwarding_enable` (filter, optional): Determines whether this port has VSX active-forwarding enabled or not. <br>This should be set on Upstream SVIs only and not on downstream SVIs <br>that have active-gateway enabled.<br><br>Key: boolean<br>
- `vsx_linkup_delay_timer_disable` (filter, optional): A value of 'true' disables vsx linkup delay timer for this port.<br><br>Key: boolean<br>
- `vsx_pdu_tx_disable` (filter, optional): When set to `false`, protocol should transmit the packet,<br>when set to `true', no packets should be transmitted<br><br>Key: boolean<br>
- `vsx_peer_mac` (filter, optional): VSX Peer's MAC address.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `vsx_peer_primary_ip4_address` (filter, optional): VSX peer's primary IPv4 address.<br><br>Maximum Length: 15<br>
- `vsx_previous_state` (filter, optional): Indicates the previous local and remote VSX state.<br>'local_up_remote_up': This LAG is up and running on both<br>               local and remote device.<br>'local_up_remote_down': This LAG is up on the local device<br>               but was down on the remote device.<br>'local_up_remote_unknown': This LAG is up on the local device<br>               and state is unknown on the remote.<br>'local_up_pending_remote_up': Local device sent a request to<br>               remote device yet to receive the response.<br>'local_up_pending_remote_down_or_unknown': Local device sent a<br>               request to remote device yet to receive the response.<br>'local_down_remote_up': This LAG is down on the local device but<br>               is up on the remote device.<br>'local_down_remote_down': This LAG is down on both local and<br>               remote device.<br>'local_up_pending_tx_rx_enable_remote_up': This LAG is blocked and<br>               waiting for TX/RX of one of its member interfaces<br>               to be enabled in hardware before it can be unblocked.<br>               The LAG is already up on the peer side.<br>'local_up_pending_tx_rx_enable_remote_down_or_unknown': This LAG is<br>               blocked and waiting for TX/RX of one of its member<br>               interfaces to be enabled in hardware before it can be<br>               unblocked. The LAG state on the peer side is either<br>               down or unknown.<br>'local_up_pending_redirect_disable_remote_up': This LAG is blocked<br>               and waiting for egress redirection to be disabled<br>               in hardware before it can be unblocked.<br>               The LAG is already up on the peer side.<br>'local_down_pending_tx_rx_disable_remote_up':<br>               This LAG is blocked and waiting for TX/RX of one of<br>               its member interfaces to be disabled in hardware.<br>               The LAG is already up on the peer side.<br>'local_down_pending_tx_rx_disable_remote_down_or_unknown':<br>               This LAG is blocked and waiting for TX/RX of one of<br>               its member interfaces to be disabled in hardware<br>               The LAG state on the peer side is either down or unknown.<br>'local_down_pending_flood_block_enable_remote_up':<br>               This LAG is waiting for flood block of one of its<br>               member interfaces to be enabled in hardware before<br>               it can be blocked. The LAG is already up on the peer side.<br>'local_down_pending_flood_block_enable_remote_down_or_unknown':<br>               This LAG is waiting for flood block of one of its<br>               member interfaces to be enabled in hardware before<br>               it can be blocked.<br>               The LAG state on the peer side is either down or unknown.<br>'local_down_pending_redirect_enable_remote_up':<br>               This LAG is waiting for egress redirection to be<br>               enabled in hardware before it can be blocked.<br>               The LAG is already up on the peer side.<br>'local_down_pending_egress_block_disable_remote_up':<br>               This LAG is waiting for egress block to be removed<br>               from its peer before it can be blocked.<br>               The LAG is already up on the peer side.<br>'local_down_pending_gshut_remote_up':<br>               This LAG is waiting for LACP to shutdown gracefully.<br>               The LAG is already up on the peer side.<br>               LACP will shut the ports<br>'local_down_pending_gshut_remote_down_or_unknown':<br>               This LAG is waiting for lacp to shutdown gracefully.<br>               The LAG is down or unknown on the peer side.<br>               LACP will shut the ports.<br><br>
- `vsx_shutdown_on_split` (filter, optional): Determines whether the port will be shutdown when VSX split occurs.<br>This is only applicable to the ports that are not configured as MCLAG.<br><br>Key: boolean<br>
- `vsx_virtual_gw_mac_v4` (filter, optional): VSX virtual gateway MAC address for the corresponding virtual gateway IPv4 addresses.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `vsx_virtual_gw_mac_v6` (filter, optional): VSX virtual gateway MAC address for the corresponding virtual gateway IPv6 addresses.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `POST /system/ports`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/ports/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/ports/{pid}/ip6_address_custom_link_local`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{pid}/ip6_address_custom_link_local`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{pid}/ip6_address_custom_link_local`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports/{pid}/ip6_addresses`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `anycast_address` (filter, optional): Configure the address as anycast address.<br><br>Key: boolean<br>
- `node_address` (filter, optional): When set to `true`, address on the link is either manually configured or dynamically<br>configured on reception of router advertisements.<br><br>Key: boolean<br>
- `origin` (filter, optional): Specifies whether the IP address is system generated<br>or user configured.<br><br>
- `preferred_lifetime` (filter, optional): The preferred validity of the IPv6 prefix associated with the address, which will<br>be sent in RA messages. The validity of 4294967295 seconds mean, infinite<br>lifetime. The default value depends on<br>[preferred_lifetime](#!/Port).<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ra_prefix` (filter, optional): When set to `true`, the prefix will be included in the RA messages.<br><br>Key: boolean<br>
- `route_tag` (filter, optional): The route tag value for connected route.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `status` (filter, optional): The status of the address with respect to IPv6 neighbor discovery. When set as<br>`tentative`, an address whose uniqueness on a link is being verified. When<br>an address is configured on a network interface (either manually or<br>automatically), the address is initially in the tentative state. Such an address<br>is not considered to be assigned to an interface. An interface discards received<br>packets addressed to a tentative address, but accepts neighbor discovery packets<br>related to duplicate address detection (DAD) for the tentative address. When set<br>as `duplicate`, DAD finds that an address is not unique and it is moved to<br>the duplicate state. Such an address cannot be used for sending and receiving<br>data. When set as `preferred`, an address used to send and receive data<br>packets from and to a network interface without any restriction on the upper<br>layer protocols. When set as `deprecated`, the address becomes<br>deprecated, when its preferred lifetime expires. The use of this address is<br>discouraged, but not prohibited. When set as `invalid`, the address<br>can no longer send or receive data packets. A valid address becomes invalid when<br>its valid lifetime expires. An invalid address is removed from the network<br>interface.<br><br>Key: string<br>
- `type` (filter, optional): Specifies the IPv6 address type.<br><br>
- `valid_lifetime` (filter, optional): The validity(seconds) of IPv6 prefix associated with the address, which will be<br>sent in RA messages. The validity of 4294967295 seconds mean, infinite lifetime.<br>The default value depends on<br>[valid_lifetime](#!/Port).<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `POST /system/ports/{pid}/ip6_addresses`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `data` (body, required): data


---
### `DELETE /system/ports/{pid}/ip6_addresses/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP6_Address address<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{pid}/ip6_addresses/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP6_Address address<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{pid}/ip6_addresses/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP6_Address address<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports/{pid}/ip6_autoconfigured_addresses`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `anycast_address` (filter, optional): Configure the address as anycast address.<br><br>Key: boolean<br>
- `node_address` (filter, optional): When set to `true`, address on the link is either manually configured or dynamically<br>configured on reception of router advertisements.<br><br>Key: boolean<br>
- `origin` (filter, optional): Specifies whether the IP address is system generated<br>or user configured.<br><br>
- `preferred_lifetime` (filter, optional): The preferred validity of the IPv6 prefix associated with the address, which will<br>be sent in RA messages. The validity of 4294967295 seconds mean, infinite<br>lifetime. The default value depends on<br>[preferred_lifetime](#!/Port).<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ra_prefix` (filter, optional): When set to `true`, the prefix will be included in the RA messages.<br><br>Key: boolean<br>
- `route_tag` (filter, optional): The route tag value for connected route.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `status` (filter, optional): The status of the address with respect to IPv6 neighbor discovery. When set as<br>`tentative`, an address whose uniqueness on a link is being verified. When<br>an address is configured on a network interface (either manually or<br>automatically), the address is initially in the tentative state. Such an address<br>is not considered to be assigned to an interface. An interface discards received<br>packets addressed to a tentative address, but accepts neighbor discovery packets<br>related to duplicate address detection (DAD) for the tentative address. When set<br>as `duplicate`, DAD finds that an address is not unique and it is moved to<br>the duplicate state. Such an address cannot be used for sending and receiving<br>data. When set as `preferred`, an address used to send and receive data<br>packets from and to a network interface without any restriction on the upper<br>layer protocols. When set as `deprecated`, the address becomes<br>deprecated, when its preferred lifetime expires. The use of this address is<br>discouraged, but not prohibited. When set as `invalid`, the address<br>can no longer send or receive data packets. A valid address becomes invalid when<br>its valid lifetime expires. An invalid address is removed from the network<br>interface.<br><br>Key: string<br>
- `type` (filter, optional): Specifies the IPv6 address type.<br><br>
- `valid_lifetime` (filter, optional): The validity(seconds) of IPv6 prefix associated with the address, which will be<br>sent in RA messages. The validity of 4294967295 seconds mean, infinite lifetime.<br>The default value depends on<br>[valid_lifetime](#!/Port).<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `DELETE /system/ports/{pid}/ip6_autoconfigured_addresses/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP6_Address address<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{pid}/ip6_autoconfigured_addresses/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP6_Address address<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{pid}/ip6_autoconfigured_addresses/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP6_Address address<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports/{pid}/mgmd_pgs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `group_ip` (filter, optional): Multicast Group IP address.<br><br>Maximum Length: 45<br>
- `mgmd_last_reporter` (filter, optional): IP address of the host which last reported the group.<br><br>Maximum Length: 45<br>
- `mgmd_type` (filter, optional): Type represents whether the entry is for IGMP or MLD.<br><br>
- `source_ip` (filter, optional): Source address from which multicast group traffic is requested to be included<br>or excluded.<br><br>Maximum Length: 45<br>
- `state` (filter, optional): 'include': Group or group, source in INCLUDE mode.<br>'exclude': Group or group, source in EXCLUDE mode.<br>'static':  Group configured as static-group.<br><br>
- `version` (filter, optional): MGMD version for the group or group, source.<br><br>Minimum Value: 1<br>Maximum Value: 3<br>


---
### `GET /system/ports/{pid}/mgmd_pgs/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id1` (path, required): Type represents whether the entry is for IGMP or MLD.<br><br>Reference Resource: [MGMD_PGS](#!/MGMD95PGS)
- `id2` (path, required): Multicast Group IP address.<br><br>Maximum Length: 45<br>Reference Resource: [MGMD_PGS](#!/MGMD95PGS)
- `id3` (path, required): Source address from which multicast group traffic is requested to be included<br>or excluded.<br><br>Maximum Length: 45<br>Reference Resource: [MGMD_PGS](#!/MGMD95PGS)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/multicast_l3_neighbor_forwardings`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Represents the address family for this entry.<br><br>
- `destination_address` (filter, optional): IPv4 or IPv6 destination address. Example 192.168.1.255<br><br>Maximum Length: 49<br>
- `from` (filter, optional): 'ip_directed_broadcast': The Multicast traffic will be flooded at the target subnet.<br>'ip_neighbor_flood':     When layer-2 port goes down, traffic to an IP neighbor<br>                         will be broadcast on VLAN until the neighbor's port information<br>                         is re-learnt.<br>'static_arp_multicast' : The traffic will be replicated to participating set of ports.<br><br>


---
### `GET /system/ports/{pid}/multicast_l3_neighbor_forwardings/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id1` (path, required): 'ip_directed_broadcast': The Multicast traffic will be flooded at the target subnet.<br>'ip_neighbor_flood':     When layer-2 port goes down, traffic to an IP neighbor<br>                         will be broadcast on VLAN until the neighbor's port information<br>                         is re-learnt.<br>'static_arp_multicast' : The traffic will be replicated to participating set of ports.<br><br>Reference Resource: [Multicast_L3_Neighbor_Forwarding](#!/Multicast95L395Neighbor95Forwarding)
- `id2` (path, required): IPv4 or IPv6 destination address. Example 192.168.1.255<br><br>Maximum Length: 49<br>Reference Resource: [Multicast_L3_Neighbor_Forwarding](#!/Multicast95L395Neighbor95Forwarding)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/mvrp_vlans`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `mvrp_applicant_state` (filter, optional): The state of the Applicant state machine. The possible states of the applicant<br>are "Very anxious Observer (VO)", "Very anxious Passive (VP)", "Very anxious New<br>(VN)", "Anxious New (AN)", "Anxious Active (AA)", "Quiet Active (QA)", "Leaving<br>Active (LA)", "Anxious Observer (AO)", "Quiet Observer (QO)", "Anxious Passive<br>(AP)", "Quiet Passive (QP)", "Leaving Observer (LO)"<br><br>
- `mvrp_registrar_state` (filter, optional): The state of the Registrar state machine. The possible states and their<br>description are: "in"  state means "Registered". "lv" state means  "Previously<br>registered, but now being timed out". "mt" state means "Not registered".<br><br>


---
### `GET /system/ports/{pid}/mvrp_vlans/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): MVRP_VLAN vlan-id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/pim_mroutes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): The IP version of this multicast route entry.<br><br>
- `creation_time` (filter, optional): Time in seconds since epoch when this multicast route entry was<br>instantiated in the system.<br><br>Key: integer<br>
- `group_address` (filter, optional): The Group Address of the stream.<br><br>Maximum Length: 45<br>
- `metric` (filter, optional): Unicast routing table metric associated with this route to reach the multicast<br>source.<br><br>Key: integer<br>
- `metric_pref` (filter, optional): Preference value assigned to the unicast routing protocol that provided the<br>route to the multicast source.<br><br>Key: integer<br>
- `source_address` (filter, optional): The Source Address of the stream.<br><br>Maximum Length: 45<br>
- `unicast_routing_protocol` (filter, optional): Unicast routing protocol through which the router learned the upstream port for<br>this route entry.<br><br>
- `upstream_neighbor` (filter, optional): Upstream neighbor address corresponding to this multicast stream.<br><br>Maximum Length: 45<br>


---
### `GET /system/ports/{pid}/pim_mroutes/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id1` (path, required): The Source Address of the stream.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Mroute](#!/PIM95Mroute)
- `id2` (path, required): The Group Address of the stream.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Mroute](#!/PIM95Mroute)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/pim_mroutes/{ppid1}/{ppid2}/pim_nexthops`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `ppid1` (path, required): The Source Address of the stream.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Mroute](#!/PIM95Mroute)
- `ppid2` (path, required): The Group Address of the stream.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Mroute](#!/PIM95Mroute)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `by_proxy_dr` (filter, optional): When VSX PIM active-active feature is enabled, one of the VSX peer<br>acts as DR and the other as proxy-DR. The multicast routes written in proxy-DR<br>would have this flag set. If set, bridge entries are populated in the forwarding path<br>instead of route entries.<br><br>Key: boolean<br>
- `is_pruned` (filter, optional): If the value is `true`, then the nexthop entry is in pruned state.<br>


---
### `GET /system/ports/{pid}/pim_mroutes/{ppid1}/{ppid2}/pim_nexthops/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `ppid1` (path, required): The Source Address of the stream.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Mroute](#!/PIM95Mroute)
- `ppid2` (path, required): The Group Address of the stream.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Mroute](#!/PIM95Mroute)
- `id` (path, required): PIM_Nexthop <br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/pim_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address` (filter, optional): IP address of the PIM neighbor.<br><br>Maximum Length: 45<br>
- `address_family` (filter, optional): IP version of the PIM neighbor.<br><br>
- `anycast_neighbor` (filter, optional): Specifies whether this is a anycast neighbor. In case of anycast neighbor,<br>neighbor's IP address and the interface's primary IP on this router will<br>have the same value.<br><br>Key: boolean<br>
- `dr_priority` (filter, optional): Designated Router Priority (DR Priority) received from the PIM neighbor.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `hold_time` (filter, optional): Hold Time(in seconds) received from the PIM neighbor.<br>


---
### `GET /system/ports/{pid}/pim_neighbors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): IP address of the PIM neighbor.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Neighbor](#!/PIM95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/port_access_auth_configurations`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `auth_enable` (filter, optional): Enables authentication on the port.<br><br>Key: boolean<br>
- `cached_reauth_enable` (filter, optional): Enables cached re-authentication on this port.<br><br>Key: boolean<br>
- `cached_reauth_period` (filter, optional): Time in seconds, during which cached re-authentication is<br>allowed on the port.<br><br>Minimum Value: 30<br>Maximum Value: 4294967295<br>
- `canned_eap_success_enable` (filter, optional): Allow the switch to send a canned EAP success packet to the<br>supplicant to indicate a successful authentication when:<br><br>1. The authentication fails due to a RADIUS server reject, but<br>the port on which the client on-boarded has a reject-role<br>configured.<br>2. The authentication fails due to a RADIUS server timeout, but<br>the port on which the client on-boarded has a critical-role<br>configured.<br><br>Key: boolean<br>
- `discovery_period` (filter, optional): Time period(in seconds) to wait before an EAPOL request<br>identity frame re-transmission on an 802.1X enabled port<br>with no authenticated client.<br>Applicable for 802.1X only.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `eapol_timeout` (filter, optional): Time period(in seconds) to wait for a response from a client<br>before retransmitting an EAPOL PDU. If the value is not set<br>the time period is calculated as per RFC 2988.<br>Applicable for 802.1X only.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `initial_auth_response_timeout` (filter, optional): Time period(in seconds) to wait for the first EAPoL frame from a<br>client before deeming the client to be incapable of 802.1X and<br>start authentication using the next configured authentication<br>method, if any.<br>Applicable for 802.1X only.<br><br>Minimum Value: 1<br>Maximum Value: 300<br>
- `max_requests` (filter, optional): Number of EAPOL requests to supplicant before authentication fails.<br>Applicable for 802.1X only.<br><br>Minimum Value: 1<br>Maximum Value: 10<br>
- `max_retries` (filter, optional): Number of authentication attempts before authentication fails.<br><br>Minimum Value: 1<br>Maximum Value: 10<br>
- `quiet_period` (filter, optional): Time period(in seconds) to wait before processing an<br>authentication request from a client that failed<br>authentication.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `reauth_enable` (filter, optional): Enables periodic re-authentication on this port.<br><br>Key: boolean<br>
- `reauth_period` (filter, optional): Time period(in seconds) to enforce periodic re-authentication<br>of clients.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>


---
### `POST /system/ports/{pid}/port_access_auth_configurations`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `data` (body, required): data


---
### `DELETE /system/ports/{pid}/port_access_auth_configurations/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): Port_Access_Auth_Configuration authentication_method<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{pid}/port_access_auth_configurations/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): Port_Access_Auth_Configuration authentication_method<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{pid}/port_access_auth_configurations/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): Port_Access_Auth_Configuration authentication_method<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports/{pid}/port_access_clients`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `accounting_session_id` (filter, optional): Accounting session identifier associated with this client's session.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `applied_role_type` (filter, optional): Type of special role applied for the client:<br> `preauth`:         applied for clients that are yet to be<br>                    authenticated.<br> `auth`:            applied for clients that have been<br>                    authenticated but have not received any<br>                    specific role or attribute from the<br>                    authentication server.<br> `reject`:          applied for clients that failed<br>                    authentication.<br> `fallback`:        applied for clients that failed<br>                    to onboard, and no role is derived.<br> `critical`:        applied for clients that failed<br>                    authentication due to unreachable.<br>                    authentication servers.<br> `radius-assigned`: applied for clients that have been<br>                    authenticated and received specific role or<br>                    attribute from the authentication server.<br><br>
- `authorization_failure_reason` (filter, optional): Reason for authorization failure:<br> `failed-to-apply-pa-policy`:         Failed to apply Port Access Policy.<br>failed-to-apply-gbp`: Failed to apply Group Based Policy.<br> `failed-to-assign-mac-based-vlan`:   Failed to assign MAC based VLAN.<br> `failed-to-assign-vlan`:             Failed to assign VLAN.<br> `failed-to-assign-vlan-group`:       Failed to assign VLAN group.<br> `failed-to-assign-ubt-vlan`:         Failed to assign UBT VLAN.<br> `failed-to-setup-user-based-tunnel`: Failed to setup User Based Tunnel.<br> `failed-due-to-vlan-limit-violation`: Failed to assign VLANs - VLAN limit per role exceeded.<br> `failed-due-to-pvlan-violation` :    Failed due to Private-VLAN violation.<br><br>
- `client_state` (filter, optional): Port client access state:<br> `initialized`:                new client request recieved.<br> `no-authentication-required`: client authentication is not required.<br> `authenticating`:             client authentication is in progress.<br> `interim-authenticated`:      client authenticated via a lower priority method.<br> `interim-authentication-failed`: client authentication failed by one of the method.<br> `authenticated`:              client authentication completed successfully.<br> `authentication-failed`:      client authentication failed.<br> `authorized`:                 client with a valid and whitelisted MAC.<br> `sticky-authorized`:          sticky client with a valid and whitelisted MAC.<br><br>
- `mac` (filter, optional): MAC address of the client.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `onboarded_method` (filter, optional): Client on-boarded method:<br> `device-profile`: Client was onboarded via the device-profile method.<br> `dot1x`:          Client was authenticated and onboarded via dot1x method.<br> `mac-auth`:       Client was authenticated and onboarded via mac-auth method.<br> `port-security`:  Client was onboarded via the port-security method.<br><br>
- `role_state` (filter, optional): Per client role state status.<br> `not-ready`:                role is not ready for client.<br> `not-valid`:                role is not valid for client.<br> `applied`:                  role has been applied successfully for client.<br> `application-in-progress`:  role update is in progress for client.<br> `application-failed`:       role failed to apply for client.<br><br>
- `session_creation_time` (filter, optional): Time (in seconds) since system boot at which the client session was created.<br>
- `ubt_client_state` (filter, optional):  `bootstrapping`:                client bootstrapping with the UBT cluster.<br> `bootstrap_timedout`:           client bootstrap timed out.<br> `bootstrap_failed`:             client bootstrap failed.<br> `registered`:                   client registered with the UBT cluster.<br> `unbootstrapping`:              client de-registering from the UBT cluster.<br> `unbootstrap_timedout`:         client de-registration process timed out.<br> `deregistered`:                 client de-registered from the UBT cluster.<br> `resource_unavailable`:         client bootstrapped failed - resource unavailable.<br><br>
- `ubt_tunnel_hw_programmed` (filter, optional):  `true`:  Hardware has been programmed to tunnel client traffic<br>          to the UBT cluster.<br> `false`: Hardware programming error, client traffic is not being<br>          tunneled.<br><br>Key: boolean<br>


---
### `GET /system/ports/{pid}/port_access_clients/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): MAC address of the client.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [Port_Access_Client](#!/Port95Access95Client)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/port_access_clients/{ppid}/port_access_client_auth_attributes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `ppid` (path, required): MAC address of the client.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [Port_Access_Client](#!/Port95Access95Client)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `auth_failure_reason` (filter, optional): Reason for authentication failure:<br> `server-timeout`:             authentication server is not reachable.<br> `supplicant-timeout`:         supplicant is not reachable.<br> `server-reject`:              authentication server rejected the client.<br> `attribute-processing-error`: error processing attributes received from<br>                               authentication server.<br><br>
- `auth_state` (filter, optional): State of port access authentication:<br> `initialized`:       the authentication process for client is started.<br> `held`:              authentication has failed for the client and reauthentication <br>                      process is yet to begin.<br> `unauthenticated`:   client to be authenticated.<br> `authenticating`:    client authentication in-progress.<br> `authenticated`:     client authentication completed successfully.<br> `reauthenticating`:  client reauthentication in-progress.<br> `cached-reauthenticated`:  client remains authenticated due to<br>                            radius server unreachability.<br><br>
- `dot1x_eap_method` (filter, optional): EAP method used for authentication in pass-through mode by the<br>802.1X authenticator.<br>`MD5`:       MD5 hash function to generate hashed password<br>`TLS`:       Transport Layer Security Protocol<br>`MS-CHAPv2`: Microsoft's Challenge Handshake Authentication<br>             Protocol<br>`PEAP`:      Protected Extensible Authentication Protocol<br>`TTLS`:      Tunneled Transport Layer Security Protocol<br>`GTC`:       Generic Token Card<br>`TNC`:       Trusted Network Connect<br>`SIM`:       Subscriber Identity Module<br>`AKA`:       Authentication and Key Agreement<br>`AKA-Prime`: Authentication and Key Agreement Prime<br>`PAX`:       Password Authenticated eXchange<br>`PSK`:       Pre-Shared key<br>`SAKE`:      Shared-secret Authentication and Key Establishment<br>`FAST`:      Flexible Authentication via Secure Tunneling<br>`IKEv2`:     Internet Key Exchange<br>`GPSK`:      Generalized Pre-Shared Key<br>`UNKNOWN`:   Unsupported EAP method<br><br>
- `username` (filter, optional): User name of the client.<br><br>Minimum Length: 1<br>Maximum Length: 255<br>


---
### `GET /system/ports/{pid}/port_access_clients/{ppid}/port_access_client_auth_attributes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `ppid` (path, required): MAC address of the client.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [Port_Access_Client](#!/Port95Access95Client)
- `id` (path, required): Port_Access_Client_Auth_Attribute authentication_method<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ports/{pid}/virtual_ip4_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `accept_mode_disable` (filter, optional): Set this value to `true`, to disable the accept mode. If accept mode is enabled,<br>routes for vritual IP addresses will be installed and VR will accept the packets<br>destined to virtual IP addresses. If accept mode is disabled, routes for virtual<br>IP addresses will not be installed hence VR will not accept any packet destined<br>to virtual IP addresses.<br><br>Key: boolean<br>
- `admin_enable` (filter, optional): Set this value to `true`, to activate the VR instance.<br><br>Key: boolean<br>
- `auth_key` (filter, optional): Authentication key to be used with VRRPv2 advertisements.<br>This does not take effect if the VRRP version is VRRPv3.<br><br>Minimum Length: 1<br>
- `auth_mode` (filter, optional): Specifies the authentication mode to be used when exchanging<br>VRRP packets. This is only applicable when VRRP version is VRRPv2.<br> `text`: a clear-text password is included in VRRP advertisements.<br> `md5` : an Authentication Header(AH) is added to the IPv4 headers<br>of the VRRP advertisement packets.<br> `none` : VRRP advertisement packets are not authenticated.<br>This does not take effect if the VRRP version is VRRPv3.<br><br>
- `master_advertise_interval` (filter, optional): Specifies advertisement interval in milliseconds which is advertised by master router.<br><br>Minimum Value: 100<br>Maximum Value: 40950<br>
- `preempt_disable` (filter, optional): Set this value to `true`, to disable preempt mode. When mode is enabled, a<br>Backup router coming up with a higher priority than another Backup that is<br>currently operating as Master will take over the Master function. When the mode<br>is disabled, the protocol prevents higher-priority Backup from taking over the<br>Master operation from a lower-priority Backup. This mode does not prevent an<br>Owner router from resuming the Master function after recovering from being<br>unavailable. Also, the VR instance must be disabled (that is, set "admin_enable"<br>to `false`) when setting this field.<br><br>Key: boolean<br>
- `priority` (filter, optional): The priority value of the VR.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `version` (filter, optional): VRRP protocol version. VRRPv3 supports usage of IPv4 and IPv6 addresses while<br>VRRPv2 only supports IPv4 addresses.<br><br>Minimum Value: 2<br>Maximum Value: 3<br>


---
### `POST /system/ports/{pid}/virtual_ip4_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `data` (body, required): data


---
### `DELETE /system/ports/{pid}/virtual_ip4_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): VRRP group-id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{pid}/virtual_ip4_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): VRRP group-id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{pid}/virtual_ip4_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): VRRP group-id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports/{pid}/virtual_ip6_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `accept_mode_disable` (filter, optional): Set this value to `true`, to disable the accept mode. If accept mode is enabled,<br>routes for vritual IP addresses will be installed and VR will accept the packets<br>destined to virtual IP addresses. If accept mode is disabled, routes for virtual<br>IP addresses will not be installed hence VR will not accept any packet destined<br>to virtual IP addresses.<br><br>Key: boolean<br>
- `admin_enable` (filter, optional): Set this value to `true`, to activate the VR instance.<br><br>Key: boolean<br>
- `auth_key` (filter, optional): Authentication key to be used with VRRPv2 advertisements.<br>This does not take effect if the VRRP version is VRRPv3.<br><br>Minimum Length: 1<br>
- `auth_mode` (filter, optional): Specifies the authentication mode to be used when exchanging<br>VRRP packets. This is only applicable when VRRP version is VRRPv2.<br> `text`: a clear-text password is included in VRRP advertisements.<br> `md5` : an Authentication Header(AH) is added to the IPv4 headers<br>of the VRRP advertisement packets.<br> `none` : VRRP advertisement packets are not authenticated.<br>This does not take effect if the VRRP version is VRRPv3.<br><br>
- `master_advertise_interval` (filter, optional): Specifies advertisement interval in milliseconds which is advertised by master router.<br><br>Minimum Value: 100<br>Maximum Value: 40950<br>
- `preempt_disable` (filter, optional): Set this value to `true`, to disable preempt mode. When mode is enabled, a<br>Backup router coming up with a higher priority than another Backup that is<br>currently operating as Master will take over the Master function. When the mode<br>is disabled, the protocol prevents higher-priority Backup from taking over the<br>Master operation from a lower-priority Backup. This mode does not prevent an<br>Owner router from resuming the Master function after recovering from being<br>unavailable. Also, the VR instance must be disabled (that is, set "admin_enable"<br>to `false`) when setting this field.<br><br>Key: boolean<br>
- `priority` (filter, optional): The priority value of the VR.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `version` (filter, optional): VRRP protocol version. VRRPv3 supports usage of IPv4 and IPv6 addresses while<br>VRRPv2 only supports IPv4 addresses.<br><br>Minimum Value: 2<br>Maximum Value: 3<br>


---
### `POST /system/ports/{pid}/virtual_ip6_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `data` (body, required): data


---
### `DELETE /system/ports/{pid}/virtual_ip6_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): VRRP group-id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/ports/{pid}/virtual_ip6_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): VRRP group-id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/ports/{pid}/virtual_ip6_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): VRRP group-id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ports/{pid}/vsx_remote_interfaces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `admin_state` (filter, optional): The administrative state of the physical network link.<br><br>
- `duplex` (filter, optional): The duplex mode of the physical network link.<br><br>
- `lacp_actor_key` (filter, optional): Peer interface's LACP actor key.<br><br>Key: integer<br>
- `lacp_actor_port_id` (filter, optional): Peer interface's LACP actor port ID.<br>If there is no remote partner value will be empty.<br><br>Key: integer<br>
- `lacp_actor_port_priority` (filter, optional): Peer interface's LACP actor port priority.<br>If there is no remote partner value will be empty.<br><br>Key: integer<br>
- `lacp_actor_system_id` (filter, optional): Peer interface's LACP actor system ID.<br>If there is no remote partner value will be empty.<br><br>Key: string<br>
- `lacp_actor_system_priority` (filter, optional): Peer interface's LACP actor system priority.<br>If there is no remote partner value will be empty.<br><br>Key: integer<br>
- `lacp_partner_key` (filter, optional): Peer interface's LACP partner key.<br><br>Key: integer<br>
- `lacp_partner_port_id` (filter, optional): Peer interface's LACP partner port ID.<br>If there is no remote partner, value will be empty.<br><br>Key: integer<br>
- `lacp_partner_port_priority` (filter, optional): Peer interface's LACP partner port priority.<br>If there is no remote partner value will be empty.<br><br>Key: integer<br>
- `lacp_partner_system_id` (filter, optional): Peer interface's LACP partner system ID.<br>If there is no remote partner value will be empty.<br><br>Key: string<br>
- `lacp_partner_system_priority` (filter, optional): Peer interface's LACP partner system priority.<br>If there is no remote partner value will be empty.<br><br>Key: integer<br>
- `lacp_port_priority` (filter, optional): LACP port-priority.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `link_speed` (filter, optional): The negotiated speed of the physical network link in bits per second. Valid<br>values are positive integers greater than 0.<br><br>Key: integer<br>
- `link_state` (filter, optional): The observed state of the physical network link. This is ordinarily the link's<br>carrier status.<br><br>
- `name` (filter, optional): Name of the peer interface.<br>


---
### `GET /system/ports/{pid}/vsx_remote_interfaces/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The port name. For non-bonded ports, the port name is the same as<br>the associated interface name. The name must otherwise be unique<br>across all ports and interfaces of the system.<br>Reference Resource: [Port](#!/Port)
- `id` (path, required): Name of the peer interface.<br>Reference Resource: [VSX_Remote_Interface](#!/VSX95Remote95Interface)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/prefix_lists`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the prefix list.<br><br>
- `description` (filter, optional): <br>Maximum Length: 80<br>
- `name` (filter, optional): Name of the prefix list.<br><br>Maximum Length: 80<br>
- `origin` (filter, optional): Indicates whether the prefix-list information has been received<br>from the peer or locally configured.<br><br>


---
### `POST /system/prefix_lists`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/prefix_lists/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/prefix_lists/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/prefix_lists/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/prefix_lists/{pid}/prefix_list_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): There are three types, permit, deny, and any.<br><br>
- `ge` (filter, optional): <br>Minimum Value: 0<br>Maximum Value: 128<br>
- `le` (filter, optional): <br>Minimum Value: 0<br>Maximum Value: 128<br>
- `origin` (filter, optional): Indicates whether the prefix-list information has been received<br>from the peer or locally configured.<br><br>
- `prefix` (filter, optional): <br>Maximum Length: 49<br>


---
### `POST /system/prefix_lists/{pid}/prefix_list_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `data` (body, required): data


---
### `DELETE /system/prefix_lists/{pid}/prefix_list_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `id` (path, required): Prefix_List_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/prefix_lists/{pid}/prefix_list_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `id` (path, required): Prefix_List_Entry preference<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/prefix_lists/{pid}/prefix_list_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of the prefix list.<br><br>Maximum Length: 80<br>Reference Resource: [Prefix_List](#!/Prefix95List)
- `id` (path, required): Prefix_List_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/q_profiles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `hw_default` (filter, optional): When true, this row contains the hardware default queue profile.<br><br>The default queue profile will be 8 queues when any of the following conditions<br>occur:<br><br>+No row in this table has hw_default true +More than one row in this table has<br>hw_default true +Any [Q_Profile_Entry](#!/Q95Profile95Entry) rows referenced do not<br>have their hw_default true<br><br>Key: boolean<br>
- `name` (filter, optional): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>


---
### `POST /system/q_profiles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/q_profiles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/q_profiles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/q_profiles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/q_profiles/{pid}/q_profile_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `description` (filter, optional): Used for documentation of these queue configuration parameters.<br><br>Maximum Length: 64<br>
- `hw_default` (filter, optional): When true, this row contains the hardware default queue profile parameters for<br>this queue.<br><br>Key: boolean<br>


---
### `POST /system/q_profiles/{pid}/q_profile_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `data` (body, required): data


---
### `DELETE /system/q_profiles/{pid}/q_profile_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `id` (path, required): Q_Profile_Entry queue_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/q_profiles/{pid}/q_profile_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `id` (path, required): Q_Profile_Entry queue_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/q_profiles/{pid}/q_profile_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the queue profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Q_Profile](#!/Q95Profile)
- `id` (path, required): Q_Profile_Entry queue_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/q_threshold_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): This parameter selects threshold cross behavior:<br><br>* `ecn` - Remark ECT packets to CE when the threshold is crossed<br><br>
- `id` (filter, optional): <br>Minimum Value: 1<br>Maximum Value: 258<br>


---
### `GET /system/q_threshold_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): <br>Minimum Value: 1<br>Maximum Value: 258<br>Reference Resource: [Q_Threshold_Entry](#!/Q95Threshold95Entry)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/q_threshold_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): <br>Minimum Value: 1<br>Maximum Value: 258<br>Reference Resource: [Q_Threshold_Entry](#!/Q95Threshold95Entry)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/qos`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `hw_default` (filter, optional): When true, this row signifies the hardware default schedule profile.<br><br>Default schedule profile is "Strict Priority" when any of the following occur:<br><br>+No row in this table has hw_default true +More than one row in this table has<br>hw_default true +Any [Queue](#!/Queue) rows referenced do not have their hw_default<br>true<br><br>Key: boolean<br>
- `name` (filter, optional): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>


---
### `POST /system/qos`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/qos/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/qos/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/qos/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/qos/{pid}/queues`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `algorithm` (filter, optional): This parameter selects the scheduling behavior of the queue:<br><br>* `strict` - Strict Priority will service all packets in the queue before any<br>packets in lower numbered queues as long as there are no packets in any higher<br>number queue.<br>`dwrr` - Deficit Weighted Round Robin will apportion available bandwidth among<br>all non-empty dwrr queues in relation to their queue weights.<br>`wfq` - Weighted Fair Queuing will apportion available bandwidth among<br>all non-empty wfq queues in relation to their queue weights.<br><br>If this parameter is missing, it is assumed to be 'strict'.<br><br>
- `bandwidth` (filter, optional): The bandwidth limit (in kilobits per second) to apply to egress queue traffic.<br>If no bandwidth value is applied, the bandwidth will not be limited per queue.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `burst` (filter, optional): The burst size (in kilobytes) allowed per bandwidth-limited queue.<br>If no burst is specified, the default burst of 32 KB will be applied.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `hw_default` (filter, optional): When true, this row contains the hardware default schedule profile parameters<br>for this queue.<br><br>Key: boolean<br>
- `weight` (filter, optional): The weight value for this queue. The maximum weight is hardware dependent.<br><br>Minimum Value: 1<br>Maximum Value: 127<br>


---
### `POST /system/qos/{pid}/queues`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `data` (body, required): data


---
### `DELETE /system/qos/{pid}/queues/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `id` (path, required): Queue queue_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/qos/{pid}/queues/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `id` (path, required): Queue queue_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/qos/{pid}/queues/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): There must be a user-defined name of the schedule profile.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [QoS](#!/QoS)
- `id` (path, required): Queue queue_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/qos_cos_map_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active_color` (filter, optional): The color currently implemented in hardware.<br><br>
- `active_local_priority` (filter, optional): The local-priority currently implemented in hardware.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `code_point` (filter, optional): The identifier for an entry in the COS map that is the 802.1Q priority code<br>point for this entry.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `color` (filter, optional): It may be used later in the pipeline in packet-drop decision points. The default<br>is 'green'.<br><br>
- `description` (filter, optional): Used for customer documentation. When empty, the default_description key value<br>from the hw_defaults column will be used.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `local_priority` (filter, optional): This is a switch internal meta-data value that will be associated with the<br>packet. This value will be used later to select the egress queue for the<br>packet. When empty, the default_local_priority key value from the hw_defaults<br>column will be used.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>


---
### `GET /system/qos_cos_map_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The identifier for an entry in the COS map that is the 802.1Q priority code<br>point for this entry.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>Reference Resource: [QoS_COS_Map_Entry](#!/QoS95COS95Map95Entry)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/qos_cos_map_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The identifier for an entry in the COS map that is the 802.1Q priority code<br>point for this entry.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>Reference Resource: [QoS_COS_Map_Entry](#!/QoS95COS95Map95Entry)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/qos_dscp_map_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active_color` (filter, optional): The color currently implemented in hardware.<br><br>
- `active_local_priority` (filter, optional): The local-priority currently implemented in hardware.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `active_priority_code_point` (filter, optional): The 802.1Q priority currently being assigned to packets with this codepoint.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `code_point` (filter, optional): The identifier for an entry in the DSCP map that represents the Differentiated<br>Services Code Point (DSCP) value for this entry.<br><br>Minimum Value: 0<br>Maximum Value: 63<br>
- `color` (filter, optional): It may be used later in the pipeline in packet-drop decision points. The default<br>is 'green'.<br><br>
- `description` (filter, optional): Used for customer documentation. When empty, the default_description key<br>value from the hw_defaults column will be used.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `local_priority` (filter, optional): This is a switch internal meta-data value that will be associated with the<br>packet. This value will be used later to select the egress queue for the<br>packet. When empty, the default_local_priority key value from the hw_defaults<br>column will be used.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>
- `priority_code_point` (filter, optional): The 802.1Q Priority Code Point (PCP) that will be assigned to any IP<br>packet with the specified DSCP codepoint, if that packet's ingress port<br>has an effective trust mode of `trust dscp`.  The new PCP is used when<br>the packet is transmitted out a port or trunk with a VLAN tag.  If the<br>key is not specified, then no remark will occur.<br><br>Minimum Value: 0<br>Maximum Value: 7<br>


---
### `GET /system/qos_dscp_map_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The identifier for an entry in the DSCP map that represents the Differentiated<br>Services Code Point (DSCP) value for this entry.<br><br>Minimum Value: 0<br>Maximum Value: 63<br>Reference Resource: [QoS_DSCP_Map_Entry](#!/QoS95DSCP95Map95Entry)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/qos_dscp_map_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The identifier for an entry in the DSCP map that represents the Differentiated<br>Services Code Point (DSCP) value for this entry.<br><br>Minimum Value: 0<br>Maximum Value: 63<br>Reference Resource: [QoS_DSCP_Map_Entry](#!/QoS95DSCP95Map95Entry)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/radius_config_attributes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `POST /system/radius_config_attributes`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/radius_config_attributes/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Specifies the RADIUS server-groups for which<br>configured attributes will be included while<br>sending access-request packets.<br><br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)<br>Reference Resource: [RADIUS_Config_Attribute](#!/RADIUS95Config95Attribute)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/radius_config_attributes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Specifies the RADIUS server-groups for which<br>configured attributes will be included while<br>sending access-request packets.<br><br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)<br>Reference Resource: [RADIUS_Config_Attribute](#!/RADIUS95Config95Attribute)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/radius_config_attributes/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `id` (path, required): Specifies the RADIUS server-groups for which<br>configured attributes will be included while<br>sending access-request packets.<br><br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)<br>Reference Resource: [RADIUS_Config_Attribute](#!/RADIUS95Config95Attribute)
- `data` (body, required): data


---
### `PUT /system/radius_config_attributes/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Specifies the RADIUS server-groups for which<br>configured attributes will be included while<br>sending access-request packets.<br><br>Reference Resource: [AAA_Server_Group](#!/AAA95Server95Group)<br>Reference Resource: [RADIUS_Config_Attribute](#!/RADIUS95Config95Attribute)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/redundant_managements`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `comm_ip_addr` (filter, optional): Source IP address for the interface port used for communication between<br>management modules. The IP address can be either in the IPv4 format or IPv6<br>format (uses '[' and ']' around the IP address). The IP address can include the<br>protocol and port number to be used, using ':' separators. <br><br>Example: tcp:[0123::4567:89ab:cdef:0123%eth1]:1234<br><br>Minimum Length: 1<br>Maximum Length: 45<br>
- `comm_mac_addr` (filter, optional): Source Ethernet MAC address for the interface port used for communication<br>between management modules.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `hardware_revision` (filter, optional): Hardware revision of the management module is used to ensure <br>the compatibility with redundant management.<br><br>Minimum Length: 1<br>
- `is_local` (filter, optional): Indicates which management module this redundant management <br>module entry belongs to.<br><br>`true`: belongs to the local management module<br>`false`: belongs to the remote management module<br>
- `mgmt_role` (filter, optional): Management role assigned to the management module.<br>`Active`:     Active management module<br>`Standby`:    Standby management module, ready to takeover for <br>              Active management module<br>`Unassigned`: Management module has not been assinged a role<br><br>
- `name` (filter, optional): Name of the management module.  Can be any unique string identifying the<br>management module (e.g. Could include slot number or slot letter).<br>
- `remote_present` (filter, optional): Status of the physical presence of the destination management module.<br>
- `software_revision` (filter, optional): Software revision of the management module is used to ensure <br>the compatibility with redundant management.<br><br>Minimum Length: 1<br>
- `state` (filter, optional): The current state of the management role. Valid values are:<br><br>`booting`:  The module is booting or rebooting.<br>`election`: The election process is taking place.<br>`failover`: A failover event is occuring.<br>`ready`:    The management role is ready.<br>`syncing`:  A file or data syncing operation is in progress.<br>`issu`:     The module is undergoing an in service system upgrade.<br>`unknown`:  The role state is currently unknown<br><br><br>


---
### `GET /system/redundant_managements/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the management module.  Can be any unique string identifying the<br>management module (e.g. Could include slot number or slot letter).<br>Reference Resource: [Redundant_Management](#!/Redundant95Management)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/replication_groups`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/route_maps`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of the routemap.<br><br>Maximum Length: 80<br>


---
### `POST /system/route_maps`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/route_maps/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/route_maps/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/route_maps/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/route_maps/{pid}/route_map_entries`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): There are three types, permit, deny, and any.<br><br>
- `description` (filter, optional): <br>Maximum Length: 80<br>
- `exitpolicy` (filter, optional): Rather than normal exiting, route map can continue on processing next route map,<br>or goto N route map and continue on processing.<br><br>
- `route_map_continue` (filter, optional): Specifies the route-map entry's sequence number that will be executed next if<br>the current entry's match clause is successful<br>If the specified entry does not exist, route-map processing will be terminated at the<br>current sequence number if its clause is matched.<br>Note that the 'continue' sequence number must be higher than the<br>current route-map sequence number for it to take effect.<br><br>Minimum Value: 2<br>Maximum Value: 4294967295<br>


---
### `POST /system/route_maps/{pid}/route_map_entries`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `data` (body, required): data


---
### `DELETE /system/route_maps/{pid}/route_map_entries/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `id` (path, required): Route_Map_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/route_maps/{pid}/route_map_entries/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `id` (path, required): Route_Map_Entry preference<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/route_maps/{pid}/route_map_entries/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of the routemap.<br><br>Maximum Length: 80<br>Reference Resource: [Route_Map](#!/Route95Map)
- `id` (path, required): Route_Map_Entry preference<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/sflows`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `agent_address` (filter, optional): IPv4 or IPv6 address used in sFlow datagrams to identify the device that sent<br>the sFlow data to the sFlow collector. It is usually set to an IP address on <br>the device that is reachable from the collector. This field is mandatory for <br>sFlow to be enabled.<br><br>Maximum Length: 45<br>
- `enabled` (filter, optional): Enables sFlow globally in the system<br><br>Key: boolean<br>
- `header` (filter, optional): Number of bytes of a sampled packet to send to the collector.<br><br>Minimum Value: 64<br>Maximum Value: 256<br>
- `max_datagram` (filter, optional): Maximum number of bytes that will be send in the sFlow datagram.<br><br>Minimum Value: 200<br>Maximum Value: 1400<br>
- `name` (filter, optional): sFlow identifier for the configuration. Should be alphanumeric.<br>
- `num_clear_stats_performed` (filter, optional): Number of clear sFlow statistics performed.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `num_clear_stats_requested` (filter, optional): Number of clear sFlow statistics requested.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `polling` (filter, optional): Specifies the interval in seconds at which counter statistics are sent to the <br>collector.<br><br>Minimum Value: 10<br>Maximum Value: 3600<br>
- `sampling` (filter, optional): Specifies the rate at which packets should be sampled and sent to the collector.<br><br>Minimum Value: 1<br>Maximum Value: 1000000000<br>


---
### `POST /system/sflows`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/sflows/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/sflows/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/sflows/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/sflows/{pid}/collectors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `ip_address` (filter, optional): IP address of the sFlow collector.<br><br>Maximum Length: 45<br>
- `status` (filter, optional): The current connectivity status of the sFlow collector.<br>Value can either be - "ok" which means the device was <br>able to send sFlow datagrams to the collector and <br>"not-reachable"which means that sending sFlow datagrams <br>to the collector failed. This can be because of various <br>reasons such as no route to collector, interface connected <br>to collector is shut, etc.<br><br>
- `udp_port` (filter, optional): Specifies the UDP port used for exchanging messages <br>between switch and sflow collector.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>


---
### `POST /system/sflows/{pid}/collectors`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `data` (body, required): data


---
### `DELETE /system/sflows/{pid}/collectors/{id1}/{id2}/{id3}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `id1` (path, required): Specifies which VRF this sFlow collector should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id2` (path, required): IP address of the sFlow collector.<br><br>Maximum Length: 45<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id3` (path, required): Specifies the UDP port used for exchanging messages <br>between switch and sflow collector.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/sflows/{pid}/collectors/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `id1` (path, required): Specifies which VRF this sFlow collector should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id2` (path, required): IP address of the sFlow collector.<br><br>Maximum Length: 45<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id3` (path, required): Specifies the UDP port used for exchanging messages <br>between switch and sflow collector.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/sflows/{pid}/collectors/{id1}/{id2}/{id3}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `id1` (path, required): Specifies which VRF this sFlow collector should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id2` (path, required): IP address of the sFlow collector.<br><br>Maximum Length: 45<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id3` (path, required): Specifies the UDP port used for exchanging messages <br>between switch and sflow collector.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `data` (body, required): data


---
### `PUT /system/sflows/{pid}/collectors/{id1}/{id2}/{id3}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): sFlow identifier for the configuration. Should be alphanumeric.<br>Reference Resource: [sFlow](#!/sFlow)
- `id1` (path, required): Specifies which VRF this sFlow collector should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id2` (path, required): IP address of the sFlow collector.<br><br>Maximum Length: 45<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `id3` (path, required): Specifies the UDP port used for exchanging messages <br>between switch and sflow collector.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [sFlow_collector](#!/sFlow95collector)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/simplivities`
**Summary**: Delete a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/simplivities`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/simplivities`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `PUT /system/simplivities`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/snmp_alarms`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `SNMP_oid` (filter, optional): The object identifier to be monitored.<br>Only variables that resolve to an ASN.1 primitive type of INTEGER<br>(INTEGER, Integer32,Counter32, Counter64, Gauge32, or TimeTicks)<br>will be monitored.<br><br>Minimum Length: 1<br>Maximum Length: 128<br>
- `absolute_value` (filter, optional): The value of the variable at the end of the sampling period.<br><br>Minimum Value: -2147483648<br>Maximum Value: 2147483647<br>
- `delta_value` (filter, optional): The delta of the variable between the beginning<br>and the end of the sampling period.<br>Applicable only for the sample type 'delta'.<br><br>Minimum Value: -2147483648<br>Maximum Value: 2147483647<br>
- `disable` (filter, optional): Disables RMON alarms.<br><br>Key: boolean<br>
- `falling_threshold` (filter, optional): Falling threshold to be compared against the current value<br>to trigger the SNMP alarm.<br><br>Minimum Value: -2147483648<br>Maximum Value: 2147483647<br>
- `index` (filter, optional): An index that uniquely identifies the SNMP alarm.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `interval` (filter, optional): The interval in seconds, over which the SNMP_oid is sampled<br>and compared with the rising and falling thresholds.<br><br>Minimum Value: 5<br>Maximum Value: 65535<br>
- `last_update_time` (filter, optional): Time (in seconds from epoch) when the last sample was processed.<br><br>Key: integer<br>
- `rising_threshold` (filter, optional): Rising threshold to be compared against the current value<br>to trigger the SNMP alarm.<br><br>Minimum Value: -2147483648<br>Maximum Value: 2147483647<br>
- `sample_type` (filter, optional): The method of sampling of the variable.<br>'absolute': Absolute value of the variable will be compared<br>            with the thresholds.<br>'delta':    The difference between the current and previous<br>            sample of the variable will be compared with the thresholds.<br><br>
- `state` (filter, optional): Current state of the alarm:<br>'rising':  Value has once crossed the rising threshold and<br>           is still above the falling threshold.<br>'falling': Value has once crossed the falling threshold and<br>           is still below the rising threshold.<br>'off':     Value neither crossed the falling nor the rising threshold.<br><br>
- `status` (filter, optional): The status of this alarm entry<br>'valid':          SNMP_oid is valid.<br>'invalid':        SNMP_oid is invalid.<br>'under_creation': Initial state when configuring alarm entry.<br><br>


---
### `POST /system/snmp_alarms`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/snmp_alarms/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): An index that uniquely identifies the SNMP alarm.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SNMP_Alarm](#!/SNMP95Alarm)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/snmp_alarms/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): An index that uniquely identifies the SNMP alarm.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SNMP_Alarm](#!/SNMP95Alarm)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/snmp_alarms/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): An index that uniquely identifies the SNMP alarm.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SNMP_Alarm](#!/SNMP95Alarm)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/snmp_community_acls`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `access_level` (filter, optional): read-only - read-only access for endpoints matching the configured ACL.<br>read-write - read-write access for endpoints matching the configured ACL.<br><br>
- `name` (filter, optional): Community name to be used by the system when communicating over<br>SNMPv1/SNMPv2c.<br><br>Maximum Length: 32<br>


---
### `POST /system/snmp_community_acls`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/snmp_community_acls/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Community name to be used by the system when communicating over<br>SNMPv1/SNMPv2c.<br><br>Maximum Length: 32<br>Reference Resource: [SNMP_Community_ACL](#!/SNMP95Community95ACL)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/snmp_community_acls/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Community name to be used by the system when communicating over<br>SNMPv1/SNMPv2c.<br><br>Maximum Length: 32<br>Reference Resource: [SNMP_Community_ACL](#!/SNMP95Community95ACL)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/snmp_community_acls/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Community name to be used by the system when communicating over<br>SNMPv1/SNMPv2c.<br><br>Maximum Length: 32<br>Reference Resource: [SNMP_Community_ACL](#!/SNMP95Community95ACL)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/snmp_traps`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `community_name` (filter, optional): SNMPv1/SNMPv2c community strings. The default community string is "public".<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `receiver_address` (filter, optional): The IP address of the trap receiver.<br><br>Maximum Length: 45<br>
- `receiver_udp_port` (filter, optional): The UDP port of the trap receiver.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `type` (filter, optional): Trap - Unacknowledged event/error notification type<br>Inform - Acknowledged event/error notification type<br><br>
- `version` (filter, optional): Trap/inform version.<br><br>


---
### `POST /system/snmp_traps`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/snmp_traps/{id1}/{id2}/{id3}/{id4}/{id5}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Specifies which VRF this association should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id2` (path, required): The IP address of the trap receiver.<br><br>Maximum Length: 45<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id3` (path, required): The UDP port of the trap receiver.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id4` (path, required): Trap - Unacknowledged event/error notification type<br>Inform - Acknowledged event/error notification type<br><br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id5` (path, required): Trap/inform version.<br><br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/snmp_traps/{id1}/{id2}/{id3}/{id4}/{id5}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Specifies which VRF this association should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id2` (path, required): The IP address of the trap receiver.<br><br>Maximum Length: 45<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id3` (path, required): The UDP port of the trap receiver.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id4` (path, required): Trap - Unacknowledged event/error notification type<br>Inform - Acknowledged event/error notification type<br><br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id5` (path, required): Trap/inform version.<br><br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/snmp_traps/{id1}/{id2}/{id3}/{id4}/{id5}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Specifies which VRF this association should connect with.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id2` (path, required): The IP address of the trap receiver.<br><br>Maximum Length: 45<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id3` (path, required): The UDP port of the trap receiver.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id4` (path, required): Trap - Unacknowledged event/error notification type<br>Inform - Acknowledged event/error notification type<br><br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `id5` (path, required): Trap/inform version.<br><br>Reference Resource: [SNMP_Trap](#!/SNMP95Trap)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/snmpv3_users`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `auth_pass_phrase` (filter, optional): The key to be used by authentication protocol.<br><br>Minimum Length: 8<br>Maximum Length: 193<br>
- `auth_protocol` (filter, optional): The authentication protocol to be used for authenticating the user.<br>Users without authentication will be disabled when system <br>snmp_security_level is authPriv or authNoPriv.<br><br>
- `enabled` (filter, optional): Indicates whether this user is operational. User might be turned<br>non-operational if it doesn't comply with the system<br>snmp_security_level.<br><br>Key: boolean<br>
- `priv_pass_phrase` (filter, optional): The key to be used by privacy protocol.<br><br>Minimum Length: 8<br>Maximum Length: 193<br>
- `priv_protocol` (filter, optional): The privacy protocol to be used for encrypting the user requests.<br>Users without privacy protocol will be disabled when system <br>snmp_security_level is authPriv<br><br>
- `remote_engine_id` (filter, optional): The SNMPv3 remote engine id in a colon separated hexadecimal <br>notation. Example 80:00:00:09:05:01:04:03:21.<br><br>
- `user_name` (filter, optional): User name that should contain alphanumeric characters.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>


---
### `POST /system/snmpv3_users`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/snmpv3_users/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): User name that should contain alphanumeric characters.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [SNMPv3_User](#!/SNMPv395User)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/snmpv3_users/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): User name that should contain alphanumeric characters.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [SNMPv3_User](#!/SNMPv395User)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/snmpv3_users/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): User name that should contain alphanumeric characters.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [SNMPv3_User](#!/SNMPv395User)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/static_ip_bindings`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the ip binding entry.<br><br>
- `ip_address` (filter, optional): IP address that is bound to the MAC.<br><br>Maximum Length: 45<br>
- `mac` (filter, optional): The MAC address of the client that this binding applies to.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `POST /system/static_ip_bindings`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/static_ip_bindings/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): VLAN of the IP binding.<br><br>Reference Resource: [VLAN](#!/VLAN)<br>Reference Resource: [Static_IP_Binding](#!/Static95IP95Binding)
- `id2` (path, required): IP address that is bound to the MAC.<br><br>Maximum Length: 45<br>Reference Resource: [Static_IP_Binding](#!/Static95IP95Binding)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/static_ip_bindings/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): VLAN of the IP binding.<br><br>Reference Resource: [VLAN](#!/VLAN)<br>Reference Resource: [Static_IP_Binding](#!/Static95IP95Binding)
- `id2` (path, required): IP address that is bound to the MAC.<br><br>Maximum Length: 45<br>Reference Resource: [Static_IP_Binding](#!/Static95IP95Binding)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/static_ip_bindings/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): VLAN of the IP binding.<br><br>Reference Resource: [VLAN](#!/VLAN)<br>Reference Resource: [Static_IP_Binding](#!/Static95IP95Binding)
- `id2` (path, required): IP address that is bound to the MAC.<br><br>Maximum Length: 45<br>Reference Resource: [Static_IP_Binding](#!/Static95IP95Binding)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/stp_instances`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bridge_identifier` (filter, optional): Unique Identifier of a bridge. It is a 64-bit value, <br>(4-bit priority, 12-bit instance ID, 48-bit system MAC address)<br><br>Maximum Length: 45<br>
- `designated_bridge` (filter, optional): The designated bridge name for this STP instance.<br><br>Maximum Length: 45<br>
- `designated_port` (filter, optional): The designated port name for this STP instance.<br><br>Maximum Length: 45<br>
- `designated_port_priority` (filter, optional): The designated port priority for this STP instance.<br><br>Minimum Value: 0<br>Maximum Value: 256<br>
- `designated_root` (filter, optional): The root bridge name for this STP instance.<br><br>Maximum Length: 45<br>
- `forward_delay` (filter, optional): The time in seconds that is spent in the <br>listening and learning states.<br><br>Minimum Value: 4<br>Maximum Value: 30<br>
- `fully_provisioned` (filter, optional): Identifies when all appropriate interfaces have fully joined the instance.<br>Might be `false` at the time of initial provisioning of the instance.<br><br>Key: boolean<br>
- `hardware_grp_id` (filter, optional): The hardware spanning tree group ID.<br><br>Key: integer<br>
- `hello_time` (filter, optional): The time in seconds between consecutive BPDUs sent to a port.<br><br>Minimum Value: 2<br>Maximum Value: 10<br>
- `instance_type` (filter, optional): Identifies, which specific STP protocol the instance is associated with.<br><br>
- `max_age` (filter, optional): The time in seconds a device waits without <br>receiving spanning tree configuration messages before <br>attempting a reconfiguration for this instance.<br><br>Minimum Value: 6<br>Maximum Value: 40<br>
- `mstp_cist_path_cost` (filter, optional): The path cost from the transmitting bridge to the CIST regional root.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `mstp_cist_regional_root` (filter, optional): The regional root bridge for the CIST instance.<br><br>Maximum Length: 45<br>
- `mstp_fid_to_msti` (filter, optional): The FID to MSTID mapping of the spanning tree.<br><br>Key: integer<br>
- `oper_forward_delay` (filter, optional): The operating forward delay time in seconds for this instance.<br><br>Minimum Value: 4<br>Maximum Value: 30<br>
- `oper_hello_time` (filter, optional): The operating hello time in seconds for this instance.<br><br>Minimum Value: 1<br>Maximum Value: 10<br>
- `oper_max_age` (filter, optional): The operating maximum-aging time in seconds for this instance.<br><br>Minimum Value: 6<br>Maximum Value: 40<br>
- `origin` (filter, optional): Specifies whether the instance is created by the system  <br>(MST CIST or RPVST), or by user configuration.<br><br>
- `priority` (filter, optional): The configured priority value.<br>The lower the value, the higher the priority.<br><br>Minimum Value: 0<br>Maximum Value: 15<br>
- `remaining_hops` (filter, optional): The hop count after which the BPDU of this instance <br>is discarded.<br><br>Minimum Value: 0<br>Maximum Value: 40<br>
- `root_path_cost` (filter, optional): The path cost from the transmitting Bridge to the Root Bridge for this instance.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `root_port` (filter, optional): The root port name for this instance.<br><br>Maximum Length: 45<br>
- `root_priority` (filter, optional): The root bridge priority. The lower the value, the higher the priority.<br><br>Minimum Value: 0<br>Maximum Value: 61440<br>
- `stp_instance_id` (filter, optional): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>
- `time_of_top_change` (filter, optional): The time at which the last topology change occurred for this instance.<br>Calculated as time (in seconds) from epoch.<br><br>Key: integer<br>
- `topology_change_count` (filter, optional): The total number of topology changes that have occurred for this instance.<br><br>Minimum Value: 0<br>Maximum Value: 2147483647<br>
- `topology_change_trap_enable` (filter, optional): Enables the topology change trap for this MSTP instance.<br><br>Key: boolean<br>
- `topology_unstable` (filter, optional): Set to 'true' just after a topology change.<br>Set  to 'false' once the topology stabilizes.<br><br>Key: boolean<br>


---
### `POST /system/stp_instances`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/stp_instances/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Identifies, which specific STP protocol the instance is associated with.<br><br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `id2` (path, required): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/stp_instances/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Identifies, which specific STP protocol the instance is associated with.<br><br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `id2` (path, required): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/stp_instances/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Identifies, which specific STP protocol the instance is associated with.<br><br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `id2` (path, required): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/stp_instances/{pid1}/{pid2}/stp_instance_ports`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): Identifies, which specific STP protocol the instance is associated with.<br><br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `pid2` (path, required): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `admin_path_cost` (filter, optional): The cost to reach root port.<br><br>Minimum Value: 0<br>Maximum Value: 200000000<br>
- `boundary_port` (filter, optional): Set to true when the port receives an MSTP BPDU from other regions.<br><br>Key: boolean<br>
- `designated_bridge` (filter, optional): The designated bridge for this port.<br><br>Key: string<br>
- `designated_bridge_priority` (filter, optional): The designated bridge priority at this port.<br><br>Minimum Value: 0<br>Maximum Value: 61440<br>
- `designated_path_cost` (filter, optional): The path cost for designated bridge.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `designated_port` (filter, optional): The designated port ID.<br><br>Maximum Length: 45<br>
- `designated_port_priority` (filter, optional): The designated port priority for this port.<br><br>Minimum Value: 0<br>Maximum Value: 256<br>
- `designated_root` (filter, optional): The root bridge name for an instance.<br><br>Key: string<br>
- `designated_root_priority` (filter, optional): The priority value for designated port.<br><br>Minimum Value: 0<br>Maximum Value: 61440<br>
- `mstp_cist_path_cost` (filter, optional): The CIST path cost from the transmitting bridge to the CIST regional root.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `mstp_cist_regional_root_id` (filter, optional): The regional Root Id for the CIST.<br><br>Key: string<br>
- `oper_path_cost` (filter, optional): The cost to reach root port. If cost is not configured, value is determined from the interface speed.<br>Bandwidth            Port cost<br>10 Mbps              2,000,000<br>100 Mbps             200,000<br>1 Gigabit Ethernet   20,000<br>10 Gigabit Ethernet  2,000<br><br>Minimum Value: 0<br>Maximum Value: 200000000<br>
- `port_priority` (filter, optional): The priority value used along with the switch MAC address to determine<br>which device is root. Configured as a multiple of 16. The lower a priority<br>value, the higher the priority. For LAGs, the default is 4.<br>For other interfaces the default is 8<br><br>Minimum Value: 0<br>Maximum Value: 15<br>
- `port_role` (filter, optional): The role of the port in the active Spanning tree topology.<br>The possible port roles and their definitons are:<br>'Root' port provides the best path (lowest cost) when the switch forwards packets to the root bridge.<br>'Designated' port connects to the designated switch, which incurs the lowest path cost when<br> forwarding packets from that LAN to the root bridge. The port through which the designated switch<br> is attached to the LAN is called the designated port.<br>'Alternate' port offers an alternate path towards the root bridge to the one provided by the current root port.<br>'Backup' port acts as a backup for the path provided by a designated port towards the leaves of the<br> spanning tree.<br>'Master' (MSTP only) port provides the best possible path to reach the common internal spanning-tree (CIST) root<br> bridge from any MSTP region.<br>'Disabled' port has no role within the operation of the spanning tree.<br><br>
- `port_state` (filter, optional): The state of the port in the active topology.<br>The possible port states and their definitons are:<br>'Blocking' means the Layer 2 LAN port does not participate in frame forwarding.<br>'Learning' means the Layer 2 LAN port prepares to participate in frame forwarding.<br>'Forwarding' means the Layer 2 LAN port forwards frames.<br>'Disabled' means the Layer 2 LAN port does not participate in STP and is not forwarding frames.<br><br>
- `reset_at` (filter, optional): Epoch time of the last port reset.<br><br>Key: integer<br>


---
### `GET /system/stp_instances/{pid1}/{pid2}/stp_instance_ports/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): Identifies, which specific STP protocol the instance is associated with.<br><br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `pid2` (path, required): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `id` (path, required): Specifies the port for the STP instance.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [STP_Instance_Port](#!/STP95Instance95Port)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/stp_instances/{pid1}/{pid2}/stp_instance_ports/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid1` (path, required): Identifies, which specific STP protocol the instance is associated with.<br><br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `pid2` (path, required): Unique identifier of the STP Instance.<br><br>Minimum Value: 0<br>Maximum Value: 4094<br>Reference Resource: [STP_Instance](#!/STP95Instance)
- `id` (path, required): Specifies the port for the STP instance.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [STP_Instance_Port](#!/STP95Instance95Port)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/subsystems`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `acl_init_status` (filter, optional): This enum is used to represent the initialization status<br>of a line card subsystem from the ACL feature perspective.<br>'none':    subsystem is still initializing.<br>'success': ACL is successfully applied on<br>           the line card subsystem during initialization or<br>           there is no ACL on the line card subsystem.<br>'failure': ACL is not successfully applied<br>           on the line card subsystem during initialization.<br><br>
- `admin_state` (filter, optional): User configurable admin state of the subsystem. Valid values are:<br><br>+ __diagnostic__:   Put the subsystem into diagnostic mode.<br>+ __down__:   Disable/power down the subsystem.<br>+ __up__:   Enable/power on the subsystem.<br><br>
- `data_plane_state` (filter, optional): Current data plane state of the subsystem row including all the<br>possible initialization and failover phases.<br>Valid values are:<br>`uninitialized`:                  Subsystem is not yet initialized.<br>`initializing_local_data_plane`:  Subsystem is performing initialization process.<br>`waiting_for_control_plane`:      Subsystem is waiting to be connected to the control plane.<br>`connecting_control_plane`:       Subsystem is connecting to the control plane for initialization or failover.<br>`control_plane_connected`:        Subsystem has already established a connection to the control plane.<br>`initialized`:                    Subsystem has completed its initialization process.<br>`connecting_self_to_others`:      Subsystem is connecting to other ready subsystems.<br>`first_run`:                      Subsystem is applying system configuration.<br>`running`:                        Subsystem is available for all the system.<br>`reconfiguring`:                  Subsystem is executing split port reconfiguration.<br>`reconfigured`:                   Subsystem has completed split port reconfiguration.<br>`recovery`:                       Subsystem is undergoing an error recovery.<br>`remote_recovery:`                Subsystem is processing a recovery from a remote subsystem<br>`enhanced_recovering`:            Subsystem is undergoing an enhanced recovery<br>`disconnecting_self_from_others`: Subsystem's configuration is being removed from other ready subsystems.<br>`warmbooting`:                    Subsystem is preparing failover caches<br>`ready_for_failover`:             Subsystem is ready to apply failover caches.<br>`sweeping`:                       Subsystem is applying sweep configuration.<br>`error`:                          Subsystem is in failure condition, when it is connected to other subsystems.<br>                                  Failure details are given in the data_plane_error field<br>`crash`:                          Subsystem is in failure condition, when it isn't connected to other subsystems.<br>`down`:                           Subsystem is being shutdown and it has been deinitialized.<br><br>
- `data_plane_target_state` (filter, optional): Contains the data plane target mode which determines the <br>state the corresponding data plane should be in.<br>Valid values are:<br>`absent`:                      Subsystem not present.<br>`initialize_local_data_plane`: Perform subsystem initialization process.<br>`wait_for_control_plane`:      Subsystem already initialized, wait for the control plane to be reachable.<br>`connect_control_plane`:       Subsystem already initialized, ready to be connected to the control plane.<br>`connect_others_to_self`:      Connect other ready subsystems to this one.<br>`connect_self_to_others`:      Connect this subsystem to other ready subsystems.<br>`first_run`:                   Subsystem is ready to apply system configuration.<br>`steady_state`:                Subsystem is available for the rest of the system.<br>`reconfigure`:                 Subsystem is ready to start split port reconfiguration.<br>`recovery`:                    Subsystem is undergoing an error recovery.<br>`remote_recovery:`             Subsystem is processing a recovery from a remote subsystem<br>`enhanced_recovery`:           Subsystem is undergoing an enhanced recovery<br>`mark_and_sweep`:              Apply mark and sweep configuration on this subsystem.<br>`disconnect_self_from_others`: Remove subsystem configuration on other ready subsystems.<br>`disconnect_others_from_self`: Disconnect other subsystems from this one.<br>`warmboot`:                    Perform warmboot configuration on subsystem.<br>`error`:                       Subsystem in failure condition.<br><br>
- `diagnostic_disable` (filter, optional): Specify *true* to disable and *false* to enable periodic  <br>diagnostics for the respective sub system<br><br>Key: boolean<br>
- `diagnostic_last_run_timestamp` (filter, optional): Epoch time stamp of the latest execution of diagnostics for <br>the respective subsystem.  This value will be populated only <br>if the test ran at least once since boot.<br>
- `diagnostic_performed` (filter, optional): Number of times diagnostics were executed.<br><br>Key: integer<br>
- `diagnostic_requested` (filter, optional): Number of times diagnostics were requested.<br><br>Key: integer<br>
- `fan_configuration_state` (filter, optional): Specify state of fan configuration currently present<br>'safe':          The system contains minimum required<br>                 number of correctly configured fans.<br>'nodata':        Subsystem is initializing and awaiting<br>                 thermal state or there is no fan data<br>                 acquired. This is the default value set<br>                 during initialization.<br>'misconfigured': Some of the fans are incorrectly<br>                 configured. This includes the case where<br>                 fan tray(s) airflow direction do not match<br>                 with System Airflow direction.<br>'insufficient':  The number of fans present are less than<br>                 minimum required.<br><br>
- `lossless_pool_percent` (filter, optional): Current percentage of packet buffer memory dedicated for lossless flow-controlled packets.<br><br>Minimum Value: 0<br>Maximum Value: 100<br>
- `macs_remaining` (filter, optional): The number of available (unused) Ethernet MAC address from the MAC address pool<br>for this subsystem.<br>
- `name` (filter, optional): 
- `next_mac_address` (filter, optional): Next available (unused) Ethernet MAC address from the MAC address pool for this<br>subsystem.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `pac_gbp_init_status` (filter, optional): This enum is used to represent the initialization status<br>of a line card subsystem from the group based policy<br>feature perspective.<br>'none':    subsystem is still initializing.<br>'success': group based policy is successfully applied on<br>           the line card subsystem during initialization or there<br>           is no group based policy on the line card subsystem.<br>'failure': group based policy is not successfully applied<br>           on the line card subsystem during initialization.<br><br>
- `part_number_cfg` (filter, optional): User configurable part number for the subsystem.  When this column is empty:<br><br>+ The subsystem is not explicitly configured yet and any compatible, supported<br>subsystem is allowed to boot.<br>+ If an existing subsystem is physically replaced with a subsystem of a<br>different part number, the interfaces associated with the existing subsystem<br>will be removed prior to adding interfaces of the newly inserted subsystem.<br><br>When this column is configured with a part number:<br><br>+ The subsystem is explicitly configured to only allow a subsystem with that<br>specific part number to boot.<br>+ Physically replacing the existing subsystem with a subsystem of a different<br>part number will require adjusting this column to match the new subsystem.<br>Otherwise subsystem won't boot.<br>+ To configure the device for a new subsystem, the user can change this column<br>with a different part number.  The interfaces associated with the existing<br>subsystem will be removed and the interfaces of the specified subsystem part<br>number will be created.<br><br>Maximum Length: 64<br>
- `poe_persistency_disable` (filter, optional): PoE persistency configuration for this subsystem. Persistent PoE provides the ability to<br>continue power delivery during a soft reboot of the switch. This feature is applicable<br>to subsystems of type `chassis` in non-modular switches, and to subsystems of type `line-card`<br>in modular switches. This configuration is ignored on a non-PoE capable subsystems.<br><br>Key: boolean<br>
- `policy_init_status` (filter, optional): This enum is used to represent the initialization status<br>of a line card subsystem from the policy feature perspective.<br>'none':    subsystem is still initializing.<br>'success': policy is successfully applied on<br>           the line card subsystem during initialization or<br>           there is no policy on the line card subsystem.<br>'failure': policy is not successfully applied<br>           on the line card subsystem during initialization.<br><br>
- `power_consumed` (filter, optional): Instantaneous power that this subsystem is consuming.  Updated<br>on a 5 second interval.  If the value is empty then this feature<br>is not supported due to no means to obtain the data.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `psu_redundancy_oper` (filter, optional): Power supply redundancy that the chassis is currently operating as:<br>'none': The chassis currently does not have power supply redundancy.<br>'n+1':  The chassis currently has N+1 power supply redundancy.<br>        One power supply is redundant.<br>'n+n':  The chassis currently has N+N power supply redundancy.<br>        The number of redundant power supplies is the same as the<br>        number of active power supplies.<br><br>
- `psu_redundancy_set` (filter, optional): Power supply redundancy configured for the chassis:<br>'none': power supply redundancy is not configured.<br>'n+1':  N+1 power supply redundancy is configured. One power<br>        supply is redundant.<br>'n+n':  N+N power supply redundancy is configured. The number of<br>        redundant power supplies is the same as the number of<br>        active power supplies.<br><br>
- `quick_poe` (filter, optional): Quick PoE configuration for this subsystem. Quick PoE provides the ability for<br>the switch (PSE) to power up connected PDs soon after a cold reboot.<br>This feature is applicable to subsystems of type `chassis` in<br>non-modular switches, and to subsystems of type `line-card`<br>in modular switches. This configuration is ignored on non-PoE capable subsystems.<br><br>Key: boolean<br>
- `selftest_disable` (filter, optional): Specify *true* to disable and *false* to enable <br>for the respective sub system<br><br>Key: boolean<br>
- `state` (filter, optional): The state of the subsystem.  Valid values are:<br><br>`deinitializing`: Subsystem is being deinitialized.<br>`diagnostic`:     Subsystem can be troubleshot.<br>`down`:           Subsystem is powered down.<br>`empty`:          Subsystem is not physically in the chassis.<br>`failed`:         Subsystem has failed due to errors.<br>`failover`:       Subsystem is failing over.<br>`initializing`:   Subsystem is being initialized.<br>`present`:        Subsystem is physically in the chassis.<br>`ready`:          Subsystem is considered available for the rest of the system.<br>`updating`:       Subsystem is undergoing In-System Programming.<br>`unsupported`:    Subsystem is unsupported.<br><br><br>
- `thermal_state` (filter, optional): Temperature status of this subsystem:<br>'safe':     Normal operating temperature conditions.  All sensors<br>            associated with this subsystem are within nominal<br>            range.<br>'nodata':   Subsystem is initializing and awaiting temperature<br>            state or there is no temperature data acquired for<br>            the subsystem.  This is the default value set during<br>            initialization.<br>'critical': Temperature has reached a critical level and it is<br>            recommended to take an immediate action.<br>'overtemp': Temperature has reached an over temperature condition<br>            and it is recommended to take action if the<br>            temperature does not return to the safe operating<br>            conditions after a time.  The amount of time is<br>            dependent upon the HW configuration.<br>'low':      Temperature has reached a low temperature condition<br>            and it is recommended to take action if the<br>            temperature does not return to the safe operating<br>            conditions after a time.  The amount of time is<br>            dependent upon the HW configuration.<br>'crit_low': Temperature has reached a low critical level and it<br>            is recommended to take an immediate action.<br>Indicates whether the subsystem is within normal operating<br>temperature ranges or if an action is required to prevent damage<br>to the HW.<br><br>
- `type` (filter, optional): <br>
- `usb_status` (filter, optional): Current USB port status:<br>`disabled`:       The USB port is disabled.<br>`empty`:          The USB port is enabled and no device is inserted.<br>`unknown_device`: The USB port is enabled and an unknown device is inserted.<br>`mass_storage`:   The USB port is enabled and a USB mass storage device is inserted.<br>`bluetooth`:      The USB port is enabled and a USB Bluetooth adapter is inserted.<br><br>


---
### `GET /system/subsystems/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `id2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/subsystems/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `id2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/subsystems/{pid1}/{pid2}/buttons`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `type` (filter, optional): The type of button. led_mode: Alters the LEDs to show useful information.<br>


---
### `GET /system/subsystems/{pid1}/{pid2}/buttons/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): Button name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/subsystems/{pid1}/{pid2}/daemons`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): The name of the daemon.<br>
- `restart_count` (filter, optional): Number of times the daemon was restarted (gracefully or not) since system boot.<br>The value might be missing if daemon doesn't support restart counting.<br><br>Key: integer<br>
- `state` (filter, optional): The state of the daemon.<br><br>`running`: Daemon is running on the subsystem.<br>`down`:    Daemon is not running currently.<br><br>


---
### `GET /system/subsystems/{pid1}/{pid2}/daemons/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): The name of the daemon.<br>Reference Resource: [Daemon](#!/Daemon)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/subsystems/{pid1}/{pid2}/daemons/{ppid}/plugins`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `ppid` (path, required): The name of the daemon.<br>Reference Resource: [Daemon](#!/Daemon)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `major_version` (filter, optional): The major version number of the currently loaded plugin<br><br>Minimum Value: 0<br>
- `minor_version` (filter, optional): The minor version number of the currently loaded plugin<br><br>Minimum Value: 0<br>


---
### `GET /system/subsystems/{pid1}/{pid2}/daemons/{ppid}/plugins/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `ppid` (path, required): The name of the daemon.<br>Reference Resource: [Daemon](#!/Daemon)
- `id` (path, required): Plugin name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/subsystems/{pid1}/{pid2}/diag_test_results`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `current_errorcode` (filter, optional): Error code corresponding to the current execution of this test. <br>On success the error code will be set to *0* where as in case of <br>failure, it contains the error code corresponding to the failure.<br>
- `errorcode_history` (filter, optional): Error code obtained from the recent failure of this test.<br>
- `failure_from_last_boot` (filter, optional): Total number of failures of this test since boot.<br>
- `failure_from_last_success` (filter, optional): Count of consecutive failures of this test since the last time <br>the test has passed.<br>
- `first_run_timestamp` (filter, optional): Epoch time stamp of the first execution of this test since boot.<br>
- `iteration_count` (filter, optional): Total number of execution of this test since boot.<br>
- `last_run_timestamp` (filter, optional): Epoch time stamp of the latest execution of this test.<br>
- `name` (filter, optional): Test case name.<br><br>Minimum Length: 1<br>Maximum Length: 60<br>
- `test_status` (filter, optional): Test case status.<br>`Pass`:    Test is successful.<br>`Fail`:    Test failed.<br>`Skipped`: Test has been skipped as the device was not ready.<br><br>


---
### `GET /system/subsystems/{pid1}/{pid2}/diag_test_results/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id1` (path, required): Management Module instance in which the test case is executed.<br><br>Reference Resource: [Subsystem](#!/Subsystem)<br>Reference Resource: [Diag_Test_Result](#!/Diag95Test95Result)
- `id2` (path, required): Test case name.<br><br>Minimum Length: 1<br>Maximum Length: 60<br>Reference Resource: [Diag_Test_Result](#!/Diag95Test95Result)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/subsystems/{pid1}/{pid2}/fans`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `direction` (filter, optional): Air flow direction for the fan (if fan supports monitoring).<br>The valid values are:<br>'b2f': Air flows from the back of the system to the front<br>'f2b': Air flows from the front of the system to the back<br>'l2b': Air flows from the left of the system to the back<br>'r2b': Air flows from the right of the system to the back<br>'l2r': Air flows from the left of the system to the right<br><br>
- `name` (filter, optional): 
- `rpm` (filter, optional): Current Fan RPM (if fan supports monitoring).<br><br>Minimum Value: 0<br>
- `speed` (filter, optional): Relative fan speed based on nominal speed range for the fan.<br>When fan speed is not monitored for a fan, this column is not<br>updated with any value. The valid values are:<br>'slow':   0-24%<br>'normal': 25-49%<br>'medium': 50-74%<br>'fast':   75-99%<br>'max':    100%<br><br>
- `status` (filter, optional): Current state of the fan:<br>'ok':    Fan is operating normally<br>'fault': Fan is in a fault event<br>'empty': Fan is not installed in the system<br><br>


---
### `GET /system/subsystems/{pid1}/{pid2}/fans/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): Reference Resource: [Fan](#!/Fan)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/subsystems/{pid1}/{pid2}/leds`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `color` (filter, optional): Color value is the color of the LED.<br><br>
- `id` (filter, optional): Logical name of the LED.<br>
- `locator` (filter, optional): Indicates whether LED is used as a locator, with a state configurable by the user.<br><br>
- `state` (filter, optional): State of the LED controls the lighting behavior.<br><br>
- `status` (filter, optional): Status of the LED is the current operational status.<br><br>


---
### `GET /system/subsystems/{pid1}/{pid2}/leds/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): Logical name of the LED.<br>Reference Resource: [LED](#!/LED)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/subsystems/{pid1}/{pid2}/leds/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): Logical name of the LED.<br>Reference Resource: [LED](#!/LED)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/subsystems/{pid1}/{pid2}/power_supplies`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): 
- `status` (filter, optional): Current status for the power supply.  Valid value are:<br>'ok':            power supply is operating normally<br>'fault_absent':  no power supply is installed<br>'fault_input':   there is a fault condition on the input of the<br>                 power supply<br>'fault_output':  there is a fault condition on the output of the<br>                 power supply<br>'fault_poe':     there is a fault condition on the PoE output of the<br>                 power supply<br>'fault_norecov': power supply has experienced a non recoverable fault<br>                 condition<br>'alert':         power supply has experienced an abnormal event<br>                 but it is still operational<br>'unknown':       power supply has experienced an unknown fault<br>                 condition<br>'unsupported':   power supply is not of a known supported type<br>'warning':       there is an internal fault condition but the<br>                 power supply is still operational<br><br>


---
### `GET /system/subsystems/{pid1}/{pid2}/power_supplies/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): Reference Resource: [Power_supply](#!/Power95supply)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/subsystems/{pid1}/{pid2}/temp_sensors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `fan_state` (filter, optional): Recommended minimum fan setting based on current temperature:<br>'normal': normal fan speed recommended<br>'medium': medium fan speed recommended<br>'fast':   fast fan speed recommended<br>'max':    recommend using the maximum fan speed<br>The fan control process chooses the worst-case sensor when<br>determining this value.<br><br>
- `location` (filter, optional): Descriptive text for the physical location of the temperature<br>sensor relative to the subsystem.<br>
- `max` (filter, optional): Historic maximum, in millidegrees Celsius.<br>
- `min` (filter, optional): Historic minimum, in millidegrees Celsius.<br>
- `name` (filter, optional): Logical name of the temperature sensor, including the subsystem<br>name and numeric identifier of the temperature sensor.<br>
- `status` (filter, optional): Results of evaluation of the current temperature against the<br>sensor's threshold values:<br>'uninitialized': Sensor has not been initialized<br>'normal':        Sensor is within nominal temperature range<br>'min':           Lowest temperature from this sensor<br>'max':           Highest temperature from this sensor<br>'low_critical':  Lowest threshold temperature for this sensor<br>'critical':      Highest threshold temperature for this sensor<br>'fault':         Fault event for this sensor<br>'emergency':     Over temperature event for this sensor<br><br>
- `temperature` (filter, optional): Current temperature reading, in millidegrees Celsius.<br>


---
### `GET /system/subsystems/{pid1}/{pid2}/temp_sensors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid1` (path, required): <br>Reference Resource: [Subsystem](#!/Subsystem)
- `pid2` (path, required): Reference Resource: [Subsystem](#!/Subsystem)
- `id` (path, required): Logical name of the temperature sensor, including the subsystem<br>name and numeric identifier of the temperature sensor.<br>Reference Resource: [Temp_sensor](#!/Temp95sensor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/syslog_remotes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `connected` (filter, optional): Transport layer protocol connection status with the server.<br>Applicable only in TCP and TLS transport type.<br><br>Key: boolean<br>
- `include_auditable_events` (filter, optional): Specifies whether auditable events (audit and authentication)<br> should be transmitted to the remote syslog server.<br><br>Key: boolean<br>
- `port_number` (filter, optional): Port number of the syslog server.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `remote_host` (filter, optional): FQDN or host name or IPv4 address or IPv6 address of the syslog server.<br><br>Minimum Length: 1<br>Maximum Length: 256<br>
- `severity` (filter, optional): Filter syslog messages with severity.  Only messages with severity higher than<br>or equal to the specified value will be sent to the remote server.<br><br>
- `tls_auth_mode` (filter, optional): TLS authentication mode used to authenticate the server:<br>'certificate':   certificate based authentication<br>'subject-name':  certificate and subject name based authentication<br><br>
- `transport` (filter, optional): Transport layer protocol used to forward messages to the server.<br><br>
- `unsecure_tls_renegotiation` (filter, optional): Enable TLS session with syslog server which does not support secure <br>renegotiation.<br><br>Key: boolean<br>


---
### `POST /system/syslog_remotes`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/syslog_remotes/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): FQDN or host name or IPv4 address or IPv6 address of the syslog server.<br><br>Minimum Length: 1<br>Maximum Length: 256<br>Reference Resource: [Syslog_Remote](#!/Syslog95Remote)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/syslog_remotes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): FQDN or host name or IPv4 address or IPv6 address of the syslog server.<br><br>Minimum Length: 1<br>Maximum Length: 256<br>Reference Resource: [Syslog_Remote](#!/Syslog95Remote)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/syslog_remotes/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): FQDN or host name or IPv4 address or IPv6 address of the syslog server.<br><br>Minimum Length: 1<br>Maximum Length: 256<br>Reference Resource: [Syslog_Remote](#!/Syslog95Remote)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/thermals`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `derate` (filter, optional): Current derating cooling settings for this group of sensors.<br>Derating affects the entire system.<br>
- `name` (filter, optional): Unique identifier for this group of sensors.<br>
- `status` (filter, optional): Current status of this group of sensors.  Status conditions can<br>affect how fans operates.<br>


---
### `GET /system/thermals/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Unique identifier for this group of sensors.<br>Reference Resource: [Thermal](#!/Thermal)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/threshold_profiles`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): The threshold profile must have a user-defined name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>


---
### `POST /system/threshold_profiles`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/threshold_profiles/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The threshold profile must have a user-defined name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Threshold_Profile](#!/Threshold95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/threshold_profiles/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The threshold profile must have a user-defined name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Threshold_Profile](#!/Threshold95Profile)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/threshold_profiles/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The threshold profile must have a user-defined name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [Threshold_Profile](#!/Threshold95Profile)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/track_entities`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `id` (filter, optional): Track entity index.<br><br>Minimum Value: 1<br>Maximum Value: 256<br>
- `status_up` (filter, optional): Specifies track entity status based on configured tracked L3 interface state.<br>The status is set to `true` if the tracked L3 interface state is `up`. Otherwise<br>set to `false`.<br><br>Key: boolean<br>


---
### `POST /system/track_entities`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/track_entities/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Track entity index.<br><br>Minimum Value: 1<br>Maximum Value: 256<br>Reference Resource: [Track_Entity](#!/Track95Entity)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/track_entities/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Track entity index.<br><br>Minimum Value: 1<br>Maximum Value: 256<br>Reference Resource: [Track_Entity](#!/Track95Entity)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/track_entities/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Track entity index.<br><br>Minimum Value: 1<br>Maximum Value: 256<br>Reference Resource: [Track_Entity](#!/Track95Entity)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/ubt_mdest_rx_tunnels`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `controller_ip` (filter, optional): SAC or S-SAC IP address of the zone that this tunnel belongs to.<br><br>Maximum Length: 45<br>
- `gre_key` (filter, optional): GRE key associated with this tunnel.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `local_ip` (filter, optional): Switch local IP address.<br><br>Maximum Length: 45<br>
- `tunnel_state` (filter, optional): Tunnel status.<br> `activating`:          Tunnel is being provisioned in the hardware.<br> `activated`:           Tunnel has been provisioned in the hardware.<br> `deactivating`:        Request to delete tunnel from the hardware.<br> `deactivated`:         Tunnel has been deleted from the hardware.<br> `activation_failed`:   Tunnel provisioning in the hardware failed.<br> `deactivation_failed`: Hardware tunnel deletion failed.<br><br>
- `ubt_statistics_clear_performed` (filter, optional): Number of times statistics information for this tunnel was cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ubt_statistics_clear_requested` (filter, optional): Number of times request was made to clear statistics for this tunnel.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `GET /system/ubt_mdest_rx_tunnels/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): VRF instance that this tunnel belongs to.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [UBT_MDEST_RX_Tunnel](#!/UBT95MDEST95RX95Tunnel)
- `id2` (path, required): Switch local IP address.<br><br>Maximum Length: 45<br>Reference Resource: [UBT_MDEST_RX_Tunnel](#!/UBT95MDEST95RX95Tunnel)
- `id3` (path, required): SAC or S-SAC IP address of the zone that this tunnel belongs to.<br><br>Maximum Length: 45<br>Reference Resource: [UBT_MDEST_RX_Tunnel](#!/UBT95MDEST95RX95Tunnel)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/ubt_uac_tunnels`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `destination_ip` (filter, optional): Tunnel destination IP address.<br><br>Maximum Length: 45<br>
- `gre_key` (filter, optional): GRE key associated with this tunnel.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `source_ip` (filter, optional): Tunnel source IP address.<br><br>Maximum Length: 45<br>
- `tunnel_state` (filter, optional): Tunnel status.<br> `activating`:          Tunnel is being provisioned in the hardware.<br> `activated`:           Tunnel has been provisioned in the hardware.<br> `deactivating`:        Request to delete tunnel from the hardware.<br> `deactivated`:         Tunnel has been deleted from the hardware.<br> `activation_failed`:   Tunnel provisioning in the hardware failed.<br> `deactivation_failed`: Hardware tunnel deletion failed.<br><br>
- `ubt_statistics_clear_performed` (filter, optional): Number of times statistics information for this tunnel was cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ubt_statistics_clear_requested` (filter, optional): Number of times request was made to clear statistics for this tunnel.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `GET /system/ubt_uac_tunnels/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): VRF instance that this tunnel belongs to.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [UBT_UAC_Tunnel](#!/UBT95UAC95Tunnel)
- `id2` (path, required): Tunnel source IP address.<br><br>Maximum Length: 45<br>Reference Resource: [UBT_UAC_Tunnel](#!/UBT95UAC95Tunnel)
- `id3` (path, required): Tunnel destination IP address.<br><br>Maximum Length: 45<br>Reference Resource: [UBT_UAC_Tunnel](#!/UBT95UAC95Tunnel)
- `id4` (path, required): GRE key associated with this tunnel.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>Reference Resource: [UBT_UAC_Tunnel](#!/UBT95UAC95Tunnel)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/udp_bcast_forwarder_servers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `udp_dport` (filter, optional): Using this destination udp port, UDP broadcast packets are<br>forwarded to the configured server(s).<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `POST /system/udp_bcast_forwarder_servers`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/udp_bcast_forwarder_servers/{id1}/{id2}/{id3}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): VRF through which server is reachable.<br>If not specified, default VRF is considered.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id2` (path, required): Reference to the routed port on which packets are received.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id3` (path, required): Using this destination udp port, UDP broadcast packets are<br>forwarded to the configured server(s).<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/udp_bcast_forwarder_servers/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): VRF through which server is reachable.<br>If not specified, default VRF is considered.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id2` (path, required): Reference to the routed port on which packets are received.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id3` (path, required): Using this destination udp port, UDP broadcast packets are<br>forwarded to the configured server(s).<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/udp_bcast_forwarder_servers/{id1}/{id2}/{id3}`
**Summary**: Create a new resource instance

**Parameters:**
- `id1` (path, required): VRF through which server is reachable.<br>If not specified, default VRF is considered.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id2` (path, required): Reference to the routed port on which packets are received.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id3` (path, required): Using this destination udp port, UDP broadcast packets are<br>forwarded to the configured server(s).<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `data` (body, required): data


---
### `PUT /system/udp_bcast_forwarder_servers/{id1}/{id2}/{id3}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): VRF through which server is reachable.<br>If not specified, default VRF is considered.<br><br>Reference Resource: [VRF](#!/VRF)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id2` (path, required): Reference to the routed port on which packets are received.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `id3` (path, required): Using this destination udp port, UDP broadcast packets are<br>forwarded to the configured server(s).<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>Reference Resource: [UDP_Bcast_Forwarder_Server](#!/UDP95Bcast95Forwarder95Server)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/user_groups`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `origin` (filter, optional): Indicator of whether the user group is built-in (system-defined)<br>or configured.<br>Unlike user configured user groups, built-in user groups cannot be modified or deleted.<br>Users belonging to configured user groups won't have access to REST APIs.<br><br>


---
### `POST /system/user_groups`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/user_groups/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/user_groups/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/user_groups/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/user_groups/{pid}/rbac_rules`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `action` (filter, optional): 'permit': User operation will be allowed.<br>'deny':   User operation will be denied.<br>RBAC rule will only be activated when an associated action is provided.<br><br>
- `comment` (filter, optional): Comment associated with the RBAC rule.<br><br>Maximum Length: 256<br>
- `invalid_reason` (filter, optional): Indicates the reason why the RBAC rule is invalid. Empty when <br>the RBAC rule is `valid` or `not_processed`.<br>'missing_action'           : The `action` field is missing.<br>'missing_regex'            : The `command` regex in `cli` field is missing.<br>'invalid_cli_command_regex': The `command` regex in `cli` field is invalid.<br><br>
- `status` (filter, optional): Indicates the status of the RBAC rule. Only the valid RBAC rules <br>are used during local authorization.<br>'valid'        : An RBAC rule is valid if one of the conditions are met.<br>                 - Only `comment` is provided.<br>                 - `action` and `cli` are provided with a valid <br>                    POSIX compliant `command` regex.<br>                 - `comment`, `action` and `cli` are provided with a <br>                    valid POSIX compliant `command` regex.<br>'invalid'      : The RBAC rule is invalid.<br>'not_processed': The RBAC rule is not processed yet.<br><br>


---
### `POST /system/user_groups/{pid}/rbac_rules`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `data` (body, required): data


---
### `DELETE /system/user_groups/{pid}/rbac_rules/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `id` (path, required): RBAC_Rule_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/user_groups/{pid}/rbac_rules/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `id` (path, required): RBAC_Rule_Entry sequence_number<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/user_groups/{pid}/rbac_rules/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): Name of the user group. Built-in user groups are as follows:<br>`administrators`: System-defined group with associated privilege level of 15.<br>                  Members have access to:<br>                      All the CLI commands and bash shell.<br>                      All the REST Methods through REST APIs.<br>`operators`:      System-defined group with associated privilege level of 1.<br>                  Members have access to:<br>                      All "show" CLI commands (except those that display sensitive information).<br>                      All "GET" requests through REST APIs.<br>`auditors`:       System-defined group with associated privilege level of 19.<br>                  Members have access to:<br>                      All "show" CLI commands to display and copy security logs.<br>                      All "GET" requests for security logs through REST APIs.<br>Only users belonging to the above three default groups will be allowed access to REST APIs.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User_Group](#!/User95Group)
- `id` (path, required): RBAC_Rule_Entry sequence_number<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/users`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `name` (filter, optional): Name of the user.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `origin` (filter, optional): Indicator of whether the user is built-in (system-defined)<br>or configured.<br>Unlike user configured users, built-in users cannot be deleted.<br><br>
- `password` (filter, optional): SHA1 or SHA512 encrypted password of the user.<br><br>Minimum Length: 0<br>Maximum Length: 192<br>


---
### `POST /system/users`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/users/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): Name of the user.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User](#!/User)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/users/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Name of the user.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User](#!/User)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/users/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `id` (path, required): Name of the user.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User](#!/User)
- `data` (body, required): data


---
### `PUT /system/users/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): Name of the user.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [User](#!/User)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/virtual_network_ids`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `id` (filter, optional): Network Identifier.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>
- `state` (filter, optional): Status of this virtual network ID:<br>'operational':         network ID is fully provisioned in the forwarding path<br>'configuration_error': network ID provisioning failed due to misconfiguration<br>'no_hw_resources':     network ID provisioning failed due to insufficient resources<br>'activating':          network ID is being provisioned<br><br>
- `type` (filter, optional): Type of the network identifier.<br><br>


---
### `POST /system/virtual_network_ids`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/virtual_network_ids/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `id1` (path, required): Type of the network identifier.<br><br>Reference Resource: [Virtual_Network_ID](#!/Virtual95Network95ID)
- `id2` (path, required): Network Identifier.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>Reference Resource: [Virtual_Network_ID](#!/Virtual95Network95ID)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/virtual_network_ids/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `id1` (path, required): Type of the network identifier.<br><br>Reference Resource: [Virtual_Network_ID](#!/Virtual95Network95ID)
- `id2` (path, required): Network Identifier.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>Reference Resource: [Virtual_Network_ID](#!/Virtual95Network95ID)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/virtual_network_ids/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `id1` (path, required): Type of the network identifier.<br><br>Reference Resource: [Virtual_Network_ID](#!/Virtual95Network95ID)
- `id2` (path, required): Network Identifier.<br><br>Minimum Value: 1<br>Maximum Value: 16777214<br>Reference Resource: [Virtual_Network_ID](#!/Virtual95Network95ID)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vlans`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `aclmac_in_cfg_version` (filter, optional): The version of the 'aclmac_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclmac_in_cfg' value. An empty value mean no ingress MAC ACL has been<br>configured for the VLAN. Ignored if configured on VLANs with type = 'internal'.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv4_in_cfg_version` (filter, optional): The version of the 'aclv4_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclv4_in_cfg' value. An empty value mean no ingress IPv4 ACL has been<br>configured for the VLAN. Ignored if configured on VLANs with type = 'internal'.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv6_in_cfg_version` (filter, optional): The version of the 'aclv6_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'aclv6_in_cfg' value. An empty value mean no ingress IPv6 ACL has been<br>configured for the VLAN. Ignored if configured on VLANs with type = 'internal'.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `admin` (filter, optional): Administratively configured state of this VLAN.<br>This is user configurable only for static VLANs.<br><br>
- `description` (filter, optional): User provided description of this VLAN.<br><br>Key: string<br>
- `dhcpv4_snooping_binding_disable` (filter, optional): Disables learning of DHCPv4 Snooping binding entries.<br><br>Key: boolean<br>
- `dhcpv4_snooping_enable` (filter, optional): Enables DHCPv4 Snooping feature on the VLAN.<br>DHCPv4 Snooping is active on the Ports of the VLAN only if the feature<br>is enabled on the VLAN and globally.<br><br>Key: boolean<br>
- `dhcpv4_snooping_guard_disable` (filter, optional): Disables DHCP packet inspection for this VLAN. This would disable<br>enforcement of any snoop policy configuration on this VLAN including<br>the trusted/untrusted port configurations. It will also disable validation<br>of DHCP packets for compliance with the snooping database information.<br><br>Key: boolean<br>
- `dhcpv6_snooping_binding_disable` (filter, optional): Disables learning of DHCPv6 Snooping binding entries.<br><br>Key: boolean<br>
- `dhcpv6_snooping_enable` (filter, optional): Enables DHCPv6 Snooping feature on the VLAN.<br>DHCPv6 Snooping is active on the Ports of the VLAN only if the feature<br>is enabled on the VLAN and globally.<br><br>Key: boolean<br>
- `dhcpv6_snooping_guard_disable` (filter, optional): Disables DHCP packet inspection for this VLAN. This would disable<br>enforcement of any snoop policy configuration on this VLAN including<br>the trusted/untrusted port configurations. It will also disable validation<br>of DHCP packets for compliance with the snooping database information.<br><br>Key: boolean<br>
- `id` (filter, optional): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>
- `macs_invalid` (filter, optional): If `true`, indicates that MACs on this VLAN are invalid. This<br>might be set by any agent of the system that decides that MACs<br>are indeed invalid. Eventually those MACs will be cleared from<br>the system and macs_invalid will revert to `false`.<br><br>Key: boolean<br>
- `mgmd_igmp_version` (filter, optional): The IGMP protocol version to use. When IGMP snooping is disabled<br>this field would be empty.<br><br>Minimum Value: 2<br>Maximum Value: 3<br>
- `mgmd_mld_version` (filter, optional): The MLD protocol version to use. When IGMP snooping is disabled,<br>this field would be empty.<br><br>Minimum Value: 1<br>Maximum Value: 2<br>
- `name` (filter, optional): User configurable VLAN name.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `oper_state` (filter, optional): Operational state of this VLAN.<br><br>
- `oper_state_reason` (filter, optional): Human readable reason for the operational state of this VLAN.<br>error: Operational state is down due to an unknown reason.<br>ok: Operational state is up for the VLAN.<br>admin_down: VLAN is administratively down.<br>no_member_port: No port is member of the VLAN.<br>no_member_forwarding: No port is forwarding.<br><br>
- `policy_in_cfg_version` (filter, optional): The version of the 'policy_in_cfg' column. This value is changed to a<br>random value each time any management interface modifies the<br>'policy_in_cfg' value. An empty value means no ingress Policy has been<br>configured for the VLAN. Ignored if configured on VLANs with type = 'internal'.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `type` (filter, optional): The value indicates whether the VLAN was statically configured<br>internal VLAN default VLAN or was learned dynamically via a<br>protocol like MVRP.<br><br>
- `voice` (filter, optional): Marks VLAN as voice VLAN.<br><br>Key: boolean<br>


---
### `POST /system/vlans`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/vlans/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vlans/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vlans/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vlans/{pid}/macs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `denied` (filter, optional): if `true`, indicates that the packets from or destined to this MAC address<br>needs to be dropped.<br><br>Key: boolean<br>
- `derived_entry_src` (filter, optional): Indicates whether this MAC entry is derived from a certain 'original' <br>MAC address and the source that triggered creating this derived entry.<br>`none`         - Original entry (not derived).<br>`pvlan`        - Replicated entry by Private VLAN.<br><br>
- `from` (filter, optional): Source of the MAC address:<br>`dynamic`:  learnt by the data path<br>`VSX`:      synchronized from the VSX peer<br>`static`:   configured statically by the user<br>`VRRP`:     added by VRRP protocol<br>`port-access-security`: added by Port Access Security.<br>`evpn`:     added by EVPN.<br>`hsc`:      added by a remote controller(e.g. NSX).<br><br>
- `gbp_role_id` (filter, optional): GBP role-id associated with this MAC entry.<br>Non GBP clients use 0 as their role-id.<br><br>Minimum Value: 0<br>Maximum Value: 8191<br>
- `inactivity_timeout` (filter, optional): Specifies the time in seconds after which the MAC entry has to be aged out<br>for lack of activity.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `mac_addr` (filter, optional): MAC address in a AA:BB:CC:DD:EE:FF form.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `never_ageout` (filter, optional): if `true`, indicates that MAC should never be aged out regardless of<br>inactivity_timeout.<br><br>Key: boolean<br>
- `selected` (filter, optional): If `true`, indicates that the MAC entry is selected for programming into the<br>ASIC. If `false`, indicates that the MAC entry is not selected.<br><br>Key: boolean<br>


---
### `GET /system/vlans/{pid}/macs/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `id1` (path, required): Source of the MAC address:<br>`dynamic`:  learnt by the data path<br>`VSX`:      synchronized from the VSX peer<br>`static`:   configured statically by the user<br>`VRRP`:     added by VRRP protocol<br>`port-access-security`: added by Port Access Security.<br>`evpn`:     added by EVPN.<br>`hsc`:      added by a remote controller(e.g. NSX).<br><br>Reference Resource: [MAC](#!/MAC)
- `id2` (path, required): MAC address in a AA:BB:CC:DD:EE:FF form.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [MAC](#!/MAC)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vlans/{pid}/mgmd_vgs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `filter_type` (filter, optional): 'filter':          Group or group, source will be filtered based<br>                   on multicast group membership.<br>'filter_additive': Includes the list of user configured forward<br>                   ports, IGMP querier detected ports and PIM<br>                   router detected ports in the VLAN.<br>                   Multicast data packets are always forwarded.<br>'flood':           Group or group, source will be flooded in the<br>                   VLAN.<br>'filter_isl':      Unknown multicast data packets will be forwarded<br>                   to port if ISL port is configured.<br><br>
- `group_ip` (filter, optional): Multicast group IP address.<br><br>Maximum Length: 49<br>
- `last_reporter` (filter, optional): Host which last reported the Group.<br><br>Maximum Length: 49<br>
- `mgmd_type` (filter, optional): Type represents whether the entry is for IGMP or MLD.<br><br>
- `source_count` (filter, optional): Count of sources included or excluded for the Group.  An empty entry indicates a<br>source count of 0.<br><br>Key: integer<br>
- `source_ip` (filter, optional): Source address from which multicast group traffic is requested to be included or<br>excluded.<br><br>Maximum Length: 49<br>
- `state` (filter, optional): State of the VLAN,Group entry. The field MUST always be filled when an MGMD<br>VLAN, group entry is created. For VLAN, group, source entries, static group<br>entries, drop unknown entry, this field is not applicable and should be left<br>empty.<br><br>
- `version_status` (filter, optional): MGMD version status for the VLAN, group. The field MUST always be filled when an<br>MGMD VLAN, group entry is created. For VLAN, group, source entries, static group<br>entries, drop unknown entry, this field is not applicable and should be left<br>empty.<br><br>Minimum Value: 1<br>Maximum Value: 3<br>


---
### `GET /system/vlans/{pid}/mgmd_vgs/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `id1` (path, required): Type represents whether the entry is for IGMP or MLD.<br><br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `id2` (path, required): Multicast group IP address.<br><br>Maximum Length: 49<br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `id3` (path, required): Source address from which multicast group traffic is requested to be included or<br>excluded.<br><br>Maximum Length: 49<br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `id4` (path, required): 'filter':          Group or group, source will be filtered based<br>                   on multicast group membership.<br>'filter_additive': Includes the list of user configured forward<br>                   ports, IGMP querier detected ports and PIM<br>                   router detected ports in the VLAN.<br>                   Multicast data packets are always forwarded.<br>'flood':           Group or group, source will be flooded in the<br>                   VLAN.<br>'filter_isl':      Unknown multicast data packets will be forwarded<br>                   to port if ISL port is configured.<br><br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vlans/{pid}/mgmd_vgs/{ppid1}/{ppid2}/{ppid3}/{ppid4}/mgmd_vgps`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `ppid1` (path, required): Type represents whether the entry is for IGMP or MLD.<br><br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `ppid2` (path, required): Multicast group IP address.<br><br>Maximum Length: 49<br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `ppid3` (path, required): Source address from which multicast group traffic is requested to be included or<br>excluded.<br><br>Maximum Length: 49<br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `ppid4` (path, required): 'filter':          Group or group, source will be filtered based<br>                   on multicast group membership.<br>'filter_additive': Includes the list of user configured forward<br>                   ports, IGMP querier detected ports and PIM<br>                   router detected ports in the VLAN.<br>                   Multicast data packets are always forwarded.<br>'flood':           Group or group, source will be flooded in the<br>                   VLAN.<br>'filter_isl':      Unknown multicast data packets will be forwarded<br>                   to port if ISL port is configured.<br><br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `excluded_source_count` (filter, optional): Count of sources requested to be excluded for the group on the port on the VLAN<br>(VGP). Only applicable when source is 0.0.0.0/0::0.  An empty entry indicates a<br>count of 0. The field is not applicable for VLAN, group, port, source (VGPS)<br>entries.<br><br>Key: integer<br>
- `requested_source_count` (filter, optional): Count of sources requested to be included for the group on the port on the VLAN<br>(VGP). Only applicable when source is 0.0.0.0/0::0.  An empty entry indicates a<br>count of 0. The field is not applicable for VLAN, group, port, source (VGPS)<br>entries.<br><br>Key: integer<br>
- `state` (filter, optional): 'include':   Group, port or group, port, source in INCLUDE mode.<br>'exclude':   Group, port or group, port, source in EXCLUDE mode.<br>'v1_member': Group, port in v1 compatibility mode.<br>'v2_member': Group, port in v2 compatibility mode.<br><br>
- `version` (filter, optional): MGMD version for the VLAN, group, port or VLAN, group, port, source. The field is<br>only applicable for a VLAN, group, port entry. For VLAN, group, port, source<br>entries, this field is not applicable and should be left empty.<br><br>Minimum Value: 1<br>Maximum Value: 3<br>


---
### `GET /system/vlans/{pid}/mgmd_vgs/{ppid1}/{ppid2}/{ppid3}/{ppid4}/mgmd_vgps/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `ppid1` (path, required): Type represents whether the entry is for IGMP or MLD.<br><br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `ppid2` (path, required): Multicast group IP address.<br><br>Maximum Length: 49<br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `ppid3` (path, required): Source address from which multicast group traffic is requested to be included or<br>excluded.<br><br>Maximum Length: 49<br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `ppid4` (path, required): 'filter':          Group or group, source will be filtered based<br>                   on multicast group membership.<br>'filter_additive': Includes the list of user configured forward<br>                   ports, IGMP querier detected ports and PIM<br>                   router detected ports in the VLAN.<br>                   Multicast data packets are always forwarded.<br>'flood':           Group or group, source will be flooded in the<br>                   VLAN.<br>'filter_isl':      Unknown multicast data packets will be forwarded<br>                   to port if ISL port is configured.<br><br>Reference Resource: [MGMD_VGS](#!/MGMD95VGS)
- `id` (path, required): MGMD_VGPS port<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vlans/{pid}/static_macs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `mac_addr` (filter, optional): MAC address in XX:XX:XX:XX:XX:XX format.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `POST /system/vlans/{pid}/static_macs`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `data` (body, required): data


---
### `DELETE /system/vlans/{pid}/static_macs/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `id` (path, required): MAC address in XX:XX:XX:XX:XX:XX format.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [Static_MAC](#!/Static95MAC)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vlans/{pid}/static_macs/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `id` (path, required): MAC address in XX:XX:XX:XX:XX:XX format.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [Static_MAC](#!/Static95MAC)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vlans/{pid}/static_macs/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): The ID of this VLAN. Non-internal VLANs must have an 'id' between<br>1 and  4094 to be effectively instantiated.<br><br>Minimum Value: 1<br>Maximum Value: 32767<br>Reference Resource: [VLAN](#!/VLAN)
- `id` (path, required): MAC address in XX:XX:XX:XX:XX:XX format.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>Reference Resource: [Static_MAC](#!/Static95MAC)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `aclv4_control_plane_cfg_version` (filter, optional): The version of the 'aclv4_control_plane_cfg' column. This value<br>should be changed to a random value each time any management<br>interface modifies the 'aclv4_control_plane_cfg' value. An empty<br>value means no IPv4 control plane ACL has been configured for the<br>VRF.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `aclv6_control_plane_cfg_version` (filter, optional): The version of the 'aclv6_control_plane_cfg' column. This value<br>should be changed to a random value each time any management<br>interface modifies the 'aclv6_control_plane_cfg' value. An empty<br>value means no IPv6 control plane ACL has been configured for the<br>VRF.<br><br>Minimum Value: -9007199254740991<br>Maximum Value: 9007199254740991<br>
- `active_router_id` (filter, optional): Router-ID (in IPv4 format) that is currently used in the system, unless<br>overridden by protocol specific one.<br><br>Maximum Length: 45<br>
- `dns_domain_name` (filter, optional): Domain name used for name resolution by the DNS client, if `dns_domain_list` is<br>not configured. If both the configurations are not present, name resolution is<br>performed with empty domain suffix.<br><br>Maximum Length: 256<br>
- `name` (filter, optional): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>
- `rd` (filter, optional): Route distinguisher in ASN:nn format or IP:nn format.<br><br>Maximum Length: 22<br>
- `snmp_enable` (filter, optional): Enable SNMP server.<br><br>Key: boolean<br>
- `snmp_status` (filter, optional): This represents SNMP operational status on a VRF.<br><br>up - indicates that SNMP is operating on this VRF.<br>down - indicates that SNMP is not operating on this VRF.<br><br>
- `ssh_enable` (filter, optional): If the value is `true`, then SSH server is enabled on this VRF.<br><br>Key: boolean<br>
- `table_id` (filter, optional): Kernel table_id assigned for routing table of this VRF.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `type` (filter, optional): The VRF type, one of:<br><br>+ __`user`__:  An ordinary VRF created by user<br>referred to as ``user VRFs'' since they are generally connected to<br>data ports.<br>+ __`default`__:  default VRF for all routed interfaces<br>+ __`management`__: A management VRF<br>that contains out of band management (mgmt) interface only.<br><br>


---
### `POST /system/vrfs`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `DELETE /system/vrfs/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `id` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `id` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/bfd_sessions`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bfd_min_rx_interval` (filter, optional): Minimum RX interval in ms configured for this particular BFD<br>session. If this field is left empty, the system will use the<br>port-specific (if any) or the global system value. If this<br>value is zero, the system does not want to receive any periodic<br>BFD Control packets.<br><br>Minimum Value: 0<br>Maximum Value: 3600000<br>
- `bfd_min_tx_interval` (filter, optional): Minimum TX interval in ms configured for this particular BFD<br>session. If this field is left empty, the system will use the<br>port-specific (if any) or the global system value. The value<br>zero is reserved.<br><br>Minimum Value: 0<br>Maximum Value: 3600000<br>
- `dst_ip` (filter, optional): Destination address of the session.<br><br>Maximum Length: 45<br>
- `dst_mac` (filter, optional): Set to an Ethernet address in the form xx:xx:xx:xx:xx:xx to set the MAC used as<br>destination for transmitted BFD packets.<br>The BFD session will not be operational until this field is populated.<br><br>Maximum Length: 17<br>
- `effective_min_rx_interval` (filter, optional): BFD session operational min_rx interval as determined after the session<br>negotiation with remote endpoint.<br>
- `effective_min_tx_interval` (filter, optional): BFD session operational min_tx interval as determined after the session<br>negotiation with remote endpoint.<br>
- `from` (filter, optional): Protocol that requested the session.<br><br>
- `from_instance_id` (filter, optional): Instance ID of the protocol that requested the session.<br><br>Minimum Value: 1<br>
- `inner_dst_mac` (filter, optional): Set to an Ethernet address in the form xx:xx:xx:xx:xx:xx to set the MAC used as<br>inner destination for transmitted BFD packets in VXLAN sessions.<br>The VXLAN originated BFD session will not be operational until this field is populated.<br><br>Maximum Length: 17<br>
- `ip_address_family` (filter, optional): IP Addresses' family.<br><br>
- `local_discriminator` (filter, optional): BFD session local discriminator value.<br>The BFD session will not be operational until this field is populated.<br>
- `operating_mode` (filter, optional): 'async':          Control packets only<br>'async_and_echo': Control and (optionally) echo packets<br>'async_vxlan':    Control packets within a VXLAN tunnel<br><br>
- `protocol_disabled` (filter, optional): The client protocol for this session has administratively disabled BFD.<br>If the BFD session is not shared, BFD will start sending packets with state<br>admin down for at least a detect multiplier time interval.<br><br>Key: boolean<br>
- `remote_discriminator` (filter, optional): BFD session endpoint's discriminator value.<br>
- `remote_min_echo_rx_interval` (filter, optional): BFD session remote operational echo min_rx interval as detected by the local endpoint.<br>
- `remote_min_rx_interval` (filter, optional): BFD session remote operational min_rx interval as detected by the local endpoint.<br>
- `remote_min_tx_interval` (filter, optional): BFD session remote operational min_tx interval as detected by the local endpoint.<br>
- `remote_multiplier` (filter, optional): BFD session remote operational multiplier as detected by the local endpoint.<br>
- `selected_src_ip` (filter, optional): Since BFD sessions can have multiple IPs on the source port, the<br>following selection algorithm is used:<br>* IPv4:<br> 1. Use the primary address if it matches the destination subnet.<br> 2. Use the secondary address if it matches the destination subnet.<br>* IPv6:<br> 1. Use the link-local address if the remote source IP is also a<br>    link-local<br> 2. Use an IP from the non local-link addresses based on the<br>    destination subnet.<br><br>Maximum Length: 45<br>
- `session_id` (filter, optional): BFD session identifier.<br>The BFD session will not be operational until this field is populated.<br>
- `src_ip` (filter, optional): Source address for transmitted BFD control packets.<br>If not present, the address from the src_port is used.<br><br>Maximum Length: 45<br>


---
### `GET /system/vrfs/{pid}/bfd_sessions/{id1}/{id2}/{id3}/{id4}/{id5}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): Protocol that requested the session.<br><br>Reference Resource: [BFD_Session](#!/BFD95Session)
- `id2` (path, required): Instance ID of the protocol that requested the session.<br><br>Minimum Value: 1<br>Reference Resource: [BFD_Session](#!/BFD95Session)
- `id3` (path, required): 'async':          Control packets only<br>'async_and_echo': Control and (optionally) echo packets<br>'async_vxlan':    Control packets within a VXLAN tunnel<br><br>Reference Resource: [BFD_Session](#!/BFD95Session)
- `id4` (path, required): Destination address of the session.<br><br>Maximum Length: 45<br>Reference Resource: [BFD_Session](#!/BFD95Session)
- `id5` (path, required): The source of the BFD session.<br>Might be empty for multi-hop sessions.<br>The BFD session will not be operational until this field is populated.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [BFD_Session](#!/BFD95Session)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/bgp_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `always_compare_med` (filter, optional): Specifies whether MED should be compared from different neighbors.<br><br>Key: boolean<br>
- `asnotation` (filter, optional): Specifies the representation of Four-Octet AS Numbers in show commands.<br>'dotted':       All the ASNs greater than 65535 should be displayed in AA.NN format.<br>'dotted-plus':  All the ASNs irrespective of value should be displayed in AA.NN format.<br>'plain-text':   All the ASNs should be displayed in plain-text format.<br><br>
- `bestpath_as_path_ignore` (filter, optional): Specifies whether the AS path length should be ignored<br>when determining the preferred route.<br><br>Key: boolean<br>
- `bestpath_as_path_multipath_relax` (filter, optional): Specifies whether to consider two or more BGP routes as ecmp routes <br>when routes AS PATH length is same but AS PATHs are different.<br><br>Key: boolean<br>
- `bestpath_compare_routerid` (filter, optional): Specifies whether the BGP router IDs should be compared to select the best path.<br><br>Key: boolean<br>
- `bestpath_med_confed` (filter, optional): Specifies whether the router should consider the MED value when choosing a path<br>from among those advertised by different ASes within a confederation. <br>All active BGP sessions belonging to this VRF will be restarted when this<br>configuration is changed for it to take effect.<br><br>Key: boolean<br>
- `bestpath_med_missing_as_worst` (filter, optional): Specifies whether the missing MED value should be treated as 0xFFFFFFFF.<br><br>Key: boolean<br>
- `cluster_id` (filter, optional): Cluster ID of this router.<br>Cluster-id can be a 32-bit integer in a range of 1-4294967295<br>or a valid IPv4 address.<br>If no cluster-id is configured, router-id will be used.<br><br>Maximum Length: 15<br>
- `confederation_id` (filter, optional): Confederation identifier assigned to this router.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `deterministic_med` (filter, optional): Specifies whether BGP should select the best-MED path among paths<br>advertised from the neighboring AS.<br><br>Key: boolean<br>
- `ebgp_distance` (filter, optional): Administrative distance for ebgp routes.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `fast_external_fallover` (filter, optional): Enables fast fall-over for directly connected EBGP sessions.<br><br>Key: boolean<br>
- `gr_enable` (filter, optional): Specifies whether the graceful restart procedures should be<br>performed in the event of peer or router failure.<br><br>Key: boolean<br>
- `gr_restart_timer` (filter, optional): Maximum time in seconds to wait for graceful restart capable peer<br>to come back up.<br><br>Minimum Value: 1<br>Maximum Value: 3600<br>
- `gr_stale_timer` (filter, optional): Maximum time in seconds to hold onto restarting peer stale paths.<br><br>Minimum Value: 1<br>Maximum Value: 3600<br>
- `ibgp_distance` (filter, optional): Administrative distance for ibgp routes.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `local_pref` (filter, optional): Local preference of the routes.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `log_neighbor_changes` (filter, optional): Enables logging of neighbor status changes.<br><br>Key: boolean<br>
- `maxas_limit` (filter, optional): Limit on the maximum AS numbers allowed in the routes<br>learned from the peers.<br><br>Minimum Value: 1<br>Maximum Value: 32<br>
- `maximum_paths` (filter, optional): Number of paths BGP may install into the routing table.<br><br>Minimum Value: 1<br>Maximum Value: 8<br>
- `protocol_disable` (filter, optional): Disable this BGP instance.<br><br>Key: boolean<br>
- `router_id` (filter, optional): Router ID for the given ASN.<br><br>Maximum Length: 15<br>
- `trap_enable` (filter, optional): Enable SNMP trap generation for BGP related events.<br><br>Key: boolean<br>


---
### `POST /system/vrfs/{pid}/bgp_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/bgp_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): BGP_Router asn<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/bgp_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): BGP_Router asn<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/bgp_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): BGP_Router asn<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/bgp_routers/{ppid}/aggregate_addresses`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `options` (filter, optional): `summary-only`:    Only summary routes will be advertised<br>                   More specific routes that make the aggregate will not be advertised<br>`as-set`:          Maintains the longest AS-Sequence, common to the aggregated routes<br>`summary-as-set`:  A combination of summary and as-set options<br>`none`:            No options. Aggregate routes are advertised<br><br>


---
### `POST /system/vrfs/{pid}/bgp_routers/{ppid}/aggregate_addresses`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/bgp_routers/{ppid}/aggregate_addresses/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `id1` (path, required): Aggregate_address address-family<br>
- `id2` (path, required): Aggregate_address ip_prefix<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/bgp_routers/{ppid}/aggregate_addresses/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `id1` (path, required): Aggregate_address address-family<br>
- `id2` (path, required): Aggregate_address ip_prefix<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/bgp_routers/{ppid}/aggregate_addresses/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `id1` (path, required): Aggregate_address address-family<br>
- `id2` (path, required): Aggregate_address ip_prefix<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/bgp_routers/{ppid}/bgp_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bfd_enable` (filter, optional): Enables BFD session to the specific neighbor.<br><br>Key: boolean<br>
- `description` (filter, optional): Free form description of the neighbor.<br><br>Maximum Length: 80<br>
- `ebgp_hop_count` (filter, optional): Maximum Hop Count for the EBGP Session.<br>If 'ttl_security_hops' is configured, then 'ebgp_hop_count' is ignored.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `fall_over` (filter, optional): Fall-over the BGP session when route to this peer fails.<br><br>Key: boolean<br>
- `gshut_status` (filter, optional): State in which the graceful shutdown process is in.<br>'initiated': graceful shutdown has been started for the neighbor.<br>'completed': graceful shutdown has been completed for the neighbor.<br>Empty if graceful shutdown had never been initiated or<br>if the new connection is established.<br><br>
- `is_peer_group` (filter, optional): Identifies specific BGP neighbor or BGP peer group<br>'true':    Entry is part of a peer-group and holds common<br>           configuration<br>'false':   Entry is a neighbor<br><br>Key: boolean<br>
- `last_shutdown_time` (filter, optional): The time (in seconds from epoch), when the connection was<br>last shut down since the last boot.<br><br>Key: integer<br>
- `local_as` (filter, optional): ASN to be used as a local ASN for this neighbor.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `local_as_mode` (filter, optional): 'no-prepend-replace-as-dual-as:<br>   The session can be established using either primary-as or alternate local-as.<br>   Selected-as is not prepended to the inbound AS_PATH list,<br>   but prepended to outbound AS_PATH list.<br>'no-prepend':<br>   The session is established via alternate local-as.<br>   Both the alternate-as and primary-as are not prepended to the inbound AS_PATH list,<br>   but prepended to the outbound AS_PATH list.<br>'none':<br>   The session is established via alternate local-as.<br>   Both the alternate-as and primary-as are prepended<br>   to both the inbound and the outbound AS_PATH list.<br><br>
- `negotiated_holdtime` (filter, optional): Negotiated hold time in seconds.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `negotiated_keepalive` (filter, optional): Negotiated keepalive interval in seconds.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `passive` (filter, optional): Identifies if 'open' messages should be sent to a neighbor<br>'true':    Do not send 'open' messages<br>'false':   Do send 'open' messages<br><br>Key: boolean<br>
- `password` (filter, optional): Password to be used with the neighbor.<br><br>Maximum Length: 90<br>
- `peer_rtrid` (filter, optional): The BGP Identifier of the peer.<br>Empty, unless bgpPeerStatusState is either 'openconfirm' or 'established'.<br><br>Maximum Length: 80<br>
- `remote_as` (filter, optional): Peer ASN.<br>EBGP: must be different from the local ASN or BGP router ASN.<br>IBGP: must be identical to either the local ASN or BGP router ASN.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `remove_private_as` (filter, optional): Specifies whether private AS should be removed.<br><br>Key: boolean<br>
- `sel_local_port` (filter, optional): Local port used by the transport connection.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `sel_remote_port` (filter, optional): Remote port used by the transport connection.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `shutdown` (filter, optional): Shuts down neighbor session without removing configuration<br><br>Key: boolean<br>
- `tcp_port_number` (filter, optional): Local TCP port to be used for the BGP session.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `ttl_security_hops` (filter, optional): Maximum allowed hops to a neighbor. This, when configured,<br>takes precedence over 'ebgp_hop_count'.<br><br>Minimum Value: 1<br>Maximum Value: 254<br>
- `update_source` (filter, optional): Source IP address for the neighbor session.<br><br>Maximum Length: 80<br>
- `vsx_sync_exclude` (filter, optional): <br>
- `weight` (filter, optional): This is the weight for routes from this neighbor.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `POST /system/vrfs/{pid}/bgp_routers/{ppid}/bgp_neighbors`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/bgp_routers/{ppid}/bgp_neighbors/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `id` (path, required): BGP_Neighbor asn<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/bgp_routers/{ppid}/bgp_neighbors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `id` (path, required): BGP_Neighbor asn<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/bgp_routers/{ppid}/bgp_neighbors/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): BGP_Router asn<br>
- `id` (path, required): BGP_Neighbor asn<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/bgp_routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family. Default value is `ipv4`.<br><br>
- `aggregate` (filter, optional): Specifies whether the notification is sent to upstream routers<br>that the route is aggregated.<br>Default is false.<br><br>Key: boolean<br>
- `aggregator` (filter, optional): IP address of the BGP node responsible for route aggregation.<br>Empty if route is not aggregated.<br><br>Maximum Length: 30<br>
- `aggregator_as` (filter, optional): Originating AS number of the aggregate route. Default value is 0.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `community` (filter, optional): Space delimited list of community names for the route.<br><br>Maximum Length: 80<br>
- `creation_time` (filter, optional): Epoch time of the route arrival from the neighbor.<br><br>Minimum Value: 0<br>
- `distance` (filter, optional): Administrative distance. Default value is 0.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `ecommunity` (filter, optional): Space delimited list of extended community names for the route.<br><br>Maximum Length: 704<br>
- `metric` (filter, optional): BGP Multi Exit Discriminator (MED) attribute.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `nexthop` (filter, optional): IP address of the nexthop device.<br>If the next-hop address is link-local IPv6, nexthop will be output interface name.<br>Empty if the route is self-originated.<br><br>Maximum Length: 45<br>
- `nexthop_link_local` (filter, optional): IPv6 link local address of the nexthop device.<br><br>Minimum Length: 3<br>Maximum Length: 45<br>
- `path_id` (filter, optional): Path ID associated with this prefix. If the peer does not send a<br>path ID, the path ID will be set to 0.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `peer` (filter, optional): <br>Maximum Length: 45<br>
- `prefix` (filter, optional): IPv4, IPv6 or EVPN destination prefix.<br>Examples: IPv4 Prefix - 192.168.0.0/16<br>          IPv6 Prefix - 2002::2/64<br>          EVPN Type 2 Prefix - 100:1-[2]:[0]:[0]:[48]:[0006.f63f.e3c1]:[32]:[172.16.30.33]<br>          EVPN Type 3 Prefix - 2.2.2.2:10-[3]:[0]:[32]:[10.1.1.1]<br>          EVPN Type 5 prefix - 100:1-[5]:[0]:[0]:[24]:[10.10.10.0]<br><br>Maximum Length: 128<br>
- `prefix_accepted` (filter, optional): Specifies whether the received prefix (or routes) was accepted.<br><br>Key: boolean<br>
- `prefix_advertised` (filter, optional): Specifies whether the prefix (or route) is advertised to neighbors.<br><br>Key: boolean<br>
- `prefix_match_type` (filter, optional): 'exact':         Route is an exact match with the specified mask<br>'longer-prefix': Route is a more-specific match compared to the specified mask.<br><br>
- `prefix_rejected` (filter, optional): Specifies whether the received prefix (or routes) was rejected.<br><br>Key: boolean<br>
- `protocol_iBGP` (filter, optional): Specifies whether the route was learned through iBGP session.<br>'true':    Route originated via iBGP session<br>'false':   Route did not originate via iBGP session, default value<br><br>Key: boolean<br>
- `protocol_internal` (filter, optional): Specifies whether the route originated locally on the BGP peer<br>'true':    Route originated locally<br>'false':   Route did not originate locally, default value<br><br>Key: boolean<br>
- `sub_address_family` (filter, optional): Subsequent address family. Default is `unicast`.<br><br>
- `vni` (filter, optional): Specifies Virtual Network Identifier.<br>This is specific to EVPN routes and will be -1 for all non-EVPN routes.<br><br>Minimum Value: -1<br>Maximum Value: 16777215<br>
- `vni_type` (filter, optional): Specifies Virtual Network Identifier type.<br><br>


---
### `GET /system/vrfs/{pid}/bgp_routes/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPv4, IPv6 or EVPN destination prefix.<br>Examples: IPv4 Prefix - 192.168.0.0/16<br>          IPv6 Prefix - 2002::2/64<br>          EVPN Type 2 Prefix - 100:1-[2]:[0]:[0]:[48]:[0006.f63f.e3c1]:[32]:[172.16.30.33]<br>          EVPN Type 3 Prefix - 2.2.2.2:10-[3]:[0]:[32]:[10.1.1.1]<br>          EVPN Type 5 prefix - 100:1-[5]:[0]:[0]:[24]:[10.10.10.0]<br><br>Maximum Length: 128<br>Reference Resource: [BGP_Route](#!/BGP95Route)
- `id2` (path, required): <br>Maximum Length: 45<br>Reference Resource: [BGP_Route](#!/BGP95Route)
- `id3` (path, required): Specifies Virtual Network Identifier.<br>This is specific to EVPN routes and will be -1 for all non-EVPN routes.<br><br>Minimum Value: -1<br>Maximum Value: 16777215<br>Reference Resource: [BGP_Route](#!/BGP95Route)
- `id4` (path, required): Path ID associated with this prefix. If the peer does not send a<br>path ID, the path ID will be set to 0.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>Reference Resource: [BGP_Route](#!/BGP95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/dhcp_leases`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the lease entry.<br><br>
- `client_hostname` (filter, optional): Specifies the hostname of the DHCP client to which IP address is assigned by the<br>DHCP server.<br><br>Key: string<br>
- `client_id` (filter, optional): Specifies the client id of the DHCP client to which IP address is assigned by<br>the DHCP server.<br><br>Key: string<br>
- `expiry_time` (filter, optional): Time (in seconds from Epoch) when lease will expire.<br>
- `ip_address` (filter, optional): Specifies the IPv4/IPv6 address that got assigned to the DHCP client. Example<br>IPv4 address: 192.168.10.27.<br><br>Maximum Length: 45<br>
- `link_address` (filter, optional): In case of IPv4 leases, specifies the Ethernet MAC address of the DHCP client to<br>which IP address is assigned by the DHCP server. Example: e6:8c:98:bb:b4:de. In<br>case of IPv6 leases, specifies the DHCP Unique Identifier (DUID) used by the<br>DHCP client to get an IP address from a DHCPv6 server. Example:<br>00:01:00:01:1e:99:8b:b6:00:00:02:b5:78:f4<br><br>Minimum Length: 17<br>Maximum Length: 59<br>


---
### `GET /system/vrfs/{pid}/dhcp_leases/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): Specifies the IPv4/IPv6 address that got assigned to the DHCP client. Example<br>IPv4 address: 192.168.10.27.<br><br>Maximum Length: 45<br>Reference Resource: [DHCP_Lease](#!/DHCP95Lease)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `DELETE /system/vrfs/{pid}/dhcp_server`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcp_server`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcp_server`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `lease_duration` (filter, optional): Lease expiry time in the format DD:HH:MM.<br>The minimum lease time is two minutes and '00:00:00'<br>represents an infinite lease.<br><br>Minimum Length: 8<br>Maximum Length: 8<br>


---
### `POST /system/vrfs/{pid}/dhcp_server/dhcp_server_pools`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): DHCP_Server_Pool <br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): DHCP_Server_Pool <br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): DHCP_Server_Pool <br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_options`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `option_number` (filter, optional): Number of the extra option that should be sent to the DHCPv4 clients.<br>
- `option_value` (filter, optional): Value of the extra option that should be sent to the DHCPv4 clients.<br><br>Maximum Length: 255<br>
- `option_value_type` (filter, optional): Type of the option value that is sent to the DHCPv4 clients:<br>`ascii`: indicates that the option value provided is an ascii string.<br>`ip`: indicates that the option value provided is an IP address.<br>`hex`: indicates that the option value provided is a hex string.<br><br>


---
### `POST /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_options`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_options/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): DHCP_Server_Option pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_options/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): DHCP_Server_Option pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_options/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): DHCP_Server_Option pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_ranges`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `end_ip_address` (filter, optional): End IPv4 address of the dynamic IP address range.<br><br>Maximum Length: 15<br>
- `prefix_len` (filter, optional): Prefix length that would be used for the assigned IPv4<br>addresses in this range and this would be sent to DHCPv4 clients.<br>If not specified, then prefix length of the switch interface that<br>received the DHCP request would be used.<br><br>Minimum Value: 1<br>Maximum Value: 31<br>
- `start_ip_address` (filter, optional): Start IPv4 address of the dynamic IP address range.<br><br>Maximum Length: 15<br>


---
### `POST /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_ranges`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_ranges/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): DHCP_Server_Range pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_ranges/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): DHCP_Server_Range pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_ranges/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): DHCP_Server_Range pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_static_hosts`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `client_hostname` (filter, optional): Hostname that should be assigned to the specified host.<br>This overrides any hostname configured on the DHCP client machine.<br><br>Maximum Length: 63<br>
- `ip_address` (filter, optional): Static IPv4 address that should be assigned to the specific host.<br>The specified IPv4 address is not constrained to be in the configured IPv4<br>range, but it must be in the same subnet as valid configured IPv4 range.<br><br>Maximum Length: 15<br>
- `mac_address` (filter, optional): MAC address of the DHCP host in a AA:BB:CC:DD:EE:FF form<br>to which the static IP address would be assigned.<br>If same MAC address is configured with multiple IPv4 addresses<br>then none of the static address mappings will be applied.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>
- `state` (filter, optional): Completion status of static host IPv4 address mapping:<br><br>`OPERATIONAL`: static host mapping is fully operational.<br>`CONFLICTING`: disabled due to multiple addresses assigned to the same mac address.<br><br>


---
### `POST /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_static_hosts`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_static_hosts/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): Static IPv4 address that should be assigned to the specific host.<br>The specified IPv4 address is not constrained to be in the configured IPv4<br>range, but it must be in the same subnet as valid configured IPv4 range.<br><br>Maximum Length: 15<br>Reference Resource: [DHCP_Server_Static_Host](#!/DHCP95Server95Static95Host)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_static_hosts/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): Static IPv4 address that should be assigned to the specific host.<br>The specified IPv4 address is not constrained to be in the configured IPv4<br>range, but it must be in the same subnet as valid configured IPv4 range.<br><br>Maximum Length: 15<br>Reference Resource: [DHCP_Server_Static_Host](#!/DHCP95Server95Static95Host)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcp_server/dhcp_server_pools/{pppid}/dhcp_server_static_hosts/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCP_Server_Pool pool_name<br>
- `id` (path, required): Static IPv4 address that should be assigned to the specific host.<br>The specified IPv4 address is not constrained to be in the configured IPv4<br>range, but it must be in the same subnet as valid configured IPv4 range.<br><br>Maximum Length: 15<br>Reference Resource: [DHCP_Server_Static_Host](#!/DHCP95Server95Static95Host)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcpv6_server`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcpv6_server`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcpv6_server`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `lease_duration` (filter, optional): Lease expiry time in the format DD:HH:MM.<br>The minimum lease time is two minutes and '00:00:00'<br>represents an infinite lease.<br><br>Minimum Length: 8<br>Maximum Length: 8<br>


---
### `POST /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): DHCPV6_Server_Pool <br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): DHCPV6_Server_Pool <br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): DHCPV6_Server_Pool <br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_options`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `option_number` (filter, optional): Number of the extra option that should be sent to the DHCPv6 clients.<br>
- `option_value` (filter, optional): Value of the extra option that should be sent to the DHCPv6 clients.<br><br>Maximum Length: 255<br>
- `option_value_type` (filter, optional): Type of the option value that is sent to the DHCPv6 clients:<br>`ascii`: indicates that the option value provided is an ascii string.<br>`ipv6`: indicates that the option value provided is an IPv6 address.<br>`hex`: indicates that the option value provided is a hex string.<br><br>


---
### `POST /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_options`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_options/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): DHCPV6_Server_Option pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_options/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): DHCPV6_Server_Option pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_options/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): DHCPV6_Server_Option pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_ranges`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `end_ipv6_address` (filter, optional): End IPv6 address of the dynamic IP address range.<br><br>Maximum Length: 45<br>
- `prefix_len` (filter, optional): Prefix length that would be used for the assigned<br>IPv6 addresses. Configured prefix length must be equal to or<br>larger than the prefix length on the local interface. If not <br>specifed, default value of 64 would be used.<br><br>Minimum Value: 64<br>Maximum Value: 128<br>
- `start_ipv6_address` (filter, optional): Start IPv6 address of the dynamic IP address range.<br><br>Maximum Length: 45<br>


---
### `POST /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_ranges`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_ranges/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): DHCPV6_Server_Range pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_ranges/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): DHCPV6_Server_Range pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_ranges/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): DHCPV6_Server_Range pool_name<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_static_hosts`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `client_hostname` (filter, optional): Hostname that should be assigned to the specified host.<br>This overrides any hostname configured on the DHCP client machine.<br><br>Maximum Length: 63<br>
- `client_id` (filter, optional): Client id or DUID of the DHCPv6 client to which the configured<br>static IPv6 address would be assigned. If same client id is<br>configured with multiple IPv6 addresses then none of the static<br>address mappings will be applied.<br><br>Minimum Length: 2<br>
- `ipv6_address` (filter, optional): Static IPv6 address that should be assigned to the specific host.<br>The specified IPv6 address is not constrained to be in the configured IPv6<br>range, but it must be in the same subnet as valid configured IPv6 range.<br><br>Maximum Length: 45<br>
- `state` (filter, optional): Completion status of static host IPv6 address mapping:<br><br>`OPERATIONAL`: static host mapping is fully operational.<br>`CONFLICTING`: disabled due to multiple addresses assigned to the same client id.<br><br>


---
### `POST /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_static_hosts`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_static_hosts/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): Static IPv6 address that should be assigned to the specific host.<br>The specified IPv6 address is not constrained to be in the configured IPv6<br>range, but it must be in the same subnet as valid configured IPv6 range.<br><br>Maximum Length: 45<br>Reference Resource: [DHCPV6_Server_Static_Host](#!/DHCPV695Server95Static95Host)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_static_hosts/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): Static IPv6 address that should be assigned to the specific host.<br>The specified IPv6 address is not constrained to be in the configured IPv6<br>range, but it must be in the same subnet as valid configured IPv6 range.<br><br>Maximum Length: 45<br>Reference Resource: [DHCPV6_Server_Static_Host](#!/DHCPV695Server95Static95Host)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/dhcpv6_server/dhcpv6_server_pools/{pppid}/dhcpv6_server_static_hosts/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `pppid` (path, required): DHCPV6_Server_Pool pool_name<br>
- `id` (path, required): Static IPv6 address that should be assigned to the specific host.<br>The specified IPv6 address is not constrained to be in the configured IPv6<br>range, but it must be in the same subnet as valid configured IPv6 range.<br><br>Maximum Length: 45<br>Reference Resource: [DHCPV6_Server_Static_Host](#!/DHCPV695Server95Static95Host)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ipsec_sas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `SPI` (filter, optional): Security Parameters Index for the Security Association.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `address_family` (filter, optional): Address Family used in the Security Association.<br><br>
- `auth_key` (filter, optional): Authentication key to use in the SA.<br><br>Minimum Length: 1<br>
- `auth_type` (filter, optional): IPsec Authentication type.<br><br>
- `dest_ip` (filter, optional): IPv4 or IPv6 destination address.<br>Example: 192.168.0.0.<br><br>Maximum Length: 45<br>
- `direction` (filter, optional): Traffic direction for the Security Association.<br>'both' : This SA is applicable to both directions.<br><br>
- `encryption_key` (filter, optional): Encryption key to use in the SA.<br><br>Minimum Length: 1<br>
- `encryption_type` (filter, optional): Cipher to be used for encryption.<br><br>
- `from` (filter, optional): Originator of this Security Association.<br><br>
- `ipsec_protocol` (filter, optional): IPsec protocol to use in the Security Association.<br>Authentication Header (AH) | Encapsulating Security Payload (ESP).<br>'AH' : Provides authentication.<br>'ESP': Provides confidentiality and authentication.<br><br>
- `mode` (filter, optional): IPsec operation mode.<br>'tunnel'    : Entire IP packet is encapsulated into a new packet with a new IP header.<br>'transport' : IP header of the packet is not modified.<br><br>
- `src_ip` (filter, optional): IPv4 or IPv6 source address.<br>Example: 192.168.0.0.<br><br>Maximum Length: 45<br>


---
### `GET /system/vrfs/{pid}/ipsec_sas/{id1}/{id2}/{id3}/{id4}/{id5}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): Security Parameters Index for the Security Association.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>Reference Resource: [IPsec_SA](#!/IPsec95SA)
- `id2` (path, required): IPsec protocol to use in the Security Association.<br>Authentication Header (AH) | Encapsulating Security Payload (ESP).<br>'AH' : Provides authentication.<br>'ESP': Provides confidentiality and authentication.<br><br>Reference Resource: [IPsec_SA](#!/IPsec95SA)
- `id3` (path, required): Address Family used in the Security Association.<br><br>Reference Resource: [IPsec_SA](#!/IPsec95SA)
- `id4` (path, required): IPv4 or IPv6 destination address.<br>Example: 192.168.0.0.<br><br>Maximum Length: 45<br>Reference Resource: [IPsec_SA](#!/IPsec95SA)
- `id5` (path, required): Traffic direction for the Security Association.<br>'both' : This SA is applicable to both directions.<br><br>Reference Resource: [IPsec_SA](#!/IPsec95SA)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ipsec_sps`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ivrl_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the neighbor.<br><br>
- `ip_address` (filter, optional): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>
- `mac` (filter, optional): MAC address learned for this neighbor.<br><br>Key: string<br>
- `state` (filter, optional): Current state of the neighbor entry.<br><br>


---
### `GET /system/vrfs/{pid}/ivrl_neighbors/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>Reference Resource: [IVRL_Neighbor](#!/IVRL95Neighbor)
- `id2` (path, required): Logical port LAG/non-aggregated physical port/L3 VLAN interface etc. at which<br>MAC was learnt.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [IVRL_Neighbor](#!/IVRL95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `DELETE /system/vrfs/{pid}/msdp_router`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/msdp_router`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/msdp_router`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address` (filter, optional): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>
- `as_number` (filter, optional): AS number on which the peer is configured.<br>Local AS is assumed, if it is not specified.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `description` (filter, optional): Optional description of the MSDP Peer.<br><br>Maximum Length: 80<br>
- `enable` (filter, optional): Enables MSDP communication with the peer.<br><br>Key: boolean<br>
- `md5_password` (filter, optional): MD5 password for the peer.<br><br>Maximum Length: 90<br>
- `mesh_group_name` (filter, optional): Name of the mesh group, if the peer is configured as<br> a part of mesh group.<br><br>Maximum Length: 20<br>
- `sa_limit` (filter, optional): Maximum number of (S, G) entries that can be accepted <br>from the Peer.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this MSDP peer have been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for this MSDP<br>peer.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `POST /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `id` (path, required): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_Peer](#!/MSDP95Peer)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `id` (path, required): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_Peer](#!/MSDP95Peer)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `id` (path, required): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_Peer](#!/MSDP95Peer)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `id` (path, required): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_Peer](#!/MSDP95Peer)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers/{pppid}/msdp_sa_caches`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `pppid` (path, required): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_Peer](#!/MSDP95Peer)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `group_address` (filter, optional): The IPv4 Multicast Group Address learnt from the MSDP Peer.<br><br>Maximum Length: 15<br>
- `rp_address` (filter, optional): The IPv4 address of the RP where the Source has registered<br>for the Multicast Group.<br><br>Maximum Length: 15<br>
- `source_address` (filter, optional): The IPv4 Source Address learnt from the MSDP Peer.<br><br>Maximum Length: 15<br>


---
### `GET /system/vrfs/{pid}/msdp_router/{ppid}/msdp_peers/{pppid}/msdp_sa_caches/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): MSDP_Router <br>
- `pppid` (path, required): IPv4 address of the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_Peer](#!/MSDP95Peer)
- `id1` (path, required): The IPv4 Source Address learnt from the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_SA_Cache](#!/MSDP95SA95Cache)
- `id2` (path, required): The IPv4 Multicast Group Address learnt from the MSDP Peer.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_SA_Cache](#!/MSDP95SA95Cache)
- `id3` (path, required): The IPv4 address of the RP where the Source has registered<br>for the Multicast Group.<br><br>Maximum Length: 15<br>Reference Resource: [MSDP_SA_Cache](#!/MSDP95SA95Cache)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/multicast_l3_bridge_control_forwardings`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Represents the address family for this entry. Default value is `ipv4`.<br><br>
- `destination_prefix` (filter, optional): IPv4 or IPv6 destination prefix. Example 255.0.10.1/32<br><br>Maximum Length: 49<br>
- `source_prefix` (filter, optional): IPv4 or IPv6 source prefix. Example 192.168.0.1/32<br><br>Maximum Length: 49<br>


---
### `GET /system/vrfs/{pid}/multicast_l3_bridge_control_forwardings/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPv4 or IPv6 source prefix. Example 192.168.0.1/32<br><br>Maximum Length: 49<br>Reference Resource: [Multicast_L3_Bridge_Control_Forwarding](#!/Multicast95L395Bridge95Control95Forwarding)
- `id2` (path, required): IPv4 or IPv6 destination prefix. Example 255.0.10.1/32<br><br>Maximum Length: 49<br>Reference Resource: [Multicast_L3_Bridge_Control_Forwarding](#!/Multicast95L395Bridge95Control95Forwarding)
- `id3` (path, required): Reference to a [VLAN](#!/VLAN) on which a MGMD protocol detects multicast traffic<br>over specific interfaces.<br><br>Reference Resource: [VLAN](#!/VLAN)<br>Reference Resource: [Multicast_L3_Bridge_Control_Forwarding](#!/Multicast95L395Bridge95Control95Forwarding)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/multicast_l3_forwardings`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Represents the address family for this entry.<br><br>
- `destination_prefix` (filter, optional): IPv4 or IPv6 destination prefix. Example 255.0.10.1/32<br><br>Maximum Length: 49<br>
- `from` (filter, optional): Protocol that is responsible for this entry. Possible values are `pim_dm`,<br>`pim_sm` and `pim_bidi`.<br><br>
- `source_prefix` (filter, optional): IPv4 or IPv6 source prefix. Example 192.168.0.1/32<br><br>Maximum Length: 49<br>
- `type` (filter, optional): Represents the type of multicast L3 Forwarding entry. The types available are<br>`bridge` and `route`<br><br>


---
### `GET /system/vrfs/{pid}/multicast_l3_forwardings/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPv4 or IPv6 source prefix. Example 192.168.0.1/32<br><br>Maximum Length: 49<br>Reference Resource: [Multicast_L3_Forwarding](#!/Multicast95L395Forwarding)
- `id2` (path, required): IPv4 or IPv6 destination prefix. Example 255.0.10.1/32<br><br>Maximum Length: 49<br>Reference Resource: [Multicast_L3_Forwarding](#!/Multicast95L395Forwarding)
- `id3` (path, required): Reference to the Upstream Port (i.e. where multicast traffic is coming from).<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [Multicast_L3_Forwarding](#!/Multicast95L395Forwarding)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the neighbor.<br><br>
- `from` (filter, optional): 'dynamic': the neighbor was dynamically learnt.<br>'static' : the neighbor was statically configured.<br>'ivrl'   : the neighbor was added by inter VRF leaking.<br>'ipdb'   : the neighbor was added by ip directed broadcast.<br><br>
- `gbp_role_id` (filter, optional): GBP role-id associated with neighbor entry.<br>Non GBP clients use 0 as their role-id.<br><br>Minimum Value: 0<br>Maximum Value: 8191<br>
- `in_use_by_routes` (filter, optional): When set to `true`, indicates this IP is used as a nexthop by one or more route entries. <br><br>Key: boolean<br>
- `ip_address` (filter, optional): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>
- `last_updated` (filter, optional): Time of the last update in seconds from epoch.<br>
- `mac` (filter, optional): MAC address learned for this neighbor.<br><br>Key: string<br>
- `state` (filter, optional): Current state of the neighbor entry.<br><br>


---
### `GET /system/vrfs/{pid}/neighbors/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>Reference Resource: [Neighbor](#!/Neighbor)
- `id2` (path, required): Logical port LAG/non-aggregated physical port/L3 VLAN interface etc. at which MAC was learnt.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [Neighbor](#!/Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ntp_associations`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address` (filter, optional): FQDN or ip address for the association.<br><br>Maximum Length: 256<br>


---
### `POST /system/vrfs/{pid}/ntp_associations`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ntp_associations/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): FQDN or ip address for the association.<br><br>Maximum Length: 256<br>Reference Resource: [NTP_Association](#!/NTP95Association)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ntp_associations/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): FQDN or ip address for the association.<br><br>Maximum Length: 256<br>Reference Resource: [NTP_Association](#!/NTP95Association)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/ntp_associations/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): FQDN or ip address for the association.<br><br>Maximum Length: 256<br>Reference Resource: [NTP_Association](#!/NTP95Association)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/ntp_associations/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): FQDN or ip address for the association.<br><br>Maximum Length: 256<br>Reference Resource: [NTP_Association](#!/NTP95Association)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ntp_masters`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ntp_masters`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/ntp_masters`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/ntp_masters`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospf_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active_router_id` (filter, optional): The router identifier elected by the OSPF instance. The router ID<br>may be configured or auto elected from one of the interface IPv4 <br>address of the router. If admin_router_id is present, the same will<br>be elected as active_router_id. The router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `admin_router_id` (filter, optional): The router identifier configured for the OSPF instance.<br>The router ID MUST be unique within the entire Autonomus System.<br>If admin_router_id is present, the same will be elected as <br>active_router_id. The router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `auto_cost_ref_bw` (filter, optional): The reference bandwidth, Mbits/second, for interface cost calculations.<br><br>Minimum Value: 1<br>Maximum Value: 4000000<br>
- `bfd_all_interfaces_enable` (filter, optional): Enables BFD on all interfaces involved in OSPF router.<br><br>Key: boolean<br>
- `default_originate` (filter, optional): Criteria for redistribution of the default routes into the OSPF domain:<br>'disable'         : no default route should be advertised.<br>'originate'       : advertise default route if it exists in the routing table.<br>'always_originate': always advertise default route,<br>                    regardless of its presence in the routing table.<br><br>
- `gr_ignore_lost_interface` (filter, optional): Specifies whether to ignore OSPF interfaces that have gone down just prior to<br>the restart event.<br><br>Key: boolean<br>
- `helper_disable` (filter, optional): Indicates whether OSPF will help a neighbor undergoing hitless restart on this<br>interface.<br><br>Key: boolean<br>
- `lsa_arrival` (filter, optional): Minimum wait time in milliseconds before same LSAs received from a peer are processed.<br><br>Minimum Value: 0<br>Maximum Value: 600000<br>
- `maximum_paths` (filter, optional): Maximum number of equal cost paths that are stored for each destination in the<br>Routing Table.<br><br>Minimum Value: 1<br>Maximum Value: 8<br>
- `neighbor_clear_performed` (filter, optional): Number of times that neighbors on this OSPF instance were cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `neighbor_clear_requested` (filter, optional): Number of times a request was made to clear neighbors learned on this OSPF instance.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `passive_interface_default` (filter, optional): This determines whether all interfaces should be set to passive by default.<br><br>Key: boolean<br>
- `protocol_disable` (filter, optional): Disable this OSPF instance.<br><br>Key: boolean<br>
- `restart_interval` (filter, optional): If OSPF is attempting to undergo a graceful restart, this field specifies the<br>length of grace period that should be requested from adjacent routers in grace<br>LSAs.<br><br>Minimum Value: 5<br>Maximum Value: 1800<br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this OSPF instance have been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for this OSPF<br>instance.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `strict_lsa_check_disable` (filter, optional): Specifies whether strict LSA checking is disabled for this OSPF router instance.<br><br>Key: boolean<br>


---
### `POST /system/vrfs/{pid}/ospf_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospf_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): OSPF_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospf_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospf_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): OSPF_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `area_type` (filter, optional): This defines how the external routing and summary lsas for this area will be<br>handled.<br><br>


---
### `POST /system/vrfs/{pid}/ospf_routers/{ppid}/areas`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id` (path, required): OSPF_Area instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id` (path, required): OSPF_Area instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id` (path, required): OSPF_Area instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bdr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Backup Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `calculated_output_cost` (filter, optional): The calculated output cost of OSPF interface, based on the<br>interface bandwidth and reference bandwidth.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `dr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `ifsm_state` (filter, optional): OSPF Interface FSM states. The default value is "depend_upon".<br><br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this OSPF interface have been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for this OSPF<br>interface.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `POST /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Interface area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Interface area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Interface area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces/{ppppid}/ospf_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `ppppid` (path, required): OSPF_Interface interface_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bdr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Backup Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `dr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `nbr_if_addr` (filter, optional): The interface address of the OSPF Neighbor on which the neighbor relationship is<br>established.<br><br>Maximum Length: 45<br>
- `nbr_priority` (filter, optional): The priority of the neighbor. The default value is 255.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `nbr_router_id` (filter, optional): The Neighbor Router ID is used to identify the neighbor.<br>The Neighbor Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `nfsm_state` (filter, optional): OSPF Neighbor FSM states. The default value is "down".<br><br>


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_interfaces/{ppppid}/ospf_neighbors/{id}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `ppppid` (path, required): OSPF_Interface interface_name<br>
- `id` (path, required): The Neighbor Router ID is used to identify the neighbor.<br>The Neighbor Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPF_Neighbor](#!/OSPF95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_summary_addresses`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `lsdb_type` (filter, optional): Type of the LSDB this summary address applies to.<br><br>
- `prefix` (filter, optional): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>


---
### `POST /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_summary_addresses`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_summary_addresses/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id1` (path, required): Type of the LSDB this summary address applies to.<br><br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `id2` (path, required): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_summary_addresses/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id1` (path, required): Type of the LSDB this summary address applies to.<br><br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `id2` (path, required): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_summary_addresses/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id1` (path, required): Type of the LSDB this summary address applies to.<br><br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `id2` (path, required): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_vlinks`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `destination_ip_address` (filter, optional): IPv4/IPv6 address of the virtual neighbor.<br><br>Maximum Length: 45<br>
- `ospf_auth_text_key` (filter, optional): The authentication key for OSPFv2 authentication type "text".<br><br>Minimum Length: 1<br>
- `ospf_auth_type` (filter, optional): The type of OSPFv2 authentication. If not set, then the area level<br>authentication of the transit area, holds for the port.<br><br>
- `source_ip_address` (filter, optional): IPv4/IPv6 source address of the virtual link.<br><br>Maximum Length: 45<br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this OSPF virtual-link have <br>been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for <br>this OSPF virtual-link.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_time` (filter, optional): Time when statistics were last cleared in seconds since the Unix <br>epoch.<br><br>Minimum Value: 0<br>


---
### `POST /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_vlinks`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_vlinks/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Vlink area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_vlinks/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Vlink area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospf_routers/{ppid}/areas/{pppid}/ospf_vlinks/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Vlink area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/clear_ospf_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `nbr_router_id` (filter, optional): Router ID corresponding to the neighbor that needs to be cleared.<br>It is in the IPv4 address format.<br><br>Maximum Length: 15<br>


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/clear_ospf_neighbors/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): Router ID corresponding to the neighbor that needs to be cleared.<br>It is in the IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [Clear_OSPF_neighbor](#!/Clear95OSPF95neighbor)
- `id2` (path, required): Port corresponding to this OSPF router instance.<br>When set, the neighbor is cleared from the specified port instance and when empty,<br>the neighbor is cleared from all port instances associated with this OSPF router.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [Clear_OSPF_neighbor](#!/Clear95OSPF95neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/ospf_lsas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `adv_router` (filter, optional): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `chksum` (filter, optional): The checksum in the OSPF LSA. <br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `ls_birth_time` (filter, optional): The OSPF LSA birth time, number of seconds elapsed since Epoch, which can be<br>used to compute LSA age.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ls_id` (filter, optional): The OSPF Link State ID. The Link State ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `ls_seq_num` (filter, optional): The sequence number of the OSPF LSA.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `lsa_type` (filter, optional): The type of the OSPF LSA.<br><br>
- `num_router_links` (filter, optional): Total number of router links. <br>This is applicable in case of Router LSA. <br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/ospf_lsas/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): The type of the OSPF LSA.<br><br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `id2` (path, required): The OSPF Link State ID. The Link State ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `id3` (path, required): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `id4` (path, required): Area to which the LSA belongs.<br><br>Reference Resource: [OSPF_Area](#!/OSPF95Area)<br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/ospf_routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `path` (filter, optional): The nexthop of the route.<br>For example x.x.x.x/ifName (or) directly attached to ifName.<br>
- `path_type` (filter, optional): The value indicates whether the path type is inter-area, intra-area, or<br>external.<br><br>
- `prefix` (filter, optional): Specifies the prefix address in A.B.C.D/M format or<br>border router-id in A.B.C.D format.<br><br>Maximum Length: 49<br>
- `route_type` (filter, optional): Specifies the the type of the route.<br>route_to_abr  -> Specifies that this is a route to an Area Border Router<br>route_to_asbr -> Specifies that this is a route to an Autonomous System Border Router<br>route_to_abr_asbr -> Specifies that this is a route to an Area Border Router and<br>Autonomous System Border Router<br>route_to_prefix -> Specifies any route to a network.<br><br>
- `vlink_route` (filter, optional): This determines whether this is a route to virtual link.<br><br>Key: boolean<br>


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/ospf_routes/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): Specifies the the type of the route.<br>route_to_abr  -> Specifies that this is a route to an Area Border Router<br>route_to_asbr -> Specifies that this is a route to an Autonomous System Border Router<br>route_to_abr_asbr -> Specifies that this is a route to an Area Border Router and<br>Autonomous System Border Router<br>route_to_prefix -> Specifies any route to a network.<br><br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `id2` (path, required): Specifies the prefix address in A.B.C.D/M format or<br>border router-id in A.B.C.D format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `id3` (path, required): The nexthop of the route.<br>For example x.x.x.x/ifName (or) directly attached to ifName.<br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `id4` (path, required): OSPF Area to which the route belongs.<br><br>Reference Resource: [OSPF_Area](#!/OSPF95Area)<br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/ospfv3_lsas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `adv_router` (filter, optional): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `chksum` (filter, optional): The checksum in the LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `interface_name` (filter, optional): Name of the interface to which the LSA belongs.<br>This is applicable in case of Link LSA.<br><br>Maximum Length: 12<br>
- `ls_birth_time` (filter, optional): The OSPFv3 LSA birth time, number of seconds elapsed since Epoch,<br>which can be used to compute LSA age.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ls_id` (filter, optional): The OSPFv3 Link State ID.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ls_seq_num` (filter, optional): The sequence number of the LSA.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `lsa_prefix` (filter, optional): The IPv6 prefix to which this LSA belongs.<br>This is applicable in case of Inter Area Prefix LSA,<br>External LSA and NSSA External LSA.<br><br>Maximum Length: 49<br>
- `lsa_type` (filter, optional): The type of the OSPFv3 LSA.<br><br>
- `num_network_links` (filter, optional): Total number of network links.<br>This is applicable in case of Network LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `num_router_links` (filter, optional): Total number of router links.<br>This is applicable in case of Router LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `ref_ls_id` (filter, optional): The OSPFv3 Link State ID to which this particular link is<br>referring to. This is applicable in case of Intra Area Prefix<br>LSA. This referrered LSA Id should refer to existing LSA Id of<br>Router LSA or Network LSA.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ref_ls_type` (filter, optional): The OSPFv3 Link State type to which this particular link is<br>referring to. This is applicable in case of Intra Area Prefix<br>LSA. The referred Link State type should be Router LSA or<br>Network LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `GET /system/vrfs/{pid}/ospf_routers/{ppid}/ospfv3_lsas/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): The type of the OSPFv3 LSA.<br><br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `id2` (path, required): The OSPFv3 Link State ID.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `id3` (path, required): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `id4` (path, required): Area to which the LSA belongs.<br><br>Reference Resource: [OSPF_Area](#!/OSPF95Area)<br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospfv3_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active_router_id` (filter, optional): The router identifier elected by the OSPF instance. The router ID<br>may be configured or auto elected from one of the interface IPv4 <br>address of the router. If admin_router_id is present, the same will<br>be elected as active_router_id. The router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `admin_router_id` (filter, optional): The router identifier configured for the OSPF instance.<br>The router ID MUST be unique within the entire Autonomus System.<br>If admin_router_id is present, the same will be elected as <br>active_router_id. The router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `auto_cost_ref_bw` (filter, optional): The reference bandwidth, Mbits/second, for interface cost calculations.<br><br>Minimum Value: 1<br>Maximum Value: 4000000<br>
- `bfd_all_interfaces_enable` (filter, optional): Enables BFD on all interfaces involved in OSPF router.<br><br>Key: boolean<br>
- `default_originate` (filter, optional): Criteria for redistribution of the default routes into the OSPF domain:<br>'disable'         : no default route should be advertised.<br>'originate'       : advertise default route if it exists in the routing table.<br>'always_originate': always advertise default route,<br>                    regardless of its presence in the routing table.<br><br>
- `gr_ignore_lost_interface` (filter, optional): Specifies whether to ignore OSPF interfaces that have gone down just prior to<br>the restart event.<br><br>Key: boolean<br>
- `helper_disable` (filter, optional): Indicates whether OSPF will help a neighbor undergoing hitless restart on this<br>interface.<br><br>Key: boolean<br>
- `lsa_arrival` (filter, optional): Minimum wait time in milliseconds before same LSAs received from a peer are processed.<br><br>Minimum Value: 0<br>Maximum Value: 600000<br>
- `maximum_paths` (filter, optional): Maximum number of equal cost paths that are stored for each destination in the<br>Routing Table.<br><br>Minimum Value: 1<br>Maximum Value: 8<br>
- `neighbor_clear_performed` (filter, optional): Number of times that neighbors on this OSPF instance were cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `neighbor_clear_requested` (filter, optional): Number of times a request was made to clear neighbors learned on this OSPF instance.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `passive_interface_default` (filter, optional): This determines whether all interfaces should be set to passive by default.<br><br>Key: boolean<br>
- `protocol_disable` (filter, optional): Disable this OSPF instance.<br><br>Key: boolean<br>
- `restart_interval` (filter, optional): If OSPF is attempting to undergo a graceful restart, this field specifies the<br>length of grace period that should be requested from adjacent routers in grace<br>LSAs.<br><br>Minimum Value: 5<br>Maximum Value: 1800<br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this OSPF instance have been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for this OSPF<br>instance.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `strict_lsa_check_disable` (filter, optional): Specifies whether strict LSA checking is disabled for this OSPF router instance.<br><br>Key: boolean<br>


---
### `POST /system/vrfs/{pid}/ospfv3_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospfv3_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): OSPF_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospfv3_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): OSPF_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `area_type` (filter, optional): This defines how the external routing and summary lsas for this area will be<br>handled.<br><br>


---
### `POST /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id` (path, required): OSPF_Area instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id` (path, required): OSPF_Area instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id` (path, required): OSPF_Area instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bdr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Backup Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `calculated_output_cost` (filter, optional): The calculated output cost of OSPF interface, based on the<br>interface bandwidth and reference bandwidth.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `dr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `ifsm_state` (filter, optional): OSPF Interface FSM states. The default value is "depend_upon".<br><br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this OSPF interface have been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for this OSPF<br>interface.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `POST /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Interface area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Interface area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Interface area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces/{ppppid}/ospf_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `ppppid` (path, required): OSPF_Interface interface_name<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bdr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Backup Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `dr` (filter, optional): OSPFv2 Router Interface IP or OSPFv3 Router ID of the Designated Router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `nbr_if_addr` (filter, optional): The interface address of the OSPF Neighbor on which the neighbor relationship is<br>established.<br><br>Maximum Length: 45<br>
- `nbr_priority` (filter, optional): The priority of the neighbor. The default value is 255.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `nbr_router_id` (filter, optional): The Neighbor Router ID is used to identify the neighbor.<br>The Neighbor Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `nfsm_state` (filter, optional): OSPF Neighbor FSM states. The default value is "down".<br><br>


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_interfaces/{ppppid}/ospf_neighbors/{id}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `ppppid` (path, required): OSPF_Interface interface_name<br>
- `id` (path, required): The Neighbor Router ID is used to identify the neighbor.<br>The Neighbor Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPF_Neighbor](#!/OSPF95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_summary_addresses`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `lsdb_type` (filter, optional): Type of the LSDB this summary address applies to.<br><br>
- `prefix` (filter, optional): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>


---
### `POST /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_summary_addresses`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_summary_addresses/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id1` (path, required): Type of the LSDB this summary address applies to.<br><br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `id2` (path, required): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_summary_addresses/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id1` (path, required): Type of the LSDB this summary address applies to.<br><br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `id2` (path, required): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_summary_addresses/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id1` (path, required): Type of the LSDB this summary address applies to.<br><br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `id2` (path, required): The prefix address in A.B.C.D/M format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Summary_Address](#!/OSPF95Summary95Address)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_vlinks`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `destination_ip_address` (filter, optional): IPv4/IPv6 address of the virtual neighbor.<br><br>Maximum Length: 45<br>
- `ospf_auth_text_key` (filter, optional): The authentication key for OSPFv2 authentication type "text".<br><br>Minimum Length: 1<br>
- `ospf_auth_type` (filter, optional): The type of OSPFv2 authentication. If not set, then the area level<br>authentication of the transit area, holds for the port.<br><br>
- `source_ip_address` (filter, optional): IPv4/IPv6 source address of the virtual link.<br><br>Maximum Length: 45<br>
- `statistics_clear_performed` (filter, optional): Number of times the statistics for this OSPF virtual-link have <br>been cleared.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear the statistics for <br>this OSPF virtual-link.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `statistics_clear_time` (filter, optional): Time when statistics were last cleared in seconds since the Unix <br>epoch.<br><br>Minimum Value: 0<br>


---
### `POST /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_vlinks`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_vlinks/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Vlink area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_vlinks/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Vlink area_id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ospfv3_routers/{ppid}/areas/{pppid}/ospf_vlinks/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `pppid` (path, required): OSPF_Area area_id<br>
- `id` (path, required): OSPF_Vlink area_id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/clear_ospf_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `nbr_router_id` (filter, optional): Router ID corresponding to the neighbor that needs to be cleared.<br>It is in the IPv4 address format.<br><br>Maximum Length: 15<br>


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/clear_ospf_neighbors/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): Router ID corresponding to the neighbor that needs to be cleared.<br>It is in the IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [Clear_OSPF_neighbor](#!/Clear95OSPF95neighbor)
- `id2` (path, required): Port corresponding to this OSPF router instance.<br>When set, the neighbor is cleared from the specified port instance and when empty,<br>the neighbor is cleared from all port instances associated with this OSPF router.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [Clear_OSPF_neighbor](#!/Clear95OSPF95neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/ospf_lsas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `adv_router` (filter, optional): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `chksum` (filter, optional): The checksum in the OSPF LSA. <br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `ls_birth_time` (filter, optional): The OSPF LSA birth time, number of seconds elapsed since Epoch, which can be<br>used to compute LSA age.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ls_id` (filter, optional): The OSPF Link State ID. The Link State ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `ls_seq_num` (filter, optional): The sequence number of the OSPF LSA.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `lsa_type` (filter, optional): The type of the OSPF LSA.<br><br>
- `num_router_links` (filter, optional): Total number of router links. <br>This is applicable in case of Router LSA. <br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/ospf_lsas/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): The type of the OSPF LSA.<br><br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `id2` (path, required): The OSPF Link State ID. The Link State ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `id3` (path, required): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `id4` (path, required): Area to which the LSA belongs.<br><br>Reference Resource: [OSPF_Area](#!/OSPF95Area)<br>Reference Resource: [OSPF_LSA](#!/OSPF95LSA)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/ospf_routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `path` (filter, optional): The nexthop of the route.<br>For example x.x.x.x/ifName (or) directly attached to ifName.<br>
- `path_type` (filter, optional): The value indicates whether the path type is inter-area, intra-area, or<br>external.<br><br>
- `prefix` (filter, optional): Specifies the prefix address in A.B.C.D/M format or<br>border router-id in A.B.C.D format.<br><br>Maximum Length: 49<br>
- `route_type` (filter, optional): Specifies the the type of the route.<br>route_to_abr  -> Specifies that this is a route to an Area Border Router<br>route_to_asbr -> Specifies that this is a route to an Autonomous System Border Router<br>route_to_abr_asbr -> Specifies that this is a route to an Area Border Router and<br>Autonomous System Border Router<br>route_to_prefix -> Specifies any route to a network.<br><br>
- `vlink_route` (filter, optional): This determines whether this is a route to virtual link.<br><br>Key: boolean<br>


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/ospf_routes/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Description**: Get a set of attributes

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): Specifies the the type of the route.<br>route_to_abr  -> Specifies that this is a route to an Area Border Router<br>route_to_asbr -> Specifies that this is a route to an Autonomous System Border Router<br>route_to_abr_asbr -> Specifies that this is a route to an Area Border Router and<br>Autonomous System Border Router<br>route_to_prefix -> Specifies any route to a network.<br><br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `id2` (path, required): Specifies the prefix address in A.B.C.D/M format or<br>border router-id in A.B.C.D format.<br><br>Maximum Length: 49<br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `id3` (path, required): The nexthop of the route.<br>For example x.x.x.x/ifName (or) directly attached to ifName.<br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `id4` (path, required): OSPF Area to which the route belongs.<br><br>Reference Resource: [OSPF_Area](#!/OSPF95Area)<br>Reference Resource: [OSPF_Route](#!/OSPF95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/ospfv3_lsas`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `adv_router` (filter, optional): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>
- `chksum` (filter, optional): The checksum in the LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `interface_name` (filter, optional): Name of the interface to which the LSA belongs.<br>This is applicable in case of Link LSA.<br><br>Maximum Length: 12<br>
- `ls_birth_time` (filter, optional): The OSPFv3 LSA birth time, number of seconds elapsed since Epoch,<br>which can be used to compute LSA age.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ls_id` (filter, optional): The OSPFv3 Link State ID.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ls_seq_num` (filter, optional): The sequence number of the LSA.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `lsa_prefix` (filter, optional): The IPv6 prefix to which this LSA belongs.<br>This is applicable in case of Inter Area Prefix LSA,<br>External LSA and NSSA External LSA.<br><br>Maximum Length: 49<br>
- `lsa_type` (filter, optional): The type of the OSPFv3 LSA.<br><br>
- `num_network_links` (filter, optional): Total number of network links.<br>This is applicable in case of Network LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `num_router_links` (filter, optional): Total number of router links.<br>This is applicable in case of Router LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>
- `ref_ls_id` (filter, optional): The OSPFv3 Link State ID to which this particular link is<br>referring to. This is applicable in case of Intra Area Prefix<br>LSA. This referrered LSA Id should refer to existing LSA Id of<br>Router LSA or Network LSA.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `ref_ls_type` (filter, optional): The OSPFv3 Link State type to which this particular link is<br>referring to. This is applicable in case of Intra Area Prefix<br>LSA. The referred Link State type should be Router LSA or<br>Network LSA.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `GET /system/vrfs/{pid}/ospfv3_routers/{ppid}/ospfv3_lsas/{id1}/{id2}/{id3}/{id4}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): OSPF_Router instance_tag<br>
- `id1` (path, required): The type of the OSPFv3 LSA.<br><br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `id2` (path, required): The OSPFv3 Link State ID.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `id3` (path, required): The Router ID of the advertising router.<br>The Router ID is in IPv4 address format.<br><br>Maximum Length: 15<br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `id4` (path, required): Area to which the LSA belongs.<br><br>Reference Resource: [OSPF_Area](#!/OSPF95Area)<br>Reference Resource: [OSPFv3_LSA](#!/OSPFv395LSA)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/pim_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `active_active` (filter, optional): Enables PIM active-active feature on the PIM router which is part of VSX pair.<br>If the value is true, then the VSX peer which is not forwarding the multicast traffic,<br>acts as proxy-DR and learns multicast routes. The multicast routes in proxy-DR<br>would be written as bridge entries in the hardware.<br>If the value is false, then PIM active-active feature would be turned off.<br>In this case, if the VSX peer which is forwarding the multicast stream goes down,<br>other peer would send joins only after the neighbor expiry. So it takes time to<br>resume multicast traffic.<br><br>Key: boolean<br>
- `bfd_all_interfaces_enable` (filter, optional): Enables BFD on all PIM interfaces.<br><br>Key: boolean<br>
- `bsm_last_received_time` (filter, optional): The epoch time at which the last BSM is received on this router.<br><br>Key: integer<br>
- `bsr_elected_time` (filter, optional): The epoch time at which the E-BSR is elected as known by this router.<br><br>Key: integer<br>
- `bst_last_expired_time` (filter, optional): The epoch time at which the Bootstrap Timer last expired on this router.<br><br>Key: integer<br>
- `candidate_bsr_bsm_interval` (filter, optional): Periodic interval(in seconds) at which the BSMs are originated from this router.<br><br>Minimum Value: 5<br>Maximum Value: 300<br>
- `candidate_bsr_hash_mask_length` (filter, optional): Candidate-BSR's hash mask length on this router.<br><br>Minimum Value: 1<br>Maximum Value: 128<br>
- `candidate_bsr_priority` (filter, optional): Candidate-BSR's priority on this router.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `candidate_rp_adv_interval` (filter, optional): Periodic interval(in seconds) at which the Candidate-RP advertisements are<br>originated from this router.<br><br>Minimum Value: 30<br>Maximum Value: 600<br>
- `candidate_rp_holdtime` (filter, optional): Candidate-RP's Holdtime (in seconds) on this router.<br><br>Minimum Value: 30<br>Maximum Value: 255<br>
- `candidate_rp_priority` (filter, optional): Candidate-RP's priority on this router.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `elected_bsr_address` (filter, optional): IP Address of the elected BSR on this router.<br><br>Maximum Length: 45<br>
- `elected_bsr_hash_mask_length` (filter, optional): Hash mask length of the elected BSR on this router.<br><br>Minimum Value: 1<br>Maximum Value: 128<br>
- `elected_bsr_priority` (filter, optional): Priority of the elected BSR on this router.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `join_prune_interval` (filter, optional): Frequency (in seconds) at which this router sends PIM Join/Prune messages.<br><br>Minimum Value: 5<br>Maximum Value: 65535<br>
- `mroutes_limit` (filter, optional): Limit on the maximum number of multicast route entries that can be programmed.<br>When the limit is configured, multicast route entries created because of IGMP or<br>MLD membership reports and multicast route entries created because of multicast<br>streams are restricted under the configured limit.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `register_messages_limit` (filter, optional): Limit on the maximum number of register messages sent per second for<br>every unique (S,G) entry. By default, there is no maximum rate set.<br>When the limit is configured, register messages generated exceeding<br>the configured limit will be suppressed.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `router_enable` (filter, optional): Enables PIM protocol on this router.<br><br>Key: boolean<br>
- `sources_per_group` (filter, optional): Total number of sources allowed for a group on this router.<br>By default, there is no limit on the number of sources for a group.<br>When the number of sources for a group exceeds the configured limit,<br>multicast traffic from additional sources will be dropped.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `spt_threshold_disable` (filter, optional): Enables Shortest Path Tree(SPT) switching on this router.<br><br>Key: boolean<br>
- `state_refresh` (filter, optional): Periodic interval (in seconds) at which state refresh datagrams are <br>transmitted by this router. This is applicable when PIM mode is set to 'dense'.<br><br>Minimum Value: 10<br>Maximum Value: 100<br>


---
### `POST /system/vrfs/{pid}/pim_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/pim_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): PIM_Router ip_version<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/pim_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): PIM_Router ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/pim_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): PIM_Router ip_version<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/pim_group_mappings`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `group_prefix` (filter, optional): The group_prefix IP-ADDR/MASK-LEN for this mapping.<br><br>Maximum Length: 49<br>
- `hold_time` (filter, optional): The Holdtime (in seconds) for this RP obtained from the E-BSR.<br>
- `last_rx_timestamp` (filter, optional): The epoch time at which the Group Mapping entry was last received from the<br>E-BSR.<br>
- `rp_address` (filter, optional): IP address of the RP.<br><br>Maximum Length: 45<br>


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/pim_group_mappings/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id1` (path, required): The group_prefix IP-ADDR/MASK-LEN for this mapping.<br><br>Maximum Length: 49<br>Reference Resource: [PIM_Group_Mapping](#!/PIM95Group95Mapping)
- `id2` (path, required): IP address of the RP.<br><br>Maximum Length: 45<br>Reference Resource: [PIM_Group_Mapping](#!/PIM95Group95Mapping)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/pim_local_group_sources`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `group_address` (filter, optional): IPv4 Multicast Group for which the Source is learnt.<br><br>Maximum Length: 15<br>
- `rp_address` (filter, optional): IPv4 address of the RP where the Source is registered.<br><br>Maximum Length: 15<br>
- `source_address` (filter, optional): IPv4 Source address for the Group learnt on the RP<br>through Register packets or directly connected Sources.<br><br>Maximum Length: 15<br>


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/pim_local_group_sources/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id1` (path, required): IPv4 Source address for the Group learnt on the RP<br>through Register packets or directly connected Sources.<br><br>Maximum Length: 15<br>Reference Resource: [PIM_Local_Group_Source](#!/PIM95Local95Group95Source)
- `id2` (path, required): IPv4 Multicast Group for which the Source is learnt.<br><br>Maximum Length: 15<br>Reference Resource: [PIM_Local_Group_Source](#!/PIM95Local95Group95Source)
- `id3` (path, required): IPv4 address of the RP where the Source is registered.<br><br>Maximum Length: 15<br>Reference Resource: [PIM_Local_Group_Source](#!/PIM95Local95Group95Source)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/pim_static_rps`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `override_enable` (filter, optional): If the value is `true`, the static-RP will take precedence over the dynamic-RP<br>for a group prefix, resulting in the dynamic-RP operating only as a backup RP.<br><br>Key: boolean<br>
- `rp_address` (filter, optional): IP address of the RP to be used for a group prefix.<br><br>Maximum Length: 45<br>


---
### `POST /system/vrfs/{pid}/pim_routers/{ppid}/pim_static_rps`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/pim_routers/{ppid}/pim_static_rps/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id` (path, required): PIM_Static_RP ip_version<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/pim_static_rps/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id` (path, required): PIM_Static_RP ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/pim_routers/{ppid}/pim_static_rps/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id` (path, required): PIM_Static_RP ip_version<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/rpf_override`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `ip_address` (filter, optional): IP address of the nexthop device.<br>If both ip address and port are specified,<br>then IP address takes precedence and port is ignored.<br><br>Maximum Length: 45<br>


---
### `POST /system/vrfs/{pid}/pim_routers/{ppid}/rpf_override`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/pim_routers/{ppid}/rpf_override/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id` (path, required): Static_Multicast_Nexthop ip_version<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/pim_routers/{ppid}/rpf_override/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id` (path, required): Static_Multicast_Nexthop ip_version<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/pim_routers/{ppid}/rpf_override/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): PIM_Router ip_version<br>
- `id` (path, required): Static_Multicast_Nexthop ip_version<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/radius_dynamic_authorization_clients`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address` (filter, optional): IPV4/IPV6 address or FQDN of the RADIUS DAC.<br>
- `connection_type` (filter, optional): Specify the connection_type of RADIUS DAC.<br><br>
- `replay_protection_enable` (filter, optional): Enables replay protection for the client.<br><br>Key: boolean<br>
- `secret_key` (filter, optional): The secret key used to communicate with this RADIUS DAC.<br><br>Minimum Length: 1<br>Maximum Length: 192<br>
- `time_window` (filter, optional): Time Window (in secs) within which RADIUS packets carrying the <br>'Event-Timestamp' attribute will be considered as current and <br>accepted for processing by the NAS.<br><br>Minimum Value: 0<br>Maximum Value: 65535<br>


---
### `POST /system/vrfs/{pid}/radius_dynamic_authorization_clients`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/radius_dynamic_authorization_clients/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS DAC.<br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `id2` (path, required): Specify the connection_type of RADIUS DAC.<br><br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/radius_dynamic_authorization_clients/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS DAC.<br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `id2` (path, required): Specify the connection_type of RADIUS DAC.<br><br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/radius_dynamic_authorization_clients/{id1}/{id2}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS DAC.<br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `id2` (path, required): Specify the connection_type of RADIUS DAC.<br><br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/radius_dynamic_authorization_clients/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS DAC.<br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `id2` (path, required): Specify the connection_type of RADIUS DAC.<br><br>Reference Resource: [Radius_Dynamic_Authorization_Client](#!/Radius95Dynamic95Authorization95Client)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/radius_servers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `accounting_udp_port` (filter, optional): UDP port to be used for the communication to RADIUS accounting.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `address` (filter, optional): IPV4/IPV6 address or FQDN of the RADIUS server.<br>
- `auth_type` (filter, optional): Specifies the server specific authentication method (pap/chap) to be used.<br>If not specified, the globally configured authentication method (pap/chap) will be used.<br><br>
- `default_group_priority` (filter, optional): Specifies the order in which a RADIUS server is configured within<br>RADIUS default family group 'radius'.<br>By default all RADIUS servers should be added to default group 'radius'<br>Priority is assigned starting with 1 and is incremental.<br>Servers with equal priority in the default family group will undergo<br>similar tie-breaker algorithm as mentioned for the user defined server group<br><br>Minimum Value: 1<br>
- `last_tracking_attempted_time` (filter, optional): Time in seconds since Epoch when the most recent reachability<br>tracking request was sent to the RADIUS server.<br><br>Minimum Value: 0<br>
- `last_tracking_status_changed_time` (filter, optional): Time in seconds since Epoch when RADIUS Server status last changed<br>from reachable to unreachable or vice versa.<br><br>Minimum Value: 0<br>
- `last_tracking_status_refreshed_time` (filter, optional): Time in seconds since Epoch when the tracking status was<br>last refreshed.<br><br>Minimum Value: 0<br>
- `passkey` (filter, optional): Specifies the passkey between RADIUS client and RADIUS server for<br>authentication.<br><br>
- `port` (filter, optional): Specifies the port number for authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `port_type` (filter, optional): Specifies the type of port (tcp/udp) for authentication.<br><br>
- `reachability_status` (filter, optional): Specifies the reachability of Configured RADIUS Server.<br>'reachable':              tracking for this server is enabled and<br>                          the server is reachable.<br>'unreachable':            tracking for this server is enabled and<br>                          the server is not reachable.<br>'reachability_unhealthy': tracking for this server is enabled and<br>                          the server is momentarily down in<br>                          between tracking interval.<br>An empty value means the reachability of this server is unknown.<br><br>
- `retries` (filter, optional): Specifies the server specific number of retries to the RADIUS server if there is no response.<br>If not specified, the globally configured number of retries will be used.<br><br>Minimum Value: 0<br>Maximum Value: 5<br>
- `timeout` (filter, optional): Specifies the server specific timeout between authentication requests to the RADIUS server.<br>If not specified, the globally configured timeout will be used.<br><br>Minimum Value: 1<br>Maximum Value: 60<br>
- `tls_connection_status` (filter, optional): Status of the TLS connection<br>'tls_connection_established': RADIUS server TLS connection<br>                              successfully established.<br>'tls_connection_closed':      RADIUS server TLS connection has<br>                              been closed.<br>'tcp_connection_failed':      RADIUS server TCP connection could<br>                              not be established.<br>'tls_connection_failed':      RADIUS server TLS connection could<br>                              not be established.<br>'tcp_connection_in_progress': RADIUS server TCP connection is in<br>                              progress.<br>'tls_connection_in_progress': RADIUS server TLS connection is in<br>                              progress.<br><br>
- `tracking_enable` (filter, optional): Specifies whether tracking should be enabled on this<br>server.<br><br>Key: boolean<br>
- `tracking_mode` (filter, optional): Specifies the tracking mode to be set for this server and is only<br>applicable when tracking is enabled for this server.<br>'any'       : Server reachability is monitored regardless of<br>              whether the server was responsive or non-responsive<br>              to prior RADIUS client requests.<br>'dead-only' : Server reachability is monitored only if it is<br>              deemed dead (based on non-responsiveness for RADIUS<br>              client requests sent to this server earlier).<br><br>
- `user_group_priority` (filter, optional): Specifies the order in which RADIUS servers are configured<br>within a user defined server group. Priority is assigned<br>starting with 1 and incremental. In case this server is<br>not part of a user defined group, this will be empty.<br>Servers where priority is not configured will be reached out last<br>Servers with equal priority in a group will be reached out as follows:<br>Those belonging to vrf where vrf_name appears alphabetically earlier<br>than the others are reached out first. If that's a tie, servers with<br>address appearing alphabetically earlier than the others is reached<br>out first. If that too is a tie, servers with smaller udp port are<br>reached out first<br><br>Minimum Value: 1<br>


---
### `POST /system/vrfs/{pid}/radius_servers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/radius_servers/{id1}/{id2}/{id3}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS server.<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id2` (path, required): Specifies the port number for authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id3` (path, required): Specifies the type of port (tcp/udp) for authentication.<br><br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/radius_servers/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS server.<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id2` (path, required): Specifies the port number for authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id3` (path, required): Specifies the type of port (tcp/udp) for authentication.<br><br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/radius_servers/{id1}/{id2}/{id3}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS server.<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id2` (path, required): Specifies the port number for authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id3` (path, required): Specifies the type of port (tcp/udp) for authentication.<br><br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/radius_servers/{id1}/{id2}/{id3}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the RADIUS server.<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id2` (path, required): Specifies the port number for authentication.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `id3` (path, required): Specifies the type of port (tcp/udp) for authentication.<br><br>Reference Resource: [Radius_Server](#!/Radius95Server)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/recursive_nexthops`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `nh_metric` (filter, optional): The cost to reach the forwarding next hops that the recursive next hop is<br>resolved to.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `rnh_ip` (filter, optional): IPv4 or IPv6 recursive next hop address to be resolved. Example 192.168.0.2<br><br>Maximum Length: 49<br>


---
### `GET /system/vrfs/{pid}/recursive_nexthops/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): IPv4 or IPv6 recursive next hop address to be resolved. Example 192.168.0.2<br><br>Maximum Length: 49<br>Reference Resource: [Recursive_Nexthop](#!/Recursive95Nexthop)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/remote_l2vpn_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family corresponding to the neighbor's IP address.<br><br>
- `from` (filter, optional): Source of the Neighbor IP address:<br>`evpn`:     added by EVPN.<br><br>
- `ip_address` (filter, optional): IPv4 or IPv6 address of the neighbor.<br><br>Maximum Length: 45<br>
- `mac` (filter, optional): MAC address of the neighbor.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `GET /system/vrfs/{pid}/remote_l2vpn_neighbors/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPv4 or IPv6 address of the neighbor.<br><br>Maximum Length: 45<br>Reference Resource: [Remote_L2VPN_Neighbor](#!/Remote95L2VPN95Neighbor)
- `id2` (path, required): Source of the Neighbor IP address:<br>`evpn`:     added by EVPN.<br><br>Reference Resource: [Remote_L2VPN_Neighbor](#!/Remote95L2VPN95Neighbor)
- `id3` (path, required): Reference to logical L3 VLAN interface associated with neighbor.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [Remote_L2VPN_Neighbor](#!/Remote95L2VPN95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/rip_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `disable` (filter, optional): Disable this RIP instance.<br><br>Key: boolean<br>
- `distance` (filter, optional): The administrative distance associated with routes advertised by this RIP instance.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `maximum_paths` (filter, optional): Maximum number of equal cost paths that can be associated with a given <br>destination in the routing table corresponding to this instance.<br><br>Minimum Value: 1<br>Maximum Value: 8<br>
- `statistics_clear_performed` (filter, optional): Number of times statistics for this RIP instance have been cleared.<br><br>Minimum Value: 0<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear statistics for this RIP<br>instance.<br><br>Minimum Value: 0<br>
- `statistics_reset_time` (filter, optional): Time in seconds since Epoch when statistics information for this RIP instance was last reset.<br><br>Minimum Value: 0<br>


---
### `POST /system/vrfs/{pid}/rip_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/rip_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/rip_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/rip_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `receive` (filter, optional):  `receive`: RIP updates will be received on this interface.<br> `doNotReceive`: RIP updates will not be received on this interface.<br><br>
- `send` (filter, optional):  `send`: RIP updates will be sent out this interface.<br> `doNotSend`: RIP updates will not be sent out this interface.<br><br>
- `shutdown` (filter, optional): Shutdown RIP on this interface.<br><br>Key: boolean<br>


---
### `POST /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): RIP_Interface address-family<br>
- `id2` (path, required): RIP_Interface intf_key<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): RIP_Interface address-family<br>
- `id2` (path, required): RIP_Interface intf_key<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/rip_routers/{ppid}/rip_interfaces/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): RIP_Interface address-family<br>
- `id2` (path, required): RIP_Interface intf_key<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/rip_routers/{ppid}/rip_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `last_update_time` (filter, optional): Value of sysUpTime corresponding to the last RIP update <br>received from this neighbor.<br><br>Minimum Value: 0<br>
- `peer_address` (filter, optional): IPv4 or IPv6 address that the peer is using as its source address.<br><br>Maximum Length: 45<br>
- `peer_version` (filter, optional): Protocol version number advertised by this neighbor.<br><br>Key: integer<br>


---
### `GET /system/vrfs/{pid}/rip_routers/{ppid}/rip_neighbors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id` (path, required): IPv4 or IPv6 address that the peer is using as its source address.<br><br>Maximum Length: 45<br>Reference Resource: [RIP_Neighbor](#!/RIP95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/rip_routers/{ppid}/rip_routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `metric` (filter, optional): Number of routed hops between the nexthop device and the destination network.<br><br>Minimum Value: 1<br>Maximum Value: 15<br>
- `nexthop` (filter, optional): IPv4 or IPv6 address of the nexthop device.<br><br>Maximum Length: 45<br>
- `prefix` (filter, optional): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br><br>Maximum Length: 49<br>


---
### `GET /system/vrfs/{pid}/rip_routers/{ppid}/rip_routes/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br><br>Maximum Length: 49<br>Reference Resource: [RIP_Route](#!/RIP95Route)
- `id2` (path, required): IPv4 or IPv6 address of the nexthop device.<br><br>Maximum Length: 45<br>Reference Resource: [RIP_Route](#!/RIP95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ripng_routers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `disable` (filter, optional): Disable this RIP instance.<br><br>Key: boolean<br>
- `distance` (filter, optional): The administrative distance associated with routes advertised by this RIP instance.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `maximum_paths` (filter, optional): Maximum number of equal cost paths that can be associated with a given <br>destination in the routing table corresponding to this instance.<br><br>Minimum Value: 1<br>Maximum Value: 8<br>
- `statistics_clear_performed` (filter, optional): Number of times statistics for this RIP instance have been cleared.<br><br>Minimum Value: 0<br>
- `statistics_clear_requested` (filter, optional): Number of times a request was made to clear statistics for this RIP<br>instance.<br><br>Minimum Value: 0<br>
- `statistics_reset_time` (filter, optional): Time in seconds since Epoch when statistics information for this RIP instance was last reset.<br><br>Minimum Value: 0<br>


---
### `POST /system/vrfs/{pid}/ripng_routers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ripng_routers/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ripng_routers/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ripng_routers/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `receive` (filter, optional):  `receive`: RIP updates will be received on this interface.<br> `doNotReceive`: RIP updates will not be received on this interface.<br><br>
- `send` (filter, optional):  `send`: RIP updates will be sent out this interface.<br> `doNotSend`: RIP updates will not be sent out this interface.<br><br>
- `shutdown` (filter, optional): Shutdown RIP on this interface.<br><br>Key: boolean<br>


---
### `POST /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): RIP_Interface address-family<br>
- `id2` (path, required): RIP_Interface intf_key<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): RIP_Interface address-family<br>
- `id2` (path, required): RIP_Interface intf_key<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ripng_routers/{ppid}/rip_interfaces/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): RIP_Interface address-family<br>
- `id2` (path, required): RIP_Interface intf_key<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ripng_routers/{ppid}/rip_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `last_update_time` (filter, optional): Value of sysUpTime corresponding to the last RIP update <br>received from this neighbor.<br><br>Minimum Value: 0<br>
- `peer_address` (filter, optional): IPv4 or IPv6 address that the peer is using as its source address.<br><br>Maximum Length: 45<br>
- `peer_version` (filter, optional): Protocol version number advertised by this neighbor.<br><br>Key: integer<br>


---
### `GET /system/vrfs/{pid}/ripng_routers/{ppid}/rip_neighbors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id` (path, required): IPv4 or IPv6 address that the peer is using as its source address.<br><br>Maximum Length: 45<br>Reference Resource: [RIP_Neighbor](#!/RIP95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/ripng_routers/{ppid}/rip_routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `metric` (filter, optional): Number of routed hops between the nexthop device and the destination network.<br><br>Minimum Value: 1<br>Maximum Value: 15<br>
- `nexthop` (filter, optional): IPv4 or IPv6 address of the nexthop device.<br><br>Maximum Length: 45<br>
- `prefix` (filter, optional): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br><br>Maximum Length: 49<br>


---
### `GET /system/vrfs/{pid}/ripng_routers/{ppid}/rip_routes/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): RIP_Router instance_tag<br>
- `id1` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br><br>Maximum Length: 49<br>Reference Resource: [RIP_Route](#!/RIP95Route)
- `id2` (path, required): IPv4 or IPv6 address of the nexthop device.<br><br>Maximum Length: 45<br>Reference Resource: [RIP_Route](#!/RIP95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/route_resolutions`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `GET /system/vrfs/{pid}/route_resolutions/{id1}/{id2}/{id3}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): Agent in the system that requires address to be resolved.<br><br>Reference Resource: [Route_Resolution](#!/Route95Resolution)
- `id2` (path, required): Destination IP address to be resolved.<br><br>Maximum Length: 45<br>Reference Resource: [Route_Resolution](#!/Route95Resolution)
- `id3` (path, required): Specifies the L3 interface of the address for which resolution is<br>requested. This is only required if the resolution request is for an IPv6<br>link-local address.<br><br>Reference Resource: [Port](#!/Port)<br>Reference Resource: [Route_Resolution](#!/Route95Resolution)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Represents the address family for this entry. Default value is `ipv4`.<br><br>
- `distance` (filter, optional): Administrative distance for the route entry. This value is populated every time<br>a protocol or a user adds a new entry. The default value is 1 which is the<br>default distance for static routes.<br><br>Minimum Value: 0<br>Maximum Value: 255<br>
- `from` (filter, optional): Protocol that is responsible for this entry:<br>`bgp`:       the route is created by BGP protocol<br>`ospf`:      the route is created by OSPF protocol<br>`static`:    the route is configured by the user<br>`connected`: the route is for a directly connected subnet<br>'local':     route for the IP address configured on the device itself<br>`<br>r<br>i<br>p<br>`<br>:<br> <br>t<br>h<br>e<br> <br>r<br>o<br>u<br>t<br>e<br> <br>i<br>s<br> <br>c<br>r<br>e<br>a<br>t<br>e<br>d<br> <br>b<br>y<br> <br>R<br>I<br>P<br> <br>p<br>r<br>o<br>t<br>o<br>c<br>o<br>l<br><br>
- `metric` (filter, optional): This is the BGP Multi Exit Discriminator (MED) attribute used in best path<br>selection. The MED provides a dynamic way to influence another AS in the way to<br>reach a certain route when there are multiple entry points for that AS.  BGP<br>decision process takes weight, local preference, AS path, Origin and MED into<br>account.  For selection, if all other factors are equal, the exit point with the<br>lowest MED is preferred. Default value is 0<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `prefix` (filter, optional): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br>Example: 192.168.0.0/16<br><br>Maximum Length: 49<br>
- `protocol_private` (filter, optional): Indicates that this row is a protocol specific route entry. The entries which<br>have this value set, should not participate in routing. Example: BGP can store<br>routes for reference and future selection but should not currently be used for<br>forwarding. Default is `false`.<br><br>Key: boolean<br>
- `route_age` (filter, optional): Time (in seconds from Epoch) when this route was added.<br><br>Minimum Value: 0<br>Maximum Value: 9223372036854775808<br>
- `selected` (filter, optional): Route table can have entries which may not be selected for forwarding. This flag<br>indicates if this entry is selected as an active route for forwarding. Default<br>is `false`.<br><br>Key: boolean<br>
- `sub_address_family` (filter, optional): Represents more information regarding this entry. Default is `unicast`.<br><br>
- `sub_protocol_type` (filter, optional): Specifies the sub-protocol type of the route:<br>ospf_intra_area : OSPF Intra Area route<br>ospf_inter_area : OSPF Inter Area route<br>ospf_type1_ext  : OSPF Extrenal Type-1 route<br>ospf_type2_ext  : OSPF External Type-2 route<br>ospf_type1_nssa : OSPF Type-1 NSSA route<br>ospf_type2_nssa : OSPF Type-2 NSSA route<br>bgp_int         : BGP Internal route<br>bgp_ext         : BGP External route<br>bgp_vpn         : BGP VPN route<br>bgp_evpn        : BGP EVPN route<br><br>Key: string<br>
- `tag` (filter, optional): Tag value associated with this route.<br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>
- `type` (filter, optional): Specifies whether the route is of type blackhole, reject, forward or local:<br>`forward`:   the packets that match the route for destination will be forwarded<br>             based on the nexthop entry.<br>`reject`:    the packets that match the route for destination will be discarded<br>             and an ICMP unreachable message is sent to the sender.<br>`blackhole`: the packets that match the route for destination will be silently<br>             discarded without sending any ICMP message to the sender.<br>'local':     the packets that match the route for destination will be consumed by<br>             the device and will not be forwarded.<br><br>


---
### `GET /system/vrfs/{pid}/routes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br>Example: 192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Route](#!/Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/routes/{ppid}/nexthops`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br>Example: 192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Route](#!/Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `ip_address` (filter, optional): IP address of the nexthop device.<br><br>Maximum Length: 45<br>
- `selected` (filter, optional): Indicates if this nexthop is actively participating in forwarding. <br>Multiple nexthops can exist for each route entry but the routing protocol can indicate if a particular nexthop should not be used in forwarding. <br><br>Key: boolean<br>
- `weight` (filter, optional): Weight is used to differentially balance the packets. <br>Example: For a route if there are 2 nexthops nh1 with weight 5 and nh2 with weight 1, then for every 5 packets that uses nh1, one packet will use nh2. <br>In the first release, the above case is not supported. <br>Only ECMP is supported. <br><br>Minimum Value: 0<br>Maximum Value: 4294967295<br>


---
### `GET /system/vrfs/{pid}/routes/{ppid}/nexthops/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format.<br>Example: 192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Route](#!/Route)
- `id` (path, required): Nexthop <br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/snmpv3_contexts`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `community_name` (filter, optional): Snmpv2 Community associated with this context.<br><br>Minimum Length: 1<br>Maximum Length: 32<br>
- `context_type` (filter, optional): Type of the snmpv3 context.<br><br>
- `name` (filter, optional): <br>Minimum Length: 1<br>Maximum Length: 32<br>


---
### `POST /system/vrfs/{pid}/snmpv3_contexts`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/snmpv3_contexts/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): <br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [SNMPv3_Context](#!/SNMPv395Context)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/snmpv3_contexts/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): <br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [SNMPv3_Context](#!/SNMPv395Context)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/snmpv3_contexts/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): <br>Minimum Length: 1<br>Maximum Length: 32<br>Reference Resource: [SNMPv3_Context](#!/SNMPv395Context)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ssh_sessions`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `client_ip` (filter, optional): IPv4/IPv6 address of the remote SSH client.<br>
- `client_port` (filter, optional): SSH client port.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `server_ip` (filter, optional): Local IPv4/IPv6 address of the switch.<br>
- `server_port` (filter, optional): SSH server port.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>


---
### `GET /system/vrfs/{pid}/ssh_sessions/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPv4/IPv6 address of the remote SSH client.<br>Reference Resource: [SSH_Session](#!/SSH95Session)
- `id2` (path, required): SSH client port.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [SSH_Session](#!/SSH95Session)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/static_neighbors`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Address family of the neighbor.<br><br>
- `ip_address` (filter, optional): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>
- `mac` (filter, optional): MAC address of configured static neighbor.<br><br>Minimum Length: 17<br>Maximum Length: 17<br>


---
### `POST /system/vrfs/{pid}/static_neighbors`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/static_neighbors/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>Reference Resource: [Static_Neighbor](#!/Static95Neighbor)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/static_neighbors/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>Reference Resource: [Static_Neighbor](#!/Static95Neighbor)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/static_neighbors/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): The IPv4 address or the IPv6 address of neighbor<br><br>Maximum Length: 45<br>Reference Resource: [Static_Neighbor](#!/Static95Neighbor)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/static_routes`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address_family` (filter, optional): Represents the address family for this entry. Default value is `ipv4`.<br><br>
- `prefix` (filter, optional): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>


---
### `POST /system/vrfs/{pid}/static_routes`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/static_routes/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/static_routes/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/static_routes/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/static_routes/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/static_routes/{ppid}/static_nexthops`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `bfd_enable` (filter, optional): Enables BFD session to the specific next hop.<br><br>Key: boolean<br>
- `distance` (filter, optional): Administrative distance to be used instead of the default.<br><br>Minimum Value: 1<br>Maximum Value: 255<br>
- `ip_address` (filter, optional): IP address of the nexthop device.<br><br>Maximum Length: 45<br>
- `tag` (filter, optional): Route tag to be used to filter routes and apply administrative policies,<br>such as redistribution with route maps.<br><br>Minimum Value: 1<br>Maximum Value: 4294967295<br>
- `type` (filter, optional): Nexthop corresponding to the static route is 'forward', 'blackhole'<br> or 'reject'.<br>`forward` - Packets to destinations that match this route will be<br> forwarded based on the nexthop entry.<br>`reject` - Packets to destinations that  match this route will be<br> discarded and corresponding ICMP unreachable messages sent to the sender.<br>`blackhole` - Packets to destinations that match this route will be<br> silently discarded.<br><br>


---
### `POST /system/vrfs/{pid}/static_routes/{ppid}/static_nexthops`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/static_routes/{ppid}/static_nexthops/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `id` (path, required): Static_Nexthop id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/static_routes/{ppid}/static_nexthops/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `id` (path, required): Static_Nexthop id<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/static_routes/{ppid}/static_nexthops/{id}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `id` (path, required): Static_Nexthop id<br>
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/static_routes/{ppid}/static_nexthops/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): IPv4 or IPv6 destination prefix and mask in the address/mask format. Example<br>192.168.0.0/16<br><br>Maximum Length: 49<br>Reference Resource: [Static_Route](#!/Static95Route)
- `id` (path, required): Static_Nexthop id<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/tacacs_servers`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `address` (filter, optional): IPV4/IPV6 address or FQDN of the TACACS+ server.<br>
- `auth_type` (filter, optional): Specifies the server specific authentication method (pap/chap) to be used.<br>If not specified, the globally configured authentication method (pap/chap) will be used.<br><br>
- `default_group_priority` (filter, optional): Specifies the order in which a TACACS+ server is configured within<br>TACACS+ default family group 'tacacs'<br>By default all TACACS+ servers should be added to default group 'tacacs'<br>Priority is assigned starting with 1 and incremental.<br>Servers with equal priority in the default family group will undergo<br>similar tie-breaker algorithm as mentioned for the user defined server group<br><br>Minimum Value: 1<br>
- `last_tracking_attempted_time` (filter, optional): Time in seconds since Epoch when the most recent reachability<br>tracking request was sent to the TACACS+ server.<br><br>Minimum Value: 0<br>
- `last_tracking_status_changed_time` (filter, optional): Time in seconds since Epoch when TACACS+ Server status last changed<br>from reachable to unreachable or vice versa.<br><br>Minimum Value: 0<br>
- `passkey` (filter, optional): Specifies the shared secret key between the TACACS+ client<br>and the TACACS+ server.<br><br>
- `reachability_status` (filter, optional): Specifies the reachability of Configured TACACS+ Server.<br>'reachable':    tracking for this server is enabled and the<br>                server is reachable.<br>'unreachable':  tracking for this server is enabled and the<br>                server is not reachable.<br>An empty value means the reachability of this server is unknown.<br><br>
- `tcp_port` (filter, optional): Specifies the tcp port number used for exchanging TACACS+ messages<br>between the client and server.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>
- `timeout` (filter, optional): Specifies the server specific timeout interval that the switch waits for response<br>from the TACACS+ server before declaring a timeout failure.<br>If not specified, the globally configured timeout will be used.<br><br>Minimum Value: 1<br>Maximum Value: 60<br>
- `tracking_enable` (filter, optional): Specifies whether tracking should be enabled for this<br>server (server tracking has to be enabled globally as<br>well).<br><br>Key: boolean<br>
- `user_group_priority` (filter, optional): Specifies the order in which TACACS+ servers are configured<br>within a user defined server group. Priority is assigned starting with 1<br>and incremental. In case this server is not part of a user<br>defined group, this will be empty.<br>Servers where priority is not configured will be reached out last<br>Servers with equal priority in a group will be reached out as follows:<br>Those belonging to vrf where vrf_name appears alphabetically earlier<br>than the others are reached out first. If that's a tie, servers with<br>address appearing alphabetically earlier than the others is reached<br>out first. If that too is a tie, servers with smaller tcp port are<br>reached out first<br><br>Minimum Value: 1<br>


---
### `POST /system/vrfs/{pid}/tacacs_servers`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/tacacs_servers/{id1}/{id2}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the TACACS+ server.<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `id2` (path, required): Specifies the tcp port number used for exchanging TACACS+ messages<br>between the client and server.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/tacacs_servers/{id1}/{id2}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the TACACS+ server.<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `id2` (path, required): Specifies the tcp port number used for exchanging TACACS+ messages<br>between the client and server.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vrfs/{pid}/tacacs_servers/{id1}/{id2}`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the TACACS+ server.<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `id2` (path, required): Specifies the tcp port number used for exchanging TACACS+ messages<br>between the client and server.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `data` (body, required): data


---
### `PUT /system/vrfs/{pid}/tacacs_servers/{id1}/{id2}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id1` (path, required): IPV4/IPV6 address or FQDN of the TACACS+ server.<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `id2` (path, required): Specifies the tcp port number used for exchanging TACACS+ messages<br>between the client and server.<br><br>Minimum Value: 1<br>Maximum Value: 65535<br>Reference Resource: [Tacacs_Server](#!/Tacacs95Server)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ubt_zones`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `cluster_alias` (filter, optional): User provided name for the cluster.<br>This is advertised to the switch as part of the cluster-switch handshake.<br><br>Maximum Length: 32<br>
- `cluster_name` (filter, optional): Name of the UBT cluster.<br><br>Maximum Length: 32<br>
- `enable` (filter, optional): Enables UBT functionality for this zone.<br><br>Key: boolean<br>
- `name` (filter, optional): Zone name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>
- `papi_security_key` (filter, optional): Shared security key that will be used to encrypt UBT PAPI messages exchanged<br>between this switch and the controller cluster corresponding to this zone.<br><br>Minimum Length: 10<br>
- `sac_heartbeat_interval` (filter, optional): Time interval (in seconds) between successive <br>heartbeat messages to the switch anchor node.<br><br>Minimum Value: 1<br>Maximum Value: 8<br>
- `switch_bootstrap_state` (filter, optional):  `not_started`:            bootstrap process has not started.<br> `bootstrapping`:          bootstrap process is on-going.<br> `standalone`:             device has bootstrapped with the SAC node.<br> `redundant`:              device has bootstrapped with the SAC and <br>                           the Standby-SAC nodes.<br> `failover`:               heartbeat to the SAC node timedout and <br>                           the device is failing over to the Standby-SAC.<br> `unbootstrapping`:        de-registering from the SAC and Standby-SAC nodes.<br><br>
- `uac_keepalive_interval` (filter, optional): Time interval (in seconds) between successive <br>keep-alive messages sent to the user anchor node.<br><br>Minimum Value: 1<br>Maximum Value: 60<br>


---
### `POST /system/vrfs/{pid}/ubt_zones`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/ubt_zones/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): Zone name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [UBT_Zone](#!/UBT95Zone)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/ubt_zones/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): Zone name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [UBT_Zone](#!/UBT95Zone)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/ubt_zones/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): Zone name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [UBT_Zone](#!/UBT95Zone)
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vrfs/{pid}/ubt_zones/{ppid}/ubt_uacs`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): Zone name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [UBT_Zone](#!/UBT95Zone)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `ip_address` (filter, optional): IP address of the UAC node.<br><br>Maximum Length: 45<br>


---
### `GET /system/vrfs/{pid}/ubt_zones/{ppid}/ubt_uacs/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `ppid` (path, required): Zone name.<br><br>Minimum Length: 1<br>Maximum Length: 64<br>Reference Resource: [UBT_Zone](#!/UBT95Zone)
- `id` (path, required): IP address of the UAC node.<br><br>Maximum Length: 45<br>Reference Resource: [UBT_UAC](#!/UBT95UAC)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /system/vrfs/{pid}/vrf_address_families`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows


---
### `POST /system/vrfs/{pid}/vrf_address_families`
**Summary**: Create a new resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `data` (body, required): data


---
### `DELETE /system/vrfs/{pid}/vrf_address_families/{id}`
**Summary**: Delete a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): VRF_Address_Family address_family<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vrfs/{pid}/vrf_address_families/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): VRF_Address_Family address_family<br>
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `PUT /system/vrfs/{pid}/vrf_address_families/{id}`
**Summary**: Update a resource instance

**Parameters:**
- `pid` (path, required): VRF identifier. Should be alphanumeric. VRF names must be unique.<br><br>Maximum Length: 32<br>Reference Resource: [VRF](#!/VRF)
- `id` (path, required): VRF_Address_Family address_family<br>
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `DELETE /system/vsx`
**Summary**: Delete a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)


---
### `GET /system/vsx`
**Summary**: Get a set of attributes

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `POST /system/vsx`
**Summary**: Create a new resource instance

**Parameters:**
- `data` (body, required): data


---
### `PUT /system/vsx`
**Summary**: Update a resource instance

**Parameters:**
- `If-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.1)
- `data` (body, required): data


---
### `GET /system/vsx_remote_lags`
**Summary**: Get a list of resources

**Description**: Get a list of resources

Parameter of the filter parameter type is a column name in the table row, enter a value to return only the rows with the given column value.

**Parameters:**
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.
- `count` (query, optional): number of rows
- `hash_scheme` (filter, optional): LAG hash scheme for this VSX as configured on the peer device.<br><br>
- `loop_protect_enabled` (filter, optional): Loop Protection admin status for this VSX as configured on the peer device.<br><br>Key: boolean<br>
- `name` (filter, optional): Peer device VSX name.<br>


---
### `GET /system/vsx_remote_lags/{id}`
**Summary**: Get a set of attributes

**Parameters:**
- `id` (path, required): Peer device VSX name.<br>Reference Resource: [VSX_Remote_Lag](#!/VSX95Remote95Lag)
- `attributes` (query, optional): columns to display
- `If-None-Match` (header, optional): entity-tag value for representation comparison (see RFC 7232 - Conditional Requests - section 3.2)
- `depth` (query, optional): Depth parameter must be greater than or equal to 0 and less than or equal to 3.
- `selector` (query, optional): Select from configuration, status, or statistics. Defaults to "no category". A comma can be added to separate list elements.


---
### `GET /traceroute`
**Summary**: Get traceroute result

**Description**: Get traceroute result.

This URI is not supported by Notification feature and by NAE.

**Parameters:**
- `ip` (query, required): destination IP. IPv4, IPv6, or hostname
- `is_ipv4` (query, required): Set the value to true if the destination is an IPV4 address
- `loose_source_ip` (query, optional): IPv4 address. Destination IP must be IPv4
- `destination_port` (query, optional): Integer in range 1-34000
- `max_ttl` (query, optional): maximum time-to-live (TTL), integer in range 1-255, default value 30.
- `min_ttl` (query, optional): minimum time-to-live (TTL), integer in range 1-255, default value 1
- `probes` (query, optional): integer in range 1-5, default value 3
- `timeout` (query, optional): integer in range 1-60, default value 3
- `mgmt` (query, optional): VRF name/Management mutually exclusive. default value false
- `vrf_name` (query, optional): VRF name/Management mutually exclusive. default value 'swns'


---
