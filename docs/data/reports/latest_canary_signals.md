# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T07:07:26.790218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.1355` n `228`; crypto_major avg `-0.0005` n `8`; equity avg `0.0173` n `78`; fx avg `0.0019` n `6`; index avg `0.0054` n `23`; metal avg `0.0031` n `18`; unknown avg `0.0009` n `702`
- 1h: commodity avg `-0.0623` n `12`; crypto_alt avg `0.259` n `228`; crypto_major avg `0.0715` n `8`; equity avg `0.0752` n `78`; fx avg `0.0012` n `6`; index avg `0.0163` n `23`; metal avg `0.0412` n `18`; unknown avg `0.0214` n `702`
- 4h: commodity avg `-0.0546` n `12`; crypto_alt avg `0.2245` n `228`; crypto_major avg `-0.1055` n `8`; equity avg `0.2596` n `78`; fx avg `-0.0032` n `6`; index avg `0.0421` n `23`; metal avg `0.0719` n `18`; unknown avg `-0.1129` n `662`
- 24h: commodity avg `0.0565` n `12`; crypto_alt avg `1.2826` n `228`; crypto_major avg `0.3515` n `8`; equity avg `0.3394` n `78`; fx avg `0.0682` n `6`; index avg `0.0203` n `23`; metal avg `0.0016` n `18`; unknown avg `-0.4544` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
