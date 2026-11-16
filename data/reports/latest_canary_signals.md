# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T04:37:27.268017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0441` n `13`; crypto_alt avg `-0.07` n `239`; crypto_major avg `-0.0525` n `8`; equity avg `-0.0507` n `162`; fx avg `0.0142` n `6`; index avg `-0.0061` n `27`; metal avg `0.0133` n `20`; unknown avg `0.0533` n `1263`
- 1h: commodity avg `0.1004` n `13`; crypto_alt avg `0.1831` n `239`; crypto_major avg `0.1223` n `8`; equity avg `-0.045` n `162`; fx avg `-0.0088` n `6`; index avg `0.0137` n `27`; metal avg `0.0373` n `20`; unknown avg `-0.4718` n `1255`
- 4h: commodity avg `-0.0154` n `13`; crypto_alt avg `0.1451` n `239`; crypto_major avg `-0.2091` n `8`; equity avg `-1.2677` n `162`; fx avg `-0.0043` n `6`; index avg `-0.1871` n `27`; metal avg `-0.3198` n `20`; unknown avg `0.5771` n `1237`
- 24h: commodity avg `-0.368` n `13`; crypto_alt avg `0.0679` n `239`; crypto_major avg `0.0773` n `8`; equity avg `0.132` n `162`; fx avg `-0.0292` n `6`; index avg `0.0194` n `27`; metal avg `0.2117` n `20`; unknown avg `1.3471` n `1129`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
