#	$OpenBSD: Makefile,v 1.10 2019/05/11 17:46:02 rob Exp $

LOCALBASE?=	/usr/local
.PATH:		${.CURDIR}/../ldapd

PROG=		ldapctl
MAN=		ldapctl.8
SRCS=		ldapctl.c parse.y btree.c log.c logmsg.c util.c \
		index.c attributes.c schema.c syntax.c matching.c

.PATH: ${.CURDIR}/../../lib/libutil
SRCS+=		ber.c

LDADD=		-levent -ltls -lssl -lcrypto -lz -limsg
DPADD=		${LIBEVENT} ${LIBTLS} ${LIBSSL} ${LIBCRYPTO} ${LIBZ} ${LIBUTIL}
CFLAGS+=	-I${.CURDIR}/../ldapd
CFLAGS+=	-Wall -Wstrict-prototypes -Wmissing-prototypes
CFLAGS+=	-Wmissing-declarations
CFLAGS+=	-Wshadow -Wpointer-arith -Wcast-qual
CFLAGS+=	-Wsign-compare
CFLAGS+=	-I${.CURDIR}/../../../libevent/src/lib/libevent \
		-I${.CURDIR}/../../../libimsg/src/lib/libutil \
		-I${.CURDIR}/../../lib/libutil \
		-I ${LOCALBASE}/include \
		-D__dead=''
LDFLAGS+=	-L${.CURDIR}/../../../libevent/src/lib/libevent \
		-L${.CURDIR}/../../../libimsg/src/lib/libutil \
		-L ${LOCALBASE}/lib
YFLAGS=

.include <bsd.prog.mk>
