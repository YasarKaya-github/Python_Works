def my_min(*x):
    min=x[0]
    for i in x:
        if i<min:
            min=i
    return(min)
