#!/usr/bin/env python3

#-------------- Sensitivity and Specitivity ------------------
#
#	This Program was made in connection with the lecture of 
#   Mathematical and Computational Biology in Drug Discovery
#	held by Jitao David Zhang on University Basel
#
#	It is to show and clarify sensitifity and specifity with
#	an simulated absolute Population.
#
#-------------------------------------------------------------

sensitivity = float(input("input sensitivity:"))#0.99
specificity = float(input("input specificity:"))#0.99
prevalence = float(input("input prevalence:"))#0.01
notInfected = 1-prevalence
groundpopulation = 100000
absInf = groundpopulation*prevalence
absNotInf = groundpopulation*notInfected
truePos = absInf*sensitivity
falseNeg = absInf-truePos
trueNeg = absNotInf*specificity
falsePos = absNotInf-trueNeg
testPosPos = truePos/(truePos+falsePos)
testPosNeg = falsePos/(truePos+falsePos)
testNegPos = falseNeg/(falseNeg+trueNeg)
testNegNeg = trueNeg/(falseNeg+trueNeg)

print("------------- simulated Population ------------\n")
print("prevalence:",prevalence)
print("groundpopulation:",groundpopulation)
print("absolute infected:",absInf)
print("absolute not infected",absNotInf)
print("true Positive:",truePos)
print("false Negative:",falseNeg)
print("true Negative:", trueNeg)
print("false Positive:", falsePos)
print()

print("---------------- Positive Test ----------------")
print(testPosPos*100,"% Chance being Positive")
print(testPosNeg*100,"% Chance being Negative\n")

print("---------------- Negative Test ----------------")
print(testNegPos*100,"% Chance being Positive")
print(testNegNeg*100,"% Chance being Negative")