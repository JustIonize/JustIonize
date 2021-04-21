#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{

    c1 = new TCanvas("c1","ALL", 1500, 1000);
    m = 1.115683;


    c1->cd();

    
    g1 = new TGraphErrors("Boltz.txt");
    g1->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g1->SetMarkerStyle(21);
    g1->SetMarkerColor(kGreen+1);
    g1->SetMarkerSize(4.0);
    
    f1 = new TF1("f1", "[0] + [1]*log(x/1.115683)",0, 10);
    f1->SetParameter(1, 1);
    f1->SetParameter(0, 1);
    f1->SetLineStyle(1);

    G1 = new TGraph("Boltz.txt");
    G1->Fit(f1,"N");
    G1->Draw("APSAME");
    g1->Draw("P");

    f1->SetLineWidth(3);
    f1->SetLineColor(kGreen+1);
    f1->Draw("SAME");

    g1->SetLineWidth(3);

    g1->Draw("PSAME");

//__________________________________________________________________



    g2 = new TGraphErrors("2001.txt");
    g2->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g2->SetMarkerStyle(3);
    g2->SetMarkerColor(kCyan+1);
    g2->SetMarkerSize(7.0);
    
    f2 = new TF1("f2", "[0] + [1]*log(x/1.115683)",0, 10);
    f2->SetParameter(1, 1);
    f2->SetParameter(0, 1);
    f2->SetLineStyle(2);

    G2 = new TGraph("2001.txt");
    G2->Fit(f2,"N");
    G2->Draw("PSAME");
    g2->Draw("P");

    f2->SetLineWidth(3);
    f2->SetLineColor(kCyan+1);
    f2->Draw("SAME");

    g2->SetLineWidth(3);

    g2->Draw("PSAME");


//________________________________________________________________





    g3 = new TGraphErrors("1012.txt");
    g3->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g3->SetMarkerStyle(20);
    g3->SetMarkerColor(kBlue+1);
    g3->SetMarkerSize(4.0);
    
    f3 = new TF1("f3", "[0] + [1]*log(x/1.115683)",0, 10);
    f3->SetParameter(1, 1);
    f3->SetParameter(0, 1);
    f3->SetLineStyle(3);

    G3 = new TGraph("1012.txt");
    G3->Fit(f3,"N");
    G3->Draw("PSAME");
    g3->Draw("P");

    f3->SetLineWidth(3);
    f3->SetLineColor(kBlue+1);
    f3->Draw("SAME");

    g3->SetLineWidth(3);

    g3->Draw("PSAME");


//________________________________________________________________


    g4 = new TGraphErrors("1203_2.txt");
    g4->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g4->SetMarkerStyle(22);
    g4->SetMarkerColor(kMagenta+1);
    g4->SetMarkerSize(4.0);
    
    f4 = new TF1("f4", "[0] + [1]*log(x/1.115683)",0, 10);
    f4->SetParameter(1, 1);
    f4->SetParameter(0, 1);
    f4->SetLineStyle(4);

    G4 = new TGraph("1203_2.txt");
    G4->Fit(f4,"N");
    G4->Draw("PSAME");
    g4->Draw("P");

    f4->SetLineWidth(3);
    f4->SetLineColor(kMagenta+1);
    f4->Draw("SAME");

    g4->SetLineWidth(3);

    g4->Draw("PSAME");


//________________________________________________________________


    g5 = new TGraphErrors("1905_1.txt");
    g5->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g5->SetMarkerStyle(23);
    g5->SetMarkerColor(kRed+1);
    g5->SetMarkerSize(4.0);
    
    f5 = new TF1("f5", "[0] + [1]*log(x/1.115683)",0, 10);
    f5->SetParameter(1, 1);
    f5->SetParameter(0, 1);
    f5->SetLineStyle(5);

    G5 = new TGraph("1905_1.txt");
    G5->Fit(f5,"N");
    G5->Draw("PSAME");
    g5->Draw("P");

    f5->SetLineWidth(3);
    f5->SetLineColor(kRed+1);
    f5->Draw("SAME");

    g5->SetLineWidth(3);

    g5->Draw("PSAME");


//________________________________________________________________


    g6 = new TGraphErrors("1505.txt");
    g6->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g6->SetMarkerStyle(24);
    g6->SetMarkerColor(kYellow+1);
    g6->SetMarkerSize(4.0);
    
    f6 = new TF1("f6", "[0] + [1]*log(x/1.115683)",0, 10);
    f6->SetParameter(1, 1);
    f6->SetParameter(0, 1);
    f6->SetLineStyle(6);

    G6 = new TGraph("1505.txt");
    G6->Fit(f6,"N");
    G6->Draw("PSAME");
    g6->Draw("P");

    f6->SetLineWidth(3);
    f6->SetLineColor(kYellow+1);
    f6->Draw("SAME");

    g6->SetLineWidth(3);

    g6->Draw("PSAME");


//________________________________________________________________    





//________________________________________________________________  




//________________________________________________________________ 





//________________________________________________________________


    g10 = new TGraphErrors("1905_2.txt");
    g10->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g10->SetMarkerStyle(28);
    g10->SetMarkerColor(kMagenta-7);
    g10->SetMarkerSize(4.0);
    
    f10 = new TF1("f10", "[0] + [1]*log(x/1.115683)",0, 10);
    f10->SetParameter(1, 1);
    f10->SetParameter(0, 1);
    f10->SetLineStyle(10);

    G10 = new TGraph("1905_2.txt");
    G10->Fit(f10,"N");
    G10->Draw("PSAME");
    g10->Draw("P");

    f10->SetLineWidth(3);
    f10->SetLineColor(kMagenta-7);
    f10->Draw("SAME");

    g10->SetLineWidth(3);

    g10->Draw("PSAME");


//________________________________________________________________


    g11 = new TGraphErrors("1905_3.txt");
    g11->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g11->SetMarkerStyle(29);
    g11->SetMarkerColor(kMagenta+3);
    g11->SetMarkerSize(4.0);
    
    f11 = new TF1("f11", "[0] + [1]*log(x/1.115683)",0, 10);
    f11->SetParameter(1, 1);
    f11->SetParameter(0, 1);
    f11->SetLineStyle(1);

    G11 = new TGraph("1905_3.txt");
    G11->Fit(f11,"N");
    G11->Draw("PSAME");
    g11->Draw("P");

    f11->SetLineWidth(3);
    f11->SetLineColor(kMagenta+3);
    f11->Draw("SAME");

    g11->SetLineWidth(3);

    g11->Draw("PSAME");


//________________________________________________________________ 



    g12 = new TGraphErrors("1203_3.txt");
    g12->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g12->SetMarkerStyle(30);
    g12->SetMarkerColor(kRed+3);
    g12->SetMarkerSize(4.0);
    
    f12 = new TF1("f12", "[0] + [1]*log(x/1.115683)",0, 10);
    f12->SetParameter(1, 1);
    f12->SetParameter(0, 1);
    f12->SetLineStyle(2);

    G12 = new TGraph("1203_3.txt");
    G12->Fit(f12,"N");
    G12->Draw("PSAME");
    g12->Draw("P");

    f12->SetLineWidth(3);
    f12->SetLineColor(kRed+3);
    f12->Draw("SAME");

    g12->SetLineWidth(3);

    g12->Draw("PSAME");


//________________________________________________________________
  

    g13 = new TGraphErrors("1012_2.txt");
    g13->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g13->SetMarkerStyle(5);
    g13->SetMarkerColor(kOrange+10);
    g13->SetMarkerSize(7.0);
    
    f13 = new TF1("f13", "[0] + [1]*log(x/1.115683)",0, 10);
    f13->SetParameter(1, 1);
    f13->SetParameter(0, 1);
    f13->SetLineStyle(3);

    G13 = new TGraph("1012_2.txt");
    G13->Fit(f13,"N");
    G13->Draw("PSAME");
    g13->Draw("P");

    f13->SetLineWidth(3);
    f13->SetLineColor(kOrange+10);
    f13->Draw("SAME");

    g13->SetLineWidth(3);

    g13->Draw("PSAME");


//________________________________________________________________







    auto legend = new TLegend(0.8,0.6,0.9,0.9);
    legend->SetTextSize(0.035);

    f1->SetMarkerStyle(21);
    f1->SetMarkerColor(kGreen+1);
    f1->SetMarkerSize(4.0);

    f2->SetMarkerStyle(3);
    f2->SetMarkerColor(kCyan+1);
    f2->SetMarkerSize(7.0);

    f3->SetMarkerStyle(20);
    f3->SetMarkerColor(kBlue+1);
    f3->SetMarkerSize(4.0);

    f4->SetMarkerStyle(22);
    f4->SetMarkerColor(kMagenta+1);
    f4->SetMarkerSize(4.0);

    f5->SetMarkerStyle(23);
    f5->SetMarkerColor(kRed+1);
    f5->SetMarkerSize(4.0);

    f6->SetMarkerStyle(24);
    f6->SetMarkerColor(kYellow+1);
    f6->SetMarkerSize(4.0);

    f10->SetMarkerStyle(28);
    f10->SetMarkerColor(kMagenta-7);
    f10->SetMarkerSize(4.0);

    f11->SetMarkerStyle(29);
    f11->SetMarkerColor(kMagenta+3);
    f11->SetMarkerSize(4.0);

    f12->SetMarkerStyle(30);
    f12->SetMarkerColor(kRed+3);
    f12->SetMarkerSize(4.0);

    f13->SetMarkerStyle(5);
    f13->SetMarkerColor(kOrange+10);
    f13->SetMarkerSize(7.0);

    legend->AddEntry("f1","F_{C1} ","lep");
    legend->AddEntry("f2","F_{C4}","lep");
    legend->AddEntry("f3","F_{C2}","lep");
    legend->AddEntry("f4","F_{T4}","lep");
    legend->AddEntry("f5","F_{C3}","lep");

    legend->AddEntry("f6","F_{T6}","lep");



    legend->AddEntry("f10","F_{T4}","lep");
    legend->AddEntry("f11","F_{T3}","lep");

    legend->AddEntry("f12","F_{T5}","lep");
    legend->AddEntry("f13","F_{L1}","lep");

    legend->Draw();





    TLatex latex;
    latex.SetTextSize(0.04);
    latex.SetTextAlign(0);
    latex.DrawLatex( 6, -0.16, "#sqrt{s_{NN}} (TeV)");

    TLatex latexY;
    latexY.SetTextSize(0.04);
    latexY.SetTextAlign(10);
    latexY.SetTextAngle(90);
    latexY.DrawLatex(-0.5,0.9,"T_{#Lambda} (GeV)");

    TLatex latexD;
    latexD.SetTextSize(0.04);
    latexD.SetTextAlign(40);
    latexD.SetTextAngle(0);
    //latexD.SetTextFont(3);
    latexD.DrawLatex(3.2,0.9,"T_{#Lambda} vs #sqrt{s_{NN}}, p-p collisions");



}
