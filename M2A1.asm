.data
myName: .asciiz "Brayden VanGilder\n"
myID: .asciiz "991739147\n"

.text
main:
    # Print my name
    la $a0, myName
    li $v0, 4
    syscall

    # Print my ID
    la $a0, myID
    li $v0, 4
    syscall

    # Initialize registers for summing 1 to 10
    li $t0, 0  # sum
    li $t1, 0  # i
    li $t2, 10 # 10
    li $t3, 1  # 1

loop:
    bge $t1, $t2, end_loop
    
    add $t0, $t0, $t1
    add $t0, $t0, $t3
    
    add $t1, $t1, $t3
    
    j loop

end_loop:
    # The sum should now be in $t0 (should be 55)

    # Exit
    li $v0, 10
    syscall


