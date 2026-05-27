# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T15:52:30.263352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.3305` n `228`; crypto_major avg `-0.2908` n `8`; equity avg `-0.09` n `67`; fx avg `0.0056` n `6`; index avg `-0.1437` n `23`; metal avg `-0.1651` n `18`; unknown avg `1.2176` n `418`
- 1h: commodity avg `-0.1001` n `12`; crypto_alt avg `0.9226` n `228`; crypto_major avg `0.4836` n `8`; equity avg `-0.514` n `67`; fx avg `-0.0137` n `6`; index avg `-0.2181` n `23`; metal avg `-0.1263` n `18`; unknown avg `2.0686` n `418`
- 4h: commodity avg `0.2714` n `12`; crypto_alt avg `0.4747` n `228`; crypto_major avg `-0.4689` n `8`; equity avg `-1.3269` n `67`; fx avg `-0.0259` n `6`; index avg `-1.1317` n `23`; metal avg `-0.1158` n `18`; unknown avg `1.5936` n `418`
- 24h: commodity avg `-1.175` n `12`; crypto_alt avg `-0.6528` n `228`; crypto_major avg `-0.6499` n `8`; equity avg `-0.4253` n `67`; fx avg `-0.0454` n `6`; index avg `-0.5939` n `23`; metal avg `-1.1741` n `18`; unknown avg `2.109` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
