# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T19:52:29.244522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `0.0167` n `232`; crypto_major avg `-0.0378` n `8`; equity avg `0.3196` n `129`; fx avg `0.0036` n `6`; index avg `0.0674` n `26`; metal avg `0.0607` n `20`; unknown avg `3.931` n `793`
- 1h: commodity avg `0.0271` n `12`; crypto_alt avg `-0.261` n `232`; crypto_major avg `-0.1389` n `8`; equity avg `0.4748` n `129`; fx avg `-0.0067` n `6`; index avg `0.0987` n `26`; metal avg `0.1339` n `20`; unknown avg `1.4981` n `791`
- 4h: commodity avg `0.0841` n `12`; crypto_alt avg `0.4934` n `232`; crypto_major avg `0.5717` n `8`; equity avg `0.4759` n `129`; fx avg `-0.011` n `6`; index avg `0.0603` n `26`; metal avg `0.1403` n `20`; unknown avg `-0.5185` n `791`
- 24h: commodity avg `0.3372` n `12`; crypto_alt avg `-0.9346` n `231`; crypto_major avg `-0.8414` n `8`; equity avg `-0.028` n `129`; fx avg `-0.0877` n `6`; index avg `-0.1511` n `26`; metal avg `-0.4217` n `20`; unknown avg `0.1111` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
