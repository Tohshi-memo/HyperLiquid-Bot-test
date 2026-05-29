# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T07:52:18.054367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0053` n `228`; crypto_major avg `0.0874` n `8`; equity avg `0.0627` n `69`; fx avg `-0.0054` n `6`; index avg `0.0321` n `23`; metal avg `0.0692` n `18`; unknown avg `0.0731` n `417`
- 1h: commodity avg `0.4568` n `12`; crypto_alt avg `-0.3676` n `228`; crypto_major avg `-0.1274` n `8`; equity avg `-0.1714` n `69`; fx avg `-0.0206` n `6`; index avg `-0.0465` n `23`; metal avg `-0.0301` n `18`; unknown avg `1.2591` n `417`
- 4h: commodity avg `0.2627` n `12`; crypto_alt avg `0.5554` n `228`; crypto_major avg `0.5011` n `8`; equity avg `0.4187` n `69`; fx avg `0.0453` n `6`; index avg `0.1521` n `23`; metal avg `0.2807` n `18`; unknown avg `1.1433` n `407`
- 24h: commodity avg `0.3874` n `12`; crypto_alt avg `0.9592` n `228`; crypto_major avg `1.6493` n `8`; equity avg `3.777` n `69`; fx avg `0.1575` n `6`; index avg `1.3142` n `23`; metal avg `1.8488` n `18`; unknown avg `1.5949` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
