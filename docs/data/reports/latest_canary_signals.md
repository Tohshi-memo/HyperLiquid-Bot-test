# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T17:37:25.538442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0404` n `12`; crypto_alt avg `0.064` n `230`; crypto_major avg `0.0687` n `8`; equity avg `0.023` n `100`; fx avg `-0.0057` n `6`; index avg `0.026` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0656` n `774`
- 1h: commodity avg `-0.069` n `12`; crypto_alt avg `0.3341` n `230`; crypto_major avg `0.4288` n `8`; equity avg `0.1236` n `100`; fx avg `0.013` n `6`; index avg `0.0539` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.1413` n `774`
- 4h: commodity avg `-0.4005` n `12`; crypto_alt avg `0.6686` n `230`; crypto_major avg `1.0088` n `8`; equity avg `0.1641` n `100`; fx avg `-0.0116` n `6`; index avg `0.0476` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.0632` n `774`
- 24h: commodity avg `-0.3559` n `12`; crypto_alt avg `0.2528` n `230`; crypto_major avg `0.9742` n `8`; equity avg `-0.845` n `100`; fx avg `-0.0055` n `6`; index avg `-0.0753` n `25`; metal avg `-0.1528` n `20`; unknown avg `-0.3835` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1289`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1122`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
