fruits1 = ['лемон', 'апельсин', 'ананас', 'банан', 'дыня', 'груша']
fruits2 = ['апельсин', 'грейпфрут', 'банан', 'яблоко', 'груша', 'кокос', ]

commonFruits = [fruit for fruit in fruits1 if fruit in fruits2]
print(commonFruits)
