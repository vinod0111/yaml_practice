import yaml

my_file = "basic-structure-2.yaml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            
            print(f"---")
            print(f"VALUE : {value}")
            print(f"----------------")
            
    except yaml.YAMLError as err:
        print(err)