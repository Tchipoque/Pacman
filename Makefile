MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs


.PHONY: install run debug clean lint lint-strict build

# Terminal colors
C_RESET = \033[0m
C_BLUE = \033[1;34m
C_GREEN = \033[1;32m
C_YELLOW = \033[1;33m
C_RED = \033[1;31m

define msg_info
	@printf "$(C_BLUE)[INFO]$(C_RESET) %s\n" "$(1)"
endef

define msg_ok
	@printf "$(C_GREEN)[OK]$(C_RESET) %s\n" "$(1)"
endef

define msg_warn
	@printf "$(C_YELLOW)[WARN]$(C_RESET) %s\n" "$(1)"
endef

define msg_error
	@printf "$(C_RED)[ERROR]$(C_RESET) %s\n" "$(1)"
endef

define msg_step
	@printf "$(C_BLUE)>>$(C_RESET) %s\n" "$(1)"
endef

install:
	$(call msg_info, Installing necessar tools...)
	@pip install uv
	@uv sync
	$(call msg_ok,All Done.)

# Run your project
run:
	$(call msg_step,Running application...)
	@uv run python3 -m src --functions_definition $(FUNCTIONS) --input $(PROMPTS) --output $(OUTPUT)

# Debug mode
debug:
	$(call msg_warn,Starting debugger for maze application...)
	@python3 -m pdb -m src $(FUNCTIONS) $(PROMPTS) $(OUTPUT)

# Clean cache files
clean:
	$(call msg_warn,Removing temporary and cache files...)
	@rm -rf .mypy_cache .venv
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	$(call msg_ok,Cleanup completed.)

# Linting (mandatory)
lint:
	$(call msg_step,Running flake8 checks...)
	@uv run python3 -m flake8 src/
	$(call msg_step,Running mypy checks...)
	@uv run python3 -m mypy src/ $(MYPY_FLAGS)
	$(call msg_ok,Lint checks passed.)

# Strict lint (optional)
lint-strict:
	$(call msg_step,Running strict lint checks...)
	@uv run python3 -m flake8  src/
	@uv run python3 -m mypy src/ --strict
	$(call msg_ok,Strict lint checks passed.)

#uv run python -m moulinette grade_student_answers --set private --student_answer_path ../data/output/function_calling_results.json