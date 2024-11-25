def get_random_mushroom():
    return {
        "name": "Amanita muscaria",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Amanita_muscaria_3_vliegenzwammen_op_rij.jpg/640px-Amanita_muscaria_3_vliegenzwammen_op_rij.jpg",
        "growth_location": "Soil",
        "cap_shape": "Convex",
    }

questionnaire = [{
        "tag": "growth_location",
        "question": "Where is this mushroom growing?",
        "options": {
            "Soil": ("Grows on soil in forests or grasslands", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWKs2uyTN_MPnilf6B2YHHqBIFbrvA-SA1fA&s"),
            "Wood": ("Grows on decaying wood or tree stumps", "https://foragerchef.com/wp-content/uploads/2022/11/Elm-oysters-8.jpg"),
            "Dung": ("Grows on animal dung or manure", "https://thumbs.dreamstime.com/b/mushroom-growing-manure-small-mushroom-probably-yellow-fieldcap-growing-cow-dung-138382380.jpg"),
        }
    },
    {
        "tag": "cap_shape",
        "question": "What shape is the **cap** of this mushroom?",
        "options": {
            "Convex": ("Rounded and smooth, typically with a domed cap", "https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg"),
            "Conical": ("Conical in shape, resembling a cone", "https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg"),
            "Flat": ("Flat cap with little or no curvature", "https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg"),
            "Bell-shaped": ("Cap shaped like an inverted bell", "https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg"),
            "Umbonate": ("Has a raised, knob-like center", "https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg"),
            "Funnel-shaped": ("Wide, funnel-like cap that tapers towards the stem", "https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg"),
        }
    }
]