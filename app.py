from flask import Flask, jsonify, render_template_string, request
import random

app = Flask(__name__)

# List of possible blog post titles
titles = [
    "5 Tips for Effective Time Management",
    "The Power of Positive Thinking",
    "How to Start a Successful Online Business",
    "10 Healthy Snacks for Busy Professionals",
    "Mastering the Art of Public Speaking",
    "The Benefits of Regular Exercise",
    "7 Ways to Boost Your Productivity",
    "The Importance of Setting Goals",
    "Top 5 Destinations for Adventure Travel",
    "Building Strong and Lasting Relationships"
]

# List of possible blog post content templates
content_templates = [
    "In this blog post, we will discuss {topic}. {Introduction}. {Body}. {Conclusion}.",
    "Are you looking for {topic}? You've come to the right place! {Introduction}. {Body}. {Conclusion}.",
    "{topic} is an important aspect of {industry}. In this post, we'll explore its significance. {Introduction}. {Body}. {Conclusion}.",
    "Do you want to learn more about {topic}? This blog post is here to help you out. {Introduction}. {Body}. {Conclusion}."
]

# List of keywords for SEO optimization
keywords = [
    "time management", "positive thinking", "online business", "healthy snacks",
    "public speaking", "regular exercise", "productivity", "goal setting",
    "adventure travel", "building relationships"
]

# Constants for SEO optimization
MAX_KEYWORD_OCCURRENCE = 3
MAX_META_DESCRIPTION_LENGTH = 160

def generate_blog_post(topic):
    # Randomly select a title from the list
    title = random.choice(titles)
    
    # Generate the content based on the selected topic
    introduction_template = [
        f"{topic} is a crucial aspect of our lives.",
        f"In today's fast-paced world, {topic} is of utmost importance.",
        f"Let's dive into the world of {topic} and its significance."
    ]
    introduction = random.choice(introduction_template)
    
    body_template = [
        f"{topic} enables us to make the most of our time and resources.",
        f"{topic} helps us achieve our goals effectively.",
        f"With proper {topic}, we can reduce stress and improve productivity.",
        f"The art of {topic} is essential for success in various areas."
    ]
    body = random.choice(body_template)
    
    conclusion_template = [
        f"In conclusion, {topic} is a key factor in achieving success.",
        f"Mastering the art of {topic} can lead to a more fulfilling life.",
        f"By practicing {topic}, we can achieve a work-life balance.",
        f"{topic} is an invaluable skill that we should all strive to improve."
    ]
    conclusion = random.choice(conclusion_template)
    
    content = f"{introduction} {body} {conclusion}"
    
    # Perform keyword frequency analysis
    keyword_occurrence = content.count(topic)
    if keyword_occurrence > MAX_KEYWORD_OCCURRENCE:
        # Reduce keyword repetition if it exceeds the maximum allowed
        content = content.replace(topic, '', keyword_occurrence - MAX_KEYWORD_OCCURRENCE)
    
    # Generate the title tag based on the title and topic
    title_tag = f"{title} - {topic}"
    
    # Generate the meta description based on the content and topic
    meta_description = content[:MAX_META_DESCRIPTION_LENGTH]
    
    # Combine the title tag, content, and meta description to form the blog post
    blog_post = {
        "title": title,
        "topic": topic,
        "content": content,
        "meta_description": meta_description
    }
    
    return blog_post

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

@app.route('/generate_blog_post', methods=['POST'])
def generate_blog_post_route():
    topic = request.form['topic']
    blog_post = generate_blog_post(topic)
    return jsonify(blog_post)

if __name__ == '__main__':
    app.run(debug=True)
