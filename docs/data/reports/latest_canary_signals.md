# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T22:37:30.093898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.1528` n `230`; crypto_major avg `-0.1145` n `8`; equity avg `-0.0838` n `98`; fx avg `0.0022` n `6`; index avg `-0.0252` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.0571` n `773`
- 1h: commodity avg `0.1765` n `12`; crypto_alt avg `-0.2214` n `230`; crypto_major avg `-0.1712` n `8`; equity avg `-0.3598` n `98`; fx avg `-0.0163` n `6`; index avg `-0.065` n `25`; metal avg `-0.118` n `20`; unknown avg `-0.0521` n `773`
- 4h: commodity avg `0.2207` n `12`; crypto_alt avg `0.0424` n `230`; crypto_major avg `0.1573` n `8`; equity avg `0.0893` n `98`; fx avg `-0.0283` n `6`; index avg `-0.0506` n `25`; metal avg `-0.1057` n `20`; unknown avg `0.0784` n `773`
- 24h: commodity avg `0.7302` n `12`; crypto_alt avg `-0.4027` n `230`; crypto_major avg `-0.6141` n `8`; equity avg `-1.1026` n `98`; fx avg `-0.0586` n `6`; index avg `-0.1917` n `25`; metal avg `0.1393` n `20`; unknown avg `1.6745` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0919`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
