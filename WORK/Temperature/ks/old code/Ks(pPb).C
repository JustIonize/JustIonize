//building and aprocsimation for ks_down
#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    c1->Divide(3,2);
    m = 0.497648;


    c1->cd(1);
    g1 = new TGraphErrors("NEWks(pPb).txt");
    g1->SetMarkerStyle(7);
    gPad->SetLogy(1);
    G1 = new TGraph("NEWks(pPb).txt");
    G1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G1->Fit(f);
    G1->Draw("APSAME");
    g1->Draw("P");
    f->SetLineWidth(3);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");




    c1->cd(3);
    g3 = new TGraphErrors("NEWks(pPb).txt");    
    g3->SetMarkerStyle(7);
    gPad->SetLogy(1);   
    G3 = new TGraph("NEWks(pPb).txt");
    G3->SetTitle("mod. Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    h = new TF1("h", "[1]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G3->Fit(h);
    G3->Draw("APSAME");
    g3->Draw("P");
    h->SetLineWidth(3);
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");




    c1->cd(4);
    g4 = new TGraphErrors("NEWks(pPb).txt");    
    g4->SetMarkerStyle(7);
    gPad->SetLogy(1);   
    G4 = new TGraph("NEWks(pPb).txt");
    G4->SetTitle("mod. Maxwell-Boltzman 2; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    j = new TF1("j", "[1]*x*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G4->Fit(j);
    G4->Draw("APSAME");
    g4->Draw("P");
    j->SetLineWidth(3);
    j->SetLineColor(kPink+0);
    j->Draw("SAME");




    c1->cd(2);
    g2 = new TGraphErrors("NEWks(pPb).txt");
    g2->SetMarkerStyle(7);
    gPad->SetLogy(1);    
    G2 = new TGraph("NEWks(pPb).txt");
    G2->SetTitle("Maxwell-Boltzman+; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
 //   t = new TF1("t", " [1]*x*pow((1+(x*[0])*(x*[0])),([2]))",0, 6);

    t = new TF1("t", " [1]*x*pow((1+(x*[0])*(x*[0])),(-[2]))",0, 6);
    t->SetParameter(2, 1);
    t->SetParameter(1, 1);

    G2->Fit(t);
    G2->Draw("APSAME");
    g2->Draw("P");
    t->SetLineWidth(3);
    t->SetLineColor(kRed+1);
    t->Draw("SAME");

    double temper2, t2e;
    temper2 = t->GetParameter(0);
    t2e = t->GetParError(0);



    c1->cd(5);
    gPad->SetLogy(1);
    g = new TGraphErrors("NEWks(pPb).txt"); 
    g->SetTitle("All together; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    g->SetMarkerStyle(7);
    g->Draw("AP");
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");
    t->SetLineColor(kRed+1);
    t->Draw("SAME");
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");
    j->SetLineColor(kPink+0);
    j->Draw("SAME");
}
