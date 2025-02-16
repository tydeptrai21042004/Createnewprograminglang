# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u016f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3J\n\3\3\4\3\4\5\4N\n\4\3\4\3\4\3\4\3\4\5\4T\n")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\\\n\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6m\n\6\3")
        buf.write("\7\3\7\3\7\3\7\5\7s\n\7\3\7\3\7\3\7\3\7\5\7y\n\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\7\b\u0081\n\b\f\b\16\b\u0084\13\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\7\n\u008c\n\n\f\n\16\n\u008f\13")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u009c\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00a3\n\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\5\r\u00ab\n\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u00b6\n\16\3\17\3\17\5\17")
        buf.write("\u00ba\n\17\3\17\3\17\5\17\u00be\n\17\3\17\3\17\5\17\u00c2")
        buf.write("\n\17\3\17\5\17\u00c5\n\17\3\17\3\17\7\17\u00c9\n\17\f")
        buf.write("\17\16\17\u00cc\13\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u00d7\n\17\f\17\16\17\u00da\13\17\3")
        buf.write("\17\5\17\u00dd\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00e7\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\5\23\u00f2\n\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\7\24\u00fa\n\24\f\24\16\24\u00fd\13\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u010e\n\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u0125\n\25\f\25\16\25\u0128")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\7\27\u0132")
        buf.write("\n\27\f\27\16\27\u0135\13\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0144\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\6\34\u014e")
        buf.write("\n\34\r\34\16\34\u014f\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\7\36\u015c\n\36\f\36\16\36\u015f\13")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\5\37\u0166\n\37\3\37\3\37")
        buf.write("\3\37\5\37\u016b\n\37\3\37\3\37\3\37\2\3( \2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2")
        buf.write("\6\3\2\31\33\3\2\34\35\3\2\36#\5\2(*\62\63\65\65\2\u018e")
        buf.write("\2?\3\2\2\2\4I\3\2\2\2\6K\3\2\2\2\bW\3\2\2\2\nl\3\2\2")
        buf.write("\2\fn\3\2\2\2\16}\3\2\2\2\20\u0085\3\2\2\2\22\u0089\3")
        buf.write("\2\2\2\24\u009b\3\2\2\2\26\u009d\3\2\2\2\30\u00a8\3\2")
        buf.write("\2\2\32\u00ae\3\2\2\2\34\u00dc\3\2\2\2\36\u00e6\3\2\2")
        buf.write("\2 \u00e8\3\2\2\2\"\u00eb\3\2\2\2$\u00ee\3\2\2\2&\u00f6")
        buf.write("\3\2\2\2(\u010d\3\2\2\2*\u0129\3\2\2\2,\u012e\3\2\2\2")
        buf.write(".\u0136\3\2\2\2\60\u013a\3\2\2\2\62\u0143\3\2\2\2\64\u0145")
        buf.write("\3\2\2\2\66\u014a\3\2\2\28\u0153\3\2\2\2:\u0158\3\2\2")
        buf.write("\2<\u0162\3\2\2\2>@\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?\3\2")
        buf.write("\2\2AB\3\2\2\2BC\3\2\2\2CD\7\2\2\3D\3\3\2\2\2EJ\5\6\4")
        buf.write("\2FJ\5\b\5\2GJ\5\f\7\2HJ\5\n\6\2IE\3\2\2\2IF\3\2\2\2I")
        buf.write("G\3\2\2\2IH\3\2\2\2J\5\3\2\2\2KM\7\3\2\2LN\7\61\2\2ML")
        buf.write("\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\4\2\2PS\5\62\32\2QR\7")
        buf.write("\5\2\2RT\5(\25\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\6\2")
        buf.write("\2V\7\3\2\2\2WX\7\7\2\2X[\7\61\2\2YZ\7\4\2\2Z\\\5\62\32")
        buf.write("\2[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\7\5\2\2^_\5(\25\2")
        buf.write("_`\7\6\2\2`\t\3\2\2\2ab\7\b\2\2bc\7\61\2\2cd\7\5\2\2d")
        buf.write("e\5\62\32\2ef\7\6\2\2fm\3\2\2\2gh\7\b\2\2hi\7\61\2\2i")
        buf.write("j\5\66\34\2jk\7\6\2\2km\3\2\2\2la\3\2\2\2lg\3\2\2\2m\13")
        buf.write("\3\2\2\2no\7\t\2\2op\7\61\2\2pr\7\n\2\2qs\5\16\b\2rq\3")
        buf.write("\2\2\2rs\3\2\2\2st\3\2\2\2tx\7\13\2\2uv\7\4\2\2vy\5\62")
        buf.write("\32\2wy\3\2\2\2xu\3\2\2\2xw\3\2\2\2yz\3\2\2\2z{\5\22\n")
        buf.write("\2{|\7\6\2\2|\r\3\2\2\2}\u0082\5\20\t\2~\177\7\f\2\2\177")
        buf.write("\u0081\5\20\t\2\u0080~\3\2\2\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\17\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0085\u0086\7\61\2\2\u0086\u0087\7\4\2")
        buf.write("\2\u0087\u0088\5\62\32\2\u0088\21\3\2\2\2\u0089\u008d")
        buf.write("\7\r\2\2\u008a\u008c\5\24\13\2\u008b\u008a\3\2\2\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7")
        buf.write("\16\2\2\u0091\23\3\2\2\2\u0092\u009c\5\6\4\2\u0093\u009c")
        buf.write("\5\26\f\2\u0094\u009c\5\30\r\2\u0095\u009c\5\32\16\2\u0096")
        buf.write("\u009c\5\34\17\2\u0097\u009c\5 \21\2\u0098\u009c\5\"\22")
        buf.write("\2\u0099\u009c\5$\23\2\u009a\u009c\5\22\n\2\u009b\u0092")
        buf.write("\3\2\2\2\u009b\u0093\3\2\2\2\u009b\u0094\3\2\2\2\u009b")
        buf.write("\u0095\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2")
        buf.write("\u009b\u0098\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3")
        buf.write("\2\2\2\u009c\25\3\2\2\2\u009d\u00a2\7\61\2\2\u009e\u009f")
        buf.write("\7\17\2\2\u009f\u00a0\5(\25\2\u00a0\u00a1\7\20\2\2\u00a1")
        buf.write("\u00a3\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7\21\2\2\u00a5\u00a6")
        buf.write("\5(\25\2\u00a6\u00a7\7\6\2\2\u00a7\27\3\2\2\2\u00a8\u00aa")
        buf.write("\7\22\2\2\u00a9\u00ab\5(\25\2\u00aa\u00a9\3\2\2\2\u00aa")
        buf.write("\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7\6\2\2")
        buf.write("\u00ad\31\3\2\2\2\u00ae\u00af\7\23\2\2\u00af\u00b0\7\n")
        buf.write("\2\2\u00b0\u00b1\5(\25\2\u00b1\u00b2\7\13\2\2\u00b2\u00b5")
        buf.write("\5\22\n\2\u00b3\u00b4\7\24\2\2\u00b4\u00b6\5\22\n\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\33\3\2\2\2\u00b7")
        buf.write("\u00c4\7\25\2\2\u00b8\u00ba\5\26\f\2\u00b9\u00b8\3\2\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd")
        buf.write("\7\6\2\2\u00bc\u00be\5(\25\2\u00bd\u00bc\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\7\6\2\2")
        buf.write("\u00c0\u00c2\5\26\f\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5(\25\2\u00c4")
        buf.write("\u00b9\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\u00ca\7\r\2\2\u00c7\u00c9\5")
        buf.write("\36\20\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cd\u00dd\7\16\2\2\u00ce\u00cf")
        buf.write("\7\25\2\2\u00cf\u00d0\7\61\2\2\u00d0\u00d1\7\f\2\2\u00d1")
        buf.write("\u00d2\7\61\2\2\u00d2\u00d3\7\26\2\2\u00d3\u00d4\7\61")
        buf.write("\2\2\u00d4\u00d8\7\r\2\2\u00d5\u00d7\5\36\20\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00db\u00dd\7\16\2\2\u00dc\u00b7\3\2\2\2\u00dc\u00ce")
        buf.write("\3\2\2\2\u00dd\35\3\2\2\2\u00de\u00e7\5\6\4\2\u00df\u00e7")
        buf.write("\5\26\f\2\u00e0\u00e7\5\30\r\2\u00e1\u00e7\5\32\16\2\u00e2")
        buf.write("\u00e7\5\34\17\2\u00e3\u00e7\5 \21\2\u00e4\u00e7\5\"\22")
        buf.write("\2\u00e5\u00e7\5$\23\2\u00e6\u00de\3\2\2\2\u00e6\u00df")
        buf.write("\3\2\2\2\u00e6\u00e0\3\2\2\2\u00e6\u00e1\3\2\2\2\u00e6")
        buf.write("\u00e2\3\2\2\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2")
        buf.write("\u00e6\u00e5\3\2\2\2\u00e7\37\3\2\2\2\u00e8\u00e9\7\27")
        buf.write("\2\2\u00e9\u00ea\7\6\2\2\u00ea!\3\2\2\2\u00eb\u00ec\7")
        buf.write("\30\2\2\u00ec\u00ed\7\6\2\2\u00ed#\3\2\2\2\u00ee\u00ef")
        buf.write("\7\61\2\2\u00ef\u00f1\7\n\2\2\u00f0\u00f2\5&\24\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3\u00f4\7\13\2\2\u00f4\u00f5\7\6\2\2\u00f5%\3\2\2")
        buf.write("\2\u00f6\u00fb\5(\25\2\u00f7\u00f8\7\f\2\2\u00f8\u00fa")
        buf.write("\5(\25\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\'\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fe\u00ff\b\25\1\2\u00ff\u0100\7&\2\2")
        buf.write("\u0100\u010e\5(\25\t\u0101\u0102\7\n\2\2\u0102\u0103\5")
        buf.write("(\25\2\u0103\u0104\7\13\2\2\u0104\u010e\3\2\2\2\u0105")
        buf.write("\u010e\5*\26\2\u0106\u010e\7\61\2\2\u0107\u010e\5\60\31")
        buf.write("\2\u0108\u0109\7\61\2\2\u0109\u010a\7\r\2\2\u010a\u010b")
        buf.write("\5,\27\2\u010b\u010c\7\16\2\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u00fe\3\2\2\2\u010d\u0101\3\2\2\2\u010d\u0105\3\2\2\2")
        buf.write("\u010d\u0106\3\2\2\2\u010d\u0107\3\2\2\2\u010d\u0108\3")
        buf.write("\2\2\2\u010e\u0126\3\2\2\2\u010f\u0110\f\16\2\2\u0110")
        buf.write("\u0111\t\2\2\2\u0111\u0125\5(\25\17\u0112\u0113\f\r\2")
        buf.write("\2\u0113\u0114\t\3\2\2\u0114\u0125\5(\25\16\u0115\u0116")
        buf.write("\f\f\2\2\u0116\u0117\t\4\2\2\u0117\u0125\5(\25\r\u0118")
        buf.write("\u0119\f\13\2\2\u0119\u011a\7$\2\2\u011a\u0125\5(\25\f")
        buf.write("\u011b\u011c\f\n\2\2\u011c\u011d\7%\2\2\u011d\u0125\5")
        buf.write("(\25\13\u011e\u011f\f\3\2\2\u011f\u0120\7\'\2\2\u0120")
        buf.write("\u0121\5(\25\2\u0121\u0122\7\4\2\2\u0122\u0123\5(\25\4")
        buf.write("\u0123\u0125\3\2\2\2\u0124\u010f\3\2\2\2\u0124\u0112\3")
        buf.write("\2\2\2\u0124\u0115\3\2\2\2\u0124\u0118\3\2\2\2\u0124\u011b")
        buf.write("\3\2\2\2\u0124\u011e\3\2\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127)\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u012a\7\61\2\2\u012a\u012b\7\r\2")
        buf.write("\2\u012b\u012c\5,\27\2\u012c\u012d\7\16\2\2\u012d+\3\2")
        buf.write("\2\2\u012e\u0133\5.\30\2\u012f\u0130\7\f\2\2\u0130\u0132")
        buf.write("\5.\30\2\u0131\u012f\3\2\2\2\u0132\u0135\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134-\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0136\u0137\7\61\2\2\u0137\u0138\7\4\2")
        buf.write("\2\u0138\u0139\5(\25\2\u0139/\3\2\2\2\u013a\u013b\t\5")
        buf.write("\2\2\u013b\61\3\2\2\2\u013c\u0144\7+\2\2\u013d\u0144\7")
        buf.write(",\2\2\u013e\u0144\7-\2\2\u013f\u0144\7.\2\2\u0140\u0144")
        buf.write("\5\64\33\2\u0141\u0144\5\66\34\2\u0142\u0144\5:\36\2\u0143")
        buf.write("\u013c\3\2\2\2\u0143\u013d\3\2\2\2\u0143\u013e\3\2\2\2")
        buf.write("\u0143\u013f\3\2\2\2\u0143\u0140\3\2\2\2\u0143\u0141\3")
        buf.write("\2\2\2\u0143\u0142\3\2\2\2\u0144\63\3\2\2\2\u0145\u0146")
        buf.write("\7\17\2\2\u0146\u0147\7\62\2\2\u0147\u0148\7\20\2\2\u0148")
        buf.write("\u0149\5\62\32\2\u0149\65\3\2\2\2\u014a\u014b\7/\2\2\u014b")
        buf.write("\u014d\7\r\2\2\u014c\u014e\58\35\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\7\16\2\2\u0152")
        buf.write("\67\3\2\2\2\u0153\u0154\7\61\2\2\u0154\u0155\7\4\2\2\u0155")
        buf.write("\u0156\5\62\32\2\u0156\u0157\7\6\2\2\u01579\3\2\2\2\u0158")
        buf.write("\u0159\7\60\2\2\u0159\u015d\7\r\2\2\u015a\u015c\5<\37")
        buf.write("\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u0160\u0161\7\16\2\2\u0161;\3\2\2\2\u0162")
        buf.write("\u0163\7\61\2\2\u0163\u0165\7\n\2\2\u0164\u0166\5\16\b")
        buf.write("\2\u0165\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u016a\7\13\2\2\u0168\u0169\7\4\2\2\u0169")
        buf.write("\u016b\5\62\32\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2")
        buf.write("\2\u016b\u016c\3\2\2\2\u016c\u016d\7\6\2\2\u016d=\3\2")
        buf.write("\2\2#AIMS[lrx\u0082\u008d\u009b\u00a2\u00aa\u00b5\u00b9")
        buf.write("\u00bd\u00c1\u00c4\u00ca\u00d8\u00dc\u00e6\u00f1\u00fb")
        buf.write("\u010d\u0124\u0126\u0133\u0143\u014f\u015d\u0165\u016a")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "':'", "'='", "';'", "'const'", 
                     "'type'", "'func'", "'('", "')'", "','", "'{'", "'}'", 
                     "'['", "']'", "':='", "'return'", "'if'", "'else'", 
                     "'for'", "'in'", "'break'", "'continue'", "'*'", "'/'", 
                     "'%'", "'+'", "'-'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'?'", "'true'", 
                     "'false'", "'nil'", "'int'", "'float'", "'boolean'", 
                     "'string'", "'struct'", "'interface'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INTLIT", 
                      "FLOATLIT", "ILLEGAL_FLOAT", "STRINGLIT", "UNCLOSE_STRING", 
                      "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_constdecl = 3
    RULE_typedecl = 4
    RULE_funcdecl = 5
    RULE_paramList = 6
    RULE_param = 7
    RULE_blockStmt = 8
    RULE_stmt = 9
    RULE_assignStmt = 10
    RULE_returnStmt = 11
    RULE_ifStmt = 12
    RULE_forStmt = 13
    RULE_loopStmt = 14
    RULE_breakStmt = 15
    RULE_continueStmt = 16
    RULE_callStmt = 17
    RULE_argList = 18
    RULE_expression = 19
    RULE_structInitExpr = 20
    RULE_structInitList = 21
    RULE_structInitField = 22
    RULE_literal = 23
    RULE_typeID = 24
    RULE_arrayType = 25
    RULE_structType = 26
    RULE_fieldDecl = 27
    RULE_interfaceType = 28
    RULE_methodDecl = 29

    ruleNames =  [ "program", "decl", "vardecl", "constdecl", "typedecl", 
                   "funcdecl", "paramList", "param", "blockStmt", "stmt", 
                   "assignStmt", "returnStmt", "ifStmt", "forStmt", "loopStmt", 
                   "breakStmt", "continueStmt", "callStmt", "argList", "expression", 
                   "structInitExpr", "structInitList", "structInitField", 
                   "literal", "typeID", "arrayType", "structType", "fieldDecl", 
                   "interfaceType", "methodDecl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    ID=47
    INTLIT=48
    FLOATLIT=49
    ILLEGAL_FLOAT=50
    STRINGLIT=51
    UNCLOSE_STRING=52
    COMMENT=53
    WS=54
    ERROR_CHAR=55
    ILLEGAL_ESCAPE=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.decl()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__4) | (1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__6))) != 0)):
                    break

            self.state = 65
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.vardecl()
                pass
            elif token in [MiniGoParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.constdecl()
                pass
            elif token in [MiniGoParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.funcdecl()
                pass
            elif token in [MiniGoParser.T__5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.typedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniGoParser.T__0)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 74
                self.match(MiniGoParser.ID)


            self.state = 77
            self.match(MiniGoParser.T__1)
            self.state = 78
            self.typeID()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__2:
                self.state = 79
                self.match(MiniGoParser.T__2)
                self.state = 80
                self.expression(0)


            self.state = 83
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MiniGoParser.T__4)
            self.state = 86
            self.match(MiniGoParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 87
                self.match(MiniGoParser.T__1)
                self.state = 88
                self.typeID()


            self.state = 91
            self.match(MiniGoParser.T__2)
            self.state = 92
            self.expression(0)
            self.state = 93
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typedecl)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(MiniGoParser.T__5)
                self.state = 96
                self.match(MiniGoParser.ID)
                self.state = 97
                self.match(MiniGoParser.T__2)
                self.state = 98
                self.typeID()
                self.state = 99
                self.match(MiniGoParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(MiniGoParser.T__5)
                self.state = 102
                self.match(MiniGoParser.ID)
                self.state = 103
                self.structType()
                self.state = 104
                self.match(MiniGoParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,0)


        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MiniGoParser.T__6)
            self.state = 109
            self.match(MiniGoParser.ID)
            self.state = 110
            self.match(MiniGoParser.T__7)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 111
                self.paramList()


            self.state = 114
            self.match(MiniGoParser.T__8)
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__1]:
                self.state = 115
                self.match(MiniGoParser.T__1)
                self.state = 116
                self.typeID()
                pass
            elif token in [MiniGoParser.T__10]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 120
            self.blockStmt()
            self.state = 121
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MiniGoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.param()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__9:
                self.state = 124
                self.match(MiniGoParser.T__9)
                self.state = 125
                self.param()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MiniGoParser.ID)
            self.state = 132
            self.match(MiniGoParser.T__1)
            self.state = 133
            self.typeID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = MiniGoParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MiniGoParser.T__10)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.ID))) != 0):
                self.state = 136
                self.stmt()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(MiniGoParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.returnStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.forStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 149
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 151
                self.callStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self.blockStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MiniGoParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniGoParser.ID)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__12:
                self.state = 156
                self.match(MiniGoParser.T__12)
                self.state = 157
                self.expression(0)
                self.state = 158
                self.match(MiniGoParser.T__13)


            self.state = 162
            self.match(MiniGoParser.T__14)
            self.state = 163
            self.expression(0)
            self.state = 164
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MiniGoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniGoParser.T__15)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__7) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__37) | (1 << MiniGoParser.T__38) | (1 << MiniGoParser.T__39) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 167
                self.expression(0)


            self.state = 170
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def blockStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniGoParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MiniGoParser.T__16)
            self.state = 173
            self.match(MiniGoParser.T__7)
            self.state = 174
            self.expression(0)
            self.state = 175
            self.match(MiniGoParser.T__8)
            self.state = 176
            self.blockStmt()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__17:
                self.state = 177
                self.match(MiniGoParser.T__17)
                self.state = 178
                self.blockStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def loopStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LoopStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LoopStmtContext,i)


        def assignStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignStmtContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MiniGoParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(MiniGoParser.T__18)
                self.state = 194
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.ID:
                        self.state = 182
                        self.assignStmt()


                    self.state = 185
                    self.match(MiniGoParser.T__3)
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__7) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__37) | (1 << MiniGoParser.T__38) | (1 << MiniGoParser.T__39) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                        self.state = 186
                        self.expression(0)


                    self.state = 189
                    self.match(MiniGoParser.T__3)
                    self.state = 191
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.ID:
                        self.state = 190
                        self.assignStmt()



                elif la_ == 2:
                    self.state = 193
                    self.expression(0)


                self.state = 196
                self.match(MiniGoParser.T__10)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 197
                    self.loopStmt()
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 203
                self.match(MiniGoParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(MiniGoParser.T__18)
                self.state = 205
                self.match(MiniGoParser.ID)
                self.state = 206
                self.match(MiniGoParser.T__9)
                self.state = 207
                self.match(MiniGoParser.ID)
                self.state = 208
                self.match(MiniGoParser.T__19)
                self.state = 209
                self.match(MiniGoParser.ID)
                self.state = 210
                self.match(MiniGoParser.T__10)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 211
                    self.loopStmt()
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 217
                self.match(MiniGoParser.T__11)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_loopStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStmt" ):
                return visitor.visitLoopStmt(self)
            else:
                return visitor.visitChildren(self)




    def loopStmt(self):

        localctx = MiniGoParser.LoopStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loopStmt)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.returnStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.forStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 226
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 227
                self.callStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = MiniGoParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MiniGoParser.T__20)
            self.state = 231
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = MiniGoParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MiniGoParser.T__21)
            self.state = 234
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStmt" ):
                return visitor.visitCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def callStmt(self):

        localctx = MiniGoParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_callStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MiniGoParser.ID)
            self.state = 237
            self.match(MiniGoParser.T__7)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__7) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__37) | (1 << MiniGoParser.T__38) | (1 << MiniGoParser.T__39) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 238
                self.argList()


            self.state = 241
            self.match(MiniGoParser.T__8)
            self.state = 242
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = MiniGoParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expression(0)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__9:
                self.state = 245
                self.match(MiniGoParser.T__9)
                self.state = 246
                self.expression(0)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def structInitExpr(self):
            return self.getTypedRuleContext(MiniGoParser.StructInitExprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def structInitList(self):
            return self.getTypedRuleContext(MiniGoParser.StructInitListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(MiniGoParser.T__35)
                self.state = 254
                self.expression(7)
                pass

            elif la_ == 2:
                self.state = 255
                self.match(MiniGoParser.T__7)
                self.state = 256
                self.expression(0)
                self.state = 257
                self.match(MiniGoParser.T__8)
                pass

            elif la_ == 3:
                self.state = 259
                self.structInitExpr()
                pass

            elif la_ == 4:
                self.state = 260
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 5:
                self.state = 261
                self.literal()
                pass

            elif la_ == 6:
                self.state = 262
                self.match(MiniGoParser.ID)
                self.state = 263
                self.match(MiniGoParser.T__10)
                self.state = 264
                self.structInitList()
                self.state = 265
                self.match(MiniGoParser.T__11)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 290
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 269
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 270
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 271
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 272
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 273
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.T__25 or _la==MiniGoParser.T__26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 274
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 275
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 276
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__31) | (1 << MiniGoParser.T__32))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 277
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 278
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 279
                        self.match(MiniGoParser.T__33)
                        self.state = 280
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 281
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 282
                        self.match(MiniGoParser.T__34)
                        self.state = 283
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 284
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 285
                        self.match(MiniGoParser.T__36)
                        self.state = 286
                        self.expression(0)
                        self.state = 287
                        self.match(MiniGoParser.T__1)
                        self.state = 288
                        self.expression(2)
                        pass

             
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StructInitExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structInitList(self):
            return self.getTypedRuleContext(MiniGoParser.StructInitListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structInitExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructInitExpr" ):
                return visitor.visitStructInitExpr(self)
            else:
                return visitor.visitChildren(self)




    def structInitExpr(self):

        localctx = MiniGoParser.StructInitExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_structInitExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MiniGoParser.ID)
            self.state = 296
            self.match(MiniGoParser.T__10)
            self.state = 297
            self.structInitList()
            self.state = 298
            self.match(MiniGoParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structInitField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructInitFieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructInitFieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structInitList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructInitList" ):
                return visitor.visitStructInitList(self)
            else:
                return visitor.visitChildren(self)




    def structInitList(self):

        localctx = MiniGoParser.StructInitListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_structInitList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.structInitField()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__9:
                self.state = 301
                self.match(MiniGoParser.T__9)
                self.state = 302
                self.structInitField()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structInitField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructInitField" ):
                return visitor.visitStructInitField(self)
            else:
                return visitor.visitChildren(self)




    def structInitField(self):

        localctx = MiniGoParser.StructInitFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_structInitField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MiniGoParser.ID)
            self.state = 309
            self.match(MiniGoParser.T__1)
            self.state = 310
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__37) | (1 << MiniGoParser.T__38) | (1 << MiniGoParser.T__39) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeID" ):
                return visitor.visitTypeID(self)
            else:
                return visitor.visitChildren(self)




    def typeID(self):

        localctx = MiniGoParser.TypeIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeID)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(MiniGoParser.T__40)
                pass
            elif token in [MiniGoParser.T__41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(MiniGoParser.T__41)
                pass
            elif token in [MiniGoParser.T__42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.match(MiniGoParser.T__42)
                pass
            elif token in [MiniGoParser.T__43]:
                self.enterOuterAlt(localctx, 4)
                self.state = 317
                self.match(MiniGoParser.T__43)
                pass
            elif token in [MiniGoParser.T__12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 318
                self.arrayType()
                pass
            elif token in [MiniGoParser.T__44]:
                self.enterOuterAlt(localctx, 6)
                self.state = 319
                self.structType()
                pass
            elif token in [MiniGoParser.T__45]:
                self.enterOuterAlt(localctx, 7)
                self.state = 320
                self.interfaceType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.T__12)
            self.state = 324
            self.match(MiniGoParser.INTLIT)
            self.state = 325
            self.match(MiniGoParser.T__13)
            self.state = 326
            self.typeID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldDeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_structType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.T__44)
            self.state = 329
            self.match(MiniGoParser.T__10)
            self.state = 331 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 330
                self.fieldDecl()
                self.state = 333 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 335
            self.match(MiniGoParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = MiniGoParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.ID)
            self.state = 338
            self.match(MiniGoParser.T__1)
            self.state = 339
            self.typeID()
            self.state = 340
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_interfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MiniGoParser.T__45)
            self.state = 343
            self.match(MiniGoParser.T__10)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 344
                self.methodDecl()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 350
            self.match(MiniGoParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def typeID(self):
            return self.getTypedRuleContext(MiniGoParser.TypeIDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(MiniGoParser.ID)
            self.state = 353
            self.match(MiniGoParser.T__7)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 354
                self.paramList()


            self.state = 357
            self.match(MiniGoParser.T__8)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 358
                self.match(MiniGoParser.T__1)
                self.state = 359
                self.typeID()


            self.state = 362
            self.match(MiniGoParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




