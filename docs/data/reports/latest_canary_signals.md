# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T15:07:30.663007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.4574` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0852` n `12`; crypto_alt avg `-0.123` n `230`; crypto_major avg `-0.0597` n `8`; equity avg `0.0383` n `102`; fx avg `-0.0459` n `6`; index avg `-0.0372` n `25`; metal avg `-0.0417` n `20`; unknown avg `-0.0089` n `779`
- 1h: commodity avg `0.2615` n `12`; crypto_alt avg `-0.0529` n `230`; crypto_major avg `0.2403` n `8`; equity avg `0.3036` n `102`; fx avg `-0.0034` n `6`; index avg `0.0252` n `25`; metal avg `-0.0785` n `20`; unknown avg `0.0274` n `779`
- 4h: commodity avg `0.27` n `12`; crypto_alt avg `0.4822` n `230`; crypto_major avg `0.5102` n `8`; equity avg `3.9676` n `102`; fx avg `-0.2752` n `6`; index avg `0.4089` n `25`; metal avg `0.0702` n `20`; unknown avg `0.0207` n `779`
- 24h: commodity avg `0.0039` n `12`; crypto_alt avg `0.6887` n `230`; crypto_major avg `0.8708` n `8`; equity avg `3.8576` n `102`; fx avg `-0.3488` n `6`; index avg `0.3685` n `25`; metal avg `0.7051` n `20`; unknown avg `-0.0037` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
