# GSS2018_Direct

This is the repository for Group 4, covering the topic of *Dark Matter Direct Detection*. See the main repository - [GRAPPA_Student_Seminar_2018](https://github.com/bradkav/GRAPPA_Student_Seminar_2018) - for more information.

In particular, for information about the scripts, [see here](https://github.com/bradkav/GRAPPA_Student_Seminar_2018/wiki/Scripts).

Use the `review/` folder for the LaTeX files for your review and the `scripts/` folder for your code.

### Comments on the scripts

The `main code` notebook looks very nice, with lots of detailed text and latex! This is exactly the kind of thing we were looking for. Here are some hints to help you along a bit:

* Your plot of the integrated velocity distribution (velocity vs. speed_integrated) looks a little odd. It looks like when you're calling `speed_integrated(i, v_e, v_esc, sigma)` that should be `speed_integrated(i, v_esc, v_e, sigma)` based on your definition of the function. Note also that `speed_integrated` has units of 1/v (it's not a dimensionless probability as suggested by your axis label).
* Your form factor calculation is very close. At the moment, you have `m = 0.05`, meaning that your nuclear mass doesn't depend on `A` the nucleon number! You should have something like `m = 0.9315*A` if you want the mass in GeV. Next, make sure everything has matching units. If you want to input a recoil energy in units of keV, then you need to multiply it by 10^-6 to get it in GeV so that it matches other things. Of course, you can use recoil energies in GeV, just make sure everything is consistent. You should also convert distances into energies using (1/GeV) = 0.1975 fm. This is very close to what you do, but just double-check. Finally, make sure that when you're multiplying q with a distance, that you're using the distance in natural units (e.g. R1_NU instead of just R1). In the end, you should find that the Xenon form factor has a first minimum around 100 keV.
* Try to make sure that your plots have the correct units (e.g. instead of just `energy`, you should specify `keV` or `GeV` or whatever).
* Make sure that you're making all the units match in your calculations. For example, in `v_min` you probably want to convert your nuclear mass into GeV, to match the DM mass (which I assume you want in GeV). Similarly, in `diff_int_rate` it looks like your nuclear mass is in kg, but your DM mass is in GeV. Note also that the reduced mass appearing in this differential event rate is the DM-*proton* reduced mass.
* In the end, you probably want your differential event rate to have units like `events/kg/keV/day` (which is sensible for thinking about kg-scale detectors with exposures of 100s of days. Once you make sure that all your units match (see above), work out what units you end up with in the differential event rate and work out what conversion factors you need to get it into `events/kg/keV/day` (here `events` is just a number so it's dimensionless). Note for example that the local DM density typically has units of GeV/cm^3, masses typically have units of GeV (unless you've used something different) and your integrated speed distribution probably has units of (km/s)^-1, so you may need some factors of c to get rid of that. Let me - Bradley - know if you want to check the normalisation of the rates, i.e. you could send me the differential rate at a particular recoil energy and mass and we can compare some numbers :)
* Your plots of the differential rate (`plt.loglog(mDM,dRdE_test,label='E=%.2g GeV'%E)`) are nice, but this is not usually how this information is presented :) Typically, you fix the DM mass and plot dRdE as a function of E. You can put curves for multiple DM masses or multiple detector targets on the same plot so that you can see how the spectrum of recoils changes with DM mass and with detector nucleus. 
* Recoil energies are typically in the keV range. For example, Xenon1T can see recoils in the range of ~2 keV up to about 50 keV - see Fig. 1 of https://arxiv.org/abs/1805.12562.
* Once you have the differential rates, you can integrate over recoil energies to determine the *number* of signal events which are expected in a detector. Only worry about this if you have time - focus first on getting the differential recoil rates correct!


### General Comments [BK 28/06/2018]

* In the introduction, 63% seems a bit small for the fraction of matter which is Dark. Shouldn't this be more like 80+% (a reference here would be good).
* In Section 2, you describe the DM distribution as 'stationary', but this should probably be 'isotropic' (i.e. the DM has not average net motion, but it is moving).
*  In Eq. 3, I think there is a mistake. The two cross sections sigma_SI and sigma_SD should not add coherently in this way (i.e. I think you have squared the sum of the cross sections, which isn't correct). Please check this.
*  Eq. 5 and 6 should probably appear after they are mentioned (i.e. "a normalised response function of an ensemble of spin-1/2 particles:" and then have Eq. 5, etc.) rather than appearing randomly.
*  Sec. 2.2 on the velocity distribution still needs to be completed, including uncertainties on the velocity distribution and what N-body simulations (including recent hydrodynamical ones) suggest about the velocity distribution (is it a standard Maxwell-Boltzmann, or something else?)
*  To be continued... 
