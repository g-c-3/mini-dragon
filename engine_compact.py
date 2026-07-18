from collections import namedtuple; Position = namedtuple('Position', 'board wtm castling ep halfmove'); E1,F1,G1,H1,D1,C1,B1,A1 = 4,5,6,7,3,2,1,0; E8,F8,G8,H8,D8,C8,B8,A8 = 116,117,118,119,115,114,113,112; KN=[-33,-31,-18,-14,14,18,31,33]; KI=[-17,-16,-15,-1,1,15,16,17]; BI=[-17,-15,15,17]; RO=[-16,-1,1,16]; QU=BI+RO; PIECE_DELTAS={'N':(KN,False),'K':(KI,False),'B':(BI,True),'R':(RO,True),'Q':(QU,True)}; CASTLES=[(True,'K',(F1,G1),H1,'R',E1,G1,'OO',(E1,F1,G1)),(True,'Q',(D1,C1,B1),A1,'R',E1,C1,'OOO',(E1,D1,C1)),(False,'k',(F8,G8),H8,'r',E8,G8,'OO',(E8,F8,G8)),(False,'q',(D8,C8,B8),A8,'r',E8,C8,'OOO',(E8,D8,C8))]; RIGHTS=((E1,'KQ'),(H1,'K'),(A1,'Q'),(E8,'kq'),(H8,'k'),(A8,'q')); MATE=100000; MAT={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}; PMG={'P':[0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0],'N':[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50],'B':[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20],'R':[0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0],'Q':[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20],'K':[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20]}; PEG=dict(PMG); PEG['K']=[-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,0,0,-10,-20,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50]; MAXP=2*(MAT['R']+MAT['B']+MAT['N'])+MAT['Q']; TT={}
def W(p): return p.isupper()
def nm(s): return "abcdefgh"[s&7]+str((s>>4)+1)
def start(): back="RNBQKBNR"; return Position(tuple(None if s&0x88 else (back[s&7] if s>>4==0 else 'P' if s>>4==1 else 'p' if s>>4==6 else back[s&7].lower() if s>>4==7 else '.') for s in range(128)), True, "KQkq", None, 0)
def king_sq(b,white): return next((s for s in range(128) if not s&0x88 and b[s]==('K' if white else 'k')), None)
def scan(b,sq,deltas,sliding):
    for d in deltas:
        t=sq+d
        while not t&0x88:
            yield t,b[t]
            if b[t]!='.' or not sliding: break
            t+=d
def attacked(b,sq,white): return any(p not in ('.',None) and W(p)==white and p.upper()==kind for kind,deltas,sliding in [(k,v[0],v[1]) for k,v in PIECE_DELTAS.items()]+[('P',(-15,-17) if white else (15,17),False)] for t,p in scan(b,sq,deltas,sliding))
def pseudo(pos):
    b,wtm,cas,ep=pos.board,pos.wtm,pos.castling,pos.ep; mv=[]
    for s in range(128):
        p=b[s]
        if p in ('.',None) or W(p)!=wtm: continue
        k=p.upper()
        if k=='P':
            fw=16 if wtm else -16; sr=1 if wtm else 6; t=s+fw
            if not t&0x88 and b[t]=='.':
                (mv.extend((s,t,False,'='+q) for q in 'QRBN') if t>>4 in (0,7) else mv.append((s,t,False,None)))
            if not t&0x88 and b[t]=='.' and s>>4==sr and b[s+2*fw]=='.': mv.append((s,s+2*fw,False,None))
            for cd in (fw-1,fw+1):
                t=s+cd
                if t&0x88: continue
                if t==ep: mv.append((s,t,True,'ep'))
                elif b[t] not in ('.',None) and W(b[t])!=wtm:
                    (mv.extend((s,t,True,'='+q) for q in 'QRBN') if t>>4 in (0,7) else mv.append((s,t,True,None)))
        else:
            for t,tp in scan(b,s,PIECE_DELTAS[k][0],PIECE_DELTAS[k][1]):
                if tp=='.' or W(tp)!=wtm: mv.append((s,t,tp!='.',None))
    mv.extend((kf,kt,False,flag) for side,right,empties,rsq,rchar,kf,kt,flag,checks in CASTLES if side==wtm and right in cas and all(b[e]=='.' for e in empties) and b[rsq]==rchar and not any(attacked(b,x,not wtm) for x in checks))
    return mv
def make_move(pos,frm,to,flag=None):
    b,wtm,cas=pos.board,pos.wtm,pos.castling; nb=list(b); p=nb[frm]; nep=None; cap=b[to] not in ('.',None) or flag=='ep'; nb[to]=p; nb[frm]='.'
    if flag=='ep': nb[to-16 if wtm else to+16]='.'
    elif flag in ('OO','OOO'):
        rf,rt=(to+1,to-1) if flag=='OO' else (to-2,to+1); nb[rt]=nb[rf]; nb[rf]='.'
    elif flag and flag[0]=='=':
        nb[to]=flag[1] if p=='P' else flag[1].lower()
    elif p.upper()=='P' and abs(to-frm)==32: nep=(frm+to)//2
    return Position(tuple(nb), not wtm, ''.join(c for c in cas if c not in ''.join(l for sq,l in RIGHTS if frm==sq or to==sq)), nep, 0 if (p.upper()=='P' or cap) else pos.halfmove+1)
def legal(pos): return [(f,t,c,fl) for f,t,c,fl in pseudo(pos) if (np:=make_move(pos,f,t,fl)) and (ks:=king_sq(np.board,pos.wtm)) is not None and not attacked(np.board,ks,not pos.wtm)]
def idx(s,w): return (s>>4)*8+(s&7) if w else (7-(s>>4))*8+(s&7)
def evaluate(b): pcs=[(s,b[s]) for s in range(128) if not s&0x88 and b[s] not in ('.',None)]; phase=sum(MAT[p.upper()] for _,p in pcs if p.upper() not in 'PK'); mg=min(1.0,phase/MAXP); sc=lambda s,p,t: (lambda w,k: (MAT[k]+t[k][idx(s,w)]) if w else -(MAT[k]+t[k][idx(s,w)]))(W(p), p.upper()); return mg*sum(sc(s,p,PMG) for s,p in pcs)+(1-mg)*sum(sc(s,p,PEG) for s,p in pcs)
def order(b,mv): return sorted(mv,key=lambda m:(100000+(MAT['P']-MAT[b[m[0]].upper()] if m[3]=='ep' else MAT[b[m[1]].upper()]-MAT[b[m[0]].upper()])) if m[2] else (PMG[b[m[0]].upper()][idx(m[1],b[m[0]].isupper())]-PMG[b[m[0]].upper()][idx(m[0],b[m[0]].isupper())]),reverse=True)
def in_check(pos): k=king_sq(pos.board,pos.wtm); return True if k is None else attacked(pos.board,k,not pos.wtm)
def poskey(pos): return (pos.board,pos.wtm,pos.castling,pos.ep)
def negamax(pos,depth,alpha,beta,root=False,seen=frozenset()):
    if not root and (pos.halfmove>=100 or poskey(pos) in seen): return 0
    if depth<=0 and not root:
        stand=evaluate(pos.board); stand=stand if pos.wtm else -stand; alpha=stand if alpha<stand else alpha
        if stand>=beta: return beta
        for f,t,c,fl in [mm for mm in order(pos.board,[m for m in legal(pos) if m[2]]) if stand+(MAT['P'] if mm[3]=='ep' else MAT[pos.board[mm[1]].upper()])+200>=alpha]:
            sc=-negamax(make_move(pos,f,t,fl),depth-1,-beta,-alpha,False,seen|{poskey(pos)})
            if sc>=beta: return beta
            alpha=sc if sc>alpha else alpha
        return alpha
    key=poskey(pos); entry=TT.get(key)
    if entry and entry[0]>=depth and not root:
        edepth,escore,eflag,emove=entry
        if eflag=='exact': return escore
        if eflag=='lower' and escore>=beta: return escore
        if eflag=='upper' and escore<=alpha: return escore
    if depth>=4 and not root and not in_check(pos) and any(pos.board[s] not in ('.',None) and W(pos.board[s])==pos.wtm and pos.board[s].upper() not in 'PK' for s in range(128)):
        if -negamax(Position(pos.board,not pos.wtm,pos.castling,None,pos.halfmove),depth-3,-beta,-beta+1,False,seen|{poskey(pos)})>=beta: return beta
    if not (mv:=legal(pos)): res=(0 if not in_check(pos) else -MATE); return (None,res) if root else res
    mv=order(pos.board,mv)
    if entry and entry[3] in mv: mv.remove(entry[3]); mv.insert(0,entry[3])
    orig_alpha=alpha; best=-float('inf'); bm=None
    for f,t,c,fl in mv:
        sc=-negamax(make_move(pos,f,t,fl),depth-1,-beta,-alpha,False,seen|{poskey(pos)}); best,bm=(sc,(f,t,c,fl)) if sc>best else (best,bm); alpha=best if best>alpha else alpha
        if alpha>=beta: break
    TT[key]=(depth,best,'lower' if best>=beta else ('exact' if best>orig_alpha else 'upper'),bm)
    return (bm,best) if root else best
def best_move(pos,max_depth,history=frozenset()):
    bm,bs=None,0
    for d in range(1,max_depth+1):
        if bm is not None:
            a,bt=bs-50,bs+50; r=negamax(pos,d,a,bt,True,history)
            if r[0] is None or not(a<r[1]<bt): r=negamax(pos,d,-float('inf'),float('inf'),True,history)
        else:
            r=negamax(pos,d,-float('inf'),float('inf'),True,history)
        if r[0] is not None: bm,bs=r
    return bm,bs
