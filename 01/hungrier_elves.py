

with open("01/input.txt", 'r') as input_file :
   global_inventory = input_file.readlines()
   wealthier_elves = [0, 0, 0]
   wealthier_stashes = [0, 0, 0]
   current_elf_s_stash = 0
   current_elf = 0
   
   for food in global_inventory :
      if food != "\n" :
         current_elf_s_stash += int(food)
      else :
         if current_elf_s_stash > wealthier_elves[0] :
            wealthier_elves.insert(0, current_elf)
            wealthier_elves.pop()
            wealthier_stashes.insert(0, current_elf_s_stash)
            wealthier_stashes.pop()
         elif current_elf_s_stash > wealthier_elves[0] :
            wealthier_elves.insert(1, current_elf)
            wealthier_elves.pop()
            wealthier_stashes.insert(1, current_elf_s_stash)
            wealthier_stashes.pop()
         elif current_elf_s_stash > wealthier_elves[0] :
            wealthier_elves.pop()
            wealthier_elves.append(current_elf)
            wealthier_stashes.pop()
            wealthier_stashes.append(current_elf_s_stash)
         current_elf_s_stash = 0
         current_elf += 1
   if current_elf_s_stash > wealthier_elves[0] :
      wealthier_elves.insert(0, current_elf)
      wealthier_elves.pop()
      wealthier_stashes.insert(0, current_elf_s_stash)
      wealthier_stashes.pop()
   elif current_elf_s_stash > wealthier_elves[0] :
      wealthier_elves.insert(1, current_elf)
      wealthier_elves.pop()
      wealthier_stashes.insert(1, current_elf_s_stash)
      wealthier_stashes.pop()
   elif current_elf_s_stash > wealthier_elves[0] :
      wealthier_elves.pop()
      wealthier_elves.append(current_elf)
      wealthier_stashes.pop()
      wealthier_stashes.append(current_elf_s_stash)
      
   print(wealthier_elves)
   print(sum(wealthier_stashes))