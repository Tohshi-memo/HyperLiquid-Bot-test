# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T10:37:30.715971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `-0.0537` n `230`; crypto_major avg `-0.0544` n `8`; equity avg `-0.0072` n `100`; fx avg `0.0046` n `6`; index avg `0.0019` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0026` n `774`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `0.079` n `8`; equity avg `0.0423` n `100`; fx avg `0.0021` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.015` n `774`
- 4h: commodity avg `0.0311` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `0.1653` n `8`; equity avg `-0.1042` n `100`; fx avg `0.0129` n `6`; index avg `0.0002` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.1781` n `774`
- 24h: commodity avg `-0.0567` n `12`; crypto_alt avg `-1.4139` n `230`; crypto_major avg `-1.1501` n `8`; equity avg `-2.9348` n `100`; fx avg `-0.0065` n `6`; index avg `-0.2504` n `25`; metal avg `-0.1568` n `20`; unknown avg `13.1691` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.101`, n `666`, weak_sample_signal
