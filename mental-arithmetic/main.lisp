(defvar *MAX* 1000)
(defvar *OPS* '(+ -))

(setf *random-state* (make-random-state t))

(defvar x)
(defvar y)
(defvar fn)
(defvar ans)
(defvar ans!)

(loop
  (setq x (random *MAX*))
  (setq y (random *MAX*))
  (setq fn (nth (random (list-length *OPS*)) *OPS*))
  (setq ans (funcall fn x y))

  ;  (with-standard-io-syntax
  ;	(prin1 x)
  ;	(prin1 fn))
  ;	(prin1 y)
  (format t "~d ~a ~d~%" x fn y)
  (setq ans! (read))

  (if (equalp (write-to-string ans!) "q")
      (return))

  (if (= ans! ans)
      (format t "Correct.~%")
      (format t "Incorrect: ~d~%" ans))

  (terpri))

