import yaml

my_file = "multi-doc.yaml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.load_all(stream, Loader=yaml.SafeLoader)
        count = 0
        for yamlDoc in data:
            doc_no = count + 1
            print(f"< < < <  Yaml Document {doc_no} > > > >")
            print(yamlDoc)
            for key, value in yamlDoc.items():
                print(f"KEY : {key}")
                print(f"VALUE : {value}")
                dt = type(value)
                print(f"Data type od {value} is {dt}")
            count+=1
    except yaml.YAMLError as err:
        print(err)