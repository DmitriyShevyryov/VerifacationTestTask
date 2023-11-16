`timescale 1ns / 1ps

module main_adder_test(
    input    [`SCR1_XLEN-1:0]  exu2ialu_main_op1_i,        // main ALU 1st operand
    input    [`SCR1_XLEN-1:0]  exu2ialu_main_op2_i,        // main ALU 2nd operand
    input    exu2ialu_cmd_i,             // IALU command
    output  [`SCR1_XLEN-1:0] ialu2exu_main_res_o,        // main ALU result
    output  reg  ialu2exu_cmp_res_o,    // IALU comparison result
    output  reg  main_sum_pos_ovflw,
    output  reg main_sum_neg_ovflw,
    output reg  flag_z,   // Zero
    output reg  flag_s,      // Sign
    output reg  flag_o,      // Overflow
    output reg  flag_c,      // Carry
    output reg  main_ops_diff_sgn, // Main adder operands have different signs
    output reg  main_ops_non_zero // Both main adder operands are NOT 0
    );

main_adder main_adder(
    .exu2ialu_main_op1_i(exu2ialu_main_op1_i),
    .exu2ialu_main_op2_i(exu2ialu_main_op2_i),
    .exu2ialu_cmd_i(exu2ialu_cmd_i),
    .ialu2exu_main_res_o(ialu2exu_main_res_o),
    .ialu2exu_cmp_res_o(ialu2exu_cmp_res_o),
    .main_sum_pos_ovflw(main_sum_pos_ovflw),
    .main_sum_neg_ovflw( main_sum_neg_ovflw),
    .flag_z(flag_z),
    .flag_s(flag_s),
    .flag_o(flag_o),
    .flag_c(flag_c),
    .main_ops_diff_sgn(main_ops_diff_sgn),
    .main_ops_non_zero(main_ops_non_zero)
);

initial begin
    $dumpfile("waves.vcd");
    $dumpvars;
end
endmodule
