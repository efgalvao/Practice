def turnOffTheLights(k, c):
    len_c = len(c)
    x = k
    if len_c <= k:
        return min(c)
    soma = 0
    while x < (len_c - 1):
        soma += c[x]
        x += 2 * k + 1
        if x >= len_c and (x - k) <= len_c:
                soma += c[-1]
    return soma


teste = [1,1,1,1,1,1,1,1,1,1,1,1,1]
teste2 = [9900, 1369, 28799, 3450, 32629, 25131, 5577, 5793, 29744, 25007, 21344, 10675, 22197, 26924, 10495, 30924, 15554, 29501, 13162, 18422, 19274, 32211, 29276, 27466, 19472, 6521, 10944, 28761, 16757, 32220, 14627, 30410, 27790, 18314, 26730, 31812, 31098, 17146, 8384, 8078, 17907, 26829, 723, 7924, 30242, 28499, 17216, 5613, 19384, 5457, 23115, 15868, 29498, 2561, 23508, 14036, 15260, 5723, 2951, 6591, 27666, 27539, 338, 23616, 11299, 15075, 29212, 17911, 12799, 31370, 28852, 32198, 11026, 31765, 15111, 29234, 4825, 14301, 26519, 8460, 27637, 29137, 1832, 592, 3966, 7029, 3772, 6733, 1689, 5931, 7618, 30470, 8781, 16562, 29835, 7385, 17810, 24300, 12029, 9822, 5547, 25316, 6027, 7058, 1206, 6159, 9829, 17461, 27266, 10706, 235, 31088, 8096, 8773, 3432, 15035, 20157, 17975, 28413, 2558, 28719, 29298, 32219, 21238, 9165, 24127, 4021, 25051, 23812, 26413, 9334, 11584, 5415, 18959, 19247, 30522, 30727, 27972, 21331, 2500, 16068, 8251, 7718, 4706, 11490, 29749, 9331, 24837, 25503, 4685, 1149, 3631, 32644, 12982, 11321, 19543, 13371, 6469, 29626, 26767, 23200, 15151, 15341, 15972, 9498, 29203, 25990, 8966, 28204, 24635, 13370, 2985, 21831, 27167, 29231, 29482, 7651, 26922, 26545, 17142, 1230, 31681, 31526, 17192, 32707, 5762, 3396, 22001, 6974, 15049, 25985, 573, 27279, 30329, 17099, 4499, 15917, 4345, 25722, 17725, 5198, 2428, 8067, 26282, 30644, 19078, 21486, 14096, 16586, 13996, 22154, 597, 27887, 29339, 8927, 22832, 18, 4187, 26980, 13964, 9343, 32725, 19954, 5165, 31992, 26771, 27257, 12949, 23816, 20680, 27122, 6185, 23444, 13712, 20372, 2960, 29619, 30840, 15947, 3420, 10176, 17985, 21606, 5356, 23213, 23265, 28559, 5264, 21401, 18123, 27905, 2287, 8101, 6512, 14837, 6054, 17924, 5382, 18525, 306, 594, 20360, 15317, 27152, 31015, 25854, 25303, 16162, 6891, 7934, 20526, 14677, 10476, 13683, 10413, 17537, 4269, 3229, 31008, 19857, 4482, 5209, 10371, 15331, 24665, 11427, 23154, 6642, 15835, 13145, 21985, 12594, 12980, 8001, 17421, 7483, 26158, 19534, 23474, 6698, 17157, 23839, 19583, 4676, 24183, 21961, 32455, 11997, 21914, 21462, 31609, 28793, 5362, 1934, 4178, 4656, 15939, 21109, 1105, 15447, 8356, 12052, 28780, 19036, 30421, 17916, 4225, 10226, 24530, 21513, 8335, 2414, 17832, 17892, 6694, 881, 9864, 11467, 26140, 17864, 29722, 28821, 22146, 32144, 32019, 25328, 31958, 8862, 5386, 6126]

#print(turnOffTheLights(1, teste))
print(turnOffTheLights(11, teste2))
resultado_teste2 = 222957


#def spliit(t):
#    return int(t.split(' '))

#print(spliit(teste2))