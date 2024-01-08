# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
    
    )

    st.write("# Metode Klasterisasi ")

if __name__ == "__main__":
    run()

import streamlit as st
import pandas as pd
import numpy as np

data = np.array([
    [516.012706, 393.014514],
    [436.211762, 408.656585],
    [512.052601, 372.022014],
    [489.140464, 401.807159],
    [446.207986, 338.516682]
])

index = np.array(['0', '1', '2', '3', '4'])

columns = np.array(['X', 'Y',])

objek = pd.DataFrame(data=data, index=index, columns=columns)
objek

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

st.area_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)

# Transpose data awal agar bisa di-append dengan label klaster
data_transpose = np.transpose(data)

# Append data awal dengan label klaster
data_append = np.append(data_transpose, [kmeans.labels_], axis=0)

# Kembalikan ke bentuk data awal
data_after_clustering = np.transpose(data_append)

# Konversi ke tabel data frame Pandas
columns_klasterisasi = np.array(['X', 'Y', 'Klaster'])

objek_klasterisasi = pd.DataFrame(data=data_after_clustering, index=index, columns=columns_klasterisasi)
objek_klasterisasi