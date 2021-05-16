import word_count


def test_valid_input():
    assert word_count.count_words("Iphone is better than rubbish Android.") == 6
    assert word_count.count_words("I'm glad that this school year is almost over:)") == 9

def test_edge_input():
    assert word_count.count_words("Why was 6 afraid of 7? Because 7 8 9") == 5
    assert word_count.count_words("Hello,    It is me") == 4