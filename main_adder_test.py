# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0


import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.binary import BinaryValue


@cocotb.test()
async def main_adder_test(dut):
    test_list = [] # Empty list for test iterations
    comm_vars = {'ADD': 0, 'SUB': 1}  # Dict for command conditions
    pos_ovflw_vars = {'': 0, 'P_OVFLW': 1} # Dict for Positive Overflow Reg markers
    neg_ovflw_vars = {'': 0, 'N_OVFLW': 1} # Dict for Negative Overflow Reg markers
    zero_vars = {'': 0, 'ZERO': 1}  # Dict for Zero Flag markers
    sign_vars = {'': 0, 'SIGN': 1}  # Dict for Sign Flag markers
    ovflw_vars = {'': 0, 'OVERFLOW': 1} # Dict for Overflow Flag markers
    carry_vars = {'': 0, 'CARRY': 1} # Dict for Carry Flag markers
    diff_sgn_vars = {'': 0, 'DIFF SIGNS': 1} # Dict for Operands` Different Sign Reg markers
    both_non_zero_vars = {'': 0, 'BOTH N ZERO': 1} # Dict for Both Operands Not 0 Reg markers
    test_list.append(["00000000000000000000000000000001", # Carry, Zero, DIFF SIGNS, BOTH N ZERO
                      "11111111111111111111111111111111",
                      "00000000000000000000000000000000", comm_vars.get('ADD'),
                      pos_ovflw_vars.get(''), neg_ovflw_vars.get(''), zero_vars.get('ZERO'), sign_vars.get(''),
                      ovflw_vars.get(''), carry_vars.get('CARRY'), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('BOTH N ZERO')])
    test_list.append(["00000000000000000000000000000000", # Carry, DIFF SIGNS
                      "11111111111111111111111111111111",
                      "00000000000000000000000000000001", comm_vars.get('SUB'),
                      pos_ovflw_vars.get(''), neg_ovflw_vars.get(''), zero_vars.get(''), sign_vars.get(''),
                      ovflw_vars.get(''), carry_vars.get('CARRY'), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('')])
    test_list.append(["00000000000000000010000000000000", # Carry, DIFF SIGNS, BOTH N ZERO
                      "11111111111111111111111111111111",
                      "00000000000000000001111111111111", comm_vars.get('ADD'),
                      pos_ovflw_vars.get(''), neg_ovflw_vars.get(''), zero_vars.get(''), sign_vars.get(''),
                      ovflw_vars.get(''), carry_vars.get('CARRY'), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('BOTH N ZERO')])
    test_list.append(["11111111111011111111111111111111", # Carry, Sign, BOTH N ZERO
                      "11111111111111111111111111111111",
                      "11111111111100000000000000000000", comm_vars.get('SUB'),
                      pos_ovflw_vars.get(''), neg_ovflw_vars.get(''), zero_vars.get(''), sign_vars.get('SIGN'),
                      ovflw_vars.get(''), carry_vars.get('CARRY'), diff_sgn_vars.get(''), both_non_zero_vars.get('BOTH N ZERO')])
    test_list.append(["00000000000000000000000000000001", # Overflow, Sign, DIFF SIGNS, BOTH N ZERO
                      "10000000000000000000000000000000",
                      "10000000000000000000000000000001", comm_vars.get('ADD'),
                      pos_ovflw_vars.get('P_OVFLW'), neg_ovflw_vars.get(''), zero_vars.get(''), sign_vars.get('SIGN'),
                      ovflw_vars.get('OVERFLOW'), carry_vars.get(''), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('BOTH N ZERO')])
    test_list.append(["11000000000000000000000000000000",  # Overflow, Carry, DIFF SIGNS, BOTH N ZERO
                      "01111111111111111111111111111111",
                      "00111111111111111111111111111111", comm_vars.get('ADD'),
                      pos_ovflw_vars.get(''), neg_ovflw_vars.get('N_OVFLW'), zero_vars.get(''), sign_vars.get(''),
                      ovflw_vars.get('OVERFLOW'), carry_vars.get('CARRY'), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('BOTH N ZERO')])
    test_list.append(["01010101010101010101010101010101",  # Overflow, Carry, Sign, DIFF SIGNS, DIFF SIGNS
                      "10101010101010101010101010101010",
                      "11111111111111111111111111111111", comm_vars.get('ADD'),
                      pos_ovflw_vars.get('P_OVFLW'), neg_ovflw_vars.get(''), zero_vars.get(''), sign_vars.get('SIGN'),
                      ovflw_vars.get('OVERFLOW'), carry_vars.get(''), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('BOTH N ZERO')])
    test_list.append(["10101000010001000010000011100001",  # Overflow, DIFF SIGNS, BOTH N ZERO
                      "01010110011100000010100000100010",
                      "01010001110100111111100010111111", comm_vars.get('SUB'),
                      pos_ovflw_vars.get(''), neg_ovflw_vars.get('N_OVFLW'), zero_vars.get(''), sign_vars.get(''),
                      ovflw_vars.get('OVERFLOW'), carry_vars.get(''), diff_sgn_vars.get('DIFF SIGNS'), both_non_zero_vars.get('BOTH N ZERO')])
    for i in range(len(test_list)):
        op1 = BinaryValue(test_list[i][0]) # Converting string first operand value into binary cocotb object
        op2 = BinaryValue(test_list[i][1]) # Converting string second operand value into binary cocotb object
        res = BinaryValue(test_list[i][2]) # Converting string result value into binary cocotb object
        comm = test_list[i][3] # Command assign
        pos_overflow = test_list[i][4] # Assigning values of testcase [i] to local vars (next 7 str)
        neg_overflow = test_list[i][5]
        flag_zero = test_list[i][6]
        flag_sign = test_list[i][7]
        flag_ovflw = test_list[i][8]
        flag_carry = test_list[i][9]
        diff_sgn = test_list[i][10]
        both_non_zero = test_list[i][11]
        dut.exu2ialu_main_op1_i.value = op1 # Assigning first operand to DUT value
        dut.exu2ialu_main_op2_i.value = op2 # Assigning second operand to DUT value
        dut.exu2ialu_cmd_i.value = comm # Assigning comand to DUT value
        await Timer(1, 'ns') # Using Timer to switch testcases instead of using clk
        assert dut.ialu2exu_main_res_o.value == res, f"Error at res: test {i}" # if DUT`s returning value equals testcase value test is completing, else returning following error
        assert dut.main_sum_pos_ovflw.value == pos_overflow, f"Error at positive overflow: test {i}"
        assert dut.main_sum_neg_ovflw.value == neg_overflow, f"Error at negative overflow: test {i}"
        assert dut.flag_z.value == flag_zero, f"Error at flag Zero: test {i}"
        assert dut.flag_s.value == flag_sign, f"Error at flag Sign: test {i}"
        assert dut.flag_o.value == flag_ovflw, f"Error at flag Overflow: test {i}"
        assert dut.flag_c.value == flag_carry, f"Error at flag Carry overflow: test {i}"
        assert dut.main_ops_diff_sgn.value == diff_sgn, f"Error at Different Operand Signs: test {i}"
        assert dut.main_ops_non_zero.value == both_non_zero, f"Error at Both Operand Not 0: test {i}"





