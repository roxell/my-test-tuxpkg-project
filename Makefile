all: test typecheck style flake8

TUXPKG_MIN_COVERAGE = 50.00

export PROJECT := my-test-tuxpkg-project

include $(shell tuxpkg get-makefile)
