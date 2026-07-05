# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T16:37:30.268388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0438` n `229`; crypto_major avg `-0.0225` n `8`; equity avg `0.0188` n `88`; fx avg `0.0315` n `6`; index avg `0.0055` n `25`; metal avg `0.003` n `20`; unknown avg `0.013` n `765`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `-0.1634` n `229`; crypto_major avg `-0.1883` n `8`; equity avg `-0.0082` n `88`; fx avg `0.015` n `6`; index avg `0.0141` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0146` n `713`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0375` n `229`; crypto_major avg `0.158` n `8`; equity avg `-0.0294` n `88`; fx avg `-0.0533` n `6`; index avg `0.0342` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0898` n `695`
- 24h: commodity avg `-0.0152` n `12`; crypto_alt avg `-1.7655` n `229`; crypto_major avg `-0.9817` n `8`; equity avg `0.2504` n `88`; fx avg `-0.0746` n `6`; index avg `0.078` n `25`; metal avg `0.0613` n `20`; unknown avg `-0.131` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
