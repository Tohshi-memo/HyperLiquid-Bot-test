# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T03:37:31.197388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.94` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0182` n `233`; crypto_major avg `0.0817` n `8`; equity avg `-0.0077` n `136`; fx avg `-0.0042` n `6`; index avg `0.0027` n `26`; metal avg `-0.0007` n `20`; unknown avg `18.7869` n `838`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.0514` n `233`; crypto_major avg `0.0215` n `8`; equity avg `-0.024` n `136`; fx avg `-0.0037` n `6`; index avg `0.006` n `26`; metal avg `-0.0065` n `20`; unknown avg `-0.0755` n `836`
- 4h: commodity avg `-0.0788` n `12`; crypto_alt avg `0.939` n `233`; crypto_major avg `0.1522` n `8`; equity avg `0.0774` n `136`; fx avg `-0.001` n `6`; index avg `0.022` n `26`; metal avg `-0.018` n `20`; unknown avg `0.0925` n `826`
- 24h: commodity avg `-0.6967` n `12`; crypto_alt avg `1.5405` n `233`; crypto_major avg `1.4474` n `8`; equity avg `1.2262` n `136`; fx avg `-0.1385` n `6`; index avg `0.3548` n `26`; metal avg `0.2947` n `20`; unknown avg `24.0186` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
