//building and aprocsimation for ks_down
#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"

{
    c1 = new TCanvas("c1","My", 1000, 1000);
    c1->Divide(2,2);
    m = 1.115683;


    c1->cd(1);

    g1 = new TGraphErrors("pa_lmm.txt");
    g1->SetMarkerStyle(7);
    gPad->SetLogy(1);

    G1 = new TGraph("pa_lmm.txt");
    G1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) "); 

    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);

    G1->Fit(f);
    //G1->SetLineWidth(0);
    G1->Draw("APSAME");
    g1->Draw("P");

    f->SetLineWidth(3);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");

    

    c1->cd(2);
    g2 = new TGraphErrors("pa_lmm.txt");
    g2->SetMarkerStyle(7);
    gPad->SetLogy(1);    

    G2 = new TGraph("pa_lmm.txt");
    G2->SetTitle("Maxwell-Boltzman + Const; pT GeV ; d(sigma)/d(pT) pb^(-1) ");

    t = new TF1("t", "[1]*((x+[2])^2)*exp(-sqrt((x+[2])^2 + pow(m,2))*[0])",0, 6);
    //t = new TF1("t", "[4]*((x+[5])^2)*exp(-sqrt((x+[5])^2 + pow(m,2))*[3])",0, 6);
    G2->Fit(t);
    G2->Draw("APSAME");
    g2->Draw("P");
    
    t->SetLineWidth(3);
    t->SetLineColor(kRed+1);
    t->Draw("SAME");



    c1->cd(3);
    g3 = new TGraphErrors("pa_lmm.txt");    
    g3->SetMarkerStyle(7);
    gPad->SetLogy(1);   

    G3 = new TGraph("pa_lmm.txt");
    G3->SetTitle("mod. Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    

    h = new TF1("h", "[1]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    //h = new TF1("h", "[7]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[6])",0, 6);
    G3->Fit(h);
    G3->Draw("APSAME");
    g3->Draw("P");
        
    h->SetLineWidth(3);
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");


    c1->cd(4);

    gPad->SetLogy(1);
    g = new TGraphErrors("pa_lmm.txt"); 
    g->SetTitle("All together; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    g->SetMarkerStyle(7);
    g->Draw("AP");

    f->SetLineColor(kGreen+1);
    f->Draw("SAME");
    t->SetLineColor(kRed+1);
    t->Draw("SAME");
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");
}
