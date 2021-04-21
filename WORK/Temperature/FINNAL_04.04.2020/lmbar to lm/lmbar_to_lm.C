#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 750, 650);



    c1->cd();

    g2 = new TGraphErrors("lmbar_to_lm_p-Pb.txt");
    g2->SetMarkerStyle(21);

    g2->SetMarkerColor(4);
    g2->SetMarkerSize(2.5);
    g2->SetLineWidth(2);
    g2->Draw("AP");


    g1 = new TGraphErrors("lmbar_to_lm_p-p.txt");
    g1->SetMarkerStyle(21);

    g1->SetMarkerColor(2);
    g1->SetMarkerSize(2.5);
    g1->SetLineWidth(2);
    g1->Draw("PSAME");

    f = new TF1("f", "1",0, 7);
    f->SetLineWidth(3);
    f->SetLineColor(1);
    f->Draw("SAME");



    auto legend = new TLegend(0.75,0.7,0.9,0.9);
    legend->SetTextSize(0.035);


    legend->AddEntry("g2","p-Pb ","l");
    legend->AddEntry("g1","p-p ","l");


    legend->Draw();





    TLatex latex;
    latex.SetTextSize(0.04);
    latex.SetTextAlign(0);
    latex.DrawLatex( 4.5, 0.3, "p_{T} (GeV)");

    TLatex latexY;
    latexY.SetTextSize(0.04);
    latexY.SetTextAlign(0);
    latexY.SetTextAngle(90);
    latexY.DrawLatex(-0.5,1.8,"#bar{#Lambda}/#Lambda");

    TLatex latexD;
    latexD.SetTextSize(0.04);
    latexD.SetTextAlign(40);
    latexD.SetTextAngle(0);
    //latexD.SetTextFont(3);
    latexD.DrawLatex(3.2,1.8,"#bar{#Lambda}/#Lambda, LHCb p-p p-Pb #sqrt{s_{NN}}= 5.02 TeV");
}
