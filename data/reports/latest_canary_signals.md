# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T21:37:27.009621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `0.0712` n `230`; crypto_major avg `0.0641` n `8`; equity avg `0.1233` n `102`; fx avg `-0.0067` n `6`; index avg `0.0282` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.019` n `783`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `0.2106` n `230`; crypto_major avg `0.2869` n `8`; equity avg `0.1198` n `102`; fx avg `0.063` n `6`; index avg `0.0427` n `25`; metal avg `0.0326` n `20`; unknown avg `0.0341` n `783`
- 4h: commodity avg `0.096` n `12`; crypto_alt avg `0.2411` n `230`; crypto_major avg `0.4889` n `8`; equity avg `0.3708` n `102`; fx avg `0.1542` n `6`; index avg `0.0629` n `25`; metal avg `0.1212` n `20`; unknown avg `0.0849` n `782`
- 24h: commodity avg `-1.1286` n `12`; crypto_alt avg `1.2985` n `230`; crypto_major avg `1.8866` n `8`; equity avg `1.7295` n `102`; fx avg `-0.0134` n `6`; index avg `0.3586` n `25`; metal avg `0.3496` n `20`; unknown avg `1.581` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
