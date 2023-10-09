def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatls = []
    def ihatemyself(l):

    for n in list:
        if type(n) == list:
            ihatemyself(n)
        else:
            flatls.append(n)
