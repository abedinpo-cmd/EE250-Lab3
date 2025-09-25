# EE250-Lab3

# Aava Abedinpour
# Conrad Nelson

Question 1: Why are RESTful APIs scalable?

REST optimizes client-server interactions. Because they are stateless, the server doesn't have to remember past client request information. Also, their well-managed caching reduces the number and time cost of some client-server interactions, improving efficiency further. 


Question 2: According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients?

The resources are the mail entries.

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

Our mail server does not use PUT. It can be used to edit existing mail entries. The client would send a JSON body with updated fields, and the server would replace the old entry.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
