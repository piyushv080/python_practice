import json 

#Json String
employee = '{"id":"01","name":"piyush","department":"IT"}'

#Converting string to python dict
employee_dict = json.loads(employee)
print(employee_dict)

print(employee_dict['name'])

#read json file
f = open('data.json',)

data = json.load(f)

for i in data['emp_details']:
    print(i)

f.close()