import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const inputDir = process.env.MAKEFUN_INPUT_DIR ?? "/input";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const candidates = [join(inputDir, "entry.png"), join(here, "entry.png")];
const src = candidates.find((p) => existsSync(p));
if (!src) throw new Error("entry.png not found in input dir or repo root");

function verifyWrittenFile(writtenPath, expectedPath) {
  const got = readFileSync(writtenPath);
  const want = readFileSync(expectedPath);
  if (!got.equals(want)) {
    throw new Error(
      "entry.png mismatch: wrote " + got.length + " bytes, expected " +
      want.length + " bytes"
    );
  }
  return got.length;
}

mkdirSync(outputDir, { recursive: true });
const dst = join(outputDir, "entry.png");
copyFileSync(src, dst);
const bytes = verifyWrittenFile(dst, src);
console.log("wrote " + dst + " (" + bytes + " bytes, verified)");
