from django.db import models
from datetime import date

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField

from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    pass


class BlogPage(Page):
    date = models.DateField("Post date", default=date.today)
    author_name = RichTextField(max_length=100, blank=True)
    subtitle = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('blockquote', blocks.BlockQuoteBlock()),
        ('code', blocks.TextBlock()),  # or use a custom CodeBlock if needed
        ('markdown', blocks.TextBlock()),
        ('embed', EmbedBlock()),
        ('highlight', blocks.RichTextBlock(features=["bold", "italic"])),
        ('document', DocumentChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author_name'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

