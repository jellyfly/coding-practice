#/usr/bin/python


# --- test package path import ---

# case 1
import module.Print

module.Print.print_results()

# case 2
from module import Print

Print.print_results()

# case 3
from module.Print import print_results

print_results()


# --- test class methods import ---

#from Print import Print

#print_test = Print()
#print_test.print_result()




# --- test direct def import ---
#import Print

#Print.print_outside()
