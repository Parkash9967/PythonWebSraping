from bs4 import BeautifulSoup
import requests

print('put something that you dont want')
dislike_field = input('>')
print(f" flitring out {dislike_field}")

html_text = requests.get(
    'https://www.scholars4dev.com/').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='post clearfix')
for index, job in enumerate(jobs):
    name = job.find('div', class_='entry clearfix').find('h2').text
    university = job.find('div', class_='post_column_1').find('p').em.text
    program = job.find('div', class_='post_column_1').find('p').text
    sibling = job.find('div', class_='entry clearfix')
    more_info = job.h2.a['href']
    nextSiblings = sibling.find_all('p')
    # for discription in nextSiblings:
    if dislike_field not in program:
        with open(f'posts/{index}.text', 'w') as f:
            f.write(f"Job_name : {name.strip()} \n")
            f.write(f"job_university : {university.strip()} \n")
            f.write(f"job_program : {program.strip()} \n")
            f.write(f"more_info : {more_info} \n")
        print(f'file saved : {index}')
