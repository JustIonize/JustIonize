#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    c1->Divide(3,2);
    c2 = new TCanvas("c2","ALL", 1250, 1000);
    m = 1.115683;




    c1->cd(1);
    g1 = new TGraphErrors("lmbar(pp).txt");
    g1->SetMarkerStyle(21);
    gPad->SetLogy(1);
    G1 = new TGraph("lmbar(pp).txt");
    G1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G1->Fit(f,"N");
    G1->Draw("APSAME");
    g1->Draw("P");
    f->SetLineWidth(5);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");
    g1->SetLineWidth(3);
    g1->Draw("PSAME");

    double temper1, t1e;
    temper1 = f->GetParameter(0);
    t1e = f->GetParError(0);





    c1->cd(2);
    g2 = new TGraphErrors("lmbar(pp).txt");    
    g2->SetMarkerStyle(21);
    gPad->SetLogy(1);   
    G2 = new TGraph("lmbar(pp).txt");
    G2->SetTitle("mod. Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    h = new TF1("h", "[1]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G2->Fit(h,"N");
    G2->Draw("APSAME");
    g2->Draw("P");
    h->SetLineWidth(5);
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");
    g2->SetLineWidth(3);
    g2->Draw("PSAME");

    double temper2, t2e;
    temper2 = h->GetParameter(0);
    t2e = h->GetParError(0);




    c1->cd(3);
    g3 = new TGraphErrors("lmbar(pp).txt");    
    g3->SetMarkerStyle(21);
    gPad->SetLogy(1);   
    G3 = new TGraph("lmbar(pp).txt");
    G3->SetTitle("mod. Maxwell-Boltzman 2; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    j = new TF1("j", "[1]*x*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    G3->Fit(j,"N");
    G3->Draw("APSAME");
    g3->Draw("P");
    j->SetLineWidth(5);
    j->SetLineColor(kPink+0);
    j->Draw("SAME");
    g3->SetLineWidth(3);
    g3->Draw("PSAME");

    double temper3, t3e;
    temper3 = j->GetParameter(0);
    t3e = j->GetParError(0);





    c1->cd(4);
    g4 = new TGraphErrors("lmbar(pp).txt");    
    g4->SetMarkerStyle(21);
    gPad->SetLogy(1);   
    G4 = new TGraph("lmbar(pp).txt");
    G4->SetTitle("mod. Maxwell-Boltzman 3; pT GeV ; d(sigma)/d(pT) pb^(-1) "); 
    k = new TF1("k", "[2]*2*pi*x*pow((1-(sqrt(pow(1.115683,2)+(x)^2)  - 1.115683 )*[0]*[1])  ,  (1/[1])  )",0, 6);
    k ->SetParameter(1, -1);
    k ->SetParameter(0,4);
    k ->SetParameter(2,50);
    G4->Fit(k,"N");
    G4->Draw("APSAME");
    g4->Draw("P");
    k->SetLineWidth(5);
    k->SetLineColor(kGreen+4);
    k->Draw("SAME");
    g4->SetLineWidth(3);
    g4->Draw("PSAME");

    double temper4, t4e;
    temper4 = k->GetParameter(0);
    t4e = k->GetParError(0);







    c1->cd(5);
    g5 = new TGraphErrors("lmbar(pp).txt");
    g5->SetMarkerStyle(21);
    gPad->SetLogy(1);    
    G5 = new TGraph("lmbar(pp).txt");
    G5->SetTitle("Maxwell-Boltzman+; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    t = new TF1("t", " [1]*x*pow((1+(x*[0])*(x*[0])),(-[2]))",0, 6);
    t->SetParameter(2, 1);
    t->SetParameter(1, 1);
    G5->Fit(t,"N");
    G5->Draw("APSAME");
    g5->Draw("P");
    t->SetLineWidth(5);
    t->SetLineColor(kRed+1);
    t->Draw("SAME");
    g5->SetLineWidth(3);
    g5->Draw("PSAME");

    double temper5, t5e;
    temper5 = t->GetParameter(0);
    t5e = t->GetParError(0);





    c1->cd(6);
    g6 = new TGraphErrors("lmbar(pp).txt");
    g6->SetMarkerStyle(21);
    gPad->SetLogy(1);    
    G6 = new TGraph("lmbar(pp).txt");
    G6->SetTitle("Maxwell-Boltzman++; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    //z = new TF1("z", " [1]*x*pow((1+x*[0]),(-[2]))",0, 6);
    z = new TF1("z", " ([1]*x*x/1.115683)*pow((1+x*[0]),(-[2]))",0, 6);
    z->SetParameter(2, 1);
    z->SetParameter(1, 1);
    G6->Fit(z,"N");
    G6->Draw("APSAME");
    g6->Draw("P");
    z->SetLineWidth(5);
    z->SetLineColor(kBlue+4);
    z->Draw("SAME");
    g6->SetLineWidth(3);
    g6->Draw("PSAME");

    double temper6, t6e;
    temper6 = z->GetParameter(0);
    t6e = z->GetParError(0);






    c2->cd();


    gPad->SetLogy(1);
    g = new TGraphErrors("lmbar(pp).txt"); 
    g->SetTitle(";p_{T} (GeV) ;d#sigma/dp_{T} (pb/GeV)");
   g->SetMarkerStyle(21);
    g->SetMarkerSize(2.0);
    g->Draw("APSAME");

    f->SetLineColor(kGreen+1);
    f->SetLineStyle(1);
    f->Draw("SAME");

    h->SetLineColor(kCyan+1);
    h->SetLineStyle(5);
    h->Draw("SAME");

    j->SetLineColor(kBlue+1);
    j->SetLineStyle(6);
    j->Draw("SAME");

    k->SetLineColor(kMagenta+1);
    k->SetLineStyle(7);
    k->Draw("SAME");

    t->SetLineColor(kRed+1);
    t->SetLineStyle(9);
    t->Draw("SAME");    

    z->SetLineColor(kYellow+1);
    z->SetLineStyle(10);
    z->Draw("SAME");
    g->SetLineWidth(3);
    g->Draw("PSAME");



    auto legend = new TLegend(0.65,0.5,0.9,0.9);
    legend->SetTextSize(0.02);
    //legend->SetTextFont(4);
    legend->SetHeader("Models","C");
    legend->AddEntry("f","Cp_{T}^{2}exp#[]{ - #frac{#sqrt{p_{T}^{2} + m^{2}}}{T}}","l");
    legend->AddEntry("h","Cp_{T}#sqrt{p_{T}^{2} + m^{2}}exp#[]{ - #frac{#sqrt{p_{T}^{2} + m^{2}}}{T}}","l");
    legend->AddEntry("j","Cp_{T}exp#[]{1 - #frac{#sqrt{p_{T}^{2} + m^{2}}}{T}}","l");
    legend->AddEntry("k","Cp_{T}#[]{1 - n#frac{(#sqrt{p_{T}^{2} + m^{2}} - m)}{T}}^{#frac{1}{n}}","l");
    legend->AddEntry("t","Cp_{T}#[]{1 + (#frac{p_{T}}{T})^{2}}^{-n}","l");
    legend->AddEntry("z","C#frac{p_{T}^{2}}{m}#[]{1 + #frac{p_{T}}{T}}^{-n}","l");
    legend->Draw();



    TLatex latex;
    latex.SetTextSize(0.04);
    latex.SetTextAlign(0);
    latex.DrawLatex( 3.3, -10, "");

    TLatex latexY;
    latexY.SetTextSize(0.04);
    latexY.SetTextAlign(10);
    latexY.SetTextAngle(90);
    latexY.DrawLatex(-0.2,0.2,"");

    TLatex latexD;
    latexD.SetTextSize(0.04);
    latexD.SetTextAlign(40);
    latexD.SetTextAngle(0);
    //latexD.SetTextFont(3);
    latexD.DrawLatex(1.5,11,"#bar{#Lambda} LHCb p-p #sqrt{s_{NN}}= 5.02 TeV");






    cout<<endl<<endl;
    cout<< "temperature 1 = "<<1/temper1<<endl;
    cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
    cout<< "temperature 2 = "<<1/temper2<<endl;
    cout<< "t2 error = " <<t2e/(temper2*temper2)<<endl;
    cout<< "temperature 3 = "<<1/temper3<<endl;
    cout<< "t3 error = " <<t3e/(temper3*temper3)<<endl;
    cout<< "temperature 4 = "<<1/temper4<<endl;
    cout<< "t4 error = " <<t4e/(temper4*temper4)<<endl;
    cout<< "temperature 5 = "<<1/temper5<<endl;
    cout<< "t5 error = " <<t5e/(temper5*temper5)<<endl;
    cout<< "temperature 6 = "<<1/temper6<<endl;
    cout<< "t6 error = " <<t6e/(temper6*temper6)<<endl<<endl;
   // cout<< "temperature 7 = "<<1/temper7<<endl;
   // cout<< "t7 error = " <<t7e/(temper7*temper7)<<endl<<endl;

    cout<< "Mean temper = " <<0.25*(1/temper1+1/temper2+1/temper3+1/temper4+1/temper5+1/temper6)<<endl;
    cout<< "Total error =  " <<0.25*sqrt(pow((t1e/(temper1*temper1)),2)+pow((t2e/(temper2*temper2)),2)+pow((t3e/(temper3*temper3)),2)+pow((t4e/(temper4*temper4)),2)+pow((t5e/(temper5*temper5)),2)+pow((t6e/(temper6*temper6)),2))<<endl<<endl;
}
