person = {
    'first_name':'John',
    'last_name':'smith',
    'age':'45',
    'address':{
        'street':'1334 Brittmore',
        'city':'Houston',
        'state':'TX'
    }
}

person_address = person['address']
person_street = person_address['street']

print(person_street)