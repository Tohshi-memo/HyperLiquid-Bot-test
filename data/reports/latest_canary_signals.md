# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T17:07:16.813685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2341` n `12`; crypto_alt avg `0.023` n `228`; crypto_major avg `-0.1254` n `8`; equity avg `0.0319` n `67`; fx avg `0.0019` n `6`; index avg `-0.046` n `23`; metal avg `0.0696` n `18`; unknown avg `0.0027` n `405`
- 1h: commodity avg `-0.6643` n `12`; crypto_alt avg `0.3909` n `228`; crypto_major avg `0.023` n `8`; equity avg `0.0275` n `67`; fx avg `0.0137` n `6`; index avg `-0.0672` n `23`; metal avg `0.2019` n `18`; unknown avg `0.127` n `405`
- 4h: commodity avg `-0.919` n `12`; crypto_alt avg `1.057` n `228`; crypto_major avg `0.0608` n `8`; equity avg `0.1486` n `67`; fx avg `-0.0389` n `6`; index avg `0.0116` n `23`; metal avg `0.6432` n `18`; unknown avg `0.7899` n `405`
- 24h: commodity avg `-1.3115` n `12`; crypto_alt avg `2.3143` n `228`; crypto_major avg `0.5949` n `8`; equity avg `0.8967` n `67`; fx avg `-0.0341` n `6`; index avg `0.4728` n `23`; metal avg `1.6253` n `18`; unknown avg `1.6454` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
