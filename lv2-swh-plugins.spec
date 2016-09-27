Summary:	SWH-LV2 - a set of LV2 audio plugins
Summary(pl.UTF-8):	SWH-LV2 - zestaw wtyczek dźwiękowych LV2
Name:		lv2-swh-plugins
Version:	1.0.16
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: https://github.com/swh/lv2/releases
Source0:	https://github.com/swh/lv2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	adc191d7e00e2ef9de0e6e5b546651a6
URL:		http://plugin.org.uk/
BuildRequires:	fftw3-single-devel
BuildRequires:	pkgconfig
Requires:	lv2core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWH-LV2 is a set of audio plugins by Steve Harris (see
<http://plugin.org.uk/> for more details) ported from LADSPA to LV2.

%description -l pl.UTF-8
SWH-LV2 to zestaw wtyczek dźwiękowych Steve'a Harrisa (więcej
informacji pod adresem <http://plugin.org.uk/>) sportowanych ze
specyfikacji LADSPA do LV2.

%prep
%setup -q -n lv2-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-system \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/lv2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2/a_law-swh.lv2
%{_libdir}/lv2/a_law-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/a_law-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/alias-swh.lv2
%{_libdir}/lv2/alias-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/alias-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/allpass-swh.lv2
%{_libdir}/lv2/allpass-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/allpass-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/am_pitchshift-swh.lv2
%{_libdir}/lv2/am_pitchshift-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/am_pitchshift-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/amp-swh.lv2
%{_libdir}/lv2/amp-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/amp-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/analogue_osc-swh.lv2
%{_libdir}/lv2/analogue_osc-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/analogue_osc-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/bandpass_a_iir-swh.lv2
%{_libdir}/lv2/bandpass_a_iir-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/bandpass_a_iir-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/bandpass_iir-swh.lv2
%{_libdir}/lv2/bandpass_iir-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/bandpass_iir-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/bode_shifter-swh.lv2
%{_libdir}/lv2/bode_shifter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/bode_shifter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/bode_shifter_cv-swh.lv2
%{_libdir}/lv2/bode_shifter_cv-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/bode_shifter_cv-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/butterworth-swh.lv2
%{_libdir}/lv2/butterworth-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/butterworth-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/chebstortion-swh.lv2
%{_libdir}/lv2/chebstortion-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/chebstortion-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/comb-swh.lv2
%{_libdir}/lv2/comb-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/comb-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/comb_splitter-swh.lv2
%{_libdir}/lv2/comb_splitter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/comb_splitter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/const-swh.lv2
%{_libdir}/lv2/const-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/const-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/crossover_dist-swh.lv2
%{_libdir}/lv2/crossover_dist-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/crossover_dist-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/dc_remove-swh.lv2
%{_libdir}/lv2/dc_remove-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/dc_remove-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/decay-swh.lv2
%{_libdir}/lv2/decay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/decay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/decimator-swh.lv2
%{_libdir}/lv2/decimator-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/decimator-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/declip-swh.lv2
%{_libdir}/lv2/declip-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/declip-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/delay-swh.lv2
%{_libdir}/lv2/delay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/delay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/delayorama-swh.lv2
%{_libdir}/lv2/delayorama-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/delayorama-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/diode-swh.lv2
%{_libdir}/lv2/diode-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/diode-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/divider-swh.lv2
%{_libdir}/lv2/divider-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/divider-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/dj_eq-swh.lv2
%{_libdir}/lv2/dj_eq-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/dj_eq-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/dj_flanger-swh.lv2
%{_libdir}/lv2/dj_flanger-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/dj_flanger-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/dyson_compress-swh.lv2
%{_libdir}/lv2/dyson_compress-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/dyson_compress-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/fad_delay-swh.lv2
%{_libdir}/lv2/fad_delay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/fad_delay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/fast_lookahead_limiter-swh.lv2
%{_libdir}/lv2/fast_lookahead_limiter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/fast_lookahead_limiter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/flanger-swh.lv2
%{_libdir}/lv2/flanger-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/flanger-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/fm_osc-swh.lv2
%{_libdir}/lv2/fm_osc-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/fm_osc-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/foldover-swh.lv2
%{_libdir}/lv2/foldover-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/foldover-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/foverdrive-swh.lv2
%{_libdir}/lv2/foverdrive-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/foverdrive-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/freq_tracker-swh.lv2
%{_libdir}/lv2/freq_tracker-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/freq_tracker-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/gate-swh.lv2
%{_libdir}/lv2/gate-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/gate-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/giant_flange-swh.lv2
%{_libdir}/lv2/giant_flange-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/giant_flange-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/gong-swh.lv2
%{_libdir}/lv2/gong-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/gong-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/gong_beater-swh.lv2
%{_libdir}/lv2/gong_beater-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/gong_beater-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/gverb-swh.lv2
%{_libdir}/lv2/gverb-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/gverb-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/hard_limiter-swh.lv2
%{_libdir}/lv2/hard_limiter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/hard_limiter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/harmonic_gen-swh.lv2
%{_libdir}/lv2/harmonic_gen-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/harmonic_gen-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/hermes_filter-swh.lv2
%{_libdir}/lv2/hermes_filter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/hermes_filter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/highpass_iir-swh.lv2
%{_libdir}/lv2/highpass_iir-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/highpass_iir-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/hilbert-swh.lv2
%{_libdir}/lv2/hilbert-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/hilbert-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/impulse-swh.lv2
%{_libdir}/lv2/impulse-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/impulse-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/inv-swh.lv2
%{_libdir}/lv2/inv-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/inv-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/karaoke-swh.lv2
%{_libdir}/lv2/karaoke-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/karaoke-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/latency-swh.lv2
%{_libdir}/lv2/latency-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/latency-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/lcr_delay-swh.lv2
%{_libdir}/lv2/lcr_delay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/lcr_delay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/lookahead_limiter-swh.lv2
%{_libdir}/lv2/lookahead_limiter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/lookahead_limiter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/lookahead_limiter_const-swh.lv2
%{_libdir}/lv2/lookahead_limiter_const-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/lookahead_limiter_const-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/lowpass_iir-swh.lv2
%{_libdir}/lv2/lowpass_iir-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/lowpass_iir-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/ls_filter-swh.lv2
%{_libdir}/lv2/ls_filter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/ls_filter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/matrix_ms_st-swh.lv2
%{_libdir}/lv2/matrix_ms_st-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/matrix_ms_st-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/matrix_spatialiser-swh.lv2
%{_libdir}/lv2/matrix_spatialiser-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/matrix_spatialiser-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/matrix_st_ms-swh.lv2
%{_libdir}/lv2/matrix_st_ms-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/matrix_st_ms-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/mbeq-swh.lv2
%{_libdir}/lv2/mbeq-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/mbeq-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/mod_delay-swh.lv2
%{_libdir}/lv2/mod_delay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/mod_delay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/multivoice_chorus-swh.lv2
%{_libdir}/lv2/multivoice_chorus-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/multivoice_chorus-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/offset-swh.lv2
%{_libdir}/lv2/offset-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/offset-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/phasers-swh.lv2
%{_libdir}/lv2/phasers-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/phasers-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/pitch_scale-swh.lv2
%{_libdir}/lv2/pitch_scale-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/pitch_scale-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/plate-swh.lv2
%{_libdir}/lv2/plate-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/plate-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/pointer_cast-swh.lv2
%{_libdir}/lv2/pointer_cast-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/pointer_cast-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/rate_shifter-swh.lv2
%{_libdir}/lv2/rate_shifter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/rate_shifter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/retro_flange-swh.lv2
%{_libdir}/lv2/retro_flange-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/retro_flange-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/revdelay-swh.lv2
%{_libdir}/lv2/revdelay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/revdelay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/ringmod-swh.lv2
%{_libdir}/lv2/ringmod-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/ringmod-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/satan_maximiser-swh.lv2
%{_libdir}/lv2/satan_maximiser-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/satan_maximiser-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sc1-swh.lv2
%{_libdir}/lv2/sc1-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sc1-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sc2-swh.lv2
%{_libdir}/lv2/sc2-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sc2-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sc3-swh.lv2
%{_libdir}/lv2/sc3-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sc3-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sc4-swh.lv2
%{_libdir}/lv2/sc4-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sc4-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/se4-swh.lv2
%{_libdir}/lv2/se4-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/se4-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/shaper-swh.lv2
%{_libdir}/lv2/shaper-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/shaper-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sifter-swh.lv2
%{_libdir}/lv2/sifter-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sifter-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/simple_comb-swh.lv2
%{_libdir}/lv2/simple_comb-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/simple_comb-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sin_cos-swh.lv2
%{_libdir}/lv2/sin_cos-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sin_cos-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/single_para-swh.lv2
%{_libdir}/lv2/single_para-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/single_para-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/sinus_wavewrapper-swh.lv2
%{_libdir}/lv2/sinus_wavewrapper-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/sinus_wavewrapper-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/smooth_decimate-swh.lv2
%{_libdir}/lv2/smooth_decimate-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/smooth_decimate-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/split-swh.lv2
%{_libdir}/lv2/split-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/split-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/surround_encoder-swh.lv2
%{_libdir}/lv2/surround_encoder-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/surround_encoder-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/svf-swh.lv2
%{_libdir}/lv2/svf-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/svf-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/tape_delay-swh.lv2
%{_libdir}/lv2/tape_delay-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/tape_delay-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/transient-swh.lv2
%{_libdir}/lv2/transient-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/transient-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/triple_para-swh.lv2
%{_libdir}/lv2/triple_para-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/triple_para-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/u_law-swh.lv2
%{_libdir}/lv2/u_law-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/u_law-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/valve-swh.lv2
%{_libdir}/lv2/valve-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/valve-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/valve_rect-swh.lv2
%{_libdir}/lv2/valve_rect-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/valve_rect-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/vynil-swh.lv2
%{_libdir}/lv2/vynil-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/vynil-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/wave_terrain-swh.lv2
%{_libdir}/lv2/wave_terrain-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/wave_terrain-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/xfade-swh.lv2
%{_libdir}/lv2/xfade-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/xfade-swh.lv2/plugin-Linux.so
%dir %{_libdir}/lv2/zm1-swh.lv2
%{_libdir}/lv2/zm1-swh.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/zm1-swh.lv2/plugin-Linux.so
