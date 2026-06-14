# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T09:07:35.424711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1023` n `12`; crypto_alt avg `-0.1073` n `228`; crypto_major avg `-0.0712` n `8`; equity avg `0.0182` n `74`; fx avg `-0.0064` n `6`; index avg `-0.0017` n `23`; metal avg `0.0009` n `18`; unknown avg `-0.1519` n `645`
- 1h: commodity avg `0.1094` n `12`; crypto_alt avg `0.1327` n `228`; crypto_major avg `0.1141` n `8`; equity avg `-0.005` n `74`; fx avg `-0.0071` n `6`; index avg `0.0137` n `23`; metal avg `0.0127` n `18`; unknown avg `2.0724` n `645`
- 4h: commodity avg `-0.1657` n `12`; crypto_alt avg `0.1508` n `228`; crypto_major avg `-0.1258` n `8`; equity avg `0.1681` n `74`; fx avg `-0.0151` n `6`; index avg `0.0211` n `23`; metal avg `0.0307` n `18`; unknown avg `1.972` n `625`
- 24h: commodity avg `-1.0705` n `12`; crypto_alt avg `0.2812` n `228`; crypto_major avg `0.6869` n `8`; equity avg `0.6471` n `74`; fx avg `0.1012` n `6`; index avg `0.1886` n `23`; metal avg `0.2941` n `18`; unknown avg `-0.8513` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
