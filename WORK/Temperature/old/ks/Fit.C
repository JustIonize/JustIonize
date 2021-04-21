//building and aprocsimation for ks_down
{
    c1 = new TCanvas("c1","My", 1000, 1000);
    c1->Divide(2,2);
    m = 0.497648;


    c1->cd(1);

    g1 = new TGraphErrors("ap_down_ks.txt");
    g1->SetMarkerStyle(22);
    gPad->SetLogy(1);

    G1 = new TGraph("ap_down_ks.txt");
    G1->SetTitle("Maxwell-Boltzman"); 

    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);

    G1->Fit(f);
    G1->Draw("APSAME");
    g1->Draw("P");

    f->SetLineColor(kGreen+1);
    f->Draw("SAME");

    

    c1->cd(2);
    g2 = new TGraphErrors("ap_down_ks.txt");
    g2->SetMarkerStyle(22);
    gPad->SetLogy(1);    

    G2 = new TGraph("ap_down_ks.txt");
    G2->SetTitle("Maxwell-Boltzman + Const");

    t = new TF1("t", "[4]*((x+[5])^2)*exp(-sqrt((x+[5])^2 + pow(m,2))*[3])",0, 6);
    G2->Fit(t);
    G2->Draw("APSAME");
    g2->Draw("P");

    t->SetLineColor(kRed+1);
    t->Draw("SAME");


    m = 0.497648;

    c1->cd(3);
    g3 = new TGraphErrors("ap_down_ks.txt");    
    g3->SetMarkerStyle(22);
    gPad->SetLogy(1);   

    G3 = new TGraph("ap_down_ks.txt");
    G3->SetTitle("mod. Maxwell-Boltzman");      

    h = new TF1("h", "[7]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[6])",0, 6);
    G3->Fit(h);
    G3->Draw("APSAME");
    g3->Draw("P");

    h->SetLineColor(kBlue+1);
    h->Draw("SAME");


    c1->cd(4);

    gPad->SetLogy(1);
    g = new TGraphErrors("ap_down_ks.txt"); 
    g->SetTitle("Al together");
    g->SetMarkerStyle(22);
    g->Draw("AP");

    f->SetLineColor(kGreen+1);
    f->Draw("SAME");
    t->SetLineColor(kRed+1);
    t->Draw("SAME");
    h->SetLineColor(kBlue+1);
    h->Draw("SAME");
}
