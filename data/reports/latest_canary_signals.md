# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T03:37:19.194926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1153` n `12`; crypto_alt avg `0.0817` n `228`; crypto_major avg `0.0092` n `8`; equity avg `0.0603` n `69`; fx avg `-0.0018` n `6`; index avg `0.0462` n `23`; metal avg `0.0774` n `18`; unknown avg `-0.1426` n `422`
- 1h: commodity avg `-0.1304` n `12`; crypto_alt avg `0.8377` n `228`; crypto_major avg `0.5497` n `8`; equity avg `0.0639` n `69`; fx avg `0.0065` n `6`; index avg `1.2261` n `23`; metal avg `-0.1906` n `18`; unknown avg `0.5902` n `422`
- 4h: commodity avg `0.0865` n `12`; crypto_alt avg `1.5152` n `228`; crypto_major avg `0.7021` n `8`; equity avg `0.245` n `69`; fx avg `0.0938` n `6`; index avg `0.6213` n `23`; metal avg `0.0228` n `18`; unknown avg `-0.0638` n `421`
- 24h: commodity avg `0.9411` n `12`; crypto_alt avg `1.3553` n `228`; crypto_major avg `-0.0718` n `8`; equity avg `0.6464` n `69`; fx avg `0.0518` n `6`; index avg `0.6907` n `23`; metal avg `0.2775` n `18`; unknown avg `1.6649` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2872`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2031`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
