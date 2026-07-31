# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T04:52:31.100381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.1197` n `230`; crypto_major avg `0.0181` n `8`; equity avg `0.1321` n `102`; fx avg `-0.0147` n `6`; index avg `0.0279` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.121` n `779`
- 1h: commodity avg `-0.1024` n `12`; crypto_alt avg `-0.2226` n `230`; crypto_major avg `-0.1584` n `8`; equity avg `0.5601` n `102`; fx avg `0.0344` n `6`; index avg `0.1083` n `25`; metal avg `0.0564` n `20`; unknown avg `0.0551` n `779`
- 4h: commodity avg `-0.1826` n `12`; crypto_alt avg `-0.6688` n `230`; crypto_major avg `-0.5334` n `8`; equity avg `-0.091` n `102`; fx avg `0.058` n `6`; index avg `-0.0424` n `25`; metal avg `-0.1012` n `20`; unknown avg `0.1492` n `779`
- 24h: commodity avg `-0.2956` n `12`; crypto_alt avg `-0.0792` n `230`; crypto_major avg `0.7964` n `8`; equity avg `9.0936` n `102`; fx avg `-0.0846` n `6`; index avg `1.2059` n `25`; metal avg `0.6303` n `20`; unknown avg `0.0531` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
