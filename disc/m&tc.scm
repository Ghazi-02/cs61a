(define-macro (multi-assign sym1 sym2 expr1 expr2)
    `(cons (define ,sym1 ,expr1)(cons (define ,sym2 ,expr2) nil))
)

(define-macro (multi-assign sym1 sym2 expr1 expr2)
    `(begin (define ,sym2 (list ,expr1 ,expr2))
            (define ,sym1 (car ,sym2))
            (define ,sym2 (car (cdr ,sym2)))
            undefined))
