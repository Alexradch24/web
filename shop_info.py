from messages_pb2 import ProdReply

cat_arr = [
    'Выпечка',
    'Алкоголь',
    'Готовая еда',
]

prod_arr = [
    {
        'category':'Выпечка',
        'prod_price':{
            'Хлеб':ProdReply.Price(pr=25),
            'Булочка с маком':ProdReply.Price(pr=50),
        },
    },
    {
        'category':'Алкоголь',
        'prod_price':{
            'Вино белое':ProdReply.Price(pr=799),
            'Вино красное':ProdReply.Price(pr=990),
        },
    },
    {
        'category':'Готовая еда',
        'prod_price':{
            'Суп куриный':ProdReply.Price(pr=145),
        },
    },
]