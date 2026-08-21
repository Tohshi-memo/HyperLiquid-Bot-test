# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T05:37:34.196718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `12`; crypto_alt avg `0.2232` n `230`; crypto_major avg `-0.0989` n `8`; equity avg `-0.0099` n `121`; fx avg `-0.0047` n `6`; index avg `-0.0106` n `25`; metal avg `0.0459` n `20`; unknown avg `-0.1019` n `793`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.4074` n `230`; crypto_major avg `0.3384` n `8`; equity avg `0.2575` n `121`; fx avg `-0.0054` n `6`; index avg `0.05` n `25`; metal avg `-0.023` n `20`; unknown avg `0.006` n `793`
- 4h: commodity avg `-0.0772` n `12`; crypto_alt avg `1.1973` n `230`; crypto_major avg `0.3636` n `8`; equity avg `0.4496` n `121`; fx avg `0.0127` n `6`; index avg `0.0864` n `25`; metal avg `0.0709` n `20`; unknown avg `-0.0964` n `793`
- 24h: commodity avg `0.2849` n `12`; crypto_alt avg `6.0982` n `230`; crypto_major avg `7.0317` n `8`; equity avg `-0.3702` n `121`; fx avg `-0.0591` n `6`; index avg `-0.0713` n `25`; metal avg `0.625` n `20`; unknown avg `3.3283` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
