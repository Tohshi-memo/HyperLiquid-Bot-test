# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T17:37:29.466945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0682` n `12`; crypto_alt avg `0.1608` n `232`; crypto_major avg `0.0956` n `8`; equity avg `0.0589` n `131`; fx avg `-0.0011` n `6`; index avg `0.012` n `26`; metal avg `0.0082` n `20`; unknown avg `-0.11` n `793`
- 1h: commodity avg `0.0576` n `12`; crypto_alt avg `0.4182` n `232`; crypto_major avg `0.3345` n `8`; equity avg `0.0416` n `131`; fx avg `0.0044` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0361` n `20`; unknown avg `0.6353` n `791`
- 4h: commodity avg `0.4434` n `12`; crypto_alt avg `0.1172` n `232`; crypto_major avg `-0.0776` n `8`; equity avg `-0.1216` n `131`; fx avg `-0.0137` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0591` n `20`; unknown avg `-0.9471` n `790`
- 24h: commodity avg `0.7284` n `12`; crypto_alt avg `0.4903` n `232`; crypto_major avg `-1.0281` n `8`; equity avg `-1.3768` n `130`; fx avg `0.046` n `6`; index avg `-0.2176` n `26`; metal avg `-0.6048` n `20`; unknown avg `-0.1857` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0379`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0368`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0348`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0341`, n `668`, weak_sample_signal
