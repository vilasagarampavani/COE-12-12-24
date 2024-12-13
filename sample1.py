project  = int (input('Enter the project score:'))
internal = int (input('Enter the internal score:'))
external = int (input('Enter the extrenal score:'))
if project >=50 and internal >=50 and external >=50 :
    total = ((70 * project)  + (10 * internal)  + (20 * external) )/ 100
    if total >90 :
       print('Grade = A')
    elif total >80 and total <90:
       print('Grade = B')
    elif total > 80 and total < 50:
       print('Grade = C')
else :
    print('Failed')
    if project < 50 :
        print('u failed in intrnal and project:')
    if internal < 50 :
        print('u falied in internal and external')
    if external <50:
        print('u falied in project and external')


