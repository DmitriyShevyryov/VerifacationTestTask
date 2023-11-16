`timescale 1ns / 1ps
`define SCR1_XLEN  32 // operand length
`define SCR1_IALU_CMD_ADD  0 // ADD code
`define SCR1_IALU_CMD_SUB  1 // SUB code
module main_adder
(
    //input clk,
    input    [`SCR1_XLEN-1:0]  exu2ialu_main_op1_i,        // main ALU 1st operand
    input    [`SCR1_XLEN-1:0]  exu2ialu_main_op2_i,        // main ALU 2nd operand
    input    exu2ialu_cmd_i,             // IALU command
    output  [`SCR1_XLEN-1:0] ialu2exu_main_res_o,        // main ALU result
    output  reg  ialu2exu_cmp_res_o,    // IALU comparison result
    output reg main_sum_pos_ovflw, // Operation causes positive overflow
    output reg main_sum_neg_ovflw, // Operation causes negative overflow
    output reg  flag_z,   // Zero
    output reg  flag_s,      // Sign
    output reg  flag_o,      // Overflow
    output reg  flag_c,   // Carry
    output reg  main_ops_diff_sgn, // Main adder operands have different signs
    output reg  main_ops_non_zero // Both main adder operands are NOT 0
    );

reg [`SCR1_XLEN:0] main_sum_res;       // Main adder result

initial begin // init block
    main_ops_diff_sgn = 0;
    main_ops_non_zero = 0;
    main_sum_pos_ovflw = 0;
    main_sum_neg_ovflw = 0;
    flag_z = 0;
    flag_s = 0;
    flag_o = 0;
    flag_c = 0;
end

assign ialu2exu_main_res_o = main_sum_res[`SCR1_XLEN-1:0]; // assigning temproray result to 32'b output result

always@ * // always_comb block
begin
    main_sum_res = (exu2ialu_cmd_i != 0)
                 ? ({1'b0, exu2ialu_main_op1_i} - {1'b0, exu2ialu_main_op2_i})   // Subtraction and comparison
                 : ({1'b0, exu2ialu_main_op1_i} + {1'b0, exu2ialu_main_op2_i});  // Addition

    main_sum_pos_ovflw = ~exu2ialu_main_op1_i[`SCR1_XLEN-1]
                       &  exu2ialu_main_op2_i[`SCR1_XLEN-1]
                       &  main_sum_res[`SCR1_XLEN-1];
    main_sum_neg_ovflw =  exu2ialu_main_op1_i[`SCR1_XLEN-1]
                       & ~exu2ialu_main_op2_i[`SCR1_XLEN-1]
                       & ~main_sum_res[`SCR1_XLEN-1];
    main_ops_diff_sgn  = (~exu2ialu_main_op1_i[`SCR1_XLEN-1]
		       & exu2ialu_main_op2_i[`SCR1_XLEN-1])
                       | (exu2ialu_main_op1_i[`SCR1_XLEN-1]
                       & ~exu2ialu_main_op2_i[`SCR1_XLEN-1]);
    main_ops_non_zero  = (|exu2ialu_main_op1_i[`SCR1_XLEN-1:0])
                       & (|exu2ialu_main_op2_i[`SCR1_XLEN-1:0]);

    flag_c = main_sum_res[`SCR1_XLEN];
    flag_z = ~|main_sum_res[`SCR1_XLEN-1:0];
    flag_s = main_sum_res[`SCR1_XLEN-1];
    flag_o = main_sum_pos_ovflw | main_sum_neg_ovflw;
end
endmodule
