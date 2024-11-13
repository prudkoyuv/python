from datetime import datetime

s1 = 'Wednesday, October 2, 2002'
s2 = 'Friday, 11.10.13'
s3 = 'Thursday, 18 August 1977'


def f(n):
    s = input()
    try:
        return datetime.strptime(s, '%A, %B %d, %Y')
    except:
        try:
            return datetime.strptime(s, '%A, %d.%m.%y')
        except:
            try:
                return datetime.strptime(s, '%A, %d %B %Y')
            except:
                return f()


print(f(input()))
