# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T01:52:26.610259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `0.2076` n `233`; crypto_major avg `0.1535` n `8`; equity avg `-0.0177` n `136`; fx avg `-0.0005` n `6`; index avg `-0.0009` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.1058` n `838`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.3295` n `233`; crypto_major avg `0.1749` n `8`; equity avg `-0.0348` n `136`; fx avg `-0.002` n `6`; index avg `-0.0035` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.0907` n `836`
- 4h: commodity avg `-0.019` n `12`; crypto_alt avg `0.7373` n `233`; crypto_major avg `0.2197` n `8`; equity avg `-0.0752` n `136`; fx avg `0.0009` n `6`; index avg `-0.0187` n `26`; metal avg `0.0052` n `20`; unknown avg `29.6203` n `804`
- 24h: commodity avg `0.0026` n `12`; crypto_alt avg `1.2325` n `233`; crypto_major avg `0.2992` n `8`; equity avg `-0.4504` n `136`; fx avg `-0.0146` n `6`; index avg `-0.0294` n `26`; metal avg `0.0324` n `20`; unknown avg `0.7914` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
