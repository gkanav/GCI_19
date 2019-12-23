all: hello

hello: kanav.o
	g++ --std=c++14 kanav.cpp -o hello
	python kanav.py
	./hello

kanav.o: kanav.cpp
	g++ --std=c++14 kanav.cpp -o hello

clean:
	rm -rf *o hello
