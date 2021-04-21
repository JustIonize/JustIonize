#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    double m = 0.497648;

    c1->cd();
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



//    cout<<endl<<endl;
//    cout<< "temperature 1 = "<<1/temper1<<endl;
 //   cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
//    cout<< "chi square = " << chi <<endl;
 //   cout<< "NDF = " << ndf <<endl<<endl; 
}
