# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T07:52:25.542887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1343` n `12`; crypto_alt avg `0.0221` n `232`; crypto_major avg `-0.0069` n `8`; equity avg `0.0829` n `133`; fx avg `0.0` n `6`; index avg `0.0129` n `26`; metal avg `0.0675` n `20`; unknown avg `0.145` n `793`
- 1h: commodity avg `-0.1188` n `12`; crypto_alt avg `0.2514` n `232`; crypto_major avg `0.0418` n `8`; equity avg `0.2445` n `133`; fx avg `0.0374` n `6`; index avg `0.0305` n `26`; metal avg `0.1953` n `20`; unknown avg `0.0988` n `791`
- 4h: commodity avg `-0.2021` n `12`; crypto_alt avg `-0.3612` n `232`; crypto_major avg `-0.3826` n `8`; equity avg `0.1882` n `133`; fx avg `-0.0252` n `6`; index avg `0.0508` n `26`; metal avg `0.1329` n `20`; unknown avg `0.6801` n `755`
- 24h: commodity avg `-0.1788` n `12`; crypto_alt avg `2.0468` n `232`; crypto_major avg `3.848` n `8`; equity avg `1.8165` n `133`; fx avg `-0.0741` n `6`; index avg `0.3591` n `26`; metal avg `0.5544` n `20`; unknown avg `1.7747` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
