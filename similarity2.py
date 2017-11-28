# -*- coding: UTF-8 -*-
if __name__ == '__build__':
    raise Exception

def canonize(source):
        stop_symbols = '.,!?:;-\n\r()'

        stop_words = (u'это', u'как', u'так',
        u'и', u'в', u'над',
        u'к', u'до', u'не',
        u'на', u'но', u'за',
        u'то', u'с', u'ли',
        u'а', u'во', u'от',
        u'со', u'для', u'о',
        u'же', u'ну', u'вы',
        u'бы', u'что', u'кто',
        u'он', u'она')

        return ( [x for x in [y.strip(stop_symbols) for y in source.lower().split()] if x and (x not in stop_words)] )

def genshingle(source):
    import binascii
    shingleLen = 1 #длина шингла
    out = [] 
    for i in range(len(source)-(shingleLen-1)):
        out.append (binascii.crc32(' '.join( [x for x in source[i:i+shingleLen]] ).encode('utf-8')))

    return out

def compaire (source1,source2):
    same = 0
    for i in range(len(source1)):
        if source1[i] in source2:
            same = same + 1

    return same*2/float(len(source1) + len(source2))

def main():
    word1 = u'владением широкой общей подготовкой (базовыми знаниями) для решения практических задач в области информационных систем и технологий, в том числе для решения проблем в области интеллектуального управления CPS'
    word2 = u'владеть широкой общей подготовкой (базовыми знаниями) для решения практических задач в области информационных систем и технологий'

    cmp1 = genshingle(canonize(word1))
    cmp2 = genshingle(canonize(word2))


    print compaire(cmp1,cmp2)

# Start program
main()