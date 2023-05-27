import yaml

my_file = "tag_1.yml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)
        
        for key, value in data.items():

            print(f"{key} : {value}")
            print(f"{type(value)}")

                    
    except yaml.YAMLError as err:
        print(err)