	.file	"main.c"
	.intel_syntax noprefix
# GNU C99 (Ubuntu 11.2.0-7ubuntu2) version 11.2.0 (x86_64-linux-gnu)
#	compiled by GNU C version 11.2.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.0, isl version isl-0.24-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed: -masm=intel -mtune=generic -march=x86-64 -std=c99 -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
	.text
	.globl	count_resistance
	.type	count_resistance, @function
count_resistance:
.LFB0:
	.cfi_startproc
	endbr64	
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	movsd	QWORD PTR -24[rbp], xmm0	# r1, r1
	movsd	QWORD PTR -32[rbp], xmm1	# r2, r2
	movsd	QWORD PTR -40[rbp], xmm2	# r3, r3
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	movsd	xmm0, QWORD PTR -24[rbp]	# tmp91, r1
	mulsd	xmm0, QWORD PTR -32[rbp]	# _1, r2
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	mulsd	xmm0, QWORD PTR -40[rbp]	# _2, r3
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	movsd	xmm1, QWORD PTR -32[rbp]	# tmp92, r2
	movapd	xmm2, xmm1	# tmp92, tmp92
	mulsd	xmm2, QWORD PTR -40[rbp]	# tmp92, r3
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	movsd	xmm1, QWORD PTR -24[rbp]	# tmp93, r1
	mulsd	xmm1, QWORD PTR -40[rbp]	# _4, r3
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	addsd	xmm2, xmm1	# _5, _4
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	movsd	xmm1, QWORD PTR -24[rbp]	# tmp94, r1
	mulsd	xmm1, QWORD PTR -32[rbp]	# _6, r2
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	addsd	xmm1, xmm2	# _7, _5
# main.c:6:     double r = (r1 * r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2);
	divsd	xmm0, xmm1	# tmp95, _7
	movsd	QWORD PTR -8[rbp], xmm0	# r, tmp95
# main.c:7:     return r;
	movsd	xmm0, QWORD PTR -8[rbp]	# _12, r
	movq	rax, xmm0	# <retval>, _12
# main.c:8: }
	movq	xmm0, rax	#, <retval>
	pop	rbp	#
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE0:
	.size	count_resistance, .-count_resistance
	.section	.rodata
.LC0:
	.string	"Enter resistors resistance:"
.LC1:
	.string	"%lf %lf %lf"
.LC2:
	.string	"%lf\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	endbr64	
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	sub	rsp, 48	#,
# main.c:11: {
	mov	rax, QWORD PTR fs:40	# tmp96, MEM[(<address-space-1> long unsigned int *)40B]
	mov	QWORD PTR -8[rbp], rax	# D.2155, tmp96
	xor	eax, eax	# tmp96
# main.c:15:     puts("Enter resistors resistance:");
	lea	rax, .LC0[rip]	# tmp87,
	mov	rdi, rax	#, tmp87
	call	puts@PLT	#
# main.c:16:     scanf("%lf %lf %lf", &r1, &r2, &r3);
	lea	rcx, -24[rbp]	# tmp88,
	lea	rdx, -32[rbp]	# tmp89,
	lea	rax, -40[rbp]	# tmp90,
	mov	rsi, rax	#, tmp90
	lea	rax, .LC1[rip]	# tmp91,
	mov	rdi, rax	#, tmp91
	mov	eax, 0	#,
	call	__isoc99_scanf@PLT	#
# main.c:18:     r = count_resistance(r1, r2, r3);
	movsd	xmm1, QWORD PTR -24[rbp]	# r3.0_1, r3
	movsd	xmm0, QWORD PTR -32[rbp]	# r2.1_2, r2
	mov	rax, QWORD PTR -40[rbp]	# r1.2_3, r1
	movapd	xmm2, xmm1	#, r3.0_1
	movapd	xmm1, xmm0	#, r2.1_2
	movq	xmm0, rax	#, r1.2_3
	call	count_resistance	#
	movq	rax, xmm0	# tmp92,
	mov	QWORD PTR -16[rbp], rax	# r, tmp92
# main.c:20:     printf("%lf\n", r);
	mov	rax, QWORD PTR -16[rbp]	# tmp93, r
	movq	xmm0, rax	#, tmp93
	lea	rax, .LC2[rip]	# tmp94,
	mov	rdi, rax	#, tmp94
	mov	eax, 1	#,
	call	printf@PLT	#
# main.c:21:     return SUCCESS;    
	mov	eax, 0	# _10,
# main.c:22: }
	mov	rdx, QWORD PTR -8[rbp]	# tmp97, D.2155
	sub	rdx, QWORD PTR fs:40	# tmp97, MEM[(<address-space-1> long unsigned int *)40B]
	je	.L5	#,
	call	__stack_chk_fail@PLT	#
.L5:
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.2.0-7ubuntu2) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
