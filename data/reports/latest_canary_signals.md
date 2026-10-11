# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T22:22:25.984108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0878` n `13`; crypto_alt avg `0.0853` n `235`; crypto_major avg `0.0623` n `8`; equity avg `0.0038` n `150`; fx avg `0.0035` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0435` n `20`; unknown avg `-0.0216` n `1134`
- 1h: commodity avg `0.009` n `13`; crypto_alt avg `0.6295` n `235`; crypto_major avg `0.4242` n `8`; equity avg `0.0454` n `150`; fx avg `-0.0161` n `6`; index avg `0.0112` n `26`; metal avg `-0.0449` n `20`; unknown avg `0.2505` n `1122`
- 4h: commodity avg `0.1192` n `13`; crypto_alt avg `-0.1181` n `235`; crypto_major avg `-0.3774` n `8`; equity avg `-0.0292` n `150`; fx avg `-0.0234` n `6`; index avg `-0.003` n `26`; metal avg `-0.051` n `20`; unknown avg `-0.0838` n `1088`
- 24h: commodity avg `0.1888` n `13`; crypto_alt avg `1.5515` n `235`; crypto_major avg `0.5748` n `8`; equity avg `0.2214` n `150`; fx avg `-0.0052` n `6`; index avg `0.032` n `26`; metal avg `0.007` n `20`; unknown avg `0.6618` n `965`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
