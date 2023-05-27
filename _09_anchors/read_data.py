import yaml

my_file = "anchor_2.yml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)
        
        for key, value in data.items():
            if key in ["server1", "server2"]:
                print("\n----")
                for k, v in value.items():
                    print(f"{k}: {v}")
                print("\n----\n")

                    
    except yaml.YAMLError as err:
        print(err)