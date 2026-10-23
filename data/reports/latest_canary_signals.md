# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T02:37:31.727052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `13`; crypto_alt avg `0.475` n `237`; crypto_major avg `0.3517` n `8`; equity avg `0.3713` n `151`; fx avg `0.0382` n `6`; index avg `0.0668` n `26`; metal avg `0.0538` n `20`; unknown avg `0.8923` n `1233`
- 1h: commodity avg `0.0387` n `13`; crypto_alt avg `0.7399` n `237`; crypto_major avg `0.5542` n `8`; equity avg `-0.1488` n `151`; fx avg `0.059` n `6`; index avg `-0.0461` n `26`; metal avg `0.0916` n `20`; unknown avg `0.8818` n `1231`
- 4h: commodity avg `0.1471` n `13`; crypto_alt avg `1.3249` n `237`; crypto_major avg `0.8397` n `8`; equity avg `0.7467` n `151`; fx avg `0.0308` n `6`; index avg `0.0078` n `26`; metal avg `-0.02` n `20`; unknown avg `0.7006` n `1225`
- 24h: commodity avg `0.4589` n `13`; crypto_alt avg `-1.8413` n `237`; crypto_major avg `-1.0168` n `8`; equity avg `-3.2326` n `151`; fx avg `-0.1158` n `6`; index avg `-0.4168` n `26`; metal avg `-0.6811` n `20`; unknown avg `52.5231` n `905`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
