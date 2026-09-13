# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T07:22:29.624170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.0484` n `233`; crypto_major avg `0.0223` n `8`; equity avg `-0.0221` n `136`; fx avg `-0.0018` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0031` n `20`; unknown avg `-0.0529` n `838`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `-0.065` n `233`; crypto_major avg `-0.207` n `8`; equity avg `-0.2061` n `136`; fx avg `-0.0045` n `6`; index avg `-0.0289` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.151` n `836`
- 4h: commodity avg `0.1` n `12`; crypto_alt avg `-0.064` n `233`; crypto_major avg `-0.3999` n `8`; equity avg `-0.4581` n `136`; fx avg `-0.0045` n `6`; index avg `-0.0712` n `26`; metal avg `-0.0016` n `20`; unknown avg `51.3898` n `804`
- 24h: commodity avg `0.1825` n `12`; crypto_alt avg `0.4188` n `233`; crypto_major avg `-0.3763` n `8`; equity avg `-0.8441` n `136`; fx avg `-0.0148` n `6`; index avg `-0.1359` n `26`; metal avg `0.0247` n `20`; unknown avg `0.3651` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
