# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u019a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\7\60\u0123")
        buf.write("\n\60\f\60\16\60\u0126\13\60\3\61\3\61\3\61\7\61\u012b")
        buf.write("\n\61\f\61\16\61\u012e\13\61\5\61\u0130\n\61\3\62\6\62")
        buf.write("\u0133\n\62\r\62\16\62\u0134\3\62\3\62\6\62\u0139\n\62")
        buf.write("\r\62\16\62\u013a\3\62\3\62\5\62\u013f\n\62\3\62\6\62")
        buf.write("\u0142\n\62\r\62\16\62\u0143\5\62\u0146\n\62\3\62\6\62")
        buf.write("\u0149\n\62\r\62\16\62\u014a\3\62\3\62\5\62\u014f\n\62")
        buf.write("\3\62\6\62\u0152\n\62\r\62\16\62\u0153\5\62\u0156\n\62")
        buf.write("\3\63\6\63\u0159\n\63\r\63\16\63\u015a\3\63\3\63\3\63")
        buf.write("\3\63\6\63\u0161\n\63\r\63\16\63\u0162\3\63\5\63\u0166")
        buf.write("\n\63\3\64\3\64\3\64\3\64\7\64\u016c\n\64\f\64\16\64\u016f")
        buf.write("\13\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0177\n\65\f")
        buf.write("\65\16\65\u017a\13\65\3\65\5\65\u017d\n\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\7\66\u0186\n\66\f\66\16\66\u0189")
        buf.write("\13\66\3\66\3\66\3\66\3\66\3\66\3\67\6\67\u0191\n\67\r")
        buf.write("\67\16\67\u0192\3\67\3\67\38\38\39\39\3\u0187\2:\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:\3\2\r\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\6\2\f\f\17\17$$^^\n\2$$\61\61^^ddhhppttvv\3\3\f\f")
        buf.write("\5\2\13\f\17\17\"\"\6\2%%((BB``\2\u01af\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3\2")
        buf.write("\2\2\5w\3\2\2\2\7y\3\2\2\2\t{\3\2\2\2\13}\3\2\2\2\r\u0083")
        buf.write("\3\2\2\2\17\u0088\3\2\2\2\21\u008d\3\2\2\2\23\u008f\3")
        buf.write("\2\2\2\25\u0091\3\2\2\2\27\u0093\3\2\2\2\31\u0095\3\2")
        buf.write("\2\2\33\u0097\3\2\2\2\35\u0099\3\2\2\2\37\u009b\3\2\2")
        buf.write("\2!\u009e\3\2\2\2#\u00a5\3\2\2\2%\u00a8\3\2\2\2\'\u00ad")
        buf.write("\3\2\2\2)\u00b1\3\2\2\2+\u00b4\3\2\2\2-\u00ba\3\2\2\2")
        buf.write("/\u00c3\3\2\2\2\61\u00c5\3\2\2\2\63\u00c7\3\2\2\2\65\u00c9")
        buf.write("\3\2\2\2\67\u00cb\3\2\2\29\u00cd\3\2\2\2;\u00d0\3\2\2")
        buf.write("\2=\u00d3\3\2\2\2?\u00d5\3\2\2\2A\u00d8\3\2\2\2C\u00da")
        buf.write("\3\2\2\2E\u00dd\3\2\2\2G\u00e0\3\2\2\2I\u00e3\3\2\2\2")
        buf.write("K\u00e5\3\2\2\2M\u00e7\3\2\2\2O\u00ec\3\2\2\2Q\u00f2\3")
        buf.write("\2\2\2S\u00f6\3\2\2\2U\u00fa\3\2\2\2W\u0100\3\2\2\2Y\u0108")
        buf.write("\3\2\2\2[\u010f\3\2\2\2]\u0116\3\2\2\2_\u0120\3\2\2\2")
        buf.write("a\u012f\3\2\2\2c\u0155\3\2\2\2e\u0165\3\2\2\2g\u0167\3")
        buf.write("\2\2\2i\u0172\3\2\2\2k\u0180\3\2\2\2m\u0190\3\2\2\2o\u0196")
        buf.write("\3\2\2\2q\u0198\3\2\2\2st\7x\2\2tu\7c\2\2uv\7t\2\2v\4")
        buf.write("\3\2\2\2wx\7<\2\2x\6\3\2\2\2yz\7?\2\2z\b\3\2\2\2{|\7=")
        buf.write("\2\2|\n\3\2\2\2}~\7e\2\2~\177\7q\2\2\177\u0080\7p\2\2")
        buf.write("\u0080\u0081\7u\2\2\u0081\u0082\7v\2\2\u0082\f\3\2\2\2")
        buf.write("\u0083\u0084\7v\2\2\u0084\u0085\7{\2\2\u0085\u0086\7r")
        buf.write("\2\2\u0086\u0087\7g\2\2\u0087\16\3\2\2\2\u0088\u0089\7")
        buf.write("h\2\2\u0089\u008a\7w\2\2\u008a\u008b\7p\2\2\u008b\u008c")
        buf.write("\7e\2\2\u008c\20\3\2\2\2\u008d\u008e\7*\2\2\u008e\22\3")
        buf.write("\2\2\2\u008f\u0090\7+\2\2\u0090\24\3\2\2\2\u0091\u0092")
        buf.write("\7.\2\2\u0092\26\3\2\2\2\u0093\u0094\7}\2\2\u0094\30\3")
        buf.write("\2\2\2\u0095\u0096\7\177\2\2\u0096\32\3\2\2\2\u0097\u0098")
        buf.write("\7]\2\2\u0098\34\3\2\2\2\u0099\u009a\7_\2\2\u009a\36\3")
        buf.write("\2\2\2\u009b\u009c\7<\2\2\u009c\u009d\7?\2\2\u009d \3")
        buf.write("\2\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4\"\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7$\3\2\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa")
        buf.write("\7n\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7g\2\2\u00ac&\3")
        buf.write("\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0(\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3*\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9")
        buf.write("\7m\2\2\u00b9,\3\2\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2.\3\2\2\2\u00c3\u00c4\7,\2\2\u00c4\60\3\2")
        buf.write("\2\2\u00c5\u00c6\7\61\2\2\u00c6\62\3\2\2\2\u00c7\u00c8")
        buf.write("\7\'\2\2\u00c8\64\3\2\2\2\u00c9\u00ca\7-\2\2\u00ca\66")
        buf.write("\3\2\2\2\u00cb\u00cc\7/\2\2\u00cc8\3\2\2\2\u00cd\u00ce")
        buf.write("\7?\2\2\u00ce\u00cf\7?\2\2\u00cf:\3\2\2\2\u00d0\u00d1")
        buf.write("\7#\2\2\u00d1\u00d2\7?\2\2\u00d2<\3\2\2\2\u00d3\u00d4")
        buf.write("\7>\2\2\u00d4>\3\2\2\2\u00d5\u00d6\7>\2\2\u00d6\u00d7")
        buf.write("\7?\2\2\u00d7@\3\2\2\2\u00d8\u00d9\7@\2\2\u00d9B\3\2\2")
        buf.write("\2\u00da\u00db\7@\2\2\u00db\u00dc\7?\2\2\u00dcD\3\2\2")
        buf.write("\2\u00dd\u00de\7(\2\2\u00de\u00df\7(\2\2\u00dfF\3\2\2")
        buf.write("\2\u00e0\u00e1\7~\2\2\u00e1\u00e2\7~\2\2\u00e2H\3\2\2")
        buf.write("\2\u00e3\u00e4\7#\2\2\u00e4J\3\2\2\2\u00e5\u00e6\7A\2")
        buf.write("\2\u00e6L\3\2\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7t\2")
        buf.write("\2\u00e9\u00ea\7w\2\2\u00ea\u00eb\7g\2\2\u00ebN\3\2\2")
        buf.write("\2\u00ec\u00ed\7h\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7")
        buf.write("n\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1\7g\2\2\u00f1P\3\2")
        buf.write("\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5R\3\2\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7v\2\2\u00f9T\3\2\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7v\2\2\u00ffV\3\2\2\2\u0100\u0101")
        buf.write("\7d\2\2\u0101\u0102\7q\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7n\2\2\u0104\u0105\7g\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7p\2\2\u0107X\3\2\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7v\2\2\u010a\u010b\7t\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7i\2\2\u010eZ\3\2\2\2\u010f\u0110")
        buf.write("\7u\2\2\u0110\u0111\7v\2\2\u0111\u0112\7t\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7e\2\2\u0114\u0115\7v\2\2\u0115\\")
        buf.write("\3\2\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\u011a\7g\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7h\2\2\u011c\u011d\7c\2\2\u011d\u011e\7e\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f^\3\2\2\2\u0120\u0124\t\2\2\2\u0121\u0123")
        buf.write("\t\3\2\2\u0122\u0121\3\2\2\2\u0123\u0126\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125`\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0127\u0130\7\62\2\2\u0128\u012c\t\4\2")
        buf.write("\2\u0129\u012b\t\5\2\2\u012a\u0129\3\2\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0127\3\2\2\2")
        buf.write("\u012f\u0128\3\2\2\2\u0130b\3\2\2\2\u0131\u0133\t\5\2")
        buf.write("\2\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0138\7\60\2\2\u0137\u0139\t\5\2\2\u0138\u0137\3\2\2")
        buf.write("\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\u0145\3\2\2\2\u013c\u013e\t\6\2\2\u013d")
        buf.write("\u013f\t\7\2\2\u013e\u013d\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f\u0141\3\2\2\2\u0140\u0142\t\5\2\2\u0141\u0140\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u013c\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0156\3\2\2\2\u0147\u0149\t\5\2\2")
        buf.write("\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e")
        buf.write("\t\6\2\2\u014d\u014f\t\7\2\2\u014e\u014d\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u0152\t\5\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0132")
        buf.write("\3\2\2\2\u0155\u0148\3\2\2\2\u0156d\3\2\2\2\u0157\u0159")
        buf.write("\t\5\2\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015d\7\60\2\2\u015d\u0166\b\63\2\2\u015e\u0160")
        buf.write("\7\60\2\2\u015f\u0161\t\5\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\b\63\3\2\u0165\u0158")
        buf.write("\3\2\2\2\u0165\u015e\3\2\2\2\u0166f\3\2\2\2\u0167\u016d")
        buf.write("\7$\2\2\u0168\u016c\n\b\2\2\u0169\u016a\7^\2\2\u016a\u016c")
        buf.write("\t\t\2\2\u016b\u0168\3\2\2\2\u016b\u0169\3\2\2\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7")
        buf.write("$\2\2\u0171h\3\2\2\2\u0172\u0178\7$\2\2\u0173\u0177\n")
        buf.write("\b\2\2\u0174\u0175\7^\2\2\u0175\u0177\t\t\2\2\u0176\u0173")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017c\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017b\u017d\t\n\2\2\u017c\u017b\3")
        buf.write("\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b\65\4\2\u017f")
        buf.write("j\3\2\2\2\u0180\u0181\7\61\2\2\u0181\u0182\7,\2\2\u0182")
        buf.write("\u0187\3\2\2\2\u0183\u0186\5k\66\2\u0184\u0186\13\2\2")
        buf.write("\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0187\u0185\3\2\2\2\u0188")
        buf.write("\u018a\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\7,\2\2")
        buf.write("\u018b\u018c\7\61\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\b\66\5\2\u018el\3\2\2\2\u018f\u0191\t\13\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\b\67\5")
        buf.write("\2\u0195n\3\2\2\2\u0196\u0197\t\f\2\2\u0197p\3\2\2\2\u0198")
        buf.write("\u0199\13\2\2\2\u0199r\3\2\2\2\32\2\u0124\u012c\u012f")
        buf.write("\u0134\u013a\u013e\u0143\u0145\u014a\u014e\u0153\u0155")
        buf.write("\u015a\u0162\u0165\u016b\u016d\u0176\u0178\u017c\u0185")
        buf.write("\u0187\u0192\6\3\63\2\3\63\3\3\65\4\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    ID = 47
    INTLIT = 48
    FLOATLIT = 49
    ILLEGAL_FLOAT = 50
    STRINGLIT = 51
    UNCLOSE_STRING = 52
    COMMENT = 53
    WS = 54
    ERROR_CHAR = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "':'", "'='", "';'", "'const'", "'type'", "'func'", 
            "'('", "')'", "','", "'{'", "'}'", "'['", "']'", "':='", "'return'", 
            "'if'", "'else'", "'for'", "'in'", "'break'", "'continue'", 
            "'*'", "'/'", "'%'", "'+'", "'-'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'&&'", "'||'", "'!'", "'?'", "'true'", "'false'", 
            "'nil'", "'int'", "'float'", "'boolean'", "'string'", "'struct'", 
            "'interface'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "ILLEGAL_FLOAT", "STRINGLIT", "UNCLOSE_STRING", 
            "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "ID", "INTLIT", "FLOATLIT", "ILLEGAL_FLOAT", 
                  "STRINGLIT", "UNCLOSE_STRING", "COMMENT", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.ILLEGAL_FLOAT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[:-1]; raise ErrorToken(self.text + ".");
     

        if actionIndex == 1:
            self.text = self.text; raise ErrorToken(self.text);
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    text = self.text[1:]  # Remove leading quote
                    if text[-1] in ['\n', '\r']: 
                        raise UncloseString(text[:-1])  # Remove trailing newline if present
                    else:
                        raise UncloseString(text) 
                
     


