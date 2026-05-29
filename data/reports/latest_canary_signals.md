# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T00:22:18.666978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `0.1718` n `228`; crypto_major avg `0.293` n `8`; equity avg `0.1077` n `69`; fx avg `0.0057` n `6`; index avg `0.0509` n `23`; metal avg `0.0962` n `18`; unknown avg `0.024` n `417`
- 1h: commodity avg `-0.1542` n `12`; crypto_alt avg `0.4529` n `228`; crypto_major avg `0.2978` n `8`; equity avg `0.0814` n `69`; fx avg `0.0546` n `6`; index avg `0.0098` n `23`; metal avg `0.1111` n `18`; unknown avg `0.4618` n `417`
- 4h: commodity avg `-0.3001` n `12`; crypto_alt avg `0.1391` n `228`; crypto_major avg `0.2437` n `8`; equity avg `0.5991` n `69`; fx avg `0.052` n `6`; index avg `0.0409` n `23`; metal avg `0.1245` n `18`; unknown avg `-0.1668` n `417`
- 24h: commodity avg `0.4058` n `12`; crypto_alt avg `-1.7177` n `228`; crypto_major avg `0.4534` n `8`; equity avg `2.8845` n `69`; fx avg `0.0218` n `6`; index avg `1.005` n `23`; metal avg `0.631` n `18`; unknown avg `0.213` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
