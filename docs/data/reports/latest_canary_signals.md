# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T06:22:25.463260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `13`; crypto_alt avg `0.2276` n `235`; crypto_major avg `0.1359` n `8`; equity avg `0.019` n `151`; fx avg `0.0083` n `6`; index avg `0.0248` n `26`; metal avg `-0.0527` n `20`; unknown avg `0.0294` n `1135`
- 1h: commodity avg `0.0551` n `13`; crypto_alt avg `-0.0558` n `235`; crypto_major avg `0.0508` n `8`; equity avg `-0.3342` n `151`; fx avg `0.0075` n `6`; index avg `-0.0336` n `26`; metal avg `-0.062` n `20`; unknown avg `0.8095` n `1117`
- 4h: commodity avg `-0.0847` n `13`; crypto_alt avg `1.8632` n `235`; crypto_major avg `1.3164` n `8`; equity avg `0.317` n `151`; fx avg `0.0824` n `6`; index avg `0.0556` n `26`; metal avg `0.1405` n `20`; unknown avg `1.4435` n `1075`
- 24h: commodity avg `0.3963` n `13`; crypto_alt avg `-3.5604` n `235`; crypto_major avg `-1.9416` n `8`; equity avg `-3.5006` n `151`; fx avg `0.0441` n `6`; index avg `-0.4773` n `26`; metal avg `-0.0513` n `20`; unknown avg `0.4035` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1967`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1813`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1432`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
