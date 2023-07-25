'''def count_names(names):
    return len(names)

names = ["John doe", 'Gwen stacy','Fret gary', "Hillary Po", 'Mary John - smith', 'Timi Emmanuel - Ipo']
total_names = count_names(names)
print("Number of names:", total_names)

def first_names(names):
   first_names = [name.split(' ')[0] for name in names]
   return first_names

first_names_only = first_names(names)
print('First names:', first_names_only )



def second_names(names):
   second_names = [name.split('  ')[-1] for name in names]
   return second_names

second_names_only = second_names(names)
print('Second names: ', second_names_only)
'''
   




names = ['Mark James', 'Fiona Ram', 'Ham Upt', 'Kin Opp', "Gon Freecs"]
count = len(names)
first_names=[]
second_names=[]


def process_names(names):
   for names in names:
       first_names.append(names.split(' ')[0])
       second_names.append(names.split(' ')[1])

process_names(names)
print(count, first_names, second_names)