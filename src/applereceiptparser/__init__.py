import pyparsing as pp
import base64


def parse_receipt( text ):
    ''' Given a plist-based receipt from Apple's storeKit
        return a native python datastructure.
    '''
    # Set up our grammar
    identifier = pp.Literal('"').suppress() + pp.Word(pp.alphanums+"-_") + pp.Literal('"').suppress()
    value = pp.Literal('"').suppress() + pp.Word(pp.alphanums+"-_/=+ '}{:.") + pp.Literal('"').suppress()
    cmplx = pp.Forward()
    expr = pp.Group( identifier + pp.Literal("=").suppress()  + pp.Combine( value|cmplx ) + pp.Literal(";").suppress() )
    gram = "{" + pp.OneOrMore( expr ) + "}"
    cmplx << gram 

    
    scope = {}
    for tok in gram.parseString(text):
        if len(tok) == 2:
            k = tok[0]
            if k == 'purchase-info':
                # recurse
                v = parse_receipt( base64.b64decode( tok[1] )  )
            else:
                v = tok[1]
            scope[k] = v
        else:
            if tok not in ( '{', '}' ):
                print "shenanigans", tok
    return scope

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1]).read()
    data = parse_receipt( inp )
    from pprint import pprint
    pprint( data )

