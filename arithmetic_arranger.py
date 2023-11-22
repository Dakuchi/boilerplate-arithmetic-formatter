def arithmetic_arranger(problems, option=False):
  if len(problems) > 5:
    err_log = "Error: Too many problems."
    return err_log
  else:
    output_line = [""] * 4
    left_operand = []
    right_operand = []
    ope = []
    leng = []
    err = False
    for i in problems:
      prob = i.split()
      if prob[1] != "+" and prob[1] != "-":
        err_log = "Error: Operator must be '+' or '-'."
        err = True
      elif not (prob[0].isnumeric() and prob[2].isnumeric()):
        err_log = "Error: Numbers must only contain digits."
        err = True
      elif (len(prob[0]) > 4) or (len(prob[2]) > 4):
        err_log = "Error: Numbers cannot be more than four digits."
        err = True
      else:
        num_len = max(len(prob[0]), len(prob[2]))
        max_len = num_len + 2
        left_operand.append(prob[0])
        ope.append(prob[1])
        right_operand.append(prob[2])
        leng.append(max_len)
    if not err:
      for i in range(len(problems)):
        output_line[0] += left_operand[i].rjust(leng[i])
        if i < (len(problems) - 1): output_line[0] += "    "
        output_line[1] += ope[i] + right_operand[i].rjust(leng[i] - 1)
        if i < (len(problems) - 1): output_line[1] += "    "
        output_line[2] += "-" * leng[i]
        if i < (len(problems) - 1): output_line[2] += "    "
        if ope[i] in "+":
          re = str(int(left_operand[i]) + int(right_operand[i]))
        else:
          re = str(int(left_operand[i]) - int(right_operand[i]))
        output_line[3] += (str(re)).rjust(leng[i])
        if i < (len(problems) - 1): output_line[3] += "    "
      if option is True:
        arranged_problems = "\n".join(output_line)
      else:
        arranged_problems = "\n".join(output_line[0:3])
      return arranged_problems
    else:
      return err_log
