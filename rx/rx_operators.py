from rx import of, operators as op


# source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

# composed = source.pipe(
#     op.map(lambda s: len(s)),
#     op.filter(lambda i: i >= 5)
# )
# composed.subscribe(lambda value: print("Received {0}".format(value)))


# of
# def of(*args: Any) -> Observable:
#     """This method creates a new observable sequence whose elements are taken
#     from the arguments.

#     .. marble::
#         :alt: of

#         [    of(1,2,3)    ]
#         ---1--2--3--|

#     Note:
#         This is just a wrapper for
#         :func:`rx.from_iterable(args) <rx.from_iterable>`

#     Example:
#         >>> res = rx.of(1,2,3)

#     Args:
#         args: The variable number elements to emit from the observable.

#     Returns:
#         The observable sequence whose elements are pulled from the
#         given arguments
#     """

# pipe
# Examples:
#     >>> source.pipe() == source
#     >>> source.pipe(f) == f(source)
#     >>> source.pipe(g, f) == f(g(source))
#     >>> source.pipe(h, g, f) == f(g(h(source)))


of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    op.map(lambda s: len(s)), op.filter(lambda i: i >= 4)
).subscribe(lambda value: print("Received {0}".format(value)))
