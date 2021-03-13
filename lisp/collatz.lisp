(defun collatz (n)
  (format t "(collatz ~d) ->~%" n)
  (if (= n 1)
	(progn
	  (print 1)
	  (terpri)
	  (return-from collatz 1))
	(if (= 0 (mod n 2))
	  (collatz (/ n 2))
	  (collatz (+ 1 (* 3 n))))))

(compile 'collatz)
(collatz (* 3 5 7 11 13 17 19 23))
