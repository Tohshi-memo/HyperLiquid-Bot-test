# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T20:52:29.997836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0442` n `13`; crypto_alt avg `0.6654` n `239`; crypto_major avg `0.6597` n `8`; equity avg `0.8584` n `168`; fx avg `-0.0043` n `6`; index avg `0.1025` n `27`; metal avg `0.0898` n `20`; unknown avg `21.5593` n `1253`
- 1h: commodity avg `-0.0188` n `13`; crypto_alt avg `0.0582` n `239`; crypto_major avg `0.1776` n `8`; equity avg `0.2923` n `168`; fx avg `-0.0042` n `6`; index avg `0.032` n `27`; metal avg `-0.0179` n `20`; unknown avg `22.7157` n `1239`
- 4h: commodity avg `0.0844` n `13`; crypto_alt avg `0.2694` n `239`; crypto_major avg `0.3228` n `8`; equity avg `0.7592` n `168`; fx avg `-0.0243` n `6`; index avg `0.1019` n `27`; metal avg `-0.0356` n `20`; unknown avg `398.2511` n `1213`
- 24h: commodity avg `0.6643` n `13`; crypto_alt avg `-2.6475` n `239`; crypto_major avg `-2.5` n `8`; equity avg `-3.4591` n `167`; fx avg `0.2334` n `6`; index avg `-0.1929` n `27`; metal avg `-1.0599` n `20`; unknown avg `431.3396` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
