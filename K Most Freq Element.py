def most_k_freq_number(arr):
    freq_bucket = {}
    for i in len(arr):
        if freq_bucket[i] in None:
            freq_bucket[i] = arr[i]
        else:
            freq_bucket[i].append(arr[i])
