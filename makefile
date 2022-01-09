PREFIX := /usr/local

all: dependencies install

dependencies:
	pip install -r requirements.txt

install:
	echo "#!/bin/sh" > $(PREFIX)/bin/rhythmbox-lyricfinder
	echo 'python3 $(CURDIR)/main.py $$1 $$2 $$3' >> $(PREFIX)/bin/rhythmbox-lyricfinder
	chmod 0755 $(DESTDIR)$(PREFIX)/bin/rhythmbox-lyricfinder

uninstall:
	$(RM) $(DESTDIR)$(PREFIX)/bin/rhythmbox-lyricfinder

.PHONY: all dependencies install uninstall
