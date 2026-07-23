# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T13:07:32.828996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.1901` n `230`; crypto_major avg `-0.1041` n `8`; equity avg `-0.1979` n `100`; fx avg `0.0073` n `6`; index avg `-0.041` n `25`; metal avg `-0.1496` n `20`; unknown avg `-0.0281` n `772`
- 1h: commodity avg `0.1396` n `12`; crypto_alt avg `-0.4755` n `230`; crypto_major avg `-0.6719` n `8`; equity avg `-0.8641` n `99`; fx avg `0.0056` n `6`; index avg `-0.1943` n `25`; metal avg `-0.3287` n `20`; unknown avg `0.155` n `772`
- 4h: commodity avg `0.2884` n `12`; crypto_alt avg `-0.6065` n `230`; crypto_major avg `-0.7974` n `8`; equity avg `-1.6141` n `99`; fx avg `-0.0036` n `6`; index avg `-0.3266` n `25`; metal avg `-0.4825` n `20`; unknown avg `0.1399` n `772`
- 24h: commodity avg `0.867` n `12`; crypto_alt avg `-0.5675` n `230`; crypto_major avg `-0.5174` n `8`; equity avg `-0.3661` n `99`; fx avg `-0.079` n `6`; index avg `-0.0636` n `25`; metal avg `-0.7378` n `20`; unknown avg `9.7221` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
