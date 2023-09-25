from TimedIterator import TimedIteratorCoR as cow
print(help(cow))
ti = cow().get_object(5)
for i in ti:
    print(i+21)
