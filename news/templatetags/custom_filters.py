import re
from django import template

register = template.Library()

verification_completed = {
    'official':'v',
    'non_official':'x'
}

@register.filter()
def verification(value, code='official'):
    verif = verification_completed[code]
    return f'{value} ({verif})'

CURSE_WORDS = ['список', 'матерных', 'слов', 'обзор']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        return value

    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in CURSE_WORDS) + r')\b', re.IGNORECASE)

    censored_value = pattern.sub(lambda match: '*' * len(match.group()), value)

    return censored_value




