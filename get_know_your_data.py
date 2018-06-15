import util
import urls

df = util.get_data(urls.CHIPOTLE_URL)

print(df)

util.show_dataframe_info(df)
most_ordered_items = util.get_most_ordered_item(df)
print(most_ordered_items)
print(util.get_head(most_ordered_items))
times_items_ordered = util.get_times_items_were_ordered(df)
print(util.get_head(times_items_ordered))
most_ordered_items_by_choice_description = util.get_most_ordered_item_by_choice_description(df)
print(util.get_head(most_ordered_items_by_choice_description))

total_ordered_items = util.get_ordered_items_in_total(df)
print('total ordered items: ',total_ordered_items)
