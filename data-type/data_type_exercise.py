from datetime import datetime

birth_year = int(input('What year were you born? '))
print(f'Your age is : {datetime.now().year - birth_year}')