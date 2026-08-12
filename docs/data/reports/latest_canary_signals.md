# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T23:37:34.934817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `0.1076` n `230`; crypto_major avg `0.1053` n `8`; equity avg `0.0351` n `113`; fx avg `0.0007` n `6`; index avg `-0.0111` n `25`; metal avg `0.0067` n `20`; unknown avg `-0.0502` n `786`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `0.125` n `230`; crypto_major avg `0.0629` n `8`; equity avg `0.2015` n `113`; fx avg `0.0001` n `6`; index avg `0.0131` n `25`; metal avg `0.0663` n `20`; unknown avg `-0.058` n `786`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `-0.5448` n `230`; crypto_major avg `-0.3151` n `8`; equity avg `-0.0344` n `113`; fx avg `-0.0076` n `6`; index avg `0.0121` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.2039` n `786`
- 24h: commodity avg `-0.0027` n `12`; crypto_alt avg `-1.4376` n `230`; crypto_major avg `-0.5941` n `8`; equity avg `2.8992` n `113`; fx avg `0.0189` n `6`; index avg `0.4018` n `25`; metal avg `0.1631` n `20`; unknown avg `-0.0644` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
