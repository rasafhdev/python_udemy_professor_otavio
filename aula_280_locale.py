import locale
import calendar


locale.setlocale(locale.LC_ALL, 'pt_BR')
locale.setlocale(locale.LC_ALL, 'pt_BR.ut6')

print(calendar.calendar(1996))