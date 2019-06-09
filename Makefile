
LENGTH=3
EDITIONS=2
EDITIONS_VALUES=1 2 3
LENGTH_VALUES=5 10 15 20 25 30
EXPERIMENT_VALUES=200 400 600 800 1000

test: test-length

test-length:
	@for L in $(LENGTH_VALUES); do make -s test-noise LENGTH=$$L || exit $$?; done

test-noise:
	@for E in $(EDITIONS_VALUES); do make -s test-average EDITIONS=$$E || exit $$?; done

test-average:
	@for X in `seq 10`; do make -s test-one || exit $$?; done | ./mean.py > mean.txt
	@echo -n $(LENGTH) $(EDITIONS)" "; cat mean.txt

test-one:
	@python3 textgenerator.py dictionary.txt $(LENGTH) original.txt
	@python3 noise.py $(EDITIONS) original.txt noisy.txt actualeditions.txt
	@python3 corrector.py dictionary.txt noisy.txt corrected.txt editions.txt
	@python3 checker.py original.txt corrected.txt actualeditions.txt editions.txt
	@cat editions.txt

experiment:
	@for L in $(EXPERIMENT_VALUES); do echo -n $$L; $$(which time) -p make -s test LENGTH=$$L 2>&1 | grep user | cut -c5- ; done

zip:
	zip corrector.zip textgenerator.py noise.py checker.py mean.py dictionary.txt Makefile
