from stmlearn.equivalencecheckers import WmethodEquivalenceChecker
from stmlearn.learners import LStarMealyLearner
from stmlearn.suls import MealyState, MealyMachine
from stmlearn.teachers import Teacher

# First, we define a Mealy machine we want to learn from.
# In "real life" this would be a black box system you don't know the implementation of
# but for the sake of simplicity, we define it in the code here.
s1 = MealyState('1')
s2 = MealyState('2')
s3 = MealyState('3')
s4 = MealyState('4')

s1.add_edge('a', 'loop', s1)
s1.add_edge('b', 'forward', s2)
s2.add_edge('a', 'loop', s2)
s2.add_edge('b', 'forward', s3)
s3.add_edge('a', 'loop', s3)
s3.add_edge('b', 'foward', s4)
s4.add_edge('a', 'win!', s4)
s4.add_edge('b', 'reset', s1)

mm = MealyMachine(s1)

# Here we set up our learning algorithm.
# We use the W-method to approximate equivalence queries,
# and use the L* learning algorithm
# The m parameter represents the upper bound of the amount of states you think the system has
eqc = WmethodEquivalenceChecker(mm, m=4)
teacher = Teacher(mm, eqc)
learner = LStarMealyLearner(teacher)

# Run the learner and collect its hypothesis
# the hypothesis returned by the learner represents the smallest possible state machine consistent with its observations
hyp = learner.run(
    show_intermediate=False,         # Draw the intermediate hypotheses
    print_observationtable=False,    # Print the observation table during the learning process
    # Uncomment this hook to pause learning after each hypothesis
    # I know, it's not pretty.
    # on_hypothesis=lambda _: input("press enter to continue\n")
)

# Draw the hypothesis
hyp.render_graph(filename="Example final hypothesis")