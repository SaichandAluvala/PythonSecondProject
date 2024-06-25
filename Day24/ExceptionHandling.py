"""
errors
  1. Compile time errors ( ex> Syntax error )
  2. Run time errors   ( ex> Syntax is fine but when running code there may be errors ex> 4/0 )


Code will be executed other than Run time error code-  To handle this errors we use
  " Exception handling errors "

    1. try:
         print(4/0)
       except Exception as e:
          print("4/0 could not be executed " )
        print("Thank you")

Exception, IndexError ---- Exception is good for all erros handling


  2. Finally:
      Finally will be executed even exception is executed or not

"""