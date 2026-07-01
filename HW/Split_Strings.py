customers = "Alice Johnson;98653263,Catherine Lee;89653215,Johnson Lam;95321453,Brandon Tan;81234567,Emily Wong;92345678,Hafiz Zaid;85678912,Isabelle Ng;96541234,Ken Lim;97865432,Noraini Ahmad;88776655,Samuel Chan;90123456"

# Part 1
customer_list = customers.split(",")

print(customer_list)

# Part 2
customer_dict = {}

for record in customer_list:
    data = record.split(";")
    name = data[0]
    phone = int(data[1])
    customer_dict[name] = phone

print(customer_dict)