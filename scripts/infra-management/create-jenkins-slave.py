import logging
import requests
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.requester import Requester
from jenkinsapi.utils.crumb_requester import CrumbRequester
from dotenv import load_dotenv

load_dotenv()

requests.packages.urllib3.disable_warnings()

log_level = getattr(logging, "DEBUG")
logging.basicConfig(level=log_level)
logger = logging.getLogger()

jenkins_url = os.getenv("JENKINS_URL")
username = os.getenv("JENKINS_USER") 
password = os.getenv("JENKINS_PASS")

jenkins = Jenkins(
    jenkins_url,
    requester=CrumbRequester(
        username, password, baseurl=jenkins_url, ssl_verify=False,
    ),
)

# Create JNLP(Java Webstart) slave
"""
node_dict = {
    "num_executors": 1,  # Number of executors
    "node_description": "Agent 1",  # Just a user friendly text
    "remote_fs": "/home/jenkins",  # Remote workspace location
    "labels": "yandex",  # Space separated labels string
    "exclusive": True,  # Only run jobs assigned to it
}
new_jnlp_node = jenkins.nodes.create_node("My new webstart node", node_dict)
"""

node_dict = {
    "num_executors": 1,
    "node_description": "Test SSH Node",
    "remote_fs": "/home/jenkins",
    "labels": "yandex",
    "exclusive": True,
    "host": "10.129.0.14",  # Remote hostname
    "port": 22,  # Remote post, usually 22
    "credential_description": "jenkins",  # Credential to use
    # [Mandatory for SSH node!]
    # (see Credentials example)
    "jvm_options": "-Xmx2000M",  # JVM parameters
    "java_path": "/bin/java",  # Path to java
    "prefix_start_slave_cmd": "",
    "suffix_start_slave_cmd": "",
    "max_num_retries": 0,
    "retry_wait_time": 0,
    "retention": "Always",  # Change to 'Always' for
    # immediate slave launch
    "ondemand_delay": 1,
    "ondemand_idle_delay": 5,
}
new_ssh_node = jenkins.nodes.create_node("My new SSH node", node_dict)

# Take this slave offline
if new_ssh_node.is_online():
    new_ssh_node.toggle_temporarily_offline()

    # Take this slave back online
    new_ssh_node.toggle_temporarily_offline()

# Get a list of all slave names
slave_names = jenkins.nodes.keys()
