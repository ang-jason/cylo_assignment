



def helloworld():
    hello='hello-world'
    return hello



def revoke_sg_rule_id_func(GroupId_id,SecurityGroupRuleIds_id):

    import boto3
    ## can customised to which profile name, which region and etc.
    session=boto3.Session(profile_name="jasondevtools", region_name="ap-southeast-1")
    ec2_cli=session.client(service_name="ec2")
    
    print("removing...")
    # this is the revoke the security group rule from the ec2.
    return_reponse=ec2_cli.revoke_security_group_ingress(

       GroupId=GroupId_id,
       SecurityGroupRuleIds=[SecurityGroupRuleIds_id]
    )

    return return_reponse['Return']