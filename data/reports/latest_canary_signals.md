# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T04:49:46.623513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `0.0018` n `228`; crypto_major avg `-0.0006` n `8`; equity avg `0.0694` n `69`; fx avg `0.0118` n `6`; index avg `0.005` n `23`; metal avg `-0.0116` n `18`; unknown avg `0.1544` n `417`
- 1h: commodity avg `-0.1608` n `12`; crypto_alt avg `0.2692` n `228`; crypto_major avg `0.1262` n `8`; equity avg `0.3374` n `69`; fx avg `-0.0018` n `6`; index avg `0.1337` n `23`; metal avg `0.2394` n `18`; unknown avg `-0.1671` n `417`
- 4h: commodity avg `-0.1032` n `12`; crypto_alt avg `-0.7938` n `228`; crypto_major avg `-0.5927` n `8`; equity avg `0.267` n `69`; fx avg `-0.0039` n `6`; index avg `0.1041` n `23`; metal avg `0.1371` n `18`; unknown avg `-0.8056` n `417`
- 24h: commodity avg `-0.2649` n `12`; crypto_alt avg `0.7673` n `228`; crypto_major avg `1.6164` n `8`; equity avg `4.7492` n `69`; fx avg `0.1534` n `6`; index avg `1.772` n `23`; metal avg `2.7254` n `18`; unknown avg `0.6005` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
