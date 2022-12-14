(define-macro (multi-assign sym1 sym2 expr1 expr2)
    `(cons (define ,sym1 ,expr1)(cons (define ,sym2 ,expr2) nil))
)

(define-macro (multi-assign sym1 sym2 expr1 expr2)
    `(begin (define ,sym2 (list ,expr1 ,expr2))
            (define ,sym1 (car ,sym2))
            (define ,sym2 (car (cdr ,sym2)))
            undefined))
(define (replace-helper e o n)
  (if (null? e) ()
      (eq? (car e) o) (cons n (replace-helper ( cdr e) o n))
      (replace-helper (cdr e ) o n)))
(define-macro (replace expr old new)
    (replace-helper expr old new))

(define (sum lst)
  (define (sumAll lst total)
    (cond 
    ((null? lst) total)
    (else (sumAll (cdr lst) (+ total (car lst))))   
        )
  )
  (sumAll lst 0)
)
(expect (sum '(1 2 3)) 6)
(expect (sum '(10 -3 4)) 11)

(define (reverse lst)
  (define (helper lst result length )
    (cond
        
        ((= length 0) result) 
        (else (helper  (cdr lst) (cons (car lst) result) (- length 1)))
        )
  )
  (helper lst nil (length lst))
)

(expect (reverse '(1 2 3)) (3 2 1))
(expect (reverse '(0 9 1 2)) (2 1 9 0))

