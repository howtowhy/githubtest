import tensorflow as tf
sess = tf.InteractiveSession()
c = tf.linspace( 0.0, 4.0, 5 )
print("The content of ''c'': \n {} \n".format( c.eval() ))
sess.close()

print("hello")
print("hi")
print("nice day")
print("only this")

# branch example
print("new day")
print("start!")
# new branch
print("hahahoho")
print("coding")
print("원격저장소")