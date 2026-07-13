# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T05:37:31.111320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `0.0383` n `230`; crypto_major avg `0.0762` n `8`; equity avg `0.1374` n `92`; fx avg `0.0017` n `6`; index avg `0.0271` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0832` n `766`
- 1h: commodity avg `0.0648` n `12`; crypto_alt avg `0.4231` n `230`; crypto_major avg `0.2048` n `8`; equity avg `0.1252` n `92`; fx avg `-0.0155` n `6`; index avg `0.0235` n `25`; metal avg `0.0904` n `20`; unknown avg `0.135` n `766`
- 4h: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.7622` n `230`; crypto_major avg `-1.1391` n `8`; equity avg `-1.0952` n `92`; fx avg `0.0192` n `6`; index avg `-0.2537` n `25`; metal avg `-0.2052` n `20`; unknown avg `1.8515` n `766`
- 24h: commodity avg `0.177` n `12`; crypto_alt avg `-1.6075` n `230`; crypto_major avg `-1.0683` n `8`; equity avg `-2.3635` n `92`; fx avg `0.0231` n `6`; index avg `-0.5159` n `25`; metal avg `-0.4096` n `20`; unknown avg `-0.0468` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
