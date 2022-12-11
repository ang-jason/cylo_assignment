

import boto3
import pprint
import revoke_sg_rule_id_func
import json
from helper_func import create_pairs_from_dict as create_pairs_from_dict
from helper_func import OUTPUT_SEC_ID_TXT_FILE


try:
    # reading the data from the file
    with open(OUTPUT_SEC_ID_TXT_FILE) as f:
        data_str = f.read()

    if len(data_str) <= 2:
        print("Text file is {}!", len(data_str))
        exit()
    else:
        print("Text file not empty!",  len(data_str))

        # print(data_str, type(data_str))
        # Outputs of the txt file is str to convert to dict back to pairs arrangement
        file_dict_sc_id_to_check = json.loads(data_str)
        # print(file_dict_sc_id_to_check, type(file_dict_sc_id_to_check))

        pairs=create_pairs_from_dict(file_dict_sc_id_to_check)

        for pair in pairs:
            # print(pair)
            print(pair[0],pair[1])
            
            ### this will call the function to revoke the security group rule
            res =revoke_sg_rule_id_func.revoke_sg_rule_id_func(pair[0],pair[1])
            print(pair[0],pair[1], res)
except FileNotFoundError:
    print("File not found. Check the path variable and filename")
    exit()