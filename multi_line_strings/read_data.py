import yaml

my_file = "multi_line_4.yml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)

        for key, value in data.items():
            if key == "dc1":
                for k, v in value.items():  
                    if k == "note1":    
                        print(f"{k}: {v}")
                        print("---------")  
                    if k == "note2":    
                        print(f"{k}: {v}")  

    except yaml.YAMLError as err:
        print(err)