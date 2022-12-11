

OUTPUT_SEC_ID_TXT_FILE='list_of_security_id.txt'


def add_to_dict(the_dict,item_groupId, itemgroupRuleId):
    
    if (item_groupId) in the_dict:
        the_dict[item_groupId].append(itemgroupRuleId)
    else:
        the_dict[item_groupId]=[itemgroupRuleId]
    
    return the_dict


def create_pairs_from_dict(the_dict):

# Iterate over a dictionary with list values and create
# a pair of all key-value pairs.
    pairs = [   (key, value) 
            for key, values in the_dict.items() 
            for value in values ]
    # for pair in pairs:
        # print(pair)
        
    return pairs