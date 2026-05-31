# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T04:22:16.072131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.106` n `12`; crypto_alt avg `0.1597` n `228`; crypto_major avg `0.2019` n `8`; equity avg `-0.0219` n `69`; fx avg `0.0027` n `6`; index avg `-0.0081` n `23`; metal avg `-0.001` n `18`; unknown avg `-0.29` n `421`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `0.2082` n `228`; crypto_major avg `0.1912` n `8`; equity avg `0.0058` n `69`; fx avg `0.0053` n `6`; index avg `-0.0477` n `23`; metal avg `0.0183` n `18`; unknown avg `-0.4571` n `421`
- 4h: commodity avg `0.1182` n `12`; crypto_alt avg `0.5579` n `228`; crypto_major avg `0.6359` n `8`; equity avg `0.1844` n `69`; fx avg `0.0203` n `6`; index avg `-0.0055` n `23`; metal avg `-0.0292` n `18`; unknown avg `-0.2862` n `419`
- 24h: commodity avg `-0.0139` n `12`; crypto_alt avg `1.1017` n `228`; crypto_major avg `2.9181` n `8`; equity avg `1.0713` n `69`; fx avg `0.0496` n `6`; index avg `0.102` n `23`; metal avg `0.0254` n `18`; unknown avg `0.4872` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
