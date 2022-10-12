# Max damage in Valorant using Dynamic

total_damage = 200

primary_guns = {
    "stringer": [67, 27, 22, 62, 25, 21],
    "spectre": [78, 26, 22, 66, 22, 18],
    "bucky": [40, 20, 17, 26, 13, 11, 18, 9, 7],
    "judge": [34, 17, 14, 20, 10, 8, 14, 7, 5],
    "bulldog": [115, 35, 29],
    "guardian": [195, 65, 48],
    "phantom": [156, 39, 33, 140, 35, 29, 124, 31, 26],
    "vandal": [160, 40, 34],
    "marshal": [202, 101, 85],
    "operator": [255, 150, 120],
    "ares": [72, 30, 25, 67, 28, 23],
    "odin": [95, 38, 32, 77, 31, 2],
    "classic": [78, 26, 22, 66, 22, 18],
    "shorty": [24, 21, 10, 16, 8, 6, 6, 3, 2],
    "frenzy": [78, 26, 22, 63, 21, 17],
    "ghost": [105, 30, 25, 87, 25, 21],
    "sheriff": [159, 55, 46, 145, 50, 42]
}

secondary_guns = {
    "classic": [66, 22, 18],
    "shorty": [16, 8, 6],
    "frenzy": [63, 21, 17],
    "ghost": [87, 25, 21],
    "sheriff": [145, 50, 42]
}

file = open("valo_damage_200.txt", "w")

# Data fetching

for gun in primary_guns.keys():
    print("Gun: " + gun)
    damage_list = primary_guns[gun]
    damage_list.append(0)
    
    damage_tuple = list(set(damage_list))
    damage_tuple.sort()
    # print(damage_tuple)
    # _ = input()

    main_table = []

    # Dummy Data

    for i in range(len(damage_tuple)):
        temp_list = []
        for j in range(total_damage + 1):
            temp_list.append(-1)
        main_table.append(temp_list)

    for i in range(len(damage_tuple)):
        for j in range(total_damage + 1):
            if(i == 0):
                main_table[i][j] = 0
            elif(j == 0):
                main_table[i][j] = 1
            elif(damage_tuple[i] > j):
                main_table[i][j] = main_table[i-1][j]
            else:
                # main_table[i][j] = max(main_table[i-1][j], main_table[i-1][j-damage_tuple[i]] + damage_tuple[i])
                main_table[i][j] = main_table[i-1][j] + main_table[i][j - damage_tuple[i]]


    # Printing Main table

    for i in range(len(damage_tuple)):
        for j in range(total_damage + 1):
            print(main_table[i][j], end=" ")
        print()

    # Printing the solution in file

    file.write("Gun: " + gun + "\n")
    file.write("Damage Tuple: " + str(damage_tuple) + "\n")
    
    for i in range(total_damage + 1):
        file.write(str(i) + "\t")
    file.write("\n")
    for i in range(len(damage_tuple)):
        for j in range(total_damage + 1):
            file.write(str(main_table[i][j]) + "\t")
        file.write("\n")
    # file.write(str(main_table[len(damage_tuple)-1][total_damage]))
    
file.close()



# damage_list = [0]

# for i in primary_guns:
#     damage_list.append(i[1])
#     damage_list.append(i[2])
#     damage_list.append(i[3])

# damage_list.sort()
# # print(damage_list)
# # _ = input()
# damage_tuple = tuple(damage_list)

# # Dynamic Table

# main_table = []

# # Dummy Data

# for i in range(total_damage + 1):
#     temp_list = []
#     for j in range(len(damage_tuple)):
#         temp_list.append(-1)
#     main_table.append(temp_list)

# # Actual Data

# # for i in range(len(damage_tuple)):
# #     for j in range(total_damage + 1):
# #         if(i == 0):
# #             main_table[i][j] = 0
# #         elif(j == 0):
# #             main_table[i][j] = 1
# #         elif(damage_tuple[i] > j):
# #             main_table[i][j] = main_table[i-1][j]
# #         else:
# #             # main_table[i][j] = max(main_table[i-1][j], main_table[i-1][j-damage_tuple[i]] + damage_tuple[i])
# #             main_table[i][j] = main_table[i-1][j] + main_table[i][j - damage_tuple[i]]

# # Considering the value of 1 for every item

# # for i in range(len(damage_tuple)):
# #     for j in range(total_damage + 1):
# #         if(i == 0 or j == 0):
# #             main_table[i][j] = 0
# #         elif(damage_tuple[i-1] < total_damage):
# #             # main_table[i][j] = max(damage_tuple[i-1] + main_table[i-1][j - damage_tuple[i-1]], main_table[i-1][j])
# #             main_table[i][j] = max(1 + main_table[i-1][j - damage_tuple[i-1]], main_table[i-1][j])
# #         else:
# #             main_table[i][j] = main_table[i-1][j]

# # GFG Solution

# for i in range(total_damage + 1):
#     for j in range(len(damage_tuple)):
#         print("I : ", i, "\tJ : ", j)
#         # Count of solutions including S[j]
#         x = main_table[i - damage_tuple[j]][j] if i-damage_tuple[j] >= 0 else 0

#         # Count of solutions excluding S[j]
#         y = main_table[i][j-1] if j >= 1 else 0

#         # total count
#         main_table[i][j] = x + y


# # Printing Main table

# for i in range(total_damage + 1):
#     for j in range(len(damage_tuple)):
#         print(main_table[i][j], end=" ")
#     print()

# # Printing the solution in file

# file = open("valo_damage.txt", "w")
# file.write(str(main_table[len(damage_tuple)-1][total_damage]))
# file.close()