release:
	rm -rf build dist Santaslist.egg-info
	python setup.py sdist bdist_wheel
	twine upload dist/*
