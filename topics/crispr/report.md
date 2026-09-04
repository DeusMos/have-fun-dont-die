# Topic: CRISPR

**Evidence cutoff:** September 3, 2026
**Last updated:** September 3, 2026

This repository is not medical advice. It is a sourced information dump for anyone who wants the details.

🤔 In the wild, “CRISPR” is three stacked bait-and-switches: any DNA-touching therapy is called CRISPR; Casgevy or a kitchen kit is sold as a walk-in / aging / germline license; and one embryo crime or one bacteria experiment is treated as the whole field (Vertex/CRISPR Therapeutics sell Casgevy; The Odin sells microbial kits, https://www.the-odin.com/crispr-kit/; He Jiankui implanted edited embryos, MIT Technology Review, 2019, https://www.technologyreview.com/2019/12/03/131752/chinas-crispr-babies-read-exclusive-excerpts-he-jiankui-paper/).

## Contents

- [The claim and the slogan](#the-claim-and-the-slogan)
- [What the words mean](#what-the-words-mean)
- [Mechanism](#mechanism)
- [Animal data](#animal-data)
- [Human data](#human-data)
- [Measurement](#measurement)
- [What clinics and self-experimenters are doing](#what-clinics-and-self-experimenters-are-doing)
- [Speculative](#speculative)
- [Named compounds](#named-compounds)
- [Adjacent hallmarks](#adjacent-hallmarks)
- [What is actually on the table](#what-is-actually-on-the-table)

## The claim and the slogan

The scientific claim under test is that CRISPR-Cas is a bacterial adaptive immune system that was engineered into a programmable nucleic-acid targeting stack — nucleases, nickases, dead-Cas regulators, base editors, prime editors — whose chemistry is known, that a lab can run, and that has produced measured human edits in defined products.

💯 CRISPR is the genomic array. Cas is the protein. “CRISPR editing” in papers means an RNA-guided Cas effector plus host repair or a fused deaminase / reverse transcriptase (Jansen et al., Molecular Microbiology, 2002, https://doi.org/10.1046/j.1365-2958.2002.02839.x, PMID 11952905; Barrangou et al., Science, 2007, https://doi.org/10.1126/science.1138140, PMID 17379808).

⛔ Collapsing Cas9 knockout, base editing, prime editing, CRISPRi, AAV gene addition, a bacteria kit, and an approved HSPC medicine into one product is a definition failure, not a mechanism result (Addgene CRISPR Guide, https://www.addgene.org/guides/crispr/; Casgevy PI, July 2026, https://pi.vrtx.com/files/uspi_exagamglogene_autotemcel.pdf; The Odin CRISPR Bacteria Gene Editing Kit, https://www.the-odin.com/crispr-kit/; Davidsohn et al., PNAS, 2019, https://doi.org/10.1073/pnas.1910073116, PMID 31685628).

⛔ “Precise” in marketing English is not zero off-target, zero bystander, zero mosaic, zero structural variant, only-the-intended cells, or reversible on demand (Tsai et al., Nature Biotechnology, 2015, https://doi.org/10.1038/nbt.3117, PMID 25513782; van Overbeek et al., Molecular Cell, 2016, https://doi.org/10.1016/j.molcel.2016.06.037, PMID 27499295).

⛔ Quoting Casgevy approval as a general human-editing license — germline, longevity, walk-in somatic editing of any gene, whole-body rewrite — fails the label: one ex vivo HSPC *BCL11A* erythroid-enhancer NHEJ edit for SCD/TDT after busulfan (FDA, 8 Dec 2023, https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapies-treat-patients-sickle-cell-disease; Casgevy PI, July 2026).

⛔ Liver LNP knockdown of a secreted protein is not organismal genome rewriting (Gillmore et al., NEJM, 2021, https://doi.org/10.1056/NEJMoa2107454, PMID 34215024; Finn et al., Cell Reports, 2018, https://doi.org/10.1016/j.celrep.2018.02.014, PMID 29490262).

⛔ AAV-FGF21 / OSK / TERT gene-addition programs labeled “CRISPR” in longevity media are a different operation unless the paper uses a Cas effector (Davidsohn et al., PNAS, 2019).

⛔ Using He Jiankui as the safety label for Casgevy or Intellia conflates implanted germline embryos with somatic HSPC / hepatocyte products (MIT Technology Review, 3 Dec 2019, https://www.technologyreview.com/2019/12/03/131752/chinas-crispr-babies-read-exclusive-excerpts-he-jiankui-paper/; Casgevy PI, July 2026; Gillmore et al., NEJM, 2021).

🤔 Vertex + CRISPR Therapeutics sell Casgevy; Intellia sells nex-z / lonvo-z; Verve / Lilly sell PCSK9 base editors; Beam, Editas, Prime Medicine, Caribou, Mammoth sell platform IP; Addgene / IDT / Synthego / Thermo sell lab reagents; The Odin sells kits; Rejuvenate-class shops sell aging gene addition that still gets called CRISPR.

## What the words mean

💯 CRISPR = clustered regularly interspaced short palindromic repeats — the spacer array in a prokaryotic genome, not the nuclease (Jansen et al., Molecular Microbiology, 2002).

💯 The immune cycle is spacer acquisition, crRNA biogenesis, then interference (Barrangou et al., Science, 2007).

📚 CRISPR-Cas systems split into Class 1 (multi-subunit effectors) and Class 2 (single-protein effectors); the 2020 frame used 6 types / 33 subtypes; a 2025 update adds type VII and more rare subtypes (Makarova et al., Nature Microbiology, 2025).

📚 A PAM (protospacer adjacent motif) is a short motif on the *non-target* DNA that most DNA-cutting Cas enzymes require before they commit to cleavage; SpCas9’s is NGG; Cas12a’s is T-rich (TTTV for Acidaminococcus/Lachnospiraceae) (Mojica et al., Microbiology, 2009, https://doi.org/10.1099/mic.0.023960-0, PMID 19246744; Jinek et al., Science, 2012, https://doi.org/10.1126/science.1225829, PMID 22745249; Zetsche et al., Cell, 2015, https://doi.org/10.1016/j.cell.2015.09.038, PMID 26422227).

📚 An sgRNA is an engineered fusion of crRNA + tracrRNA that programs Cas9 with one RNA (Jinek et al., Science, 2012).

📚 Knockout in practice is usually an NHEJ/MMEJ indel distribution that often frameshifts a coding sequence — not a clean deletion of the gene (van Overbeek et al., Molecular Cell, 2016; Shen et al., Nature, 2018, https://doi.org/10.1038/s41586-018-0686-x, PMID 30405244).

📚 Ex vivo editing takes cells out, edits them, conditions the patient, and reinfuses (Casgevy). In vivo editing puts LNP or AAV into the body (Intellia liver, Verve, EDIT-101 retina). Those are different delivery, tox, and mosaic problems (Casgevy PI, July 2026; Gillmore et al., NEJM, 2021; Pierce et al., NEJM, 2024, https://doi.org/10.1056/NEJMoa2309915, PMID 38709228).

📚 Somatic edits are in the patient’s body and are not designed to enter the germline. Germline edits are embryos or gametes; He Jiankui is the latter; Casgevy is the former (Casgevy PI, July 2026; MIT Technology Review, 2019).

📚 Gene *editing* rewrites a locus. Many approved gene therapies are *addition* (AAV or lentiviral cDNA) with no CRISPR. Lyfgenia is addition. Rejuvenate Bio’s founding mouse work is addition (FDA Lyfgenia SBRA, 2023, https://www.fda.gov/media/175250/download; Davidsohn et al., PNAS, 2019).

🤔 A “CRISPR kit” on The Odin is a bacterial or yeast education SKU plus plasmids, not a human-injectable Cas9 RNP/LNP (The Odin, https://www.the-odin.com/crispr-kit/).

## Mechanism

### Array, acquisition, types

📚 Ishino et al. sequenced five 29-nt direct repeats with 32-nt spacers downstream of *E. coli iap* and wrote that the biological significance was unknown (Ishino et al., Journal of Bacteriology, 1987, https://doi.org/10.1128/jb.169.12.5429-5433.1987, PMID 3316184).

📚 Jansen et al. named the repeat family CRISPR and the adjacent genes *cas1*–*cas4*; *cas* genes sat next to the arrays and were present only in CRISPR-containing prokaryotes (Jansen et al., Molecular Microbiology, 2002).

📚 Mojica et al. showed CRISPR spacers derive from preexisting chromosomal or mobile-element sequences and that those elements fail to infect the spacer-carrier strain (Mojica et al., Journal of Molecular Evolution, 2005, https://doi.org/10.1007/s00239-004-0046-3, PMID 15791728).

📚 After phage challenge, *S. thermophilus* integrated new phage-derived spacers; adding or removing particular spacers changed the resistance phenotype (Barrangou et al., Science, 2007).

📚 Type I uses a Cascade multi-subunit complex; Brouns et al. showed small CRISPR RNAs guide antiviral defense, with later type-I descriptions using Cas3 as a DNA shredder from the target rather than a blunt DSB (Brouns et al., Science, 2008, https://doi.org/10.1126/science.1159689, PMID 18703739).

📚 Type II uses Cas9. Type V Cas12a (Cpf1) is a single RNA-guided Class 2 endonuclease with a T-rich PAM, a single RuvC-like nuclease domain, staggered cuts, and no tracrRNA requirement (Zetsche et al., Cell, 2015).

📚 Type VI Cas13 (C2c2) is an RNA-guided RNase: it targets RNA, not DNA, and can show collateral RNase activity after target recognition (Abudayyeh et al., Science, 2016, https://pubmed.ncbi.nlm.nih.gov/27256883/, PMID 27256883).

### Cas9 chemistry: guide, PAM, seed, R-loop, cut

💯 Cas9 is an RNA-guided DNA endonuclease: a guide RNA specifies the target, and the protein cuts both DNA strands (Jinek et al., Science, 2012; Gasiunas et al., PNAS, 2012, https://doi.org/10.1073/pnas.1208507109, PMID 22949671).

📚 Deltcheva et al. found a trans-encoded tracrRNA in *S. pyogenes* with complementarity to CRISPR repeats; tracrRNA, host RNase III, and Cas9 were required for crRNA maturation (Deltcheva et al., Nature, 2011, https://doi.org/10.1038/nature09886, PMID 21455174).

📚 Jinek et al. reconstituted *S. pyogenes* Cas9 in vitro: dual tracrRNA:crRNA directs a DSB at a complementary site next to a PAM; HNH cuts the complementary strand and the RuvC-like domain cuts the non-complementary strand; a chimeric sgRNA also programmed cleavage (Jinek et al., Science, 2012).

📚 Gasiunas et al. isolated *S. thermophilus* Cas9–crRNA RNP and showed PAM-dependent DSB formation; a 20-nt crRNA fragment specifies the protospacer (Gasiunas et al., PNAS, 2012).

📚 Sternberg et al. showed binding and cleavage both require a PAM; sequences fully complementary to the guide but lacking a nearby PAM are ignored; strand separation and R-loop formation initiate at the PAM and proceed toward the distal end (Sternberg et al., Nature, 2014, https://doi.org/10.1038/nature13011, PMID 24476820).

📚 Seed mismatches (≈8–10 nt adjacent to the PAM) block cleavage more than PAM-distal mismatches; the two-domain cut is ≈3–4 nt upstream of the PAM (Jinek et al., Science, 2012; Sternberg et al., Nature, 2014; Addgene CRISPR Guide).

📚 Nishimasu et al. reported the 2.5 Å structure of SpCas9 bound to sgRNA and target DNA (PDB 4OO8): REC and NUC lobes (RuvC, HNH, PAM-interacting) hold the heteroduplex, with HNH and RuvC positioned to cut opposite strands (Nishimasu et al., Cell, 2014, https://doi.org/10.1016/j.cell.2014.02.001, PMID 24529477).

📚 Cong et al. expressed codon-optimized SpCas9 with crRNA/tracrRNA or sgRNA in human 293FT cells and obtained SURVEYOR-detectable indels at endogenous *EMX1*; a D10A nickase catalyzed HDR insertion; a single array multiplexed two loci (Cong et al., Science, 2013, https://doi.org/10.1126/science.1231143, PMID 23287718).

📚 Mali et al. reported Cas9+gRNA targeting rates at endogenous *AAVS1* of 10–25% in 293T, 8–13% in K562, and 2–4% in iPS cells (Mali et al., Science, 2013, https://doi.org/10.1126/science.1232033, PMID 23287722).

### Repair writes a distribution

💯 DNA double-strand breaks exist and eukaryotic cells repair them by non-homologous end joining or, in S/G2 with a homologous donor, homology-directed repair (Ran et al., Nature Protocols, 2013, https://doi.org/10.1038/nprot.2013.143, PMID 24157548).

💯 Classical homologous recombination that uses a sister chromatid is restricted to S/G2; c-NHEJ operates through the cell cycle, including G0/G1 and post-mitotic cells (Cox, Platt, Zhang, Nature Medicine, 2015, https://doi.org/10.1038/nm.3793, PMID 25654603).

📚 Cas9 DSBs at 223 human genomic sites produced nonrandom but still site-specific indel *distributions*, reproducible across replicates, cell lines, and delivery methods, set by protospacer sequence rather than a single specified genotype (van Overbeek et al., Molecular Cell, 2016).

📚 inDelphi, trained on 1,872 SpCas9 target sites, predicts template-free indel frequencies at single-base resolution; only 5–11% of human gRNAs yield one genotype in ≥50% of edited products (Shen et al., Nature, 2018).

📚 On-target Cas9 repair in mouse ES cells, mouse hematopoietic progenitors, and human RPE1 cells frequently produced kilobase-scale deletions and complex rearrangements missed by short-amplicon genotyping; at *PigA*, 10/48 (21%) alleles from an exonic gRNA had deletions >250 bp up to 6 kb (Kosicki, Tomberg, Bradley, Nature Biotechnology, 2018, https://doi.org/10.1038/nbt.4192, PMID 30010673).

📚 In CRISPR-Cas9–edited early human embryos targeting *POU5F1*, unintended on-target outcomes (LOH; segmental loss/gain of chromosome 6) were present in ~16% of analyzed cells and spanned 4–20 kb (Alanis-Lobato et al., PNAS, 2021, https://doi.org/10.1073/pnas.2004832117, PMID 34050011).

📚 Cas9 cleavage of a paternal *EYS* allele in human zygotes left ~half of breaks unrepaired, producing an undetectable paternal allele and, after mitosis, loss of chromosomal arms (Zuccaro et al., Cell, 2020, https://doi.org/10.1016/j.cell.2020.10.025, PMID 33125898).

⛔ Treating a Cas9 cut as a sequence-perfect, allele-complete rewrite is a definition game: the molecule specifies a cut (or nick / deaminase window); host NHEJ/MMEJ/HDR writes a distribution (van Overbeek 2016; Shen 2018; Kosicki 2018).

📚 CRISPR-Cas9 HDR remains low-efficiency especially in post-mitotic cells; NHEJ is the pathway available unless the cell is in cycle (Nambiar et al., Frontiers in Genetics, 2021, https://doi.org/10.3389/fgene.2021.728520, PMID 34539755; Taha et al., Journal of Controlled Release, 2022, https://doi.org/10.1016/j.jconrel.2022.01.013, PMID 35026352).

⛔ Reviews that treat HDR as the default mammalian CRISPR outcome omit the cell-cycle constraint; Casgevy itself is an NHEJ enhancer disruption, not an HDR rewrite of *HBB* (Casgevy PI, July 2026; Cox et al., Nature Medicine, 2015).

📚 Richardson et al. designed asymmetric ssDNA donors complementary to the Cas9-released nontarget strand and raised HDR to up to 60% in human cells for small replacements; Cas9 dwell time on DNA was ~6 h (Richardson et al., Nature Biotechnology, 2016, https://doi.org/10.1038/nbt.3481, PMID 26789497).

🤔 Addgene’s lab guide states HDR efficiency is generally low (<10% of modified alleles) and that most Cas9 DSBs still go to NHEJ, so the pool is WT + NHEJ alleles + rare HDR alleles until clones are isolated (Addgene CRISPR Guide).

### Nickases, dCas, CRISPRi/a, CRISPRoff

📚 Cas9 D10A (RuvC-dead) nicks one strand; paired nickases on opposite strands were used to raise specificity versus a single nuclease DSB (Ran et al., Cell, 2013, https://doi.org/10.1016/j.cell.2013.08.021, PMID 23992846).

📚 dCas9 (D10A + H840A) binds without cutting; CRISPRi is dCas9 ± KRAB at a promoter and repressed transcription in *E. coli* by up to ~1,000-fold with no DNA cleavage (Qi et al., Cell, 2013, https://doi.org/10.1016/j.cell.2013.02.022, PMID 23452860).

📚 CRISPRa is dCas9 fused to activators (VP64 and later VPR / SAM / SunTag) (Gilbert et al., Cell, 2013, https://doi.org/10.1016/j.cell.2013.06.044, PMID 23849981).

📚 CRISPRoff is dCas9 fused to KRAB + DNMT3A–DNMT3L; transient expression deposits DNA methylation and H3K9me3 that can persist through cell division without a DSB (Nuñez et al., Cell, 2021, https://doi.org/10.1016/j.cell.2021.03.025, PMID 33838111).

### Base editors and prime editors

📚 Cytosine base editors fuse a cytidine deaminase to nCas9 plus UGI (BE3) and convert C•G to T•A in a small window without a classical DSB or donor; Komor et al. reported ~15–75% correction with typically ≤1% indels in four cell lines (Komor et al., Nature, 2016, https://doi.org/10.1038/nature17946, PMID 27096365).

📚 Adenine base editors convert A•T to G•C using a TadA-derived deaminase on nCas9; ABE7.10 converted ~50% of alleles in human cells with ≥99.9% product purity and typically ≤0.1% indels (Gaudelli et al., Nature, 2017, https://doi.org/10.1038/nature24644, PMID 29160308).

📚 Prime editors fuse Cas9 H840A nickase to an engineered reverse transcriptase programmed by a pegRNA; Anzalone et al. performed >175 edits in human cells (all 12 substitutions, insertions, deletions) without a DSB or donor; PE3 typically reached 20–50% desired edit with 1–10% indels in HEK293T (Anzalone et al., Nature, 2019, https://doi.org/10.1038/s41586-019-1711-4, PMID 31634902).

📚 Cytosine base editor BE3 induced a mean 283 SNVs per mouse embryo by GOTI — ≥20× the Cre/Cas9 spontaneous-range background — while ABE7.10 averaged 10 SNVs/embryo near the spontaneous rate (Zuo et al., Science, 2019, https://doi.org/10.1126/science.aav9973, PMID 30819928).

📚 CRISPR-guided DNA cytosine base editors induced transcriptome-wide off-target RNA C-to-U editing, independent of the “no DSB” slogan (Grünewald et al., Nature, 2019, https://doi.org/10.1038/s41586-019-1161-z, PMID 30995674).

⛔ Filing “base editors / prime editors = CRISPR is now safe/precise” as if they were the same product as a Cas9 knockout kit, or as if CBE bystander and RNA off-targets were gone, fails the papers (Komor 2016; Zuo 2019; Grünewald 2019; Anzalone 2019).

🤔 Addgene’s cookbook line: base editing is high-efficiency in a window but bystander-prone; prime editing is more flexible and typically lower efficiency with more indels than CBE/ABE (Addgene CRISPR Guide).

### Off-targets, p53, chromothripsis

📚 GUIDE-seq of 13 RNA-guided nucleases in two human cell lines found wide variability in off-target DSBs; most recovered sites were not predicted by computation or ChIP-seq (Tsai et al., Nature Biotechnology, 2015).

📚 CIRCLE-seq of non-repetitive gRNAs recovered tens to >100 in vitro off-target cleavage sites per gRNA, including sites missed by GUIDE-seq (Tsai et al., Nature Methods, 2017, https://doi.org/10.1038/nmeth.4278, PMID 28459458).

📚 CHANGE-seq applied to 110 sgRNAs across 13 loci in primary T cells reported 201,934 off-target sites; cellular hits were 2–4× likelier near active promoters/enhancers (Lazzarotto et al., Nature Biotechnology, 2020, https://doi.org/10.1038/s41587-020-0555-7, PMID 32541958).

📚 Digenome-seq digests purified genomic DNA with Cas9 RNP in vitro and finds cleavage signatures by WGS (Kim et al., Nature Methods, 2015, https://doi.org/10.1038/nmeth.3284, PMID 25664545).

🥼 Cell-based (GUIDE-seq) versus biochemical (CIRCLE-seq / CHANGE-seq / Digenome) menus do not return the same site list; reviews treat them as complementary, not interchangeable gold standards (Tsai 2015; Tsai 2017; Kim 2015; Lazzarotto 2020).

📚 Cas9 editing in immortalized human RPE1 cells induced a p53-mediated DNA-damage response and cell-cycle arrest, selecting against cells with a functional p53 pathway (Haapaniemi et al., Nature Medicine, 2018, https://doi.org/10.1038/s41591-018-0049-z, PMID 29892067).

📚 In hPSCs, Cas9 DSBs at high indel efficiency were toxic in a TP53-dependent manner; transient P53DD raised HDR ~17-fold (Ihry et al., Nature Medicine, 2018, https://doi.org/10.1038/s41591-018-0050-6, PMID 29892062).

📚 Cas9 expression activated the p53 pathway and selected for p53-inactivating mutations (Enache et al., Nature Genetics, 2020, https://doi.org/10.1038/s41588-020-0623-4, PMID 32424350).

🥼 Whether DSB-driven p53 selection is a clinical show-stopper versus a cell-type/assay finding is a live paper fight: Haapaniemi 2018 / Ihry 2018 / Enache 2020 report selection against p53-functional cells, while Casgevy’s FDA review reported no trial malignancy signal and required 15-year PMR follow-up rather than declaring p53 selection observed in patients (Haapaniemi 2018; Ihry 2018; Enache 2020; FDA Casgevy SBRA, 2023, https://www.fda.gov/media/175179/download).

📚 Single-cell WGS after CRISPR-Cas9 showed micronuclei and chromosome bridges that initiate chromothripsis; the same cytological hallmarks appeared after editing a clinically relevant locus in clinically relevant cells (Leibowitz et al., Nature Genetics, 2021, https://doi.org/10.1038/s41588-021-00838-7, PMID 33846636).

🥼 Chromothripsis-as-on-target-consequence (Leibowitz 2021) versus “not seen as a clinical genotoxic event in Casgevy packages” is a live fight: FDA-facing assessments reported no karyotypic translocations and no empirical off-target editing after hybrid-capture of nominated sites, while still listing off-target risk as the major residual uncertainty (Leibowitz 2021; FDA Casgevy SBRA, 2023).

### Delivery

💯 Wild-type AAV packaging capacity is ~4.7 kb of DNA; SpCas9 (~4.1 kb) cannot be packaged with gRNA, promoter, and poly(A) in one conventional AAV (Taha et al., Journal of Controlled Release, 2022).

📚 Dual-AAV split Cas9 or smaller orthologs (SaCas9, CjCas9, Cas12, CasΦ) are workarounds that trade efficiency, PAM, and immunogenicity (Taha et al., Journal of Controlled Release, 2022; Pierce et al., NEJM, 2024).

📚 Ionizable LNPs delivering Cas9 mRNA + sgRNA produce durable liver knockout because ApoE/LDLR tropism sends the particles to hepatocytes — liver pharmacology, not organismal rewrite (Finn et al., Cell Reports, 2018).

📚 Pre-existing neutralizing antibodies to common AAV serotypes are frequent in healthy humans and exclude or blunt systemic AAV gene transfer (Boutin et al., Human Gene Therapy, 2010, https://doi.org/10.1089/hum.2009.182, PMID 20095819).

📚 Adult-mouse IV AAV-CRISPR for DMD was immunogenic (humoral and cellular responses to Cas9/AAV); neonatal dosing avoided that; the same study reported unintended genome and transcript alterations (Nelson et al., Nature Medicine, 2019, https://doi.org/10.1038/s41591-019-0344-3, PMID 30778238).

🤔 Practical lab objects are plasmid (Cas9 + sgRNA, e.g. pX330 / Addgene #42230), RNP (Cas9 protein + synthetic sgRNA or crRNA:tracrRNA), mRNA+gRNA, electroporation / nucleofection, lipid transfection, lentivirus, AAV, and LNP (Addgene CRISPR Guide; Addgene pX330, https://www.addgene.org/42230/; Thermo TrueCut Cas9 v2 User Guide, https://assets.thermofisher.com/TFS-Assets/LSG/manuals/MAN0017066_TrueCut_Cas9_Protein_v2_UG.pdf).

📚 Casgevy is ex vivo RNP electroporation of autologous CD34+ HSPCs. NTLA-2001 / nex-z is LNP-encapsulated Cas9 mRNA + *TTR* sgRNA, IV. EDIT-101 is AAV5 encoding SaCas9 + two gRNAs under a photoreceptor GRK1 promoter, subretinal (Casgevy PI, July 2026; Gillmore et al., NEJM, 2021; Pierce et al., NEJM, 2024).

## Animal data

📚 Wang et al. co-injected Cas9 mRNA and sgRNAs into mouse zygotes and obtained mice with biallelic mutations in both *Tet1* and *Tet2* at 80% (22/28 pups mutant at all four alleles from 144 transferred embryos; 21% live birth); single-sgRNA injections produced up to 95% biallelic mutants (Wang et al., Cell, 2013, https://doi.org/10.1016/j.cell.2013.04.025, PMID 23643243).

📚 A single IV LNP dose of Cas9 mRNA + sgRNA reduced mouse TTR protein >97% at 52 weeks (Finn et al., Cell Reports, 2018).

📚 NHP surrogate of NTLA-2001 at 3–6 mg/kg gave >94% TTR reduction for 12 months with 73% whole-liver editing (Gillmore et al., NEJM, 2021).

📚 Adult IV AAV-CRISPR in *mdx* mice was immunogenic over 1 year; neonates were not; unintended genome and transcript alterations were reported in the same paper (Nelson et al., Nature Medicine, 2019).

📚 BE3 cytosine base editing produced a mean 283 SNVs per mouse embryo by GOTI versus ~10 for ABE7.10 (Zuo et al., Science, 2019).

📚 Rejuvenate Bio’s founding mouse work is AAV8 gene *addition* of FGF21, sTGFβR2, ± αKlotho — no Cas effector (Davidsohn et al., PNAS, 2019).

## Human data

### Casgevy (exa-cel) — ex vivo HSPC NHEJ

📚 Exagamglogene autotemcel (Casgevy) is autologous CD34+ HSPCs electroporated with Cas9/SPY101 RNP at the GATA1 site in the *BCL11A* erythroid enhancer to raise HbF; Vertex leads commercialization and splits costs/profits 60/40 with CRISPR Therapeutics (Casgevy PI, July 2026; FDA, 8 Dec 2023).

📚 First US approvals were 8 Dec 2023 (SCD, ≥12 y) and Jan 2024 (TDT, ≥12 y); the July 2026 label extends to patients aged 2 years and older with SCD with recurrent VOCs or TDT (FDA, 8 Dec 2023; Casgevy PI, July 2026).

📚 Conditioning on the label is full myeloablative busulfan 48 h–7 days before infusion; ≥12 y starting 3.2 mg/kg/day qd or 0.8 mg/kg q6h × 4 days, PK-adjusted; minimum dose 3×10^6 CD34+ cells/kg; backup unmodified CD34+ ≥2×10^6/kg; plerixafor mobilization (no G-CSF in SCD) (Casgevy PI, July 2026).

📚 Frangoul et al. 2021 (n=2 first patients): TDT patient reached Hb 13.1 g/dL at month 18 and stopped transfusions at day 30; SCD patient went from 7 VOCs/year to zero over 16.6 months, HbF 9.1% → 43.2% at month 15 (Frangoul et al., NEJM, 2021, https://doi.org/10.1056/NEJMoa2031054, PMID 33283989; funded by CRISPR Therapeutics and Vertex).

📚 In the FDA SCD efficacy set, 44 subjects received Casgevy; 29/31 (93.5%) VF12-evaluable were free of severe VOCs for ≥12 months; 30/30 HF12-evaluable were free of sVOC hospitalizations for ≥12 months; mean HbF ≥40% from month 6 (FDA Casgevy SBRA, 2023; Casgevy PI, July 2026).

📚 Frangoul et al. 2024 phase 3 SCD: 44 treated, median follow-up 19.3 months; of 30 with enough follow-up, 29 (97%) VOC-free ≥12 months; safety described as consistent with busulfan + autologous HSPC transplant; no cancers in that report (Frangoul et al., NEJM, 2024, https://doi.org/10.1056/NEJMoa2309676, PMID 38661449).

📚 TDT Trial 2 / Locatelli 2024: 52 infused; TI12 in 32/35 (91.4%) on the 2026 label; mean weighted Hb 13.1 g/dL in responders (Casgevy PI, July 2026; Locatelli et al., NEJM, 2024, https://doi.org/10.1056/NEJMoa2309673, PMID 38657265).

📚 Grade 3/4 neutropenia, thrombocytopenia, and leukopenia occurred in 98–100% after busulfan + Casgevy in SCD Trial 1; one SCD death from COVID-19 respiratory failure, labeled unrelated to Casgevy (Casgevy PI, July 2026).

📚 In TDT Trial 2, VOD occurred in 5/52 (10%); one patient developed VOD + HLH and died of pneumonia / multi-organ failure after busulfan + Casgevy (Casgevy PI, July 2026).

📚 USPI section 5.4 (added 08/2025): unintended off-target editing in an individual’s CD34+ cells due to genetic variants cannot be ruled out; clinical significance unknown (Casgevy PI, July 2026).

📚 FDA’s 2023 SBRA called potential off-target CRISPR/Cas9 editing the major residual risk and required PMR studies for off-target editing and long-term malignancy (FDA Casgevy SBRA, 2023).

🤔 Vertex set a published list / WAC of $2.2 million per dose; at approval Vertex named nine treatment centers in seven states plus D.C. (Pagliarulo, BioPharma Dive, 8 Dec 2023, https://www.biopharmadive.com/news/crispr-sickle-cell-price-millions-gene-therapy-vertex-bluebird/702066/).

### Lyfgenia is not CRISPR

📚 Lyfgenia (lovotibeglogene autotemcel) is autologous HSPCs transduced with BB305 lentiviral vector encoding βA-T87Q-globin — gene addition, not a CRISPR cut; same-day FDA approval (8 Dec 2023) with a boxed warning for hematologic malignancy; 28/32 = 88% VOE-CR (FDA, 8 Dec 2023; FDA Lyfgenia SBRA, https://www.fda.gov/media/175250/download).

⛔ Calling Lyfgenia a CRISPR approval is false on mechanism (FDA, 8 Dec 2023).

### Intellia — in vivo liver LNP

📚 NTLA-2001 / nexiguran ziclumeran (nex-z) is LNP Cas9 mRNA + *TTR* sgRNA (spacer AAAGGCUGCUGAUGACACCU) for hepatocyte TTR knockout; first-in-human n=6: day-28 mean serum TTR −52% at 0.1 mg/kg (range 47–56) and −87% at 0.3 mg/kg (range 80–96); AEs grade 1 only in that 28-day window (Gillmore et al., NEJM, 2021; Intellia + Regeneron).

📚 On 27 Oct 2025 Intellia reported Grade 4 liver transaminases and increased total bilirubin in a MAGNITUDE (NCT06128629) patient dosed with nex-z; FDA placed clinical holds on MAGNITUDE and MAGNITUDE-2 on 29 Oct 2025; that patient died 5 Nov 2025; the PI reported death due to septic shock secondary to a perforated duodenal ulcer; the course included acute liver injury treated with corticosteroids (Intellia 8-K, https://www.sec.gov/Archives/edgar/data/1652130/000119312526008307/d15047d8k.htm; CGTLive, https://www.cgtlive.com/view/patient-treated-trial-intellia-transthyretin-amyloidosis-gene-editing-therapy-nex-z-dies).

📚 FDA lifted the MAGNITUDE-2 hold 27 Jan 2026 and the MAGNITUDE hold 2 Mar 2026 after enhanced liver-lab monitoring, short-course steroids for early transaminase rises, exclusion of certain liver abnormalities, and (MAGNITUDE) extra CV-instability / EF<25% exclusions (Intellia, 27 Jan 2026, https://ir.intelliatx.com/news-releases/news-release-details/intellia-therapeutics-announces-fda-lift-clinical-hold-magnitude; Intellia, 2 Mar 2026, https://www.globenewswire.com/news-release/2026/03/02/3247267/0/en/Intellia-Therapeutics-Announces-FDA-Lift-of-Clinical-Hold-on-MAGNITUDE-Phase-3-Clinical-Trial-in-ATTR-CM.html).

⛔ A lifted hold is not proof the liver SAE was hypothetical; it is a protocol change after a Grade 4 Hy’s-law-pattern event and a death in the same patient. The PI attributed death to ulcer/sepsis; liver injury was part of the course, not a published causal adjudication that nex-z was the sole cause of death (Intellia 8-K).

📚 NTLA-2002 / lonvoguran ziclumeran (lonvo-z) is the same LNP CRISPR platform aimed at *KLKB1* / plasma kallikrein for HAE. Phase 1 (n=10; 25/50/75 mg): mean kallikrein −67/−84/−95%; mean monthly-attack change weeks 1–16 −91/−97/−80%; no DLT, SAE, or ≥Grade 3 AE in that report (Longhurst et al., NEJM, 2024, https://doi.org/10.1056/NEJMoa2309149, PMID 38294975).

📚 Phase 2 (n=27; 25 mg / 50 mg / placebo 2:2:1): estimated mean monthly attack rate 0.70 vs 0.65 vs 2.82 weeks 1–16; −75% and −77% vs placebo; kallikrein −55% / −86% at week 16 (Cohn / Longhurst et al., NEJM, 2024, https://doi.org/10.1056/NEJMoa2405734, PMID 39445704).

🤔 HAELO Phase 3 topline (company / SEC, 27 Apr 2026): one 50 mg infusion; weeks 5–28 mean monthly attacks 0.26 vs 2.10 placebo, 87% reduction (p<0.0001); 62% vs 11% entirely attack-free; TEAEs infusion reaction / headache / fatigue, all mild–moderate, no SAE in the lonvo-z arm as of the 10 Feb 2026 cutoff (Intellia SEC EX-99.1, 27 Apr 2026, https://www.sec.gov/Archives/edgar/data/1652130/000119312526179401/d138980dex991.htm).

### Verve / Lilly — PCSK9 base editing

🤔 VERVE-101 is an in vivo A→G *PCSK9* base editor in an LNP; Heart-1 Phase 1b paused enrollment 2 Apr 2024 after the sixth patient at 0.45 mg/kg developed Grade 3 ALT rise + thrombocytopenia within 4 days; 13 enrolled, 6 at that dose; IND remained active (Verve, 2 Apr 2024, https://www.globenewswire.com/news-release/2024/04/02/2855795/0/en/Verve-Therapeutics-Announces-Updates-on-its-PCSK9-Program.html).

🤔 Verve later stated nonclinical studies with a non-targeting guide implicated the VERVE-101 LNP, not the editor chemistry, and prioritized VERVE-102 (same editor + guide, different ionizable lipid + GalNAc) (Verve, 2 Apr 2024).

📚 Heart-2 interim (VERVE-102): 35 participants, six dose cohorts, ≥28 days follow-up; no DLT; mild–moderate IRRs and transient ALT; one aspiration pneumonitis in a GERD patient; mean PCSK9 −51% at 0.3 mg/kg to −88% at 1.0 mg/kg; mean LDL-C −9% to −62% (absolute −78 mg/dL at 1.0 mg/kg); durability ≥1 year in 15 participants (Vafai et al., NEJM, 2026, https://pubmed.ncbi.nlm.nih.gov/42187087/, PMID 42187087; NCT06164730; funded by Verve; Lilly acquired Verve).

### Other dosed human programs

📚 EDIT-101 (AAV5-SaCas9, subretinal, *CEP290* IVS26) in BRILLIANCE (NCT03872479) treated 14 patients; 3/14 met the pre-specified multi-endpoint responder rule (all in the homozygous IVS26 subset); Editas paused further enrollment 17 Nov 2022 citing a small US homozygous population and no independent development path (Pierce et al., NEJM, 2024).

🤔 BEAM-101 / risto-cel is ex vivo A→G base editing of *HBG1/2* promoters in autologous CD34+ HSPCs plus busulfan (BEACON NCT05456880); Beam reported a NEJM writeup of 31 treated as of a 6 Aug 2025 cutoff with company-claimed HbF >60% and HbS <40% and no severe VOC post-engraftment — company press, not independently DOI-fetched here (Beam, 1 Apr 2026, https://www.globenewswire.com/news-release/2026/04/01/3267053/0/en/Beam-Therapeutics-Announces-Publication-of-BEACON-Phase-1-2-Data-for-risto-cel-in-Patients-with-Sickle-Cell-Disease-SCD-in-The-New-England-Journal-of-Medicine.html).

🤔 PM359 (Prime Medicine) is ex vivo all-RNA prime editing of autologous HSCs to correct the *NCF1* GT deletion (p47phox CGD). First patient dosed Apr 2025 (18 y): company-reported DHR 58% day 15 / 66% day 30; neutrophil engraftment day 14–16 (Prime Medicine, 19 May 2025, https://investors.primemedicine.com/news-releases/news-release-details/prime-medicine-announces-breakthrough-clinical-data-showing).

🤔 Caribou vispa-cel / CB-010 is allogeneic anti-CD19 CAR-T with three Cas9 chRDNA edits (TRAC KO + CAR knock-in + PD-1 KO); ANTLER NCT04637763 has dosed humans (Caribou pipeline, https://www.cariboubio.com/pipeline/).

🤔 Mammoth MB-111 (CasΦ LNP vs hepatic *APOC3*) was preclinical as of late 2025 with IND/CTA aimed 2H 2026; no human dose found this round.

📚 Novartis CADPT03A12101 CRISPR HSPC SCD trial NCT04443907 is TERMINATED: “business reasons and was not a consequence of any safety concern” (ClinicalTrials.gov, https://clinicaltrials.gov/study/NCT04443907).

📚 EdiGene ET-01 CRISPR HSPC TDT trial NCT04925206 is TERMINATED: “Development plan change” (ClinicalTrials.gov, https://clinicaltrials.gov/study/NCT04925206).

### He Jiankui — implanted germline, not Casgevy

📚 He Jiankui used CRISPR-Cas9 on IVF embryos from HIV-serodiscordant couples to disrupt *CCR5*, aiming at a CCR5-Δ32-like HIV-resistance phenotype; twins “Lulu” and “Nana” were born Oct 2018; a third child followed in 2019 (MIT Technology Review excerpts of the unpublished manuscript, 3 Dec 2019).

📚 The implanted edits were not CCR5-Δ32: contemporaneous reads of the drafts show mosaicism and novel alleles (e.g. 15-bp in-frame deletion vs −4 / +1 frameshifts), not the natural 32-bp deletion (MIT Technology Review, 2019).

📚 Nanshan District Court, Shenzhen, 30 Dec 2019: He guilty of illegal medical practice — forged ethics documents, recruited HIV-serodiscordant couples, implanted edited embryos; three gene-edited babies born; sentence 3 years prison + 3 million yuan (China court English release, https://english.court.gov.cn/2019-12/31/c_761907.htm).

🐉 Published follow-up establishing disease or cancer in the three He Jiankui children was not found this round; unknown pediatric outcome is not a clean bill of health and is not a ☠︎︎ medical-harm adjudication.

### No CRISPR aging RCT

🐉 A ClinicalTrials.gov query on 3 Sep 2026 for CRISPR AND (aging OR longevity OR senolytic) did not return an interventional CRISPR trial with an organismal aging / healthspan primary endpoint (ClinicalTrials.gov API v2).

🐉 No completed human RCT of a CRISPR effector as an aging therapy was found this round. That absence is not disproof that someone will run one.

## Measurement

📚 TIDE decomposes Sanger traces from a PCR of the cut site versus a control to report indel frequencies (Brinkman et al., Nucleic Acids Research, 2014, https://doi.org/10.1093/nar/gku936, PMID 25300484).

🤔 ICE (Inference of CRISPR Edits, Synthego) is the competing Sanger-deconvolution tool: upload .ab1 pairs + spacer; outputs a KO score (frameshift or ≥21 bp indel fraction); hosted at ice.synthego.com (Synthego ICE guide, https://www.synthego.com/guide/how-to-use-crispr/ice-analysis-guide/).

🤔 IDT sells T7EI mismatch cleavage as a fast gel readout; the protocol states T7EI misses 1-bp indels and therefore underrepresents total editing (IDT Alt-R Genome Editing Detection Kit Protocol, https://sfvideo.blob.core.windows.net/sitefinity/docs/default-source/protocol/alt-r-genome-editing-detection-kit.pdf).

🤼 TIDE vs ICE vs T7EI vs amplicon-NGS is a lab-practice split on what “percent editing” means: T7EI misses 1-bp events; Sanger deconvolution is cheap and model-dependent; NGS is the ground-truth distribution (IDT T7EI protocol; Brinkman 2014; Synthego ICE).

🤔 rhAmpSeq is IDT’s targeted amplicon-NGS product for on-target / nominated off-target quantification — a vendor assay, not a genome-wide discovery method.

📚 Genome-wide off-target discovery methods are GUIDE-seq (cell-based dsODN capture), CIRCLE-seq / CHANGE-seq / Digenome-seq (biochemical). They disagree on site lists (Tsai 2015; Tsai 2017; Lazzarotto 2020; Kim 2015).

🤔 Clinics do not sell a consumer “CRISPR edit score.” What exists in the wild as a longevity score is clocks / telomeres / CHIP panels, not duplex-sequenced Cas9 outcomes (adjacent hallmark 01 / 03 practice, not this page’s assay).

## What clinics and self-experimenters are doing

🤔 A competent academic lab knocks out a locus with Cas enzyme + a unique ~20-nt spacer next to a PAM (NGG for SpCas9), delivered as plasmid, mRNA, or RNP, then genotypes the indel distribution; knock-in uses a donor and is less efficient than NHEJ knockout (Addgene CRISPR Guide; Ran et al., Nature Protocols, 2013).

🤔 Typical vendor knockout loop: design 1–3 guides → RNP nucleofection/lipofection → PCR + Sanger → ICE/TIDE → optional clone isolation → protein assay (Synthego ICE guide; IDT Alt-R T7EI protocol; Thermo TrueCut UG).

🤔 Synthego’s RNP cookbook forms sgRNA:Cas9 at 3:1–9:1 for electroporation; example 180 pmol sgRNA + 20 pmol Cas9 in 30 µL for 1.5×10^5 cells; incubate 10 min RT (Synthego Synthetic sgRNA Quickstart, https://andersenlab.org/Protocols/20190524_synthego-quickstart-sgrna.pdf).

🤔 Thermo TrueCut Cas9 v2: maintain 1:1 molar Cas9:gRNA; deliver with Lipofectamine CRISPRMAX or Neon electroporation (Thermo TrueCut UG MAN0017066).

🤔 Typical HDR workflow in the Addgene guide: cut as close as possible to the edit; donor = ssODN for small changes or dsDNA/plasmid for large inserts; silent-mutate PAM/seed in the donor; expect NHEJ-majority pools (Addgene CRISPR Guide).

🤔 On 3–4 Oct 2017 Josiah Zayner livestreamed a forearm injection of a plasmid encoding Cas9 + a myostatin-exon-1 gRNA; he later reported no increase in arm circumference and an inconclusive DNA-change assay (Zayner, Oct 2017, http://www.josiahzayner.com/2017/10/the-first-human-to-attempt-crispr-gene.html; Technology Networks interview, https://www.technologynetworks.com/genomics/articles/meet-josiah-zayner-the-biohacker-next-door-320964; The Odin sells the kits).

📚 FDA states it considers any use of CRISPR/Cas9 gene editing in humans to be gene therapy; sale of gene-therapy products intended for self-administration and DIY kits to produce them is against the law (FDA, “Information About Self-Administration of Gene Therapy,” https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/information-about-self-administration-gene-therapy).

🤔 The Odin’s current CRISPR SKUs fetched this round are microbial education kits: CRISPR Bacteria Gene Editing Kit $129 (starter $49.99), combo with fluorescent yeast $278; DH5α *E. coli*, Cas9 / gRNA / repair-template plasmids, antibiotic-resistance readout — not a human RNP/LNP (The Odin, https://www.the-odin.com/crispr-kit/).

⛔ “Inject The Odin plasmid and you are edited” is contradicted by Zayner’s own null/inconclusive read-out, by the product’s not-injectable label, and by the absence of a documented human myostatin knockout from that stunt (Zayner 2017; FDA 2017; The Odin 2026 kit page).

🤼 DIY-bio marketing (“anyone can edit DNA”) versus FDA 2017 + microbial-only SKUs is an amateur fight, not a paper fight (The Odin kit pages; FDA 2017; Zayner 2017).

🤔 Cash-pay “gene therapy” tourism exists in Próspera / Roatán (Minicircle follistatin plasmid; Unlimited Bio cocktails; GARM Clinic) under a regulation that lists “Gene and Plasmid Therapies” — plasmid/AAV gene-addition products, not Cas editors (MIT Technology Review, 13 Feb 2023, https://www.technologyreview.com/2023/02/13/1068330/minicircle-prospera-honduras-biohacking-follistatin-gene-therapy/).

🤔 No cash-pay clinic page fetched this round that actually administers Cas9 / Cas12 / base editor / prime editor as a named CRISPR medicine. The tourism that exists is mislabeled gene addition.

🤔 Human candidate RJB-0402 is described as AAV8 liver-expressed FGF21 for DSP arrhythmogenic cardiomyopathy — gene addition, not CRISPR (Davidsohn et al., PNAS, 2019).

🤔 Ownership fight is Broad/MIT/Harvard (Zhang) vs CVC (UC Berkeley / Vienna / Charpentier) over eukaryotic CRISPR-Cas9. Interference 106,115: PTAB awarded eukaryotic priority to Broad (2022); Federal Circuit vacated and remanded (12 May 2025); PTAB reaffirmed Broad 26 Mar 2026; CVC noticed appeal 26 May 2026 (PTAB Law Blog, 24 Jun 2026, https://www.ptablaw.com/2026/06/24/ptab-reaffirms-broad-institute-priority-in-crispr-cas9-interference-no-106-115/).

⛔ Patent priority is not evidence that Cas9 cuts DNA (Jinek et al., Science, 2012).

## Speculative

🐉 Transient partial reprogramming, AAV-TERT, or OSK delivered as gene addition might change tissue function without a Cas cut; calling that “CRISPR for aging” is a definition launder, not a CRISPR result.

🐉 In vivo extrahepatic CRISPR (muscle, CNS, heart) is a delivery problem, not a missing PAM: AAV immunogenicity, cargo limits, and LNP tropism are why liver secreted-protein knockdowns exist and whole-body aging edits do not (Taha 2022; Nelson 2019; Finn 2018).

🐉 Prime editing or high-fidelity base editors might write specified alleles in HSPCs or hepatocytes at rates that matter clinically without a classical DSB; PM359 and VERVE-102 are early human objects, not an aging protocol (Anzalone 2019; Vafai 2026; Prime Medicine 2025).

🐉 Allele-specific mtDNA base editing (DdCBE/TALED) is a TALE-deaminase stack, not CRISPR-Cas, because Cas proteins do not import into mitochondria with a guide RNA; it is parked on hallmarks 01 and 07 as not-systemic-aging-therapy (Mok et al., Nature, 2020, https://doi.org/10.1038/s41586-020-2477-4, PMID 32641830).

🐉 A one-and-done liver LNP that knocks down a secreted aging-associated protein (TTR-class logic applied to some other hepatocyte target) is a coherent hope; it is still liver pharmacology, not organismal genome rewriting (Gillmore 2021; Finn 2018).

🐉 Published medical harm in the He Jiankui children remains unknown; absence of a paper is not a safety result.

## Named compounds

None. This page is the editor stack and the products, not a molecule SKU. No `compounds/` dir exists for Cas9, Casgevy, nex-z, or VERVE-102. Catalog: [compounds/README.md](../../compounds/README.md).

## Adjacent hallmarks

📚 Cas9 DSBs, off-target cuts, large deletions, chromothripsis, and p53 selection are genomic-instability objects — hallmark 01 — not proof that ordinary aging is an editable mutation burden ([hallmarks/01-genomic-instability/report.md](../../hallmarks/01-genomic-instability/report.md); Kosicki 2018; Leibowitz 2021; Haapaniemi 2018).

📚 CRISPRi/a and CRISPRoff change transcription or deposit methylation without a sequence rewrite; that coupling lives in hallmark 03 ([hallmarks/03-epigenetic-alterations/report.md](../../hallmarks/03-epigenetic-alterations/report.md); Qi 2013; Nuñez 2021).

📚 mtDNA editors in the repo are DdCBE/TALED (TALE-deaminase), not nuclear CRISPR-Cas; hallmark 07 parks them as not-systemic-aging-therapy ([hallmarks/07-mitochondrial-dysfunction/report.md](../../hallmarks/07-mitochondrial-dysfunction/report.md); Mok et al., Nature, 2020).

## What is actually on the table

💯 The array, the RNA-guided Cas cut, and DSB repair as NHEJ-vs-HDR are textbook. The molecule specifies a target next to a PAM; the cell writes the genotype.

📚 Engineered editors (nickase, dCas, CBE, ABE, PE) and mammalian cell editing are published and not in a naming fight. Outcome distributions, large deletions, CBE RNA/DNA off-targets, AAV cargo/NAb limits, and LNP liver tropism are published too.

🥼 p53 selection and chromothripsis after DSBs are live paper fights against Casgevy packages that did not report those events in patients and still require long-term malignancy PMR. Off-target assay menus disagree on site lists.

📚 Casgevy is a real ex vivo HSPC *BCL11A*-enhancer medicine with VOC-free / transfusion-independence rates in the 90% range after busulfan, a $2.2M list price, center-capacity limits, and documented transplant-regimen deaths. Intellia liver LNP knocked down TTR and KLKB1 in humans; nex-z took a 2025 Grade 4 liver SAE, a death attributed by the PI to ulcer/sepsis, a hold, and a 2026 lift. Verve paused VERVE-101 after LNP-attributed Grade 3 liver/platelet events and published VERVE-102 PCSK9/LDL reductions. EDIT-101 dosed 14 retinas and paused. He Jiankui implanted mosaic non-Δ32 *CCR5* edits and went to prison.

🤔 Labs run Addgene plasmids and IDT/Synthego/Thermo RNPs and argue TIDE vs ICE vs T7EI. Zayner injected a myostatin plasmid on camera and reported a null. The Odin sells $50–$129 bacteria kits. No cash-pay CRISPR clinic was fetched. No CRISPR aging RCT was fetched. Longevity shops selling AAV-FGF21 / follistatin plasmids are not CRISPR.

⛔ CRISPR is not one product, not a kitchen-to-human protocol, not Lyfgenia, not Rejuvenate AAV, and not a general aging rewrite.

🐉 Extrahepatic in vivo editing, a specified-allele aging indication, and the long-term health of the He Jiankui children remain guesses or unknowns.
