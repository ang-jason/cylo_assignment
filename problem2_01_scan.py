
import boto3
import pprint
import revoke_sg_rule_id_func
from helper_func import add_to_dict as add_to_dict
from helper_func import OUTPUT_SEC_ID_TXT_FILE

SPECIAL_TAG_KEY='GROUP_RULES_ID_TAG'
SPECIAL_TAG_VALUE='JASON'



session=boto3.Session(profile_name="jasondevtools", region_name="ap-southeast-1")
ec2_cli=session.client(service_name="ec2")




security_groupId_to_check=[]
print("\nInstances Info with Client")
# to find each security group id associated with the instances
for each in ec2_cli.describe_instances()['Reservations']:
    # print(each)
    for each_in in each['Instances']:
        print(each_in['InstanceId'], each_in['State']['Name'])
        # print(each_in)
        if each_in['State']['Name'] == 'running':
            print(each_in['InstanceId'])
            for each_in_in in each_in['NetworkInterfaces'][0]['Groups']:
                print(each_in_in)
                print(each_in_in['GroupName'],each_in_in['GroupId'])
                security_groupId_to_check.append(each_in_in['GroupId'])

# Trigger point is attached security groups to the instances
print("\nsecurity_groupId_to_check[]")
for each in security_groupId_to_check:
    print("security_groupId_to_check",each)

#response = ec2_cli.describe_security_groups(GroupIds=security_groupId_to_check)
# pprint.pprint(response)


# SPECIAL TAGS: [{'Key': 'GROUP_RULES_ID_TAG', 'Value': 'JASON'}]
# ELSE is not SPECIAL TAGS

response = ec2_cli.describe_security_group_rules()
# pprint.pprint(response)

security_group_rulesId_to_check={}

counter=0

for each_groupId in security_groupId_to_check:
    for each in response['SecurityGroupRules']:
        # print(each)
        if each['GroupId']== each_groupId and each['ToPort']==22 and each['CidrIpv4']=='0.0.0.0/0' and each['GroupId']: #FromPort and ToPort
            print('ALL',each['GroupId'],each['SecurityGroupRuleId'],each['ToPort'],each['CidrIpv4'], each['Tags']) #CidrIpv6 
            if each['Tags']== []:
                counter+= 1
                print("DEBUG", counter,each['GroupId'],each['SecurityGroupRuleId'],each['ToPort'],each['CidrIpv4'], each['Tags']) #CidrIpv6 

                # repeat
                add_to_dict(security_group_rulesId_to_check,each['GroupId'],each['SecurityGroupRuleId'])

            elif each['Tags'][0]['Key'] != SPECIAL_TAG_KEY and each['Tags'][0]['Value'] != SPECIAL_TAG_VALUE :
                counter+= 1
                print("DEBUG",counter,each['GroupId'],each['SecurityGroupRuleId'],each['ToPort'],each['CidrIpv4'], each['Tags'][0]['Key'],':',each['Tags'][0]['Value'] ) #CidrIpv6 

                # repeat
                add_to_dict(security_group_rulesId_to_check,each['GroupId'],each['SecurityGroupRuleId'])
 


# each security group only allow 1 rule of 22 0.0.0.0 tcp / udp can add port 22 also.

# Trigger point is attached security groups RULES to revoke
print("\nsecurity_group_rulesId_to_check{}")
print(security_group_rulesId_to_check)





import json
with open(OUTPUT_SEC_ID_TXT_FILE, 'w+') as convert_file:
    convert_file.write(json.dumps(security_group_rulesId_to_check))

