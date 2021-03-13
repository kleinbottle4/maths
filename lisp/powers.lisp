(defun power (b i)
  (if (= i 0)
      1
      (if (< i 0)
	  (/ (power b (1+ i)) b)
	  (* (power b (1- i)) b))))
