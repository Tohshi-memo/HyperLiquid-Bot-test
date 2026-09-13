# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T13:07:29.168467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `-0.1224` n `233`; crypto_major avg `0.0162` n `8`; equity avg `-0.0212` n `136`; fx avg `-0.0041` n `6`; index avg `-0.0011` n `27`; metal avg `0.0016` n `20`; unknown avg `-0.0604` n `836`
- 1h: commodity avg `0.025` n `12`; crypto_alt avg `0.1374` n `233`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0974` n `136`; fx avg `-0.0013` n `6`; index avg `-0.0181` n `27`; metal avg `-0.0008` n `20`; unknown avg `-0.1354` n `830`
- 4h: commodity avg `0.1996` n `12`; crypto_alt avg `-0.4265` n `233`; crypto_major avg `-0.7986` n `8`; equity avg `-0.7897` n `136`; fx avg `0.0064` n `6`; index avg `-0.1427` n `27`; metal avg `-0.0483` n `20`; unknown avg `0.3321` n `826`
- 24h: commodity avg `0.2998` n `12`; crypto_alt avg `-0.627` n `233`; crypto_major avg `-2.0458` n `8`; equity avg `-1.9293` n `136`; fx avg `-0.0069` n `6`; index avg `-0.3122` n `26`; metal avg `-0.081` n `20`; unknown avg `-0.1025` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
