#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    c1->Divide(3,2);
    c2 = new TCanvas("c2","ALL", 1500, 1000);
    m = 0.497648;


//__________________________________________________________________________________

// __________________BOLTZMAN_______________________

    c1->cd(1);
    g1 = new TGraphErrors("ks_pp5.txt");
    g1->SetMarkerStyle(21);
    gPad->SetLogy(1);

    g1->SetTitle("Maxwell-Boltzman; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");
    
    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    f->SetParameter(1, 5000);
    f->SetParameter(0, 5.8);

    g1->Fit(f,"NRM");
    g1->Draw("APSAME");
    

    f->SetLineWidth(3);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");

    g1->SetLineWidth(3);
    g1->Draw("PSAME");


    double temper1, t1e, chi, ndf;
    temper1 = f->GetParameter(0);
    t1e = f->GetParError(0);
    chi = f->GetChisquare();
    ndf = f->GetNDF();


//____________1505__________________________


    c1->cd(2);
    g2 = new TGraphErrors("ks_pp5.txt");
    g2->SetMarkerStyle(21);

    gPad->SetLogy(1);
    g2->SetTitle("1505; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");
    
    v = new TF1("v", "[2]*x*pow((1-(sqrt(pow(0.497648,2)+(x)^2)  - 0.497648 )*[0]*[1])  ,  (1/[1])  )",0, 6);
    v ->SetParameter(0,5.8);    
    v ->SetParameter(1, -0.01);
    v ->SetParameter(2,1000);


    g2->Fit(v,"NRM");
    g2->Draw("APSAME");



    v->SetLineWidth(3);
    v->SetLineColor(kGreen+1);
    v->Draw("SAME");

    g2->SetLineWidth(3);
    g2->Draw("PSAME");


    double temper2, t2e, chi2, ndf2;
    temper2 = v->GetParameter(0);
    t2e = v->GetParError(0);
    chi2 = v->GetChisquare();
    ndf2 = v->GetNDF();


//_______________________2001_Hagedorn__________


    c1->cd(3);
    g3 = new TGraphErrors("ks_pp5.txt");
    g3->SetMarkerStyle(21);

    gPad->SetLogy(1);


    g3->SetTitle("Hagedorn; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");
    
    h = new TF1("h", "[1]*x*pow((1+x*[0]),(-[2]))",0, 6);
    h->SetParameter(2, 5.08244e+00);
    h->SetParameter(1, 1.94716e+04);
    h->SetParameter(0, 3.53319e+00);



    g3->Fit(h,"NRM");
    g3->Draw("APSAME");

    

    h->SetLineWidth(3);
    h->SetLineColor(kGreen+1);
    h->Draw("SAME");

    g3->SetLineWidth(3);
    g3->Draw("PSAME");


    double temper3, t3e, chi3, ndf3;
    temper3 = h->GetParameter(0);
    t3e = h->GetParError(0);
    chi3 = h->GetChisquare();
    ndf3 = h->GetNDF();



//______________________1905_2____________________________



    c1->cd(4);
    g4 = new TGraphErrors("ks_pp5.txt");
    g4->SetMarkerStyle(21);

    gPad->SetLogy(1);

   g4->SetTitle("1905_2; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    j = new TF1("j", "[1]*x*pow((1-[2]*[0]*(pow((x*x+0.497648*0.497648),0.5))),(1/[2]))",0, 6);
    j->SetParameter(2, 0.001);
    j->SetParameter(1, 100);
    j->SetParameter(0, 5);


    g4->Fit(j,"NRM");
    g4->Draw("APSAME");

    

    j->SetLineWidth(3);
    j->SetLineColor(kGreen+1);
    j->Draw("SAME");

    g4->SetLineWidth(3);
    g4->Draw("PSAME");


    double temper4, t4e, chi4, ndf4;
    temper4 = j->GetParameter(0);
    t4e = j->GetParError(0);
    chi4 = j->GetChisquare();
    ndf4 = j->GetNDF();

//___________________________1905_3________________________________

    c1->cd(5);
    g5 = new TGraphErrors("ks_pp5.txt");
    g5->SetMarkerStyle(21);

    gPad->SetLogy(1);

    g5->SetTitle("1905_3; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    k = new TF1("k", "[1]*x*pow((1-[2]*[0]*x),(1/[2]))",0, 6);
    k->SetParameter(2, -0.0736931);
    k->SetParameter(1, 296.137);
    k->SetParameter(0, 4.04043);


    g5->Fit(k,"NRM");
    g5->Draw("APSAME");


    

    k->SetLineWidth(3);
    k->SetLineColor(kGreen+1);
    k->Draw("SAME");

    g5->SetLineWidth(3);
    g5->Draw("PSAME");


    double temper5, t5e, chi5, ndf5;
    temper5 = k->GetParameter(0);
    t5e = k->GetParError(0);
    chi5 = k->GetChisquare();
    ndf5 = k->GetNDF();



//_________________________Andr_____________________________


   c1->cd(6);
    g6 = new TGraphErrors("ks_pp5.txt");
    g6->SetMarkerStyle(21);

    gPad->SetLogy(1);
    g6->SetTitle("Andronic; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");
    
    l = new TF1("l", "[1]*x*pow((1+pow((x*[0]),2)),(-[2]))",0, 6);

    l->SetParameter(2, 4);
    l->SetParameter(1, 1000000);
    l->SetParameter(0, 5);


    g6->Fit(l,"NRM");
    g6->Draw("APSAME");
    

    l->SetLineWidth(3);
    l->SetLineColor(kGreen+1);
    l->Draw("SAME");

    g6->SetLineWidth(3);
    g6->Draw("PSAME");


    double temper6, t6e, chi6, ndf6;
    temper6 = l->GetParameter(0);
    t6e = l->GetParError(0);
    chi6 = l->GetChisquare();
    ndf6 = l->GetNDF();




//__________________________________________________________________________________
  

    c2->cd();


    gPad->SetLogy(1);
    g = new TGraphErrors("ks_pp5.txt"); 
    g->SetTitle(";p_{T} (GeV) ;d#sigma/dp_{T} (mb/GeV)");
    g->SetMarkerStyle(21);
    g->SetMarkerSize(2.0);
    g->Draw("APSAME");

    f->SetLineColor(kGreen+1);
    f->SetLineStyle(1);
    f->Draw("SAME");

    h->SetLineColor(kCyan+1);
    h->SetLineStyle(5);
    h->Draw("SAME");

    v->SetLineColor(kMagenta-5);
    v->SetLineStyle(10);
    v->Draw("SAME");

    j->SetLineColor(kBlue+1);
    j->SetLineStyle(6);
    j->Draw("SAME");

    k->SetLineColor(kMagenta+1);
    k->SetLineStyle(7);
    k->Draw("SAME");

    l->SetLineColor(kOrange+10);
    l->SetLineStyle(9);
    l->Draw("SAME");

    g->SetLineWidth(3);
    g->Draw("PSAME");





}
