#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("TvsW(Lm)","My", 1000, 1000);


    c1->cd(1);
    
    g3 = new TGraphErrors("0.9, 5, 7 (Lm)№3.txt");
    g3->SetName("g3");
    g3->SetMarkerStyle(21);
    g3->SetMarkerSize(2.0);
    g3->SetMarkerColor(2);
    g3->Draw("ACPSAME");
    g3->SetTitle("T(#Lambda), p-p #sqrt{s_{NN}}= 0.9, 5.02, 7 TeV;#sqrt{s_{NN}} (GeV) ;T (GeV)");

    g4 = new TGraphErrors("0.9, 5, 7 (Lm)№4.txt");
    g4->SetName("g4");
    g4->SetMarkerStyle(21);
    g4->SetMarkerSize(2.0);
    g4->SetMarkerColor(3);
    g4->Draw("CPSAME");

    g2 = new TGraphErrors("0.9, 5, 7 (Lm)№2.txt");
    g2->SetName("g2");
    g2->SetMarkerStyle(21);
    g2->SetMarkerSize(2.0);
    g2->SetMarkerColor(4);
    g2->Draw("CPSAME");

    g1 = new TGraphErrors("0.9, 5, 7 (Lm)№1.txt");
    g1->SetName("g1");
    g1->SetMarkerStyle(21);
    g1->SetMarkerSize(2.0);
    g1->SetMarkerColor(6);
    g1->Draw("CPSAME");



    legend = new TLegend(0.1,0.7,0.53,0.9);
    legend->SetTextSize(0.026);
    //legend->SetTextFont(4);
    //legend->SetHeader("Models","C");
    legend->AddEntry("g1","Maxwell-Boltzmann dist.","lep");
    legend->AddEntry("g2","Bolt. + Fermi-Dir. + Bose-Ein.","lep");
    legend->AddEntry("g3","Mod. Maxwell-Boltzmann dist.","lep");
    legend->AddEntry("g4","Mod. Tsallis form","lep");
    legend->Draw();
}
