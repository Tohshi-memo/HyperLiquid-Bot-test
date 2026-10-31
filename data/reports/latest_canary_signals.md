# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T19:07:27.268296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `13`; crypto_alt avg `-0.0102` n `238`; crypto_major avg `0.0307` n `8`; equity avg `0.0093` n `156`; fx avg `-0.0048` n `6`; index avg `-0.0024` n `27`; metal avg `0.0005` n `20`; unknown avg `0.8097` n `1254`
- 1h: commodity avg `0.0025` n `13`; crypto_alt avg `0.0294` n `238`; crypto_major avg `0.0569` n `8`; equity avg `0.0491` n `156`; fx avg `0.0028` n `6`; index avg `-0.001` n `27`; metal avg `0.0027` n `20`; unknown avg `-0.6043` n `1252`
- 4h: commodity avg `-0.0112` n `13`; crypto_alt avg `0.2337` n `238`; crypto_major avg `0.533` n `8`; equity avg `0.0939` n `156`; fx avg `-0.0177` n `6`; index avg `-0.0034` n `27`; metal avg `0.006` n `20`; unknown avg `0.5854` n `1196`
- 24h: commodity avg `-0.4034` n `13`; crypto_alt avg `1.6571` n `238`; crypto_major avg `0.8181` n `8`; equity avg `1.3115` n `156`; fx avg `-0.0271` n `6`; index avg `0.0685` n `27`; metal avg `0.1518` n `20`; unknown avg `0.8936` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
