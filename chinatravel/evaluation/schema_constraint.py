
import sys

# from chinatravel.environment.tools.accommodations.apis import Accommodations
# from chinatravel.environment.tools.restaurants.apis import Restaurants
# from chinatravel.environment.tools.attractions.apis import Attractions
# from chinatravel.environment.tools.intercity_transport.apis import IntercityTransport
# from chinatravel.environment.tools.transportation.apis import Transportation
# from env.tools.transportation.apis import GoTo
# from envs import goto
import json
import os
import sys
from tqdm import tqdm

    
import pandas as pd

import json
import jsonschema
from jsonschema import validate

def validate_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        # raise e
        # print(e)
        return False

def evaluate_schema_constraints(data_index, plan_json_dict, schema):
    # assert len(symbolic_input_list)==len(plan_json_list)
    
    total_correct = 0
    result_agg = pd.DataFrame(columns=['data_id', "schema"])
    result_agg['data_id'] = data_index

    pass_id = []

    for ii, idx in tqdm(enumerate(data_index), total=len(data_index)):

        plan_json = plan_json_dict[idx]  
        
        # print(idx)

        succ_flag = 0
        try:        
            if validate_json(plan_json, schema):
                succ_flag = 1
                pass_id.append(idx)
        except Exception as e:
            print(idx, e)
            pass
        

        result_agg.loc[ii, "schema"] = succ_flag
        total_correct += succ_flag

    total_count=len(data_index)

    return 1. * total_correct / total_count*100, result_agg, pass_id

if __name__ == "__main__":
    
    
    
    from evaluation.utils import load_json_file
    # test_example=load_json_file("./example/query_53.json")
    # test_plan=load_json_file("./example/plan_53.json")
    # evaluate_commonsense_constraints([test_example], [test_plan])
    
    # exit(0)
    
    symbolic_input_list=[]
    plan_json_list=[]

    for i in range(1):
        test_plan_path='./example/a_result.json'.format(i+1)
        test_example_path='./example/a_query.json'.format(i+1)
        test_example=load_json_file(test_example_path)
        test_plan=load_json_file(test_plan_path)
        symbolic_input_list.append(test_example)
        plan_json_list.append(test_plan)
    macro_accuracy, micro_accuracy, _ =evaluate_commonsense_constraints(symbolic_input_list,plan_json_list)
    print('macro: {}%, micro: {}%'.format(macro_accuracy,micro_accuracy))

    # test_plan_path='./example/plan_4.json'
    # test_example_path='./example/query_4.json'
    # test_example=load_json_file(test_example_path)
    # test_plan=load_json_file(test_plan_path)

    # print(Is_intercity_transport_correct(test_example,test_plan))
    # print(Is_attractions_correct(test_example,test_plan))
    # print(Is_hotels_correct(test_example,test_plan))
    # print(Is_restaurants_correct(test_example,test_plan))
    # print(Is_transport_correct(test_example,test_plan))
    # print(Is_time_correct(test_example,test_plan))
    # print(Is_space_correct(test_example,test_plan))

    
    # pass_flag = True

    

    # info_list = []
    # for func_i in func_list:
    #     flag, info = func_i(test_example,test_plan)

    #     print(info)

    #     pass_flag = pass_flag and flag
    #     info_list.append(info)

    # print("final result: ", pass_flag)
    
    # for item in info_list:
    #     print(item)
    # print(info_list)

