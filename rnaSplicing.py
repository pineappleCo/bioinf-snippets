import fastaForm
import transcription
import translation

def splicing(sequence, introns):
    intronRemovedSeq = sequence.getSequence()
    for intron in introns:
        intronRemovedSeq = intronRemovedSeq.replace(intron.getSequence(), '')
    toTranscribe = fastaForm.NucleicFasta()
    toTranscribe.assignSequence(intronRemovedSeq)
    mRNA = transcription.transcribe(toTranscribe)
    return translation.translate(mRNA)




