# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T15:07:18.190886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.0745` n `228`; crypto_major avg `0.061` n `8`; equity avg `0.0124` n `69`; fx avg `-0.0001` n `6`; index avg `-0.0137` n `23`; metal avg `-0.0119` n `18`; unknown avg `-0.0953` n `421`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.0433` n `228`; crypto_major avg `0.2092` n `8`; equity avg `0.0809` n `69`; fx avg `0.0066` n `6`; index avg `0.0197` n `23`; metal avg `-0.0204` n `18`; unknown avg `-0.0229` n `421`
- 4h: commodity avg `0.2135` n `12`; crypto_alt avg `0.2355` n `228`; crypto_major avg `0.7156` n `8`; equity avg `0.3891` n `69`; fx avg `0.0252` n `6`; index avg `0.1678` n `23`; metal avg `-0.0621` n `18`; unknown avg `0.1092` n `421`
- 24h: commodity avg `0.4938` n `12`; crypto_alt avg `1.9317` n `228`; crypto_major avg `2.4877` n `8`; equity avg `1.5578` n `69`; fx avg `0.0303` n `6`; index avg `0.4119` n `23`; metal avg `-0.6989` n `18`; unknown avg `0.6534` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
