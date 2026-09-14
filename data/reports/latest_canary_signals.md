# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T09:07:29.233861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0551` n `233`; crypto_major avg `0.0208` n `8`; equity avg `-0.0777` n `136`; fx avg `-0.0074` n `6`; index avg `-0.0163` n `27`; metal avg `0.0033` n `20`; unknown avg `1.4277` n `892`
- 1h: commodity avg `0.0708` n `12`; crypto_alt avg `-0.1908` n `233`; crypto_major avg `-0.1471` n `8`; equity avg `-0.12` n `136`; fx avg `-0.0132` n `6`; index avg `-0.0504` n `27`; metal avg `-0.0763` n `20`; unknown avg `8.364` n `886`
- 4h: commodity avg `0.1707` n `12`; crypto_alt avg `-0.2727` n `233`; crypto_major avg `0.1247` n `8`; equity avg `-0.7691` n `136`; fx avg `-0.0029` n `6`; index avg `-0.1122` n `27`; metal avg `-0.2686` n `20`; unknown avg `0.1097` n `832`
- 24h: commodity avg `0.7304` n `12`; crypto_alt avg `-0.2351` n `233`; crypto_major avg `0.8247` n `8`; equity avg `-1.5188` n `136`; fx avg `0.0301` n `6`; index avg `-0.3406` n `27`; metal avg `-0.3717` n `20`; unknown avg `0.8797` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
