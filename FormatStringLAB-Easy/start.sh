#!/bin/bash
socat TCP-LISTEN:8000,reuseaddr,fork EXEC:./vuln
