# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T05:37:32.183211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0609` n `13`; crypto_alt avg `0.1303` n `239`; crypto_major avg `0.1281` n `8`; equity avg `-0.0184` n `161`; fx avg `0.0203` n `6`; index avg `0.0176` n `27`; metal avg `0.052` n `20`; unknown avg `0.1321` n `1260`
- 1h: commodity avg `-0.0005` n `13`; crypto_alt avg `0.068` n `239`; crypto_major avg `-0.131` n `8`; equity avg `-0.6536` n `161`; fx avg `-0.0133` n `6`; index avg `-0.0574` n `27`; metal avg `0.0135` n `20`; unknown avg `159.3752` n `1252`
- 4h: commodity avg `-0.0143` n `13`; crypto_alt avg `-0.2171` n `239`; crypto_major avg `-0.2634` n `8`; equity avg `-1.05` n `161`; fx avg `-0.1141` n `6`; index avg `-0.0741` n `27`; metal avg `-0.0849` n `20`; unknown avg `18.9595` n `1234`
- 24h: commodity avg `0.0938` n `13`; crypto_alt avg `-1.6864` n `239`; crypto_major avg `-0.7491` n `8`; equity avg `-0.5173` n `161`; fx avg `-0.1905` n `6`; index avg `-0.0779` n `27`; metal avg `-0.5917` n `20`; unknown avg `43.9838` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
