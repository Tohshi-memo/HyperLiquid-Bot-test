# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T00:22:27.439128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.0878` n `233`; crypto_major avg `-0.0419` n `8`; equity avg `-0.0092` n `136`; fx avg `0.0012` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0007` n `20`; unknown avg `12.2278` n `838`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.2419` n `233`; crypto_major avg `-0.0183` n `8`; equity avg `0.0021` n `136`; fx avg `0.0016` n `6`; index avg `-0.0087` n `26`; metal avg `0.0068` n `20`; unknown avg `11.0518` n `836`
- 4h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.1667` n `233`; crypto_major avg `-0.018` n `8`; equity avg `-0.0631` n `136`; fx avg `-0.0039` n `6`; index avg `-0.0152` n `26`; metal avg `-0.0182` n `20`; unknown avg `2.4261` n `796`
- 24h: commodity avg `-0.0742` n `12`; crypto_alt avg `1.2768` n `233`; crypto_major avg `0.1854` n `8`; equity avg `-0.3694` n `136`; fx avg `-0.0002` n `6`; index avg `-0.0316` n `26`; metal avg `0.002` n `20`; unknown avg `0.7297` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
