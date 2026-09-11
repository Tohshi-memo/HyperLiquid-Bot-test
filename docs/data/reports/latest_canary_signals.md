# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T21:52:30.226473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.5222` n `233`; crypto_major avg `-0.3088` n `8`; equity avg `-0.0118` n `136`; fx avg `0.0023` n `6`; index avg `0.0024` n `26`; metal avg `0.0146` n `20`; unknown avg `0.4866` n `822`
- 1h: commodity avg `-0.0383` n `12`; crypto_alt avg `-0.4609` n `233`; crypto_major avg `-0.156` n `8`; equity avg `0.0018` n `136`; fx avg `-0.0008` n `6`; index avg `0.006` n `26`; metal avg `0.027` n `20`; unknown avg `0.1974` n `820`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `-1.0952` n `233`; crypto_major avg `-0.7534` n `8`; equity avg `-0.445` n `136`; fx avg `-0.0076` n `6`; index avg `-0.0562` n `26`; metal avg `-0.0367` n `20`; unknown avg `0.0325` n `770`
- 24h: commodity avg `-1.0207` n `12`; crypto_alt avg `-0.2608` n `233`; crypto_major avg `0.8183` n `8`; equity avg `0.7612` n `136`; fx avg `-0.1763` n `6`; index avg `0.3099` n `26`; metal avg `0.2848` n `20`; unknown avg `1.1282` n `668`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
