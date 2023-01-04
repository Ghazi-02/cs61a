(define (vir-fib n)
    (if (or (= n 1) (= n 0) ) n (+(vir-fib (- n 1))(vir-fib (- n 2))))
)


(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)

(define with-list
    (list (list 'a 'b) 'c 'd (list 'e))
)
(draw with-list)

(define (list-concat a b)
    (cond 
        ((null? a) b)
    
    
        (else  (cons (car a)  (list-concat (cdr a) b))
                    
                      
        )
    )
)    

    