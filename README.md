The primary purpose of it was for dealing with wash sale losses, to run a different version of the symphonies in the month of December, for instance. Additionally, it is useful for creating an alternate version for your IRA as well, so that you don't mix assets between your investment account and your IRA (also important for wash sale losses).

Another purpose could be to easily remove K-1 assets.

**Inputs:**
- Original output of code from Composer from a symphony in the form a of a ".txt" using the "Edit"-> "Copy Composer Code" feature
   - Example: TestSymphony.txt
- ".csv" files that contain a mapping of the assets you'd like to replace and what to replace them with
   - Examples: 
      - Mapping_EndOfYear.csv
      - Mapping_IRA.csv
      - Mapping_Main.csv
   - Edit these as necessary to cover all assets you'd like to replace in the symphony. Basic format is the first column is assets to replace and the second column is assets to replace it with

**Outputs**
- One text file for every mapping input csv file that contains the symphony after replacing all assets in the original with those in the mapping csv input file.
   - Examples:
      - TestSymphony_EndOfYear.csv
      - TestSymphony_IRA.csv
      - TestSymphony_Main.csv

**Python Script**
- ReplaceTickers.py
   - Change the input string "initialSymphony" to match the name of your input symphony ".txt" file
   - Change the name of "inputFiles" to match the input mapping csv files (if necessary)
   - Execute script with all input files in the same directory

The final step is to create the new symphonies using "Create with AI" and pasting each text file in the "Code" tab. You'll need to do this individually for each symphony (ie, for each output text file.
