# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T11:52:20.073220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.114` n `12`; crypto_alt avg `-0.3785` n `228`; crypto_major avg `-0.2359` n `8`; equity avg `0.0399` n `69`; fx avg `-0.0024` n `6`; index avg `-0.0034` n `23`; metal avg `0.0221` n `18`; unknown avg `-0.024` n `417`
- 1h: commodity avg `0.2568` n `12`; crypto_alt avg `-0.5925` n `228`; crypto_major avg `-0.4714` n `8`; equity avg `-0.1608` n `69`; fx avg `-0.0127` n `6`; index avg `0.0847` n `23`; metal avg `-0.1454` n `18`; unknown avg `0.8134` n `417`
- 4h: commodity avg `-0.2293` n `12`; crypto_alt avg `-0.4355` n `228`; crypto_major avg `-0.3023` n `8`; equity avg `-0.2967` n `69`; fx avg `-0.0322` n `6`; index avg `0.1362` n `23`; metal avg `0.002` n `18`; unknown avg `-0.1567` n `417`
- 24h: commodity avg `-0.1024` n `12`; crypto_alt avg `1.2386` n `228`; crypto_major avg `1.6968` n `8`; equity avg `3.3921` n `69`; fx avg `0.1312` n `6`; index avg `1.5487` n `23`; metal avg `2.437` n `18`; unknown avg `1.8769` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
