(define-macro (when condition exprs)
  
  (cond 
  ((eval condition) (cons 'begin exprs))
  (else (print 'okay))
  )
)

(define-macro (switch expr cases)
  (cons _________
        (map (_________ (_________)
                        (cons _________ (cdr case)))
             cases)))
