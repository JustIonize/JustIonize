//building and aprocsimation for ks_down

{
    g = new TGraph("ap_down_ks.txt");
   // g->SetTitle("");
    double x;
    double mass;

// fit function    
    mass = 0.497648;
    fun = new TF1("fun", "-sqrt(x*x + mass*mass)/[0]"); 
    f = new TF1("f", "[1]*x*x*exp(fun)",0, 6);
    

    g->Fit(f);
    g->SetMarkerStyle(22);
    g->Draw("AP");
   // f->SetTitle("Title");
    //f->Draw("SAME");
}
