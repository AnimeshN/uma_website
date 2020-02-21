# from django.db import models
# from wagtail.images.blocks import ImageChooserBlock
# from wagtail.core.models import Page
# from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import StreamField


# from streams import blocks

# class MediaPage(Page):
#     template = "media_gallery/mediagallery_page.html"
    
#     content = StreamField(
# 		[
# 			("img_upload",blocks.MediaBlock())
# 		],
# 		null=True,
# 		blank=True,
# 	) 

#     content_panels = Page.content_panels + [
         
#          StreamFieldPanel("content"),
        
#         ]

#     class Meta:
#          verbose_name = "Media Gallery Page" 
 


