.text
.globl main

main:
    li $t0, 0  # sum
    li $t1, 0  # i
    li $t2, 10 # 10
    li $t3, 1  # 1

loop:
    bge $t1, $t2, end_loop  # Exit loop if i >= 10

    add $t1, $t1, $t3  # i = i + 1
    add $t0, $t0, $t1  # sum += i
    
    j loop  # Jump back to loop

end_loop:
    li $v0, 10  # Prepare to exit
    syscall     # Exit