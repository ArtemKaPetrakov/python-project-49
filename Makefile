install:
		@poerty install
# чтобы подавить вывод команды в терминале надо добавить @ перед командой
brain-games:
		@poetry run brain-games	

build:
		@poetry build

publish:
		@poetry publish --dry-run

package-install:
		@python3 -m pip install --user dist/*.whl
