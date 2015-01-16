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

