; ex 1.1 : sicp 

(display 10) (newline)
(display (+ 5 3 4)) (newline)
(display (- 9 1)) (newline)
(display (/ 6 2)) (newline)
(display (+ (* 2 4) (- 4 6)))(newline)
(define a 3)
(define b (+ a 1))
(display (+ a b (* a b))) (newline) 
(= a b)
(if (and (> b a) (< b (* a b)))
   (display b)
   (display a)) (newline)
(cond ((= a 4) (display 6) (newline))
      ((= b 4) (display (+ 6 7 a)) (newline))
      (else (display 25)))
(display a) (newline)
(define d 5)
(define c 17)
(display (= c d)) (newline)
(display c) (newline)
(display (+ 2 (if (> b a) b a))) (newline)
(display (* (cond ((> a b) a)
         ((< a b) b)
         (else -1))
   (+ a 1)))
(newline)

; ex1.2 : sicp

(display 
       (/
        (+ 5 (/ 1 2) (- 2 (- 3 ( + 6 ( / 1 5)))))
        (* 3 (- 6 2) (- 2 7))
       )
)
(newline)

; ex1.3 :

; Define a procedure that takes three numbers as arguments and return the 
; sum of the squares of the two larger numbers

; procedure to calculate sum of squares
; of two numbers

(define (sum-of-squares a1 a2) 
        (+ (* a1 a1) (* a2 a2))
)

(display (sum-of-squares 3 4))
(newline)

; procedure to calculate the greatest of two numbers

(define (greater a1 a2)
        (if (> a1 a2) 
            a1 
            a2
        )
)

(display (greater 4 5))
(newline)

(define (lesser a1 a2)
        (if (< a1 a2)
            a1
            a2
        )
)

(display (lesser 3 4))
(newline)

(define (compute-mid a1 a2 a3)
        ;(define n1 (greater (greater a1 a2) a3))
        ;(define n2 (lesser (lesser a1 a2) a3))
        (if (and (< a1 a2) (< a2 a3))
            a2
           (if (and (<= a3 a2) (<= a2 a1))
              a2
              (if (and (<= a2 a1) (<= a1 a3))
                 a1
                 (if (and (<= a3 a1) (<= a1 a2))
                    a1
                    (if (and (<= a1 a3) (<= a3 a2))
                       a3
                       (if (and (<= a2 a3) (<= a3 a1))
                          a3
                     
                       )
                    )
                 )
              )
           )
        )

)
      


(display (compute-mid 3 4 5)) 
(newline)



(define (sum-of-squares-greater-two a1 a2 a3)
        (define n1 (greater (greater a1 a2) a3))  
        (define n2 (compute-mid a1 a2 a3))
        (sum-of-squares n1 n2)
)


(display (sum-of-squares-greater-two 6 2 3))
(newline)



