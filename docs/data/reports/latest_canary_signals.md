# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T03:37:20.136494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0692` n `12`; crypto_alt avg `0.0475` n `228`; crypto_major avg `0.0795` n `8`; equity avg `0.0291` n `69`; fx avg `0.0` n `6`; index avg `-0.0119` n `23`; metal avg `0.0042` n `18`; unknown avg `-0.0755` n `421`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `0.3008` n `228`; crypto_major avg `0.3421` n `8`; equity avg `0.0761` n `69`; fx avg `0.0139` n `6`; index avg `0.0494` n `23`; metal avg `-0.0` n `18`; unknown avg `-0.2969` n `421`
- 4h: commodity avg `0.0264` n `12`; crypto_alt avg `0.9397` n `228`; crypto_major avg `0.9803` n `8`; equity avg `0.2441` n `69`; fx avg `0.023` n `6`; index avg `-0.0057` n `23`; metal avg `-0.0424` n `18`; unknown avg `-0.0214` n `419`
- 24h: commodity avg `-0.1515` n `12`; crypto_alt avg `0.4568` n `228`; crypto_major avg `2.4125` n `8`; equity avg `1.0223` n `69`; fx avg `0.0425` n `6`; index avg `0.1476` n `23`; metal avg `-0.0508` n `18`; unknown avg `1.5501` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
