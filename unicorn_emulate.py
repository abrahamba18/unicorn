from __future__ import print_function
from unicorn import *
from unicorn.x86_const import *

# code to be emulated
X86_CODE32 = b"\xB8\x00\x00\x00\x00\x8D\x50\x01\x89\xD0\xC1\xF8\x1F\xC1\xE8\x18\x01\xC2\x0F\xB6\xD2\x29\xC2\x89\xD0" # INC ecx; DEC edx

# memory address where emulation starts
ADDRESS = 0x1000000

print("Emulate i386 code")
# Initialize emulator in X86-32bit mode
mu = Uc(UC_ARCH_X86, UC_MODE_32)

# map 2MB memory for this emulation
mu.mem_map(ADDRESS, 2 * 1024 * 1024)

# write machine code to be emulated to memory
mu.mem_write(ADDRESS, X86_CODE32)

# initialize machine registers
#mu.reg_write(UC_X86_REG_ECX, 0x1234)
#mu.reg_write(UC_X86_REG_EDX, 0x7890)
#mu.reg_write(UC_X86_REG_EAX, 0x0)


# emulate code in infinite time & unlimited instructions
mu.emu_start(ADDRESS, ADDRESS + len(X86_CODE32))

# now print out some registers
print("Emulation done. Below is the CPU context")
#
#r_ecx = mu.reg_read(UC_X86_REG_ECX)
r_edx = mu.reg_read(UC_X86_REG_EDX)
r_eax = mu.reg_read(UC_X86_REG_EAX)
#print(">>> ECX = 0x%x" %r_ecx)
print(">>> EDX = 0x%x" %r_edx)
print(">>> EAX = 0x%x" %r_eax)
