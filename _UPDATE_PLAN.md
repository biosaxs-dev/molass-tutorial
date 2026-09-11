# molass-tutorial Update Plan (Post MyST v2 Migration)

**Date:** 2026-07-06 (Status corrected)  
**Status:** ✅ **MIGRATION COMPLETE**

---

## 📊 Current State

**Checker updated to ignore empty placeholder cells and use execution_count (not outputs).**

### Notebook Execution Status (12 notebooks total)

**Summary:**
- ✅ **Fully executed: 12 notebooks** (100%)
- ⚠️ **Partially executed: 0**
- ❌ **Not executed: 0**
- 📄 **No code cells: 0**

All notebooks have been fully executed:
- chapters/00/quick_start.ipynb — 6/6
- chapters/01/data_objects.ipynb — 11/11
- chapters/02/data_trimming.ipynb — 8/8
- chapters/04/data_correction.ipynb — 8/8
- chapters/04/work-1.ipynb — 1/1
- chapters/05/lrf.ipynb — 11/11
- chapters/06/rank_estimation.ipynb — 7/7
- chapters/07/denss.ipynb — 3/3
- chapters/08/backward.ipynb — 5/5
- chapters/10/nontrivial.ipynb — 6/6
- chapters/11/advanced-models.ipynb — 3/3
- chapters/20/rigorous.ipynb — 4/4

### Configuration Status

- ✅ **myst.yml**: Correct, minimal MyST v2 config
- ⚠️ **_config.yml**: Legacy Jupyter Book v1 config (ignored by MyST but confusing)
- ⚠️ **_toc.yml**: Jupyter Book v1 format (works but could be modernized)

---

## 🎯 Update Tasks

### Task 1: Clean Up Legacy Config ⚠️

**Issue:** `_config.yml` contains Jupyter Book v1 settings that are ignored by MyST v2

**Options:**
- **A) Delete _config.yml** (cleanest - MyST doesn't use it)
- **B) Add deprecation comment** (keep for reference)
- **C) Leave as-is** (no harm, just confusing)

**Recommendation:** Option B - add comment explaining it's legacy

### Task 2: Execute Notebooks 🚀

**Priority order:**
1. **quick_start.ipynb** (PARTIAL, 1 cell missing) - highest priority, user-facing
2. **data_trimming.ipynb** (PARTIAL, 1 cell missing)
3. **lrf.ipynb** (EMPTY) - core functionality
4. **rank_estimation.ipynb** (EMPTY)
5. **denss.ipynb** (EMPTY) - may need DENSS installed
6. **backward.ipynb** (EMPTY)
7. **nontrivial.ipynb** (EMPTY)
8. **advanced-models.ipynb** (EMPTY)

**Command:**
```powershell
cd c:\Users\takahashi\GitHub\molass-tutorial

# Execute one by one for better control
jupyter nbconvert --to notebook --execute --inplace chapters/00/quick_start.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/02/data_trimming.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/05/lrf.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/06/rank_estimation.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/07/denss.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/08/backward.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/10/nontrivial.ipynb
jupyter nbconvert --to notebook --execute --inplace chapters/11/advanced-models.ipynb
```

**Estimated time:** 10-15 minutes

### Task 3: Rebuild and Verify 🔍

**Steps:**
1. Rebuild with MyST:
   ```powershell
   cd c:\Users\takahashi\GitHub\molass-tutorial
   myst build --html
   ```

2. Check for build warnings/errors

3. Verify sample pages:
   - https://biosaxs-dev.github.io/molass-tutorial/quick-start
   - https://biosaxs-dev.github.io/molass-tutorial/lrf
   - https://biosaxs-dev.github.io/molass-tutorial/denss

4. Check that:
   - Code cells are visible
   - Outputs render (text, plots, tables)
   - Images load
   - Navigation works

### Task 4: Commit and Push 📦

```powershell
git add chapters/**/*.ipynb _config.yml
git commit -m "docs(tutorial): execute notebooks and clean legacy config for MyST v2"
git push
```

Wait for GitHub Pages deployment (~2-5 minutes)

---

## ⚠️ Potential Issues

1. **denss.ipynb** - may fail if DENSS not installed in environment
2. **rigorous.ipynb** - already has outputs but marked as excluded in old config (check if it should be re-executed)
3. **Long execution times** - some notebooks may take 5+ minutes
4. **Data dependencies** - all notebooks require `molass_data` package

---

## 🔄 Execution Order

### Phase 1: Quick Fixes (Now)
1. ✅ Add deprecation note to _config.yml
2. ✅ Execute quick_start.ipynb (highest priority)
3. ✅ Execute data_trimming.ipynb

### Phase 2: Core Notebooks (Next)
4. Execute lrf.ipynb
5. Execute rank_estimation.ipynb

### Phase 3: Advanced Notebooks (Then)
6. Execute denss.ipynb (check DENSS availability first)
7. Execute backward.ipynb
8. Execute nontrivial.ipynb
9. Execute advanced-models.ipynb

### Phase 4: Verify and Deploy
10. Rebuild with myst
11. Verify rendering
12. Commit and push
13. Verify published site

---

## 📝 Notes

- **Do NOT delete _config.yml** until verifying MyST doesn't need any settings from it
- **rigorous.ipynb** was in exclude list but has outputs - verify if this is intentional
- **_toc.yml** format works with MyST v2, no urgent need to convert
- After this is complete, molass-essence and molass-technical will follow the same pattern

---

## ✅ Ready to Start?

Begin with Task 1 (cleanup) and Task 2 Phase 1 (quick fixes).
