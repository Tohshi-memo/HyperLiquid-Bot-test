# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T21:21:55.661196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.1567` n `233`; crypto_major avg `0.1193` n `8`; equity avg `-0.0153` n `136`; fx avg `0.0041` n `6`; index avg `0.0133` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.0847` n `824`
- 1h: commodity avg `-0.0984` n `12`; crypto_alt avg `0.0996` n `233`; crypto_major avg `0.0665` n `8`; equity avg `0.0072` n `136`; fx avg `-0.0012` n `6`; index avg `0.0023` n `26`; metal avg `0.0059` n `20`; unknown avg `0.1041` n `802`
- 4h: commodity avg `0.0336` n `12`; crypto_alt avg `-0.5848` n `233`; crypto_major avg `-0.4595` n `8`; equity avg `-0.3546` n `136`; fx avg `0.0051` n `6`; index avg `-0.0485` n `26`; metal avg `-0.073` n `20`; unknown avg `-0.1586` n `740`
- 24h: commodity avg `-0.7363` n `12`; crypto_alt avg `0.5014` n `233`; crypto_major avg `1.2856` n `8`; equity avg `0.6821` n `136`; fx avg `-0.1546` n `6`; index avg `0.3002` n `26`; metal avg `0.2473` n `20`; unknown avg `1.2011` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
