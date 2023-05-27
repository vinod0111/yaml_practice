import yaml

my_file = "sets_1.yml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            
            print(f"{key}: {value}")
            print("----")
            dt = type(value)
            print(f"Data type od {value} is {dt}")
            print("-----")

    except yaml.YAMLError as err:
        print(err)