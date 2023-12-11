# HR_SYSTEM
# name id_number job_title salary

# with open("hr_system.txt") as line:
#     for name in line:

#         parts = name.split(" ")

#         people_name = parts[0]
#         id = parts[1]
#         job_title = parts[2]
#         salary = float(parts[3])

#         # unit value of salary paid twice a month
#         salary_amount = float(salary / 24)

#         # add a bonus for every Engineer
#         if job_title.lower() == 'engineer':
#             bonus_salary = float(salary_amount + 1000)
#             salary = float(bonus_salary)

#         salary = float(salary_amount)

#         print(f"{people_name} - (ID:{id}), {job_title} - ${'%.2f' % salary}")

# BOOKS

# with open("books.data") as book:
#     for author in book:
#         author_book = author.strip()

#         print(author_book)

# line = "     text"

# strip_line = line.strip()

# print(strip_line)