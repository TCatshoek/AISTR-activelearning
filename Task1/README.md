# Task 1 - Setup & Theory

Make sure you set everything up correctly before beginning. Follow the main readme file for instructions.

In `example.py` you can edit the call to `run` 
```python
hyp = learner.run(
    show_intermediate=False,         # Draw the intermediate hypotheses
    print_observationtable=False,    # Print the observation table during the learning process
    # Uncomment this hook to pause learning after each hypothesis
    # I know, it's not pretty.
    # on_hypothesis=lambda _: (print("press enter to continue"), input())
)
```
to enable showing intermediate hypotheses and enable printing the observation table. The last line you can uncomment to pause after each intermediate hypothesis, however this is not strictly required.

Observe the learning process and answer the questions posed in the assignment document.