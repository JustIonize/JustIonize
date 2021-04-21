#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"


{
    c1 = new TCanvas("c1","My", 1000, 1000);
    //c1->Divide(2,1);
    m = 0.497648;


    //c1->cd(1);
    g1 = new TGraphErrors("NEWks.txt");
    g1->SetMarkerStyle(7);
    gPad->SetLogy(1);
    G1 = new TGraph("NEWks.txt");
    G1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G1->Fit(f);
    G1->Draw("APSAME");
    g1->Draw("P");
    f->SetLineWidth(3);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");

}
