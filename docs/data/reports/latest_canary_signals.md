# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T14:47:30.909077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `13`; crypto_alt avg `0.2357` n `236`; crypto_major avg `0.0138` n `8`; equity avg `0.1028` n `151`; fx avg `-0.0025` n `6`; index avg `0.0319` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.0123` n `1088`
- 1h: commodity avg `-0.1266` n `13`; crypto_alt avg `0.5268` n `236`; crypto_major avg `0.5891` n `8`; equity avg `0.4682` n `151`; fx avg `0.0232` n `6`; index avg `0.0718` n `26`; metal avg `-0.0067` n `20`; unknown avg `2.7884` n `1020`
- 4h: commodity avg `-0.3854` n `13`; crypto_alt avg `0.0496` n `236`; crypto_major avg `-0.1302` n `8`; equity avg `-1.199` n `151`; fx avg `0.0242` n `6`; index avg `-0.0991` n `26`; metal avg `0.0145` n `20`; unknown avg `1.8211` n `1012`
- 24h: commodity avg `-0.4288` n `13`; crypto_alt avg `2.7716` n `236`; crypto_major avg `1.4594` n `8`; equity avg `0.6728` n `151`; fx avg `0.0586` n `6`; index avg `0.0607` n `26`; metal avg `0.196` n `20`; unknown avg `0.0012` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0986`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0823`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
