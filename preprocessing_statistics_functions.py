def num_words(text):
    count = 0
    for i in text:
        count = count + len(i)
    return count

def count_aoc(text):
    value = 0
    acc1 = '@AOC'
    acc2 = '@RepAOC'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_mtg(text):
    value = 0
    acc1 = '@mtgreenee'
    acc2 = '@RepMTG'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_gaetz(text):
    value = 0
    acc1 = '@mattgaetz'
    acc2 = '@RepMattGaetz'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_cruz(text):
    value = 0
    acc1 = '@tedcruz'
    acc2 = '@SenTedCruz'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_harris(text):
    value = 0
    acc1 = '@KamalaHarris'
    acc2 = '@VP'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_buttigieg(text):
    value = 0
    acc1 = '@PeteButtigieg'
    acc2 = '@SecretaryPete'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_boebert(text):
    value = 0
    acc1 = '@laurenboebert'
    acc2 = '@RepBoebert'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def count_booker(text):
    value = 0
    acc1 = '@CoryBooker'
    acc2 = '@SenBooker'
    if acc1 in text:
        value = 1
    if acc2 in text:
        value = 1
    return value

def single_mention(number):
    boolean = True
    if number > 1:
        boolean = False
    return boolean
