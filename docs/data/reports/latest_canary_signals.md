# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T10:22:29.481182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `13`; crypto_alt avg `0.2467` n `236`; crypto_major avg `0.1659` n `8`; equity avg `0.0639` n `151`; fx avg `0.0027` n `6`; index avg `0.033` n `26`; metal avg `0.0529` n `20`; unknown avg `0.5412` n `1136`
- 1h: commodity avg `0.1286` n `13`; crypto_alt avg `-0.0879` n `236`; crypto_major avg `-0.2274` n `8`; equity avg `-0.2227` n `151`; fx avg `-0.0141` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0208` n `20`; unknown avg `0.8722` n `1134`
- 4h: commodity avg `0.079` n `13`; crypto_alt avg `0.1539` n `236`; crypto_major avg `0.0245` n `8`; equity avg `-0.1379` n `151`; fx avg `0.0061` n `6`; index avg `0.0206` n `26`; metal avg `0.0795` n `20`; unknown avg `0.344` n `1066`
- 24h: commodity avg `0.0242` n `13`; crypto_alt avg `4.4979` n `236`; crypto_major avg `2.2304` n `8`; equity avg `2.3618` n `151`; fx avg `0.0287` n `6`; index avg `0.3156` n `26`; metal avg `0.3041` n `20`; unknown avg `25.6641` n `920`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.098`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0862`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
