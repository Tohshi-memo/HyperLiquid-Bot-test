# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T13:37:26.814005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `0.1194` n `233`; crypto_major avg `0.0452` n `8`; equity avg `-0.0179` n `136`; fx avg `0.0015` n `6`; index avg `0.0024` n `27`; metal avg `-0.0108` n `20`; unknown avg `0.2008` n `838`
- 1h: commodity avg `0.0269` n `12`; crypto_alt avg `-0.1643` n `233`; crypto_major avg `-0.0924` n `8`; equity avg `-0.0746` n `136`; fx avg `0.0004` n `6`; index avg `0.0096` n `27`; metal avg `-0.0091` n `20`; unknown avg `0.4218` n `836`
- 4h: commodity avg `0.1997` n `12`; crypto_alt avg `-0.0167` n `233`; crypto_major avg `-0.2486` n `8`; equity avg `-0.3397` n `136`; fx avg `0.0018` n `6`; index avg `-0.0433` n `27`; metal avg `-0.0339` n `20`; unknown avg `0.2154` n `826`
- 24h: commodity avg `0.3077` n `12`; crypto_alt avg `-0.5155` n `233`; crypto_major avg `-2.0602` n `8`; equity avg `-1.9463` n `136`; fx avg `0.0016` n `6`; index avg `-0.3042` n `26`; metal avg `-0.0878` n `20`; unknown avg `0.0635` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
