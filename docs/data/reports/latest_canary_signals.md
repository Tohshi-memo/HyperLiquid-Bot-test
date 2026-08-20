# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T07:52:23.874288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.1999` n `230`; crypto_major avg `0.1247` n `8`; equity avg `-0.038` n `121`; fx avg `-0.0049` n `6`; index avg `-0.0056` n `25`; metal avg `0.0222` n `20`; unknown avg `-0.0176` n `792`
- 1h: commodity avg `0.0995` n `12`; crypto_alt avg `0.0881` n `230`; crypto_major avg `-0.0322` n `8`; equity avg `-0.3173` n `121`; fx avg `0.0338` n `6`; index avg `-0.0461` n `25`; metal avg `-0.053` n `20`; unknown avg `0.0462` n `792`
- 4h: commodity avg `0.1393` n `12`; crypto_alt avg `0.7544` n `230`; crypto_major avg `1.0342` n `8`; equity avg `-0.1022` n `121`; fx avg `0.0297` n `6`; index avg `-0.0118` n `25`; metal avg `-0.126` n `20`; unknown avg `0.3116` n `776`
- 24h: commodity avg `0.1066` n `12`; crypto_alt avg `5.8642` n `230`; crypto_major avg `10.4932` n `8`; equity avg `0.3023` n `120`; fx avg `0.0973` n `6`; index avg `0.1542` n `25`; metal avg `0.9551` n `20`; unknown avg `1.9701` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
