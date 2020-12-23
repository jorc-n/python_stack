print("---------------------------------------")
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
def actualiza_valores():
    z = [{'x': 10, 'y': 20}]
    x[1][0]=15
    print(x)
    students[0]['last_name']="Bryant"
    print(students)
    sports_directory['soccer'][0]="Andrés"
    print(sports_directory)
    z[0]['y']=30
    print(z)

actualiza_valores()

print("---------------------------------------")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for x in range(len(students)):
        for key, val in students[x].items():
            print(key," = ", val)

iterateDictionary(students)

print("---------------------------------------")

def iterateDictionary2(key_name, some_list):
    for x in range (len(some_list)):
        print(some_list[x][key_name])
iterateDictionary2 ('first_name', students)
print()
iterateDictionary2 ('last_name', students)

print("---------------------------------------")

dojos = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojos):
    for dojo in dojos:
        print(len(dojos[dojo]), dojo)
        for posicion in range(len(dojos[dojo])):
            print(dojos[dojo][posicion])

printInfo(dojos)

print("---------------------------------------")
