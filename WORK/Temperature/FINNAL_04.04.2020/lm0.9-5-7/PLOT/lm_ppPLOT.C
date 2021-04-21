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
    g1->SetMarkerSize(2.0);
    
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
    g2->SetMarkerSize(3.6);
    
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
    g3->SetMarkerSize(2.0);
    
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
    g4->SetMarkerSize(2.0);
    
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
    g5->SetMarkerSize(2.0);
    
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
    g6->SetMarkerSize(2.0);
    
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


    g7 = new TGraphErrors("Andr.txt");
    g7->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g7->SetMarkerStyle(25);
    g7->SetMarkerColor(kSpring+10);
    g7->SetMarkerSize(2.0);
    
    f7 = new TF1("f7", "[0] + [1]*log(x/1.115683)",0, 10);
    f7->SetParameter(1, 1);
    f7->SetParameter(0, 1);
    f7->SetLineStyle(7);

    G7 = new TGraph("Andr.txt");
    G7->Fit(f7,"N");
    G7->Draw("PSAME");
    g7->Draw("P");

    f7->SetLineWidth(3);
    f7->SetLineColor(kSpring+10);
    f7->Draw("SAME");

    g7->SetLineWidth(3);

    g7->Draw("PSAME");


//________________________________________________________________  

    g8 = new TGraphErrors("1805.txt");
    g8->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g8->SetMarkerStyle(26);
    g8->SetMarkerColor(kTeal-1);
    g8->SetMarkerSize(2.0);
    
    f8 = new TF1("f8", "[0] + [1]*log(x/1.115683)",0, 10);
    f8->SetParameter(1, 1);
    f8->SetParameter(0, 1);
    f8->SetLineStyle(8);

    G8 = new TGraph("1805.txt");
    G8->Fit(f8,"N");
    G8->Draw("PSAME");
    g8->Draw("P");

    f8->SetLineWidth(3);
    f8->SetLineColor(kTeal-1);
    f8->Draw("SAME");

    g8->SetLineWidth(3);

    g8->Draw("PSAME");


//________________________________________________________________ 


   g9 = new TGraphErrors("2001 Hag.txt");
    g9->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g9->SetMarkerStyle(2);
    g9->SetMarkerColor(kAzure-2);
    g9->SetMarkerSize(2.0);
    
    f9 = new TF1("f9", "[0] + [1]*log(x/1.115683)",0, 10);
    f9->SetParameter(1, 1);
    f9->SetParameter(0, 1);
    f9->SetLineStyle(9);

    G9 = new TGraph("2001 Hag.txt");
    G9->Fit(f9,"N");
    G9->Draw("PSAME");
    g9->Draw("P");

    f9->SetLineWidth(3);
    f9->SetLineColor(kAzure-2);
    f9->Draw("SAME");

    g9->SetLineWidth(3);

    g9->Draw("PSAME");


//________________________________________________________________


    g10 = new TGraphErrors("1905_2.txt");
    g10->SetTitle(";sqrt(s_{NN}) (TeV) ; T (GeV)");
    g10->SetMarkerStyle(28);
    g10->SetMarkerColor(kMagenta-7);
    g10->SetMarkerSize(2.0);
    
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
    g11->SetMarkerSize(2.0);
    
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
    g12->SetMarkerSize(2.0);
    
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
    g13->SetMarkerSize(3.5);
    
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







    auto legend = new TLegend(0.56,0.7,0.9,0.9);
    legend->SetTextSize(0.027);



    legend->AddEntry("f1","Boltz","l");
    legend->AddEntry("f2","2001","l");
    legend->AddEntry("f3","1012","l");
    legend->AddEntry("f4","1203_2","l");
    legend->AddEntry("f5","1905_1","l");

    legend->AddEntry("f6","1505","l");
    legend->AddEntry("f7","Andronic","l");
    legend->AddEntry("f8","1805","l");
    legend->AddEntry("f9","2001 Hagedorn","l");
    legend->AddEntry("f10","1905_2","l");
    legend->AddEntry("f11","1905_3","l");

    legend->AddEntry("f12","1203_3","l");
    legend->AddEntry("f13","1012_2","l");

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
    latexD.DrawLatex(1.5,17,"K_{s}^{0} LHCb p-p #sqrt{s_{NN}}= 5.02 TeV");



}
