# Zero-Knowlede Proofs: Defective server
This illustrates the most basic principle of a zero-knowledge proof; it is possible to forge it if you know the challenges the server will issue to the client in advance. This is what distinguishes them from a digital signature, as it is not possible for the server to cryptographically prove to a third party that this conversation was actually with the client (though it certainly does provide some circumstantial evidence). This is because such a third party is assumed to be unable to verify the code running on the client and server, which implies that they cannot know that the parties whose communications they are examining did not use a predetermined set of challenges.

## Challenge files/setup
The challenge files are public_key.json and server.py. server.py needs to be run as a remote service, using the attached Dockerfile.

## Challenge description
I've just found out about this new authentication scheme, and I decided to try it out. I even found a way to optimize it!