def pick_peaks(arr):
    #your code here
    pos=[]
    peaks=[]
    if len(arr) >2:
        for i in range(1,len(arr)-1):
        	if arr[i-1] < arr[i] and arr[i] >= arr[i+1] and arr[i] !=min(arr[i+1:]) :
        		pos.append(i)
        		peaks.append(arr[i])
    if len(pos) >1:
        for i in range(0,len(pos)-1):
        	if arr[pos[i]] <= min(arr[pos[i]:pos[i+1]]):
        		pos.pop(i)
        		peaks.pop(i)
    return {"pos": pos,"peaks":peaks}
# answer
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
a = pick_peaks([])
print(a)
