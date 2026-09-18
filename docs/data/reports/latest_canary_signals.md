# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T22:41:05.701114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `-0.2648` n `234`; crypto_major avg `-0.1793` n `8`; equity avg `-0.0584` n `140`; fx avg `-0.0012` n `6`; index avg `-0.003` n `26`; metal avg `-0.003` n `20`; unknown avg `-0.006` n `942`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `-0.282` n `234`; crypto_major avg `-0.0941` n `8`; equity avg `-0.016` n `140`; fx avg `-0.0151` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0039` n `20`; unknown avg `15.9172` n `922`
- 4h: commodity avg `-0.0812` n `12`; crypto_alt avg `0.7821` n `234`; crypto_major avg `0.2424` n `8`; equity avg `0.6233` n `140`; fx avg `0.0411` n `6`; index avg `0.1058` n `26`; metal avg `-0.0795` n `20`; unknown avg `0.4204` n `872`
- 24h: commodity avg `-0.0827` n `12`; crypto_alt avg `6.9338` n `234`; crypto_major avg `6.9155` n `8`; equity avg `1.3658` n `140`; fx avg `0.2332` n `6`; index avg `0.0578` n `26`; metal avg `0.3573` n `20`; unknown avg `3.9435` n `757`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
