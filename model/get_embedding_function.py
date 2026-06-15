{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cc83ac71",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'get_embedding_function'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mget_embedding_function\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m get_embedding_function\n\u001b[0;32m      3\u001b[0m embeddings \u001b[38;5;241m=\u001b[39m get_embedding_function()\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mlen\u001b[39m(embeddings\u001b[38;5;241m.\u001b[39membed_query(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;124m\"\u001b[39m)))\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'get_embedding_function'"
     ]
    }
   ],
   "source": [
    "from get_embedding_function import get_embedding_function\n",
    "\n",
    "embeddings = get_embedding_function()\n",
    "print(len(embeddings.embed_query(\"hello\")))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7089864a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
