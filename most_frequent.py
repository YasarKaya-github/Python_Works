def most_freq(given_list):
    return(max(given_list,key=given_list.count))
print(most_freq([1,3,2,5,6,4,4,4,4]))