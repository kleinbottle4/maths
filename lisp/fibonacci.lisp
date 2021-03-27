;;; Here is the Fibonacci sequence, solved
;;; procedurally, in the C programming language:

int fib(int n)
{
    int a = 0, b = 1, tmp;
    for (int i = 1; i < n; i++) {
        tmp = b;
        b += a;
        a = tmp;
    }
    return a;
}

;; However, it can be defined very elegantly with
;; "simple" recursion:
(defun fib-1 (n)
  (cond ((= n 1) 0)
	    ((= n 2) 1)
	    (t (+ (fib-1 (- n 2)) (fib-1 (- n 1))))))

;; Here is another definition, which is less elegant,
;; but faster for a computer to run
(defun fib-2 (n &optional (i 0) (j 1))
  (if (= n 1)
      (return-from fib-2 i)
      (fib-2 (- n 1) j (+ i j))))

(compile 'fib-2)
