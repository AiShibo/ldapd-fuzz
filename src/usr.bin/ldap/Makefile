LOCALBASE?=	/usr/local
PROG=		ldap
SRCS=		ldapclient.c aldap.c log.c
LDADD+=		-levent -ltls -lssl -lcrypto -lutil
DPADD+=		${LIBEVENT} ${LIBTLS} ${LIBSSL} ${LIBCRYPTO} ${LIBUTIL}

.PATH: ${.CURDIR}/../../lib/libutil
SRCS+=		ber.c

CFLAGS+=	-Wall
CFLAGS+=	-Wstrict-prototypes -Wmissing-prototypes
CFLAGS+=	-Wmissing-declarations
CFLAGS+=	-Wshadow -Wpointer-arith
CFLAGS+=	-Wsign-compare -Wcast-qual
CFLAGS+=	-I${.CURDIR}/../../../libevent/src/lib/libevent \
		-I${.CURDIR}/../../lib/libutil \
		-I${LOCALBASE}/include \
		-D__dead=''

LDFLAGS+=       -L${.CURDIR}/../../../libevent/src/lib/libevent \
		-L${LOCALBASE}/lib

.include <bsd.prog.mk>
