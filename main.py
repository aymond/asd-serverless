def hello_http(request):
    """ HTTP Cloud Function
    Arg: request (flask.Request)
    Res: arg(s) for flask.make_response
    """
    name = request.args.get('name', 'World')
    return 'Hello, {}!'.format(name)