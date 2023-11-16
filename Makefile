SIM ?= verilator
TOPLEVEL_LANG ?= verilog
EXTRA_ARGS += --coverage
VERILOG_SOURCES += $(PWD)/main_adder.v
VERILOG_SOURCES += $(PWD)/wrappers/main_adder_test.v
or:
	rm -rf sim_build
	$(MAKE) sim MODULE=main_adder_test TOPLEVEL=main_adder_test
include $(shell cocotb-config --makefiles)/Makefile.sim
