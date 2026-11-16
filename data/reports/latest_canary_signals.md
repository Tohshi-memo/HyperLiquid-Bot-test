# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T10:22:37.621220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `13`; crypto_alt avg `0.1626` n `239`; crypto_major avg `0.2311` n `8`; equity avg `0.0811` n `162`; fx avg `0.0146` n `6`; index avg `0.0136` n `27`; metal avg `0.0571` n `20`; unknown avg `0.3641` n `1263`
- 1h: commodity avg `0.1919` n `13`; crypto_alt avg `0.1782` n `239`; crypto_major avg `0.4432` n `8`; equity avg `-0.1042` n `162`; fx avg `-0.0044` n `6`; index avg `-0.0131` n `27`; metal avg `-0.028` n `20`; unknown avg `0.4874` n `1263`
- 4h: commodity avg `-0.1517` n `13`; crypto_alt avg `0.0143` n `239`; crypto_major avg `0.1225` n `8`; equity avg `0.0254` n `162`; fx avg `-0.0095` n `6`; index avg `0.0478` n `27`; metal avg `-0.055` n `20`; unknown avg `35.591` n `1093`
- 24h: commodity avg `-0.3052` n `13`; crypto_alt avg `-1.2502` n `239`; crypto_major avg `-1.22` n `8`; equity avg `-0.9687` n `162`; fx avg `-0.0585` n `6`; index avg `-0.0529` n `27`; metal avg `-0.0307` n `20`; unknown avg `36.0515` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
