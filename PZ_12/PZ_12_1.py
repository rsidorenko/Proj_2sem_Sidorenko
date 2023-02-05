from random import randint
seq = [(randint(-10, 10)) for i in range(10)]
seq_plus = [i for i in seq if i > 0 and i % 2 == 0]
seq_summ = sum(seq_plus)
seq_av = seq_summ / len(seq_plus)
print(seq)
print(seq_plus)
print(seq_summ)
print(seq_av)
