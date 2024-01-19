# Wazuh custom-gotify.py ingegration

This script provides the ability to send alerts from wazuh-server to a gotify-server.

## Installation

Save the script on the folowing path and change the file permissions:

```bash
/var/ossec/integrations/custom-gotify.py
chown root:wazuh custom-gotify.py
chmod 750 custom-gotify.py
```

Add the following lines to your wazuh global config inside <ossec_config></ossec_config>:
(change <gotify_url> and <gotify_app_token>)

```xml
  <integration>
   <name>custom-gotify.py</name>
   <hook_url>https://<gotify_url>/message?token=<gotify_app_token></hook_url>
   <alert_format>json</alert_format>
   <level>7</level>
  </integration>
```
