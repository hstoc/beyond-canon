class Chapter:
    def __init__(self, number, title, page):
        self.number = number
        self.title = title.replace("’", "'")
        self.page = page
    
    def __repr__(self):
        return f"Chapter({self.number}, {self.title}, {self.page})"
    
    def html(self):
        title = self.title.replace("'", "&apos;")
        s = ""
        s += f'<tr class="chapter">\n'
        s += f'  <td class="chapter-number">{self.number}.</td>\n'
        s += f'  <td class="chapter-title">{title}</td>\n'
        s += f'  <td class="page-link"><a href="https://beyondcanon.com/story/{self.page}">{self.page}</a></td>\n'
        s += f'</tr>'
        return s
    
chapters = [
    Chapter("..", "Somewhere, in the distant reaches of space...", 1),
    Chapter(1, "Ghostflusters", 33),
    Chapter(2, "Clown Logistics", 57),
    Chapter(3, "How Are Your Feelings", 96),
    Chapter(4, "The Contest", 119),
    Chapter(5, "YOUR 3Y3S H4V3 B33N CLOS3D", 144),
    Chapter(6, "A Conversation Regarding Relevance", 145),
    Chapter(7, "Distress Call From the Closet", 170),
    Chapter(8, "A Daughter Astray", 192),
    Chapter(9, "How Goes The Eulogizing, Dear?", 236),
    Chapter(10, "1 WOND3R WH4T TH3Y T4ST3 L1K3", 263),
    Chapter(11, "History's Most Notorious Haters", 277),
    Chapter(12, "Really Convoluted Metaphorical Horseshit", 291),
    Chapter(13, "The Funeral", 303),
    Chapter(14, "The Best Laid Plans", 327),
    Chapter(15, "Ok So There’s This Flower", 376),
    Chapter(16, "Welcome to my Secret Lair", 394),

    # Start of non-official chapters
    Chapter(17, "TH1S T1M3 1’LL G3T 1T R1GHT", 408),
    Chapter(18, "Re-Dead", 441),
    Chapter(19, "I Was The Bitches?", 443),
    Chapter(20, "The Arduous Task of Being a Vriska", 455),
    Chapter(21, "We Don’t Got Time for This Who Over", 476),
    Chapter(22, "Everyone's Out of Character", 486),
    Chapter(23, "Fathoming its Vast Vastness", 497),
    Chapter(24, "It All Kinda Blurs Together", 510),
    Chapter(25, "Methodically Cycling Through Neckwear", 533),
    Chapter(26, "I Knew You Would Forgive Me", 554),
    Chapter(27, "Majyyked To An Untimely Slumber", 577),
    Chapter(28, "Getting The Baby's Room Ready", 602),
    Chapter(29, "Bring in the Mothafuckin Lobsters", 615),
    Chapter(30, "I Think I Can Let This One Go", 626),
    Chapter(31, "My Narratively Significant Friend", 638),
    Chapter(32, "Multichromatic Circus Freak Rejects", 656),
    Chapter(33, "Hyperbolic Helltier Chamber", 666),
]

for chapter in chapters:
    print(chapter.html())