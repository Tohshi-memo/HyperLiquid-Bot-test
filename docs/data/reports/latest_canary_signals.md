# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T05:52:31.225908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.0294` n `236`; crypto_major avg `-0.0066` n `8`; equity avg `-0.0413` n `151`; fx avg `0.0011` n `6`; index avg `0.0052` n `26`; metal avg `-0.002` n `20`; unknown avg `0.3075` n `1193`
- 1h: commodity avg `-0.0198` n `13`; crypto_alt avg `-0.1405` n `236`; crypto_major avg `0.0679` n `8`; equity avg `0.0376` n `151`; fx avg `0.0005` n `6`; index avg `0.0258` n `26`; metal avg `-0.0153` n `20`; unknown avg `4.2973` n `1191`
- 4h: commodity avg `0.0083` n `13`; crypto_alt avg `0.3061` n `236`; crypto_major avg `0.2187` n `8`; equity avg `0.1142` n `151`; fx avg `-0.012` n `6`; index avg `0.0518` n `26`; metal avg `0.0056` n `20`; unknown avg `0.362` n `1185`
- 24h: commodity avg `0.6322` n `13`; crypto_alt avg `-1.6364` n `236`; crypto_major avg `-1.2729` n `8`; equity avg `-4.1926` n `151`; fx avg `0.0332` n `6`; index avg `-0.6535` n `26`; metal avg `-0.2391` n `20`; unknown avg `40.9363` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1777`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
