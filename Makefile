#
# Makefile for use with Koji build system
#

NAME=srp-sm-helper
VERSION=0.1
RELEASE=0
NV=$(NAME)-$(VERSION)
TARBALL=$(NV).tgz

WGET_URL=https://github.com/ofaaland/$(NAME)/archive/$(VERSION)-$(RELEASE).tar.gz
WGET=wget

sources:
	rm -f $(TARBALL)
	$(WGET) -O $(TARBALL) $(WGET_URL)

clean:
	rm -f $(TARBALL)
	rm -rf $(NV)

.PHONY: clean
