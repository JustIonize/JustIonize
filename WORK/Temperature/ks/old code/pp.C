#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
{
    c1 = new TCanvas("c1","My", 500, 500);
    m = 0.497648;



    g1 = new TGraphErrors("ks_pp.txt");
    g1->SetMarkerStyle(7);
    gPad->SetLogy(1);
    G1 = new TGraph("ks_pp.txt");
    G1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G1->Fit(f);
    G1->Draw("APSAME");
    g1->Draw("P");
    f->SetLineWidth(3);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");

    double temper1, t1e;
    temper1 = f->GetParameter(0);
    t1e = f->GetParError(0);
}
