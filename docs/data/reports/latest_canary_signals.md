# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T12:37:34.202752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `13`; crypto_alt avg `-0.0729` n `234`; crypto_major avg `-0.0847` n `8`; equity avg `-0.0005` n `142`; fx avg `-0.0221` n `6`; index avg `0.0105` n `26`; metal avg `0.0277` n `20`; unknown avg `-0.2154` n `975`
- 1h: commodity avg `-0.0855` n `13`; crypto_alt avg `-0.1084` n `234`; crypto_major avg `0.0174` n `8`; equity avg `-0.0833` n `142`; fx avg `-0.0163` n `6`; index avg `0.0341` n `26`; metal avg `0.1623` n `20`; unknown avg `0.0` n `967`
- 4h: commodity avg `-0.3332` n `13`; crypto_alt avg `-0.1197` n `234`; crypto_major avg `0.6537` n `8`; equity avg `0.2326` n `142`; fx avg `-0.0274` n `6`; index avg `0.1358` n `26`; metal avg `0.3229` n `20`; unknown avg `2.7382` n `967`
- 24h: commodity avg `-0.2084` n `13`; crypto_alt avg `-1.6437` n `234`; crypto_major avg `-0.7685` n `8`; equity avg `-0.0299` n `142`; fx avg `0.0276` n `6`; index avg `0.0891` n `26`; metal avg `-0.1489` n `20`; unknown avg `775.8789` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
