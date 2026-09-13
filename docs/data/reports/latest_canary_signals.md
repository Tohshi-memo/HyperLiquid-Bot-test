# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T03:22:31.611558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.0146` n `233`; crypto_major avg `0.002` n `8`; equity avg `-0.0131` n `136`; fx avg `-0.0028` n `6`; index avg `-0.0009` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.1082` n `838`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `0.1025` n `233`; crypto_major avg `0.0223` n `8`; equity avg `-0.0399` n `136`; fx avg `-0.0012` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0032` n `20`; unknown avg `-0.2054` n `836`
- 4h: commodity avg `-0.0185` n `12`; crypto_alt avg `0.5026` n `233`; crypto_major avg `0.0426` n `8`; equity avg `-0.1091` n `136`; fx avg `0.0023` n `6`; index avg `-0.0347` n `26`; metal avg `0.0071` n `20`; unknown avg `3.5919` n `806`
- 24h: commodity avg `-0.0125` n `12`; crypto_alt avg `1.0269` n `233`; crypto_major avg `0.2489` n `8`; equity avg `-0.4793` n `136`; fx avg `-0.0114` n `6`; index avg `-0.057` n `26`; metal avg `0.0316` n `20`; unknown avg `-0.2756` n `706`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
