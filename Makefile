build:
	docker build -t demo-todo-backend .

run:
	docker run --rm -p 8000:8000 -t demo-todo-backend