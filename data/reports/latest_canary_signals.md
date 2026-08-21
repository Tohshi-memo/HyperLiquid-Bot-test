# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T16:07:31.813337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.2184` n `230`; crypto_major avg `-0.4577` n `8`; equity avg `-0.2849` n `121`; fx avg `0.0154` n `6`; index avg `-0.0432` n `25`; metal avg `0.0038` n `20`; unknown avg `0.065` n `793`
- 1h: commodity avg `0.1001` n `12`; crypto_alt avg `-0.5064` n `230`; crypto_major avg `-0.7336` n `8`; equity avg `0.1676` n `121`; fx avg `0.0281` n `6`; index avg `0.0505` n `25`; metal avg `0.0823` n `20`; unknown avg `0.0532` n `793`
- 4h: commodity avg `0.0421` n `12`; crypto_alt avg `1.1232` n `230`; crypto_major avg `0.8437` n `8`; equity avg `-0.4536` n `121`; fx avg `-0.0072` n `6`; index avg `-0.035` n `25`; metal avg `-0.06` n `20`; unknown avg `0.1156` n `793`
- 24h: commodity avg `0.2137` n `12`; crypto_alt avg `7.2367` n `230`; crypto_major avg `4.5689` n `8`; equity avg `1.3247` n `121`; fx avg `-0.0797` n `6`; index avg `0.1325` n `25`; metal avg `0.5471` n `20`; unknown avg `2.3216` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2389`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
