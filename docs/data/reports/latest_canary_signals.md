# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T02:37:30.323412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `12`; crypto_alt avg `-0.0192` n `233`; crypto_major avg `0.0283` n `8`; equity avg `0.003` n `136`; fx avg `0.0035` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.0517` n `838`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `-0.0414` n `233`; crypto_major avg `0.0611` n `8`; equity avg `-0.0477` n `136`; fx avg `0.0057` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.1703` n `812`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `0.5487` n `233`; crypto_major avg `0.1659` n `8`; equity avg `-0.0592` n `136`; fx avg `0.0043` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0019` n `20`; unknown avg `3.5811` n `806`
- 24h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.8342` n `233`; crypto_major avg `0.1932` n `8`; equity avg `-0.4529` n `136`; fx avg `-0.0062` n `6`; index avg `-0.0361` n `26`; metal avg `0.0282` n `20`; unknown avg `0.0395` n `706`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
