# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T12:37:38.859346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `-0.4146` n `232`; crypto_major avg `-0.497` n `8`; equity avg `-0.115` n `130`; fx avg `0.0022` n `6`; index avg `-0.0177` n `26`; metal avg `-0.0544` n `20`; unknown avg `0.3052` n `792`
- 1h: commodity avg `0.0603` n `12`; crypto_alt avg `-0.6357` n `232`; crypto_major avg `-0.6236` n `8`; equity avg `-0.4742` n `130`; fx avg `0.0057` n `6`; index avg `-0.0736` n `26`; metal avg `-0.0761` n `20`; unknown avg `0.1239` n `790`
- 4h: commodity avg `-0.1065` n `12`; crypto_alt avg `0.0137` n `232`; crypto_major avg `-0.1897` n `8`; equity avg `-0.7426` n `130`; fx avg `0.0242` n `6`; index avg `-0.1249` n `26`; metal avg `-0.0654` n `20`; unknown avg `-0.5092` n `790`
- 24h: commodity avg `0.3326` n `12`; crypto_alt avg `0.6877` n `232`; crypto_major avg `-0.1539` n `8`; equity avg `-0.9923` n `130`; fx avg `0.0902` n `6`; index avg `-0.3136` n `26`; metal avg `-0.7813` n `20`; unknown avg `-0.0465` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0421`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0301`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0284`, n `668`, weak_sample_signal
