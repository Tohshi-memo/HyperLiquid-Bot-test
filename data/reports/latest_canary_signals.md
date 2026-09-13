# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T02:07:27.352111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.1176` n `233`; crypto_major avg `-0.0991` n `8`; equity avg `-0.0208` n `136`; fx avg `-0.0029` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.1204` n `836`
- 1h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.1352` n `233`; crypto_major avg `0.0013` n `8`; equity avg `-0.0696` n `136`; fx avg `-0.0043` n `6`; index avg `-0.0074` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.2115` n `836`
- 4h: commodity avg `-0.0449` n `12`; crypto_alt avg `0.5497` n `233`; crypto_major avg `0.0972` n `8`; equity avg `-0.0888` n `136`; fx avg `-0.0053` n `6`; index avg `-0.0216` n `26`; metal avg `0.0041` n `20`; unknown avg `29.3257` n `822`
- 24h: commodity avg `-0.0022` n `12`; crypto_alt avg `1.0897` n `233`; crypto_major avg `0.1724` n `8`; equity avg `-0.4533` n `136`; fx avg `-0.0159` n `6`; index avg `-0.0326` n `26`; metal avg `0.0293` n `20`; unknown avg `0.9093` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
