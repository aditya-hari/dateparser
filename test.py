import dateparser
print(dateparser.parse('after 15 days'))
'''
WEEKDAYS_TOKENS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                    'saturday', 'sunday'] 
MONTHS_TOKENS = ['january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november',
                'december']
OTHER_TOKENS = ['year', 'month', 'week', 'day', 'hour', 'minute', 'second',
                 'ago', 'in', 'am', 'pm']
KNOWN_WORD_TOKENS = WEEKDAYS_TOKENS+MONTHS_TOKENS+OTHER_TOKENS
MODIFIERS = ['next','last']

MODIFIED_PATTERN = re.compile(r'(?:%s)\s+(?:%s)'%('|'.join(MODIFIERS), '|'.join(WEEKDAYS_TOKENS+MONTHS_TOKENS)))
'''