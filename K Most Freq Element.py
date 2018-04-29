def most_k_freq_number(arr, k):
    freq_bucket = {}
    for i in range(len(arr)):
        if len(freq_bucket[i]) == 0:
            freq_bucket[i] = arr[i]
        else:
            freq_bucket[i].append(arr[i])
    s = 0

    if s < k:
        for i in range(len(freq_bucket), -1, 0):
            s += 1
            return(freq_bucket[i])
