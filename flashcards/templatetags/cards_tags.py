from django import template


from flashcards.models import BOXES, Card


register = template.Library()


@register.inclusion_tag("flashcards/box_links.html")
def boxes_as_links():

    boxes = []

    for box_num in BOXES:

        card_count = Card.objects.filter(box_number=box_num).count()

        boxes.append({

            "number": box_num,

            "card_count": card_count,

        })


    return {"boxes": boxes}