#!/usr/bin/env python3

import secrets
import uuid

def main():
    return str(uuid.UUID(bytes=secrets.token_bytes(16)))
