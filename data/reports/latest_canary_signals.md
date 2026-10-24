# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T00:22:31.963821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0328` n `13`; crypto_alt avg `-0.4813` n `237`; crypto_major avg `-0.4528` n `8`; equity avg `-0.2114` n `152`; fx avg `-0.0015` n `6`; index avg `-0.0256` n `26`; metal avg `-0.0366` n `20`; unknown avg `0.0588` n `1230`
- 1h: commodity avg `0.0586` n `13`; crypto_alt avg `-0.0935` n `237`; crypto_major avg `-0.2535` n `8`; equity avg `-0.01` n `152`; fx avg `-0.0045` n `6`; index avg `0.0023` n `26`; metal avg `-0.0313` n `20`; unknown avg `-0.0072` n `1216`
- 4h: commodity avg `0.1693` n `13`; crypto_alt avg `-1.0538` n `237`; crypto_major avg `-0.8091` n `8`; equity avg `-0.2626` n `152`; fx avg `0.0143` n `6`; index avg `-0.0367` n `26`; metal avg `-0.0761` n `20`; unknown avg `0.2971` n `1196`
- 24h: commodity avg `0.6123` n `13`; crypto_alt avg `-1.1312` n `237`; crypto_major avg `-0.6302` n `8`; equity avg `1.3593` n `152`; fx avg `-0.0229` n `6`; index avg `0.115` n `26`; metal avg `-0.1735` n `20`; unknown avg `200.46` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
