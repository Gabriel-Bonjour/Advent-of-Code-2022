

with open("01/input.txt", 'r') as input_file :
   global_inventory = input_file.readlines()
   wealthier_elf = 0
   wealthier_stash = 0
   current_elf_s_stash = 0
   current_elf = 0
   
   for food in global_inventory :
      if food != "\n" :
         current_elf_s_stash += int(food)
      else :
         print("debug3")
         if current_elf_s_stash > wealthier_stash :
            print("debug4")
            wealthier_elf = current_elf
            wealthier_stash = current_elf_s_stash
         current_elf_s_stash = 0
         current_elf += 1
   if current_elf_s_stash > wealthier_stash :
      wealthier_elf = current_elf
      wealthier_stash = current_elf_s_stash
   
   print(wealthier_stash)