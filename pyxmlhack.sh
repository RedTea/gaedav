#!/bin/sh
sed -i "s/\\b\(xml\)\./pyxml./g" `find pyxml/ pyfileserver/ -name "*.py"`

