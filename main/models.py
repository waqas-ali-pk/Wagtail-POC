from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index


class PostCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    materalized_path = models.TextField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title


# class BlogPage(Page):

#     # Database fields

#     body = RichTextField()
#     date = models.DateField("Post date")
#     feed_image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )

#     # Search index configuration

#     search_fields = Page.search_fields + [
#         index.SearchField('body'),
#         index.FilterField('date'),
#     ]


#     # Editor panels configuration

#     content_panels = Page.content_panels + [
#         FieldPanel('date'),
#         FieldPanel('body'), 
#         InlinePanel('related_links', heading="Related links", label="Related link"),
#     ]

#     promote_panels = [
#         MultiFieldPanel(Page.promote_panels, "Common page configuration"),
#         FieldPanel('feed_image'),
#     ]


#     # Parent page / subpage type rules

#     parent_page_types = ['main.BlogIndexPage']
#     subpage_types = []

#     api_fields = [
#         APIField('body'),
#         APIField('date'),
#         APIField('feed_image'),
#     ]


# class BlogPageRelatedLink(Orderable):
#     page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
#     name = models.CharField(max_length=255)
#     url = models.URLField()

#     panels = [
#         FieldPanel('name'),
#         FieldPanel('url'),
#     ]


# class BlogIndexPage(Page):
    

#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)

#         # Add extra variables and return the updated context
#         context['blog_entries'] = BlogPage.objects.child_of(self).live()
#         return context
        

class PostPage(Page):
    body = RichTextField()
    tags = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField("Created at", auto_now_add=True)
    updated_at = models.DateField("Updated at", auto_now=True)
    
    post_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('tags'),
        index.SearchField('category'),
        index.FilterField('created_at'),
    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        # FieldPanel('created_at'),
        # FieldPanel('updated_at'),
        FieldPanel('body'), 
        FieldPanel('tags'),
        FieldPanel('category'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('post_image'),
    ]


    # Parent page / subpage type rules

    parent_page_types = ['main.PostIndexPage']
    subpage_types = []

    api_fields = [
        APIField('body'),
        APIField('created_at'),
        APIField('updated_at'),
        APIField('tags'),
        APIField('category'),
        APIField('post_image'),
    ]


class PostIndexPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['post_entries'] = PostPage.objects.child_of(self).live()
        return context

