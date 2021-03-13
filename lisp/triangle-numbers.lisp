(defun triangle-basic (n)
  (if (= n 1)
      1
      (+ n (triangle-basic (1- n)))))
(defun triangle (n &optional (tmp 0))
  (if (= n 0)
      (return-from triangle tmp)
      (triangle (1- n) (+ n tmp))))
(compile 'triangle)
