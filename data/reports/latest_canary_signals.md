# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T04:22:32.465641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `12`; crypto_alt avg `-0.2084` n `234`; crypto_major avg `-0.1037` n `8`; equity avg `-0.1838` n `140`; fx avg `-0.0058` n `6`; index avg `-0.0138` n `26`; metal avg `0.0147` n `20`; unknown avg `19.7527` n `944`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.5737` n `234`; crypto_major avg `0.9949` n `8`; equity avg `-0.3616` n `140`; fx avg `-0.0032` n `6`; index avg `-0.0424` n `26`; metal avg `-0.0282` n `20`; unknown avg `21.9745` n `936`
- 4h: commodity avg `0.1527` n `12`; crypto_alt avg `-0.2026` n `234`; crypto_major avg `-0.4853` n `8`; equity avg `-0.5507` n `140`; fx avg `-0.0597` n `6`; index avg `-0.0858` n `26`; metal avg `-0.2052` n `20`; unknown avg `22.3986` n `936`
- 24h: commodity avg `-0.1084` n `12`; crypto_alt avg `3.2249` n `234`; crypto_major avg `5.1429` n `8`; equity avg `1.9677` n `140`; fx avg `-0.2271` n `6`; index avg `0.418` n `26`; metal avg `-0.1071` n `20`; unknown avg `7.6537` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
