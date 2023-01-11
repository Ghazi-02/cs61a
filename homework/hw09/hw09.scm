(define-macro (when condition exprs)
  
  (cond 
  ((eval condition) (cons 'begin exprs))
  (else (print 'okay))
  )
)



(define-macro (switch expr cases)
  (define (helper lst)
    (cond 
    ((eq? (eval expr) (car (car lst))) (car (cdr (car lst))))
    (else (helper (cdr lst)))
      )
    )
  (helper cases)
  )