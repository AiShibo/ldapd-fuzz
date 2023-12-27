#	$OpenBSD: Makefile,v 1.10 2019/05/11 17:46:02 rob Exp $

LOCALBASE?=	/usr/local
EVENTDIR?=	${.CURDIR}/../../../libevent
IMSGDIR?=	${.CURDIR}/../../../libimsg

.PATH:		${.CURDIR}/../ldapd

PROG=		ldapctl
MAN=		ldapctl.8
SRCS=		ldapctl.c parse.y btree.c log.c logmsg.c util.c \
		index.c attributes.c schema.c syntax.c matching.c

.PATH: ${.CURDIR}/../../lib/libutil
SRCS+=		ber.c

LDADD=		${EVENTDIR}/src/lib/libevent/libevent.a
LDADD+= 	${IMSGDIR}/src/lib/libutil/libimsg.a

.ifdef SSLDIR
LDADD+= 	${SSLDIR}/tls/.libs/libtls.a \
		${SSLDIR}/ssl/.libs/libssl.a \
		${SSLDIR}/crypto/.libs/libcrypto.a
.else
LDADD+= 	/usr/local/lib/libtls.a \
		/usr/local/lib/libssl.a \
		/usr/local/lib/libcrypto.a
.endif

LDADD+= 	-lz
DPADD=		${LIBEVENT} ${LIBTLS} ${LIBSSL} ${LIBCRYPTO} ${LIBZ} ${LIBUTIL}
CFLAGS+=	-I${.CURDIR}/../ldapd
CFLAGS+=	-Wall -Wstrict-prototypes -Wmissing-prototypes
CFLAGS+=	-Wmissing-declarations
CFLAGS+=	-Wshadow -Wpointer-arith -Wcast-qual
CFLAGS+=	-Wsign-compare
CFLAGS+=	-I${EVENTDIR}/src/lib/libevent \
		-I${IMSGDIR}/src/lib/libutil \
		-I${.CURDIR}/../../lib/libutil

.ifdef SSLDIR
CFLAGS+=	-I${SSLDIR}/include
.else
CFLAGS+=	-I${LOCALBASE}/include
.endif

CFLAGS+=	-D__dead=''
YFLAGS=

.include <bsd.prog.mk>
