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
	echo rm -f $(TARBALL)
	echo $(WGET) -O $(TARBALL) $(WGET_URL)

clean:
	echo rm -f $(TARBALL)
	echo rm -rf $(NV)

.PHONY: clean
