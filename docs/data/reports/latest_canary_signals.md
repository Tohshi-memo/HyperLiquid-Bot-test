# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T06:52:27.507828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0349` n `234`; crypto_major avg `-0.1044` n `8`; equity avg `-0.0194` n `140`; fx avg `-0.0027` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0074` n `20`; unknown avg `-0.0623` n `942`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.0582` n `234`; crypto_major avg `-0.1996` n `8`; equity avg `-0.0395` n `140`; fx avg `-0.0189` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.0551` n `904`
- 4h: commodity avg `-0.0374` n `12`; crypto_alt avg `-1.0772` n `234`; crypto_major avg `-0.4862` n `8`; equity avg `-0.1355` n `140`; fx avg `-0.0111` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.047` n `894`
- 24h: commodity avg `0.2957` n `12`; crypto_alt avg `3.2555` n `234`; crypto_major avg `4.3344` n `8`; equity avg `0.106` n `140`; fx avg `0.065` n `6`; index avg `-0.0956` n `26`; metal avg `-0.1511` n `20`; unknown avg `2.2871` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
