install: 
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

build:
	uv build

package-install:
	uv tool install dist/*.whl
	
package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games