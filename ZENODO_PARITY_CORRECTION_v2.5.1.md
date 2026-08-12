# Zenodo Parity Correction — v2.5.1

## Reason for this release

GitHub v2.5.0 published the frozen Tivrex Crop #1 ZIP and its SHA-256 file as GitHub Release assets.

The enabled GitHub–Zenodo integration automatically created Zenodo v2.5.0 (`10.5281/zenodo.21896607`). However, Zenodo archived the Git tag's repository source tree rather than the separately uploaded GitHub Release assets. As a result, the Zenodo v2.5.0 archive did not contain the canonical 54-file Crop #1 ZIP, its checksum, the durable archive extension, or the preserved live-model flight-check evidence.

GitHub v2.5.0 remains part of the public history. It is not deleted or rewritten.

## Correction

v2.5.1 commits the two canonical Crop #1 artifacts directly into the repository tree:

- `releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.zip`
- `releases/v2.5.1/TIVREX_CROP_1_VERIFIED_Aug11_2026.sha256`

Because Zenodo archives the tagged repository tree, the automatic Zenodo v2.5.1 archive should now contain the exact frozen Crop #1 ZIP and checksum.

## Canonical Crop #1 identity

- Archive inventory: 54 files
- SHA-256: `25310c1d827d7a498ebe7f5016ed2d61ea293cc90f53df2570a68fee8d80c752`
- Deterministic reference tests: 4/4 passed
- Successful bounded live-model run: `gpt-4o-mini-2024-07-18`

## Claim boundary

This correction establishes repository and archival content parity for the frozen reference artifact. It does not establish independent external validation, production security, broad adversarial robustness, legal compliance, universal model-provider transfer, or a finished enterprise implementation.
