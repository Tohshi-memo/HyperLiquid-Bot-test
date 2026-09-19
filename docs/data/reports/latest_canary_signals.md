# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T00:22:29.858178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `12`; crypto_alt avg `0.1813` n `234`; crypto_major avg `0.2744` n `8`; equity avg `0.0354` n `140`; fx avg `-0.0237` n `6`; index avg `0.0039` n `26`; metal avg `0.0189` n `20`; unknown avg `0.1133` n `942`
- 1h: commodity avg `0.1636` n `12`; crypto_alt avg `0.1931` n `234`; crypto_major avg `-0.0058` n `8`; equity avg `0.0555` n `140`; fx avg `-0.0247` n `6`; index avg `0.0074` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.0814` n `934`
- 4h: commodity avg `0.1814` n `12`; crypto_alt avg `0.5827` n `234`; crypto_major avg `-0.2026` n `8`; equity avg `0.0086` n `140`; fx avg `0.0182` n `6`; index avg `-0.0157` n `26`; metal avg `-0.0383` n `20`; unknown avg `1.2561` n `900`
- 24h: commodity avg `0.1686` n `12`; crypto_alt avg `7.0278` n `234`; crypto_major avg `6.813` n `8`; equity avg `1.4782` n `140`; fx avg `0.1771` n `6`; index avg `0.1277` n `26`; metal avg `0.2903` n `20`; unknown avg `3.9162` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
