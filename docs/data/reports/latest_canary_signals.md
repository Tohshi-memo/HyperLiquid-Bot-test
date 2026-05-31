# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T15:22:20.857097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.3555` n `228`; crypto_major avg `0.2627` n `8`; equity avg `-0.0122` n `69`; fx avg `-0.0005` n `6`; index avg `0.0798` n `23`; metal avg `-0.0122` n `18`; unknown avg `0.0088` n `421`
- 1h: commodity avg `0.0527` n `12`; crypto_alt avg `0.3069` n `228`; crypto_major avg `0.2031` n `8`; equity avg `0.0531` n `69`; fx avg `0.0025` n `6`; index avg `0.0564` n `23`; metal avg `-0.0152` n `18`; unknown avg `0.1468` n `421`
- 4h: commodity avg `0.1055` n `12`; crypto_alt avg `-0.6289` n `228`; crypto_major avg `-0.0424` n `8`; equity avg `0.0008` n `69`; fx avg `0.0201` n `6`; index avg `0.0089` n `23`; metal avg `-0.0168` n `18`; unknown avg `-0.161` n `421`
- 24h: commodity avg `0.1694` n `12`; crypto_alt avg `-0.7143` n `228`; crypto_major avg `0.3795` n `8`; equity avg `0.6976` n `69`; fx avg `-0.0224` n `6`; index avg `-0.2204` n `23`; metal avg `-0.063` n `18`; unknown avg `0.3791` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
