# cylo_assignment
# Problem 1


# Problem 2

## Automation Code
```python
## main code
problem2_01_scan.py
problem2_02_revoke.py


## helper functions
revoke_sg_rule_id_func.py
helper_func.py
```

## Demonstration
The script revoke security group rules based attached intances and running.
AWS allows flexibility tagging of security groups and security groups rules.
The assumption here is that there are multiple security rules in a group and "specific" tags only happen on the individual rules level. 

Special tag: key:value = 'GROUP_RULES_ID_TAG':'JASON'

Further assumption that the AWS configure and IAM group have been given correctly to perform require actions and the regions ```ap-southeast-1``` is being selected but it can be extensible to other regions.

Scanning filter based on "Inbound 0.0.0.0/0 on port 22"

Revoking based on the security group can also be adjusted.

### Execution Steps
Ideally, all the scripts could be run in automatically. ```problem2_01_scan.py``` followed by ```problem2_02_revoke.py```, brokening down was done intentionally for easy troubleshooting and considerations of operational requirements (e.g. separate IAM policies or separation of roles/privileges)

#### problem2_01_scan.py
After running the script, a text file is produced with the results of the security groups rules and its associated security rules which were ```Inbound 0.0.0.0/0 on port 22```. The text file could also serve as a logging feature for inputs to other aggregated dashboards.

```problem2_01_scan.py``` Results
![](https://github.com/ang-jason/cylo_assignment/blob/main/images/scanned_results.png?raw=true)


#### Test Cases
Test cases were setup with terraform to spin up an instances with 4 security groups

**4 PORT 22 (3 tcp and 1 udp)**
- allow_ssh_tcp_udp of port 22 tcp and udp
- allow_ssh_good of port 22 tcp **[special tag]**
- allow_https_ssh of port 443 tcp, 22 tcp
- allow_http of port 80 tcp
![](https://github.com/ang-jason/cylo_assignment/blob/main/images/terraform_test.png?raw=true)

Unfortunately, terraform could not tag individual security group rules at the rules level. (https://github.com/hashicorp/terraform-provider-aws/issues/20104)

Therefore after spinning up from with terraform

![](https://github.com/ang-jason/cylo_assignment/blob/main/images/security_groups_test.png?raw=true)

Manually to add tags(can be further refine with aws cli)

![](https://github.com/ang-jason/cylo_assignment/blob/main/images/tag_test.png?raw=true)

Using aws cli (https://aws.amazon.com/blogs/aws/easily-manage-security-group-rules-with-the-new-security-group-rule-id/) announced on 07 JUL 2021

With the above screenshots to notice the "good" rule id
```
aws ec2 create-tags                         \
        --resources sgr-abcdefghi01234561   \
        --tags "Key=GROUP_RULES_ID_TAG,Value=JASON"

```


Based on the Test cases setup, **3 rules to be remove**

#### problem2_02_revoke.py
After executing the scripts, 3 rules were remove, remaining ```Inbound 0.0.0.0/0 on port 22``` with special tag. In production-ready, a new main script to bundle 2 scripts together and run sequentially. 

![](https://github.com/ang-jason/cylo_assignment/blob/main/images/revoke_results.png?raw=true)


With a lightweight server of AWS cli installed, and python, the scripts could be called routinely with the cron-job. More to be improved with logging activities and time data to be equipped on the status of these running scripts.