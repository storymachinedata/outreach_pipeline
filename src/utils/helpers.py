from datetime import datetime


def get_actual_date(url: str) -> datetime:
    """This function extracts the unix timestamp from the LinkedIn URL.

    Args:
        url (str): The URL from which the timestamp must be extracted.

    Returns:
        datetime: Returns the date extracted from the URL.
    """
    unix_timestamp = int(format(int(url.split(":")[-1]), "b")[:41], 2)
    time_stamp = datetime.fromtimestamp(unix_timestamp / 1000).strftime(
        "%Y-%m-%d %H:%M:%S %Z"
    )

    return time_stamp


def post_interaction_mapper(interaction: str):
    mapper = {
        "Post": "post",
        "liked": "liked a comment on their own post",
        "likes": "liked post",
        "commented": "commented",
        "replied": "replied to a comment",
        "celebrates": "celebrates",
        "supports": "supports",
        "insightful": "finds insightful",
        "curious": "curious",
        "loves": "loves",
        "reposted": "reposted",
        "supported": "supports",
        "loved": "loves",
        "celebrated": "celebrates",
        "funny": "funny",
    }
    if "Post" in interaction:
        return mapper["Post"]
    
    if "liked" in interaction:
        return mapper["liked"]
    elif "likes" in interaction:
        return mapper["likes"]
    elif "commented" in interaction:
        return "commented"
    elif "replied" in interaction:
        return mapper["replied"]
    elif "celebrates" in interaction:
        return mapper["celebrates"]
    elif "supports" in interaction:
        return mapper["supports"]
    elif "insightful" in interaction:
        return mapper["insightful"]
    elif "curious" in interaction:
        return mapper["curious"]
    elif "loves" in interaction:
        return mapper["loves"]
    elif "reposted" in interaction:
        return mapper["reposted"]
    elif "supported" in interaction:
        return mapper["supports"]
    elif "loved" in interaction:
        return mapper["loved"]
    elif "celebrated" in interaction:
        return mapper["celebrated"]
    elif "funny" in interaction:
        return mapper["funny"]
    else:
        raise ValueError(f"Missing value in dictionary {interaction}")


url_to_names = {
    "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/": "Leo Birnbaum",
    "https://www.linkedin.com/in/herbertdiess/": "Herbert Diess",
    "https://www.linkedin.com/in/buschroland/": "Roland Busch",
    "https://www.linkedin.com/in/markussteilemann/": "Markus Steilemann",
    "https://www.linkedin.com/in/oestberg/": "Niklas Östberg",
    "https://www.linkedin.com/in/christian-klein/": "Christian Klein",
    "https://www.linkedin.com/in/christian-bruch/": "Christian Bruch",
    "https://www.linkedin.com/in/carsten-knobel/": "Carsten Knobel",
    "https://www.linkedin.com/in/berndmontag/": "Bernd Montag",
    "https://www.linkedin.com/in/timh%C3%B6ttges/": "Tim Höttges",
    "https://www.linkedin.com/in/jocheneickholt/recent-activity/": "Jochen Eickholt",
    "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/": "Martin Brudermüller",
    "https://www.linkedin.com/in/melissad2/": "Melissa Di Donato",
    "https://www.linkedin.com/in/manasfuloria/": "Manas Human",
    "https://www.linkedin.com/in/oliver-b%C3%A4te/": "Oliver Bäte",
    "https://www.linkedin.com/in/markus-krebber/": "Markus Krebber",
}

likes_reactions_repost_mapper = {
    "post": "post",
    "liked post": "likes and reactions",
    "celebrates": "likes and reactions",
    "loves": "likes and reactions",
    "finds insightful": "likes and reactions",
    "curious": "likes and reactions",
    "supports": "likes and reactions",
    "reposted": "repost",
    "funny": "likes and reactions",
    "commented": "comments",
    "replied to a comment": "replied to a comment",
    "liked a comment on their own post": "liked a comment on their own post",
}

outrch_commnty_mangmnt_mapper = {
    "likes and reactions": "Outreach",
    "liked a comment on their own post": "Community Management",
    "comments": "Outreach",
    "replied to a comment": "Community Management",
    "reposted": "Outreach",
}

quarter_mapper = {1: [1, 3], 2: [4, 6], 3: [7, 9], 4: [10, 12]}
