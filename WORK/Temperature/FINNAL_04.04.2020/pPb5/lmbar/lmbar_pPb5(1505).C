#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    double m = 1.115683;

    c1->cd();
    g1 = new TGraphErrors("lmbar_pPb5.txt");
    g1->SetMarkerStyle(21);

    gPad->SetLogy(1);
    G1 = new TGraph("lmbar_pPb5.txt");
    G1->SetTitle("1505; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    f = new TF1("f", "[2]*x*pow((1-(sqrt(pow(1.115683,2)+(x)^2)  - 1.115683 )*[0]*[1])  ,  (1/[1])  )",0, 6);


 //   f ->SetParameter(0,5.8);    
//    f ->SetParameter(1, -0.01);
//    f ->SetParameter(2,1000);


    f ->SetParameter(0,11.6);    
    f ->SetParameter(1, -0.01);
    f ->SetParameter(2,1000);

    G1->Fit(f,"NRM");
    G1->Draw("APSAME");


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



    cout<<endl<<endl;
    cout<< "temperature 1 = "<<1/temper1<<endl;
    cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
    cout<< "chi square = " << chi <<endl;
    cout<< "NDF = " << ndf <<endl<<endl;
}
