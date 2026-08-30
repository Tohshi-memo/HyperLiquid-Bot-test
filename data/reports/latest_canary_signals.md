# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T15:07:28.189176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.1019` n `231`; crypto_major avg `-0.0417` n `8`; equity avg `0.0055` n `128`; fx avg `0.0001` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0074` n `20`; unknown avg `-0.0415` n `793`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.1739` n `231`; crypto_major avg `-0.1645` n `8`; equity avg `-0.0038` n `128`; fx avg `0.002` n `6`; index avg `0.003` n `26`; metal avg `0.0106` n `20`; unknown avg `0.0549` n `793`
- 4h: commodity avg `-0.0084` n `12`; crypto_alt avg `0.5016` n `231`; crypto_major avg `0.5708` n `8`; equity avg `0.0164` n `128`; fx avg `0.0016` n `6`; index avg `0.0235` n `26`; metal avg `0.0575` n `20`; unknown avg `0.0123` n `791`
- 24h: commodity avg `-0.0285` n `12`; crypto_alt avg `1.0345` n `231`; crypto_major avg `0.7991` n `8`; equity avg `0.2968` n `128`; fx avg `0.0112` n `6`; index avg `0.0769` n `26`; metal avg `0.1063` n `20`; unknown avg `-0.3252` n `738`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
