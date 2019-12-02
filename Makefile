
# Simple Makefile for ercole agent

DESTDIR=build

all: ercole-agent-exadata

default: ercole-agent-exadata

clean:
	rm -rf ercole-agent-exadata build

ercole-agent-exadata:
	go build -o ercole-agent-exadata

install: all install-fetchers install-bin install-bin install-config

install-fetchers:
	install -d $(DESTDIR)/fetch
	cp -rp fetch/* $(DESTDIR)/fetch

install-bin:
	install -m 755 ercole-agent-exadata $(DESTDIR)/ercole-agent-exadata

install-config:
	install -m 644 config.json $(DESTDIR)/config.json
