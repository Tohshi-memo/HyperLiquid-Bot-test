# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T03:37:29.309882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.2209` n `238`; crypto_major avg `-0.1694` n `8`; equity avg `-0.0022` n `156`; fx avg `-0.0001` n `6`; index avg `-0.0124` n `27`; metal avg `0.0026` n `20`; unknown avg `-0.1585` n `1258`
- 1h: commodity avg `0.0513` n `13`; crypto_alt avg `-0.0866` n `238`; crypto_major avg `-0.1685` n `8`; equity avg `0.0249` n `156`; fx avg `-0.0083` n `6`; index avg `-0.0325` n `27`; metal avg `0.0203` n `20`; unknown avg `-0.1104` n `1244`
- 4h: commodity avg `0.0204` n `13`; crypto_alt avg `-0.493` n `238`; crypto_major avg `-0.1485` n `8`; equity avg `0.0177` n `156`; fx avg `0.0038` n `6`; index avg `-0.0341` n `27`; metal avg `0.0006` n `20`; unknown avg `-0.4062` n `1234`
- 24h: commodity avg `-0.0121` n `13`; crypto_alt avg `2.7583` n `238`; crypto_major avg `-0.4693` n `8`; equity avg `-2.3381` n `156`; fx avg `-0.0923` n `6`; index avg `-0.136` n `27`; metal avg `-0.6358` n `20`; unknown avg `-0.6657` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
