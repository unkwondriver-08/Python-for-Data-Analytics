subject =[ 'chemsity', 'phys', 'bio']

course_str = ' - '.join(subject)
print(course_str)
course_str = ' ,'.join(subject)
print(course_str)

#given a separted item, then make a list out of it

new_list =course_str.split(' ,')
print(new_list)