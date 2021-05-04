from pathlib import Path

SRC_DP = Path(__file__).absolute().parent.parent
ROOT_DP = SRC_DP.parent
DOCS_DP = ROOT_DP / "docs"
NOTE_DP = ROOT_DP / "note"
SCRIPTS_DP = ROOT_DP / "scripts"
SOLUTION_DP = ROOT_DP / "solution"

# Directory paths
DPS = dict(
    root=ROOT_DP,
    docs=DOCS_DP,
    note=NOTE_DP,
    scripts=SCRIPTS_DP,
    solution=SOLUTION_DP,
    src=SRC_DP,
)

# Filepaths
introduction_fp = DOCS_DP / "01-introduction.md"
instructions_fp = DOCS_DP / "02-instructions.md"
qry_description_fp = DOCS_DP / "03-qry-descriptions.md"
submissions_fp = DOCS_DP / "04-submissions.md"
verification_fp = DOCS_DP / "05-verification.md"

DOC_FPS = dict(
    intro=introduction_fp,
    instructions=instructions_fp,
    query_description=qry_description_fp,
    submissions=submissions_fp,
    verification=verification_fp,
)

DEMO_Q_PARAMS_FP = SOLUTION_DP / "demo_q_params.json"
ALL_Q_PARAMS_FP = SOLUTION_DP / "all_q_params.json"

ALL_Q_COLNAM_FP = SOLUTION_DP / "all_q_colnam.json"
DUMMY_SOLUTION_FP = SCRIPTS_DP / "dummy_solution.py"
MODEL_SOLUTION_FP = SCRIPTS_DP / "model_solution.py"
