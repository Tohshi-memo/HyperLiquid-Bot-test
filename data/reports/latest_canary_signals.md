# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T14:37:28.734399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.1389` n `233`; crypto_major avg `0.0813` n `8`; equity avg `0.0127` n `136`; fx avg `0.0029` n `6`; index avg `-0.0035` n `27`; metal avg `0.0078` n `20`; unknown avg `1.2682` n `838`
- 1h: commodity avg `-0.15` n `12`; crypto_alt avg `0.6868` n `233`; crypto_major avg `0.7338` n `8`; equity avg `0.3862` n `136`; fx avg `0.0084` n `6`; index avg `0.0579` n `27`; metal avg `0.0315` n `20`; unknown avg `2.9255` n `836`
- 4h: commodity avg `0.0529` n `12`; crypto_alt avg `0.6413` n `233`; crypto_major avg `0.5178` n `8`; equity avg `0.1232` n `136`; fx avg `0.009` n `6`; index avg `0.0282` n `27`; metal avg `0.0063` n `20`; unknown avg `2.7555` n `826`
- 24h: commodity avg `0.1864` n `12`; crypto_alt avg `-0.01` n `233`; crypto_major avg `-1.4637` n `8`; equity avg `-1.5808` n `136`; fx avg `0.0081` n `6`; index avg `-0.2491` n `26`; metal avg `-0.0658` n `20`; unknown avg `2.9371` n `708`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
