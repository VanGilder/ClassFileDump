.data
myName:  .asciiz "My name is: Brayden VanGilder\n"
myID:    .asciiz "My student ID is: 991739147\n"

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

    # Exit
    li $v0, 10
    syscall

