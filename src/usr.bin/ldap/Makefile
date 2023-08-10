LOCALBASE?=	/usr/local
PROG=		ldap
SRCS=		ldapclient.c aldap.c log.c
LDADD=		../../../libevent/src/lib/libevent/libevent.a
LDADD+= 	/usr/local/lib/libtls.a \
		/usr/local/lib/libssl.a \
		/usr/local/lib/libcrypto.a
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

.include <bsd.prog.mk>
