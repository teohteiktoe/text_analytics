#!/usr/bin/env python
# coding: utf-8

# In[15]:


from textblob import TextBlob


# In[16]:


from flask import Flask


# In[17]:


app = Flask(__name__)


# In[18]:


from flask import render_template,request


# In[19]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:




