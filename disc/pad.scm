(define (if-program condition if-true if-false)
    `(if ,condition ,if-true ,if-false )
)
(expect (if-program '(= 0 0) '2 '3) (if (= 0 0) 2 3))
(expect (if-program '(= 1 0) '(print 3) '(print 5)) (if (= 1 0) (print 3) (print 5)))
(expect (eval (if-program '(= 0 0) '2 '3)) 2)
(expect (eval (if-program '(= 1 0) '(print 3) '(print 5))) 5)

(define (pow n p) ; just pow procedure 
  (define (helper m q)
    `(cond
        ,((= q 1) m)
        (else
            ,(helper (* n m) (- q 1)))
    )
  )
    (helper n p) 

)

(define (pow-expr base exp) 
        (cond
            ((= exp 0)
                1)
            (else
                  `(* ,(pow-expr base (- exp 1)) ,base))
            
    
        )

)

(define expr (pow-expr 5 1))
(define expr2 (pow-expr 5 2))
(expect expr
(* 1 5))
(expect (eval expr)
5)
(expect expr2 
(* (* 1 5) 5))
(expect (eval expr2)
25)

(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (swap expr)
    (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
        (cond
            ((> (eval first) (eval second)) expr)
            (else  (cons (car expr) (cons second  (cons first rest))) 
            )
        )
    )
)
(expect (swap '(- 1 (+ 3 5) 7 9))
(- (+ 3 5) 1 7 9))
(expect (swap '(* (+ 1 1) (- 2 1)))
(* (+ 1 1) (- 2 1)))