"""
Let's use decorators to build a name directory!
You are given some information about N people.
Each person has a first name, last name, age and sex.
Print their names in a specific format sorted by their age in ascending order
i.e. the youngest person's name should be printed first.
For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:
Mr. Henry Davids

For Mary George, the output should be:
Ms. Mary George

Input Format

The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name,
last name, age and sex, respectively.

Constraints
1<= N <= 10

Output Format
Output N names on separate lines in the format described above in ascending order of age.

Sample Input
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""
import operator


def person_lister(f):
    def inner(people):
        items = [[fn, ln, int(age), gen] for fn, ln, age, gen in people]
        items.sort(key=operator.itemgetter(2))
        return [f(item) for item in items]
        # return map(f, sorted(people, key=lambda p: int(p[2])))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    data = ['Mike Thomson 20 M', 'Robert Bustle 32 M', 'Andria Bustle 30 F', 'Ana Bolei 12 F', 'Xavier Argus 12 M']
    people = [x.split() for x in data]
    print(*name_format(people), sep='\n')
