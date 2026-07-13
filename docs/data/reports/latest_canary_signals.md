# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T11:07:29.336494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0591` n `12`; crypto_alt avg `0.0798` n `230`; crypto_major avg `0.2196` n `8`; equity avg `0.1697` n `92`; fx avg `0.0133` n `6`; index avg `0.0571` n `25`; metal avg `0.0615` n `20`; unknown avg `0.0334` n `766`
- 1h: commodity avg `0.0739` n `12`; crypto_alt avg `0.1367` n `230`; crypto_major avg `0.1184` n `8`; equity avg `0.1457` n `92`; fx avg `0.029` n `6`; index avg `0.0121` n `25`; metal avg `-0.0253` n `20`; unknown avg `0.0056` n `766`
- 4h: commodity avg `-0.1253` n `12`; crypto_alt avg `0.3744` n `230`; crypto_major avg `0.2331` n `8`; equity avg `0.6328` n `92`; fx avg `-0.0609` n `6`; index avg `0.1207` n `25`; metal avg `0.1837` n `20`; unknown avg `-0.0758` n `766`
- 24h: commodity avg `-0.1979` n `12`; crypto_alt avg `-0.8042` n `230`; crypto_major avg `-0.9604` n `8`; equity avg `-1.8004` n `92`; fx avg `-0.0435` n `6`; index avg `-0.3889` n `25`; metal avg `-0.198` n `20`; unknown avg `-0.0366` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
