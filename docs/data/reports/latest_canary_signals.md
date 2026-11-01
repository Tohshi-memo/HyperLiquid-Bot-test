# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T06:07:25.681483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `0.1776` n `238`; crypto_major avg `0.1134` n `8`; equity avg `0.032` n `156`; fx avg `-0.0012` n `6`; index avg `0.0033` n `27`; metal avg `0.0023` n `20`; unknown avg `115.7416` n `1240`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `0.3484` n `238`; crypto_major avg `0.1721` n `8`; equity avg `0.0688` n `156`; fx avg `-0.0021` n `6`; index avg `0.0111` n `27`; metal avg `-0.0017` n `20`; unknown avg `0.744` n `1240`
- 4h: commodity avg `-0.0157` n `13`; crypto_alt avg `0.507` n `238`; crypto_major avg `0.137` n `8`; equity avg `0.2224` n `156`; fx avg `-0.0055` n `6`; index avg `0.0336` n `27`; metal avg `0.001` n `20`; unknown avg `0.6431` n `1226`
- 24h: commodity avg `-0.0495` n `13`; crypto_alt avg `0.7975` n `238`; crypto_major avg `0.3726` n `8`; equity avg `0.304` n `156`; fx avg `-0.0045` n `6`; index avg `-0.0016` n `27`; metal avg `0.0448` n `20`; unknown avg `2.8587` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
