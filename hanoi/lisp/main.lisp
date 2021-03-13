(defun sum-list (l1 l2)
  (when (and l1 l2)
	(cons
	  (+ (car l1) (car l2))
	  (sum-list (cdr l1) (cdr l2)))))

(defun bump (len bi b k &optional (i 0))
  (if (= i len)
	nil
	(cons
	  (if (= i bi) b k)
	  (bump len bi b k (1+ i)))))

(defun move (stacks f to)
  (print stacks)
  (terpri)
  (format t "Move a disc from stack ~d to stack ~d." f to)
  (let ((l (list-length stacks)))
	(sum-list
	  (sum-list
		(bump l f  -1 0)
		(bump l to +1 0))
	  stacks)))

(defun hanoi (s n f to v)
  (if (= n 0)
	s
	(hanoi
	  (hanoi (move s f to) (1- n) f v to)
	  (1- n) v to f)))

(defvar *s* '(3 0 0))
(print *s*) (terpri)
(let
  ((l (list-length *s*)))
  (print
	(hanoi *s* l 0 2 1)))
(terpri)
