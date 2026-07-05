# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T01:07:25.610758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0564` n `229`; crypto_major avg `0.0071` n `8`; equity avg `0.0139` n `88`; fx avg `0.0007` n `6`; index avg `0.0378` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.1051` n `765`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.0034` n `229`; crypto_major avg `-0.2244` n `8`; equity avg `0.037` n `88`; fx avg `-0.0037` n `6`; index avg `0.0337` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.2571` n `765`
- 4h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.6671` n `229`; crypto_major avg `-0.6464` n `8`; equity avg `0.0212` n `88`; fx avg `0.0112` n `6`; index avg `0.054` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0581` n `765`
- 24h: commodity avg `-0.0381` n `12`; crypto_alt avg `0.3231` n `229`; crypto_major avg `0.1267` n `8`; equity avg `0.2814` n `88`; fx avg `-0.0226` n `6`; index avg `0.0851` n `25`; metal avg `0.1102` n `20`; unknown avg `-0.7066` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
