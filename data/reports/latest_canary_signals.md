# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T17:52:32.778346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8761` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1283` n `13`; crypto_alt avg `0.0772` n `237`; crypto_major avg `0.0284` n `8`; equity avg `-0.1227` n `151`; fx avg `0.0057` n `6`; index avg `-0.04` n `26`; metal avg `0.0028` n `20`; unknown avg `24.5996` n `1233`
- 1h: commodity avg `0.2725` n `13`; crypto_alt avg `0.754` n `237`; crypto_major avg `0.4652` n `8`; equity avg `-0.0006` n `151`; fx avg `0.0159` n `6`; index avg `0.0322` n `26`; metal avg `0.0713` n `20`; unknown avg `1.1154` n `1231`
- 4h: commodity avg `0.242` n `13`; crypto_alt avg `-0.6617` n `237`; crypto_major avg `-0.5921` n `8`; equity avg `-2.4682` n `151`; fx avg `0.0662` n `6`; index avg `-0.2142` n `26`; metal avg `-0.1289` n `20`; unknown avg `2.3725` n `1083`
- 24h: commodity avg `0.7124` n `13`; crypto_alt avg `-4.9847` n `237`; crypto_major avg `-4.004` n `8`; equity avg `-5.2273` n `151`; fx avg `-0.1261` n `6`; index avg `-0.6414` n `26`; metal avg `-0.9391` n `20`; unknown avg `5.6942` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
