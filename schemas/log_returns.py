{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "304ac77e-c924-41a9-a597-c155e7db28f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandera.pandas as pa\n",
    "\n",
    "schema_log_returns = pa.DataFrameSchema(\n",
    "    {\n",
    "        \"LogReturn\": pa.Column(\n",
    "            float,\n",
    "            checks=[\n",
    "                pa.Check.greater_than(-1),\n",
    "                pa.Check.less_than(1)\n",
    "            ],\n",
    "            nullable=False,\n",
    "        )\n",
    "    },\n",
    "    index=pa.Index(\n",
    "        pa.DateTime,\n",
    "        name=\"Date\",\n",
    "        checks=[\n",
    "            pa.Check.in_range('2021-01-01', '2021-12-31'),\n",
    "            # pa.Check(lambda idx: idx.is_monotonic_incressing, element_wise=False)\n",
    "        ]\n",
    "    ),\n",
    "    strict=True, #nie moze miec wiecej kolumn niz tu mamy zdefiniownaych\n",
    "    coerce=True\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be502b24-c27c-4549-9b1b-902269eca446",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
