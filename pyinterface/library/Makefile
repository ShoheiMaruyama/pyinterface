
CC = gcc
CFLAGS = -Wall -fPIC
LDFLAGS = -shared

TARGET_LIB = lib_gpg3100.so


all: ${TARGET_LIB}

lib_gpg3100.so: lib_gpg3100.o
	$(CC) $(LDFLAGS) -o lib_gpg3100.so lib_gpg3100.o -lgpg3100

lib_gpg3100.o:
	$(CC) $(CFLAGS) -c lib_gpg3100.c -o lib_gpg3100.o


clean:
	rm -f $(TARGET_LIB) *.o
