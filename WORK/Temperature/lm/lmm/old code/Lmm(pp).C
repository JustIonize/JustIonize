//building and aprocsimation for ks_down
#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    c1->Divide(3,2);
    m = 1.115683;


    c1->cd(1);
    g1 = new TGraphErrors("lm_pp.txt");
    g1->SetMarkerStyle(7);
    gPad->SetLogy(1);
    G1 = new TGraph("lm_pp.txt");
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
    

    


    c1->cd(2);
    g2 = new TGraphErrors("lm_pp.txt");
    g2->SetMarkerStyle(7);
    gPad->SetLogy(1);    
    G2 = new TGraph("lm_pp.txt");
    G2->SetTitle("Maxwell-Boltzman + Const; pT GeV ; d(sigma)/d(pT) pb^(-1) ");
    t = new TF1("t", "[1]*((x+[2])^2)*exp(-sqrt((x+[2])^2 + pow(m,2))*[0])",0, 6);
    G2->Fit(t);
    G2->Draw("APSAME");
    g2->Draw("P");
    t->SetLineWidth(3);
    t->SetLineColor(kRed+1);
    t->Draw("SAME");

    double temper2, t2e;
    temper2 = t->GetParameter(0);
    t2e = t->GetParError(0);




    c1->cd(3);
    g3 = new TGraphErrors("lm_pp.txt");    
    g3->SetMarkerStyle(7);
    gPad->SetLogy(1);   
    G3 = new TGraph("lm_pp.txt");
    G3->SetTitle("mod. Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    h = new TF1("h", "[1]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    //h = new TF1("h", "[7]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[6])",0, 6);
    G3->Fit(h);
    G3->Draw("APSAME");
    g3->Draw("P");
    h->SetLineWidth(3);
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");

    double temper3, t3e;
    temper3 = h->GetParameter(0);
    t3e = h->GetParError(0);


    c1->cd(4);
    g4 = new TGraphErrors("lm_pp.txt");    
    g4->SetMarkerStyle(7);
    gPad->SetLogy(1);   
    G4 = new TGraph("lm_pp.txt");
    G4->SetTitle("mod. Maxwell-Boltzman 2; pT GeV ; d(sigma)/d(pT) pb^(-1) ");      
    j = new TF1("j", "[1]*x*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    //h = new TF1("h", "[7]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[6])",0, 6);
    G4->Fit(j);
    G4->Draw("APSAME");
    g4->Draw("P");
    j->SetLineWidth(3);
    j->SetLineColor(kPink+0);
    j->Draw("SAME");

    double temper4, t4e;
    temper4 = j->GetParameter(0);
    t4e = j->GetParError(0);



    c1->cd(5);
    gPad->SetLogy(1);
    g = new TGraphErrors("lm_pp.txt"); 
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



    cout<<endl<<endl;
    cout<< "temperature 1 = "<<1/temper1<<endl;
    cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
    cout<< "temperature 2 = "<<1/temper2<<endl;
    cout<< "t2 error = " <<t2e/(temper2*temper2)<<endl;
    cout<< "temperature 3 = "<<1/temper3<<endl;
    cout<< "t3 error = " <<t3e/(temper3*temper3)<<endl;
    cout<< "temperature 4 = "<<1/temper4<<endl;
    cout<< "t4 error = " <<t4e/(temper4*temper4)<<endl<<endl;
    cout<< "Mean temper = " <<0.25*(1/temper1+1/temper2+1/temper3+1/temper4)<<endl;
    cout<< "Total error =  " <<0.25*sqrt(pow((t1e/(temper1*temper1)),2)+pow((t2e/(temper2*temper2)),2)+pow((t3e/(temper3*temper3)),2)+pow((t4e/(temper4*temper4)),2))<<endl<<endl;
    

}
