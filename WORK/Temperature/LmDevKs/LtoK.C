#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("Lambda to K short","My", 1000, 1000);


    c1->cd(1);

    g3 = new TGraphErrors("Lm(Dev)Ks7.txt");
    g3->SetName("g3");
    g3->SetMarkerStyle(21);
    g3->SetMarkerSize(2.0);
    g3->SetMarkerColor(kRed+1);
    g3->Draw("APSAME");
    g3->SetTitle("#Lambda/K_{s}^{0}, p-p #sqrt{s_{NN}}= 0.9, 5.02, 7 TeV;p_{T} (GeV) ;d#sigma/dp_{T} (pb/GeV)");

    g2 = new TGraphErrors("Lm(Dev)Ks5.txt");
    g2->SetName("g2");
    g2->SetMarkerStyle(21);
    g2->SetMarkerSize(2.0);
    g2->SetMarkerColor(kBlue+1);
    g2->Draw("PSAME");


    g1 = new TGraphErrors("Lm(Dev)Ks0.9.txt");
    g1->SetName("g1");
    g1->SetMarkerStyle(21);
    g1->SetMarkerSize(2.0);
    g1->SetMarkerColor(kGreen+1);
    g1->Draw("PSAME");

    f = new  TF1("f", "1", 0, 5);
    f->SetLineColor(kBlack);
    f->Draw("SAME");


auto legend = new TLegend(0.1,0.7,0.3,0.9);
    legend->SetTextSize(0.027);
    //legend->SetTextFont(4);
    //legend->SetHeader("Models","C");
    legend->AddEntry("g1","0.9 Tev","lep");
    legend->AddEntry("g2","5.02 TeV","lep");
    legend->AddEntry("g3","7 TeV","lep");
    legend->Draw();
}
