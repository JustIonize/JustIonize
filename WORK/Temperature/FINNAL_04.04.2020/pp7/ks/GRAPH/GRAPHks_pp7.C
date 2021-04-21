#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1000, 1000);
    c1->Divide(3,2);

    double m = 0.497648;


//____________________________________________________________



    c1->cd(1);
    g1 = new TGraphErrors("ks_pp7.txt");
    g1->SetMarkerStyle(21);

    gPad->SetLogy(1);
    G1 = new TGraph("ks_pp7.txt");
    G1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    f1 = new TF1("f1", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    f1->SetParameter(1, 1);
    f1->SetParameter(0, 11.6);


    G1->Fit(f1,"NRM");
    G1->Draw("APSAME");


    f1->SetLineWidth(3);
    f1->SetLineColor(kGreen+1);
    f1->Draw("SAME");

    g1->SetLineWidth(3);
    g1->Draw("PSAME");





//________________________________________________________





    c1->cd(2);
    g2 = new TGraphErrors("ks_pp7.txt");
    g2->SetMarkerStyle(21);

    gPad->SetLogy(1);
    G2 = new TGraph("ks_pp7.txt");
    G2->SetTitle("1203 nameless; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    f2 = new TF1("f2", "[1]*x*pow((x*x+0.497648*0.497648),0.5)*pow((1+([2]-1)*pow((x*x+0.497648*0.497648),0.5)*[0]),-([2]/([2]-1)))",0, 6);
    f2->SetParameter(2, 1.15);
    f2->SetParameter(1, 1000);
    f2->SetParameter(0, 11.6);


    G2->Fit(f2,"NRM");
    G2->Draw("APSAME");


    f2->SetLineWidth(3);
    f2->SetLineColor(kGreen+1);
    f2->Draw("SAME");

    g2->SetLineWidth(3);
    g2->Draw("PSAME");




//__________________________________________________________





    c1->cd(3);
    g3 = new TGraphErrors("ks_pp7.txt");
    g3->SetMarkerStyle(21);

    gPad->SetLogy(1);
    G3 = new TGraph("ks_pp7.txt");
    G3->SetTitle("1905_2; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    f3 = new TF1("f3", "[1]*x*pow((1-[2]*[0]*(pow((x*x+0.497648*0.497648),0.5))),(1/[2]))",0, 6);
    f3->SetParameter(2, 0.015);
    f3->SetParameter(1, 100000);
    f3->SetParameter(0, 11.6);


    G3->Fit(f3,"NRM");
    G3->Draw("APSAME");


    f3->SetLineWidth(3);
    f3->SetLineColor(kGreen+1);
    f3->Draw("SAME");

    g3->SetLineWidth(3);
    g3->Draw("PSAME");





//-------------------------------------------------



    c1->cd(4);
    g4 = new TGraphErrors("ks_pp7.txt");
    g4->SetMarkerStyle(21);

    gPad->SetLogy(1);
    G4 = new TGraph("ks_pp7.txt");
    G4->SetTitle("1905_3; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    f4 = new TF1("f4", "[1]*x*pow((1-[2]*[0]*x),(1/[2]))",0, 6);

    f4->SetParameter(2, -0.15);
    f4->SetParameter(1, 100);
    f4->SetParameter(0, 5.8);


    g4->Fit(f4,"NRM");
    g4->Draw("APSAME");


    f4->SetLineWidth(3);
    f4->SetLineColor(kGreen+1);
    f4->Draw("SAME");

    g4->SetLineWidth(3);
    g4->Draw("PSAME");


//_____________________________________________________________



    c1->cd(5);
    g5 = new TGraphErrors("ks_pp7.txt");
    g5->SetMarkerStyle(21);

    gPad->SetLogy(1);
    G5 = new TGraph("ks_pp7.txt");
    G5->SetTitle("1505; pT GeV ; d(sigma)/d(pT) mb*C/(GeV)");

    
    f5 = new TF1("f5", "[2]*x*pow((1-(sqrt(pow(0.497648,2)+(x)^2)  - 0.497648 )*[0]*[1])  ,  (1/[1])  )",0, 6);

    f5 ->SetParameter(0,1);    
    f5 ->SetParameter(1, -0.15);
    f5 ->SetParameter(2,1);



    g5->Fit(f5,"NRM");
    g5->Draw("APSAME");


    f5->SetLineWidth(3);
    f5->SetLineColor(kGreen+1);
    f5->Draw("SAME");

    g5->SetLineWidth(3);
    g5->Draw("PSAME");











//_____________________________________________________________

    c2 = new TCanvas("c2","ALL", 750, 650);

    c2->cd();

    gPad->SetLogy(1);
    g = new TGraphErrors("ks_pp7.txt"); 
    g->SetTitle(";p_{T} (GeV/c);#frac{1}{N_{evt}} #frac{d^{2}N}{dydp_{T}} (#frac{1}{GeV/c})");

    g->SetMarkerStyle(21);
    g->SetMarkerSize(2.0);
    g->Draw("APSAME");


// FUNCTIONS :


    f1->SetLineColor(kGreen+1);
    f1->SetLineStyle(1);
    f1->Draw("SAME");

    f2->SetLineColor(kCyan+1);
    f2->SetLineStyle(5);
    f2->Draw("SAME");

    f3->SetLineColor(kBlue+0);
    f3->SetLineStyle(6);
    f3->Draw("SAME");

    f4->SetLineColor(kMagenta+1);
    f4->SetLineStyle(7);
    f4->Draw("SAME");

    f5->SetLineColor(kRed+1);
    f5->SetLineStyle(10);
    f5->Draw("SAME");

    g->SetLineWidth(3);
    g->Draw("PSAME");








    auto legend = new TLegend(0.8,0.6,0.9,0.9);
    legend->SetTextSize(0.035);
    //legend->SetTextFont(4);
    //legend->SetHeader("Models","C");
    legend->AddEntry("f1","F_{C1} ","l");
    legend->AddEntry("f2","F_{T7}","l");
    legend->AddEntry("f3","F_{T4}","l");
    legend->AddEntry("f4","F_{T3}","l");
    legend->AddEntry("f5","F_{T6}","l");
    legend->Draw();


    TLatex latex;
    latex.SetTextSize(0.04);
    latex.SetTextAlign(0);
    latex.DrawLatex( 3.3, -10, "");

    TLatex latexY;
    latexY.SetTextSize(0.04);
    latexY.SetTextAlign(10);
    latexY.SetTextAngle(90);
    latexY.DrawLatex(-0.2,0.5,"");

    TLatex latexD;
    latexD.SetTextSize(0.04);
    latexD.SetTextAlign(40);
    latexD.SetTextAngle(0);
    //latexD.SetTextFont(3);
    latexD.DrawLatex(1.5,1,"K_{s}^{0}, ALICE p-p #sqrt{s_{NN}}= 7 TeV");



}
