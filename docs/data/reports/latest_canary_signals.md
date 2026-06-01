# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T06:52:19.662206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0624` n `12`; crypto_alt avg `0.2245` n `228`; crypto_major avg `0.1434` n `8`; equity avg `-0.0114` n `69`; fx avg `0.0082` n `6`; index avg `0.3753` n `23`; metal avg `-0.0975` n `18`; unknown avg `-0.1431` n `422`
- 1h: commodity avg `0.2266` n `12`; crypto_alt avg `-0.8761` n `228`; crypto_major avg `-0.3488` n `8`; equity avg `-0.2148` n `69`; fx avg `0.0158` n `6`; index avg `0.4123` n `23`; metal avg `-0.4221` n `18`; unknown avg `-0.1127` n `412`
- 4h: commodity avg `0.4313` n `12`; crypto_alt avg `-1.4954` n `228`; crypto_major avg `-0.7769` n `8`; equity avg `-0.0354` n `69`; fx avg `-0.1031` n `6`; index avg `0.1991` n `23`; metal avg `-0.2462` n `18`; unknown avg `-0.1151` n `412`
- 24h: commodity avg `1.3245` n `12`; crypto_alt avg `-0.538` n `228`; crypto_major avg `-0.8699` n `8`; equity avg `0.1813` n `69`; fx avg `-0.0674` n `6`; index avg `0.8492` n `23`; metal avg `-0.0198` n `18`; unknown avg `1.613` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2874`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2239`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
