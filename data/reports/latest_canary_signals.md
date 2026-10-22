# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T22:22:28.294280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.2793` n `237`; crypto_major avg `-0.1975` n `8`; equity avg `-0.0086` n `151`; fx avg `-0.0123` n `6`; index avg `0.0064` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.2101` n `1233`
- 1h: commodity avg `0.0362` n `13`; crypto_alt avg `-0.3292` n `237`; crypto_major avg `-0.3476` n `8`; equity avg `-0.1087` n `151`; fx avg `-0.0151` n `6`; index avg `0.0283` n `26`; metal avg `0.009` n `20`; unknown avg `-0.0971` n `1231`
- 4h: commodity avg `0.0524` n `13`; crypto_alt avg `-0.0511` n `237`; crypto_major avg `0.128` n `8`; equity avg `-0.2343` n `151`; fx avg `-0.0607` n `6`; index avg `-0.0427` n `26`; metal avg `-0.0931` n `20`; unknown avg `-0.3622` n `1167`
- 24h: commodity avg `0.553` n `13`; crypto_alt avg `-5.3894` n `237`; crypto_major avg `-3.9785` n `8`; equity avg `-5.8146` n `151`; fx avg `-0.2025` n `6`; index avg `-0.678` n `26`; metal avg `-0.9647` n `20`; unknown avg `60.0223` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
