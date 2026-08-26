# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T11:22:29.588750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `0.0188` n `231`; crypto_major avg `-0.1889` n `8`; equity avg `0.043` n `122`; fx avg `0.0026` n `6`; index avg `0.0008` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.1065` n `797`
- 1h: commodity avg `0.0715` n `12`; crypto_alt avg `0.5815` n `231`; crypto_major avg `0.5408` n `8`; equity avg `0.1978` n `122`; fx avg `0.005` n `6`; index avg `0.0505` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.1161` n `797`
- 4h: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0017` n `231`; crypto_major avg `0.046` n `8`; equity avg `0.2053` n `122`; fx avg `-0.0189` n `6`; index avg `0.0115` n `25`; metal avg `-0.0723` n `20`; unknown avg `-0.0199` n `797`
- 24h: commodity avg `-0.2877` n `12`; crypto_alt avg `-1.1652` n `231`; crypto_major avg `-0.8035` n `8`; equity avg `0.45` n `122`; fx avg `-0.0248` n `6`; index avg `0.0026` n `25`; metal avg `0.1305` n `20`; unknown avg `0.5568` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
