# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T14:26:57.096966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.2265` n `230`; crypto_major avg `0.1468` n `8`; equity avg `-0.1428` n `100`; fx avg `-0.0041` n `6`; index avg `-0.0555` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.011` n `772`
- 1h: commodity avg `0.1033` n `12`; crypto_alt avg `0.2565` n `230`; crypto_major avg `-0.0711` n `8`; equity avg `1.0264` n `100`; fx avg `-0.0061` n `6`; index avg `0.0538` n `25`; metal avg `0.049` n `20`; unknown avg `0.0421` n `772`
- 4h: commodity avg `0.1848` n `12`; crypto_alt avg `-0.3074` n `230`; crypto_major avg `-0.8708` n `8`; equity avg `-0.6398` n `99`; fx avg `-0.0041` n `6`; index avg `-0.2673` n `25`; metal avg `-0.3066` n `20`; unknown avg `0.0957` n `772`
- 24h: commodity avg `0.8982` n `12`; crypto_alt avg `-0.7368` n `230`; crypto_major avg `-0.933` n `8`; equity avg `-0.7789` n `99`; fx avg `-0.0806` n `6`; index avg `-0.2675` n `25`; metal avg `-0.8748` n `20`; unknown avg `-0.0511` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0657`, n `666`, weak_sample_signal
