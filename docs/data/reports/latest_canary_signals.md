# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T06:22:33.166694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.2593` n `234`; crypto_major avg `-0.2004` n `8`; equity avg `-0.0053` n `140`; fx avg `0.0155` n `6`; index avg `0.0134` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.1742` n `942`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.8813` n `234`; crypto_major avg `-0.325` n `8`; equity avg `-0.0637` n `140`; fx avg `0.0218` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.0189` n `904`
- 4h: commodity avg `-0.04` n `12`; crypto_alt avg `-1.3284` n `234`; crypto_major avg `-0.6477` n `8`; equity avg `-0.1523` n `140`; fx avg `0.0087` n `6`; index avg `-0.022` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.1815` n `894`
- 24h: commodity avg `0.1931` n `12`; crypto_alt avg `2.9226` n `234`; crypto_major avg `4.0628` n `8`; equity avg `0.2088` n `140`; fx avg `0.0873` n `6`; index avg `-0.0428` n `26`; metal avg `-0.1213` n `20`; unknown avg `2.5385` n `785`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
