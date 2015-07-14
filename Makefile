.PHONY: tests
tests:
	nosetests

.PHONY: clean
clean:
	rm -f `find . | grep .pyc`

