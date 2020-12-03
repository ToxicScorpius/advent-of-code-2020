from day3_function import check_trees

p1, p2, p3 = check_trees(1, 1), check_trees(3, 1), check_trees(5, 1)
p4, p5 = check_trees(7, 1), check_trees(1, 2)
product = p1 * p2 * p3 * p4 * p5
print(product)
