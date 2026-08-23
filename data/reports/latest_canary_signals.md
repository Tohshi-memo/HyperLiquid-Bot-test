# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T06:52:26.125867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5485` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5485` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.0622` n `230`; crypto_major avg `-0.1346` n `8`; equity avg `-0.0157` n `121`; fx avg `-0.0801` n `6`; index avg `-0.0017` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0551` n `794`
- 1h: commodity avg `0.0111` n `12`; crypto_alt avg `0.539` n `230`; crypto_major avg `0.2589` n `8`; equity avg `-0.017` n `121`; fx avg `-0.0276` n `6`; index avg `-0.0202` n `25`; metal avg `-0.014` n `20`; unknown avg `0.2592` n `778`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `-1.5776` n `230`; crypto_major avg `-1.5797` n `8`; equity avg `-0.2473` n `121`; fx avg `-0.0554` n `6`; index avg `-0.0312` n `25`; metal avg `-0.0312` n `20`; unknown avg `0.2588` n `778`
- 24h: commodity avg `-0.0181` n `12`; crypto_alt avg `-4.3452` n `230`; crypto_major avg `-2.4806` n `8`; equity avg `-0.1867` n `121`; fx avg `0.0363` n `6`; index avg `-0.0293` n `25`; metal avg `0.0639` n `20`; unknown avg `3.38` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
