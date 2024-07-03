from sitetree.utils import item
from core.utils.tree import G3Wtree

# Be sure you defined `sitetrees` in your module.
sitetrees = (
  # Define a tree with `tree` function.
  G3Wtree(
        'report',
        title='G3W Report',
        module='report',
        items=[]
    ),

  # G3Wtree('report', title='G3W Report', module='report', items=[
  #     # Then define items and their children with `item` function.
  #     item('PS TIMESERIES', '#', type_header=True),
  #     item('Projects', '#', icon_css_class='fa fa-users', children=[
  #         item('Add project', 'qpstimeseries-project-add', url_as_pattern=True, icon_css_class='fa fa-plus',
  #              access_by_perms=['qps_timeseries.add_qpstimeseriesproject']),
  #         item('Projects list', 'qpstimeseries-project-list', url_as_pattern=True, icon_css_class='fa fa-list'),
  #         item('Update project {{ object.project.title }}', 'qpstimeseries-project-update object.pk', url_as_pattern=True,
  #              icon_css_class='fa fa-edit', in_menu=False, alias='qpstimeseries-project-update'),
  #     ]),
  # ]),
)