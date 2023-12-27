LOCALBASE?=	/usr/local
EVENTDIR?=	${.CURDIR}/../../../libevent

PROG=		ldap
SRCS=		ldapclient.c aldap.c log.c

LDADD=		${EVENTDIR}/src/lib/libevent/libevent.a

.ifdef SSLDIR
LDADD+= 	${SSLDIR}/tls/.libs/libtls.a \
		${SSLDIR}/ssl/.libs/libssl.a \
		${SSLDIR}/crypto/.libs/libcrypto.a
.else
LDADD+= 	/usr/local/lib/libtls.a \
		/usr/local/lib/libssl.a \
		/usr/local/lib/libcrypto.a
.endif

DPADD+=		${LIBEVENT} ${LIBTLS} ${LIBSSL} ${LIBCRYPTO} ${LIBUTIL}

.PATH: ${.CURDIR}/../../lib/libutil
SRCS+=		ber.c

CFLAGS+=	-Wall
CFLAGS+=	-Wstrict-prototypes -Wmissing-prototypes
CFLAGS+=	-Wmissing-declarations
CFLAGS+=	-Wshadow -Wpointer-arith
CFLAGS+=	-Wsign-compare -Wcast-qual
CFLAGS+=	-I${EVENTDIR}/src/lib/libevent \
		-I${.CURDIR}/../../lib/libutil

.ifdef SSLDIR
CFLAGS+=	-I${SSLDIR}/include
.else
CFLAGS+=	-I${LOCALBASE}/include
.endif

CFLAGS+=	-D__dead=''

.include <bsd.prog.mk>
