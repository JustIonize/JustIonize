{
    c1 = new TCanvas("c1","My", 500, 500);
    m = 0.497648;

    g1 = new TGraph("ap_down_ks.txt");    
    g1->SetTitle("New Title 1");   
    f = new TF1("f", "[1]*x*sqrt((x)^2+m^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);
    g1->Fit(f);
    g1->SetMarkerStyle(22);
    g1->Draw("AP");
}
