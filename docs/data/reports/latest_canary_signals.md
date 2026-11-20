# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T03:22:28.659212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `13`; crypto_alt avg `0.2944` n `239`; crypto_major avg `0.3109` n `8`; equity avg `0.3139` n `165`; fx avg `0.0087` n `6`; index avg `0.0432` n `27`; metal avg `0.0241` n `20`; unknown avg `0.0156` n `1260`
- 1h: commodity avg `-0.0065` n `13`; crypto_alt avg `0.4911` n `239`; crypto_major avg `0.774` n `8`; equity avg `0.0948` n `165`; fx avg `0.0332` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0328` n `20`; unknown avg `215.9907` n `1258`
- 4h: commodity avg `-0.1102` n `13`; crypto_alt avg `-1.2014` n `239`; crypto_major avg `-0.5454` n `8`; equity avg `-1.0635` n `165`; fx avg `0.0242` n `6`; index avg `-0.1092` n `27`; metal avg `-0.7818` n `20`; unknown avg `0.0807` n `1252`
- 24h: commodity avg `-0.0271` n `13`; crypto_alt avg `-2.0699` n `239`; crypto_major avg `-0.824` n `8`; equity avg `-4.9473` n `165`; fx avg `0.0515` n `6`; index avg `-0.3422` n `27`; metal avg `-1.4823` n `20`; unknown avg `17.458` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
