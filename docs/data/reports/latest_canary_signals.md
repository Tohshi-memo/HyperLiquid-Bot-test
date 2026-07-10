# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T20:52:30.034808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0478` n `229`; crypto_major avg `-0.0315` n `8`; equity avg `0.0204` n `92`; fx avg `0.001` n `6`; index avg `0.0027` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0595` n `765`
- 1h: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.139` n `229`; crypto_major avg `-0.1528` n `8`; equity avg `-0.0269` n `92`; fx avg `-0.0184` n `6`; index avg `0.0187` n `25`; metal avg `0.0565` n `20`; unknown avg `-0.21` n `765`
- 4h: commodity avg `0.116` n `12`; crypto_alt avg `-0.2465` n `229`; crypto_major avg `-0.2563` n `8`; equity avg `-0.2642` n `92`; fx avg `-0.0463` n `6`; index avg `0.0173` n `25`; metal avg `0.0435` n `20`; unknown avg `-0.2761` n `765`
- 24h: commodity avg `-0.2426` n `12`; crypto_alt avg `0.5164` n `229`; crypto_major avg `0.7361` n `8`; equity avg `-0.6527` n `92`; fx avg `-0.1655` n `6`; index avg `0.0601` n `25`; metal avg `0.1417` n `20`; unknown avg `-0.1721` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
