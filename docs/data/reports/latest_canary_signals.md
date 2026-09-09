# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T15:07:29.677812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.5546` n `233`; crypto_major avg `-0.4981` n `8`; equity avg `-0.1241` n `134`; fx avg `0.0127` n `6`; index avg `-0.0604` n `26`; metal avg `-0.2251` n `20`; unknown avg `11.6193` n `795`
- 1h: commodity avg `0.1637` n `12`; crypto_alt avg `-0.6664` n `233`; crypto_major avg `-0.5867` n `8`; equity avg `-0.3773` n `134`; fx avg `0.0316` n `6`; index avg `-0.1343` n `26`; metal avg `-0.1697` n `20`; unknown avg `11.9241` n `795`
- 4h: commodity avg `0.0686` n `12`; crypto_alt avg `-0.2418` n `233`; crypto_major avg `-0.3433` n `8`; equity avg `0.3753` n `134`; fx avg `0.0389` n `6`; index avg `0.0069` n `26`; metal avg `0.2475` n `20`; unknown avg `12.8859` n `766`
- 24h: commodity avg `0.4398` n `12`; crypto_alt avg `-0.9413` n `232`; crypto_major avg `0.0623` n `8`; equity avg `-0.1415` n `134`; fx avg `-0.1057` n `6`; index avg `-0.1746` n `26`; metal avg `0.2052` n `20`; unknown avg `11.3505` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
