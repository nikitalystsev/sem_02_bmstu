GAS LISTING /tmp/ccTwQb7Z.s 			page 1


   1              		.file	"main.c"
   2              		.text
   3              		.globl	count_resistance
   4              		.type	count_resistance, @function
   5              	count_resistance:
   6              	.LFB0:
   7              		.cfi_startproc
   8 0000 F30F1EFA 		endbr64
   9 0004 55       		pushq	%rbp
  10              		.cfi_def_cfa_offset 16
  11              		.cfi_offset 6, -16
  12 0005 4889E5   		movq	%rsp, %rbp
  13              		.cfi_def_cfa_register 6
  14 0008 F20F1145 		movsd	%xmm0, -24(%rbp)
  14      E8
  15 000d F20F114D 		movsd	%xmm1, -32(%rbp)
  15      E0
  16 0012 F20F1155 		movsd	%xmm2, -40(%rbp)
  16      D8
  17 0017 F20F1045 		movsd	-24(%rbp), %xmm0
  17      E8
  18 001c F20F5945 		mulsd	-32(%rbp), %xmm0
  18      E0
  19 0021 F20F5945 		mulsd	-40(%rbp), %xmm0
  19      D8
  20 0026 F20F104D 		movsd	-32(%rbp), %xmm1
  20      E0
  21 002b 660F28D1 		movapd	%xmm1, %xmm2
  22 002f F20F5955 		mulsd	-40(%rbp), %xmm2
  22      D8
  23 0034 F20F104D 		movsd	-24(%rbp), %xmm1
  23      E8
  24 0039 F20F594D 		mulsd	-40(%rbp), %xmm1
  24      D8
  25 003e F20F58D1 		addsd	%xmm1, %xmm2
  26 0042 F20F104D 		movsd	-24(%rbp), %xmm1
  26      E8
  27 0047 F20F594D 		mulsd	-32(%rbp), %xmm1
  27      E0
  28 004c F20F58CA 		addsd	%xmm2, %xmm1
  29 0050 F20F5EC1 		divsd	%xmm1, %xmm0
  30 0054 F20F1145 		movsd	%xmm0, -8(%rbp)
  30      F8
  31 0059 F20F1045 		movsd	-8(%rbp), %xmm0
  31      F8
  32 005e 66480F7E 		movq	%xmm0, %rax
  32      C0
  33 0063 66480F6E 		movq	%rax, %xmm0
  33      C0
  34 0068 5D       		popq	%rbp
  35              		.cfi_def_cfa 7, 8
  36 0069 C3       		ret
  37              		.cfi_endproc
  38              	.LFE0:
  39              		.size	count_resistance, .-count_resistance
  40              		.section	.rodata
  41              	.LC0:
GAS LISTING /tmp/ccTwQb7Z.s 			page 2


  42 0000 456E7465 		.string	"Enter resistors resistance:"
  42      72207265 
  42      73697374 
  42      6F727320 
  42      72657369 
  43              	.LC1:
  44 001c 256C6620 		.string	"%lf %lf %lf"
  44      256C6620 
  44      256C6600 
  45              	.LC2:
  46 0028 256C660A 		.string	"%lf\n"
  46      00
  47              		.text
  48              		.globl	main
  49              		.type	main, @function
  50              	main:
  51              	.LFB1:
  52              		.cfi_startproc
  53 006a F30F1EFA 		endbr64
  54 006e 55       		pushq	%rbp
  55              		.cfi_def_cfa_offset 16
  56              		.cfi_offset 6, -16
  57 006f 4889E5   		movq	%rsp, %rbp
  58              		.cfi_def_cfa_register 6
  59 0072 4883EC30 		subq	$48, %rsp
  60 0076 64488B04 		movq	%fs:40, %rax
  60      25280000 
  60      00
  61 007f 488945F8 		movq	%rax, -8(%rbp)
  62 0083 31C0     		xorl	%eax, %eax
  63 0085 488D0500 		leaq	.LC0(%rip), %rax
  63      000000
  64 008c 4889C7   		movq	%rax, %rdi
  65 008f E8000000 		call	puts@PLT
  65      00
  66 0094 488D4DE8 		leaq	-24(%rbp), %rcx
  67 0098 488D55E0 		leaq	-32(%rbp), %rdx
  68 009c 488D45D8 		leaq	-40(%rbp), %rax
  69 00a0 4889C6   		movq	%rax, %rsi
  70 00a3 488D0500 		leaq	.LC1(%rip), %rax
  70      000000
  71 00aa 4889C7   		movq	%rax, %rdi
  72 00ad B8000000 		movl	$0, %eax
  72      00
  73 00b2 E8000000 		call	__isoc99_scanf@PLT
  73      00
  74 00b7 F20F104D 		movsd	-24(%rbp), %xmm1
  74      E8
  75 00bc F20F1045 		movsd	-32(%rbp), %xmm0
  75      E0
  76 00c1 488B45D8 		movq	-40(%rbp), %rax
  77 00c5 660F28D1 		movapd	%xmm1, %xmm2
  78 00c9 660F28C8 		movapd	%xmm0, %xmm1
  79 00cd 66480F6E 		movq	%rax, %xmm0
  79      C0
  80 00d2 E8000000 		call	count_resistance
  80      00
GAS LISTING /tmp/ccTwQb7Z.s 			page 3


  81 00d7 66480F7E 		movq	%xmm0, %rax
  81      C0
  82 00dc 488945F0 		movq	%rax, -16(%rbp)
  83 00e0 488B45F0 		movq	-16(%rbp), %rax
  84 00e4 66480F6E 		movq	%rax, %xmm0
  84      C0
  85 00e9 488D0500 		leaq	.LC2(%rip), %rax
  85      000000
  86 00f0 4889C7   		movq	%rax, %rdi
  87 00f3 B8010000 		movl	$1, %eax
  87      00
  88 00f8 E8000000 		call	printf@PLT
  88      00
  89 00fd B8000000 		movl	$0, %eax
  89      00
  90 0102 488B55F8 		movq	-8(%rbp), %rdx
  91 0106 64482B14 		subq	%fs:40, %rdx
  91      25280000 
  91      00
  92 010f 7405     		je	.L5
  93 0111 E8000000 		call	__stack_chk_fail@PLT
  93      00
  94              	.L5:
  95 0116 C9       		leave
  96              		.cfi_def_cfa 7, 8
  97 0117 C3       		ret
  98              		.cfi_endproc
  99              	.LFE1:
 100              		.size	main, .-main
 101              		.ident	"GCC: (Ubuntu 11.2.0-7ubuntu2) 11.2.0"
 102              		.section	.note.GNU-stack,"",@progbits
 103              		.section	.note.gnu.property,"a"
 104              		.align 8
 105 0000 04000000 		.long	1f - 0f
 106 0004 10000000 		.long	4f - 1f
 107 0008 05000000 		.long	5
 108              	0:
 109 000c 474E5500 		.string	"GNU"
 110              	1:
 111              		.align 8
 112 0010 020000C0 		.long	0xc0000002
 113 0014 04000000 		.long	3f - 2f
 114              	2:
 115 0018 03000000 		.long	0x3
 116              	3:
 117 001c 00000000 		.align 8
 118              	4:
GAS LISTING /tmp/ccTwQb7Z.s 			page 4


DEFINED SYMBOLS
                            *ABS*:0000000000000000 main.c
     /tmp/ccTwQb7Z.s:5      .text:0000000000000000 count_resistance
     /tmp/ccTwQb7Z.s:50     .text:000000000000006a main

UNDEFINED SYMBOLS
puts
__isoc99_scanf
printf
__stack_chk_fail
