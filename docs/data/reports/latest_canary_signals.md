# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T04:39:37.293621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.0279` n `230`; crypto_major avg `-0.0039` n `8`; equity avg `0.127` n `100`; fx avg `0.0144` n `6`; index avg `0.0143` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.1574` n `772`
- 1h: commodity avg `-0.0648` n `12`; crypto_alt avg `-0.0595` n `230`; crypto_major avg `-0.1009` n `8`; equity avg `0.0605` n `100`; fx avg `0.0136` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0219` n `20`; unknown avg `0.0261` n `772`
- 4h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.6667` n `230`; crypto_major avg `0.4193` n `8`; equity avg `-0.3602` n `100`; fx avg `-0.0546` n `6`; index avg `-0.1273` n `25`; metal avg `-0.2077` n `20`; unknown avg `0.7275` n `772`
- 24h: commodity avg `0.585` n `12`; crypto_alt avg `-1.1431` n `230`; crypto_major avg `-1.7986` n `8`; equity avg `-2.198` n `99`; fx avg `-0.0988` n `6`; index avg `-0.6269` n `25`; metal avg `-1.0801` n `20`; unknown avg `-0.2621` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1109`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0928`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
