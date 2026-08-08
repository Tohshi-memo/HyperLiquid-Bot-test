# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T05:52:29.364129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `-0.0714` n `230`; crypto_major avg `-0.093` n `8`; equity avg `0.0526` n `112`; fx avg `0.005` n `6`; index avg `-0.0187` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.1705` n `784`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0189` n `230`; crypto_major avg `-0.0529` n `8`; equity avg `0.0075` n `112`; fx avg `0.0032` n `6`; index avg `-0.0197` n `25`; metal avg `0.0048` n `20`; unknown avg `0.636` n `783`
- 4h: commodity avg `0.0307` n `12`; crypto_alt avg `0.2511` n `230`; crypto_major avg `0.2814` n `8`; equity avg `-0.0944` n `112`; fx avg `-0.0008` n `6`; index avg `-0.0433` n `25`; metal avg `-0.0193` n `20`; unknown avg `1.1267` n `783`
- 24h: commodity avg `-0.2365` n `12`; crypto_alt avg `-0.1949` n `230`; crypto_major avg `0.7369` n `8`; equity avg `1.4583` n `112`; fx avg `-0.0624` n `6`; index avg `0.1377` n `25`; metal avg `0.2067` n `20`; unknown avg `0.0167` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
