(defun collatz (n) (if (= n 1) (return-from collatz 1) (if (= 0 (mod n 2)) (collatz (/ n 2)) (collatz (+ 1 (* 3 n))))))
