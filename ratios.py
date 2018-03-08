#documentation of sources used:
#Multilevel sorting: https://stackoverflow.com/questions/22709310/why-multilevel-sort-using-sorted-function-in-python-get-the-wrong-answer
#                    https://docs.python.org/3/howto/sorting.html
#General reference: https://docs.python.org/2/library/functions.html#cmp (looked up multiple times for reference)
#                   http://portingguide.readthedocs.io/en/latest/dicts.html


d = {1: 1, 2: 1, 3: 1}
portion = 11

def get_ratios(d, portion):
    """Function that caclulates ratios of food type based on portions:
        >>> get_ratios({},1)
        {}

        >>> get_ratios({1: 1}, 2)
        {1: 2}

        >>> get_ratios({1: 1}, 0)
        {1: 0}

        >>> get_ratios({1: 1, 2: 1, 3: 1}, 11)
        {1: 4, 2: 4, 3: 3}

        >>> get_ratios({1: 1, 2: 2, 3: 1}, 11)
        {1: 3, 2: 6, 3: 2}
    """
    #handle edge case
    if len(d.keys())==0:
        return {}
    lst = []
    #add all the vals together to get a total
    total = sum(d.values())


    for key in d.keys():
        val = d.get(key)
        #divide each dict value from the sum of all values to get fraction
        frac = val / float(total)
        #multiply fraction by portion amount
        result = frac * portion
        #round to whole number
        rounded = int(result)
        #get remainder
        remainder = result - rounded
        #append tuple to list
        lst.append( (key, rounded, remainder))

    #add all [1] from tuple to get whole number
    add_vals = sum([item[1] for item in lst])
    #subtract whole from portion to get whole number remainder
    w_remainder = portion - add_vals
    #sort by remainder using comparator function

    #I'm fairly certain there are more elegant ways to handle multilevel sorting
    #but I had a tough time wraping my head around this part so I used the most
    #obvious/intuitve (to me) method.
    def comparator(a,b):
        if a[2]>b[2]:
            return 1
        elif a[2]<b[2]:
            return -1
        elif a[2]==b[2]:
            if a[0]==b[0]:
                return 0
            elif a[0]>b[0]:
                return 1
            elif a[0]<b[0]:
                return -1

    srt = sorted(lst, cmp=comparator)
    #set up results dict using indices from list of sorted tuples
    portions = dict([(item[0],item[1]) for item in srt])
    #dole out remaining portions
    for i in range(w_remainder):
        key = srt[i][0]
        portions[key] +=1

    return portions
