# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T14:52:28.459875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `13`; crypto_alt avg `-0.8754` n `234`; crypto_major avg `-0.6649` n `8`; equity avg `-0.2025` n `142`; fx avg `-0.0242` n `6`; index avg `-0.0404` n `26`; metal avg `-0.123` n `20`; unknown avg `1.3517` n `951`
- 1h: commodity avg `0.0384` n `13`; crypto_alt avg `-0.9521` n `234`; crypto_major avg `-0.6293` n `8`; equity avg `-0.1336` n `142`; fx avg `-0.0976` n `6`; index avg `-0.1168` n `26`; metal avg `-0.1078` n `20`; unknown avg `-0.1246` n `917`
- 4h: commodity avg `0.3465` n `13`; crypto_alt avg `-1.3429` n `234`; crypto_major avg `-0.7403` n `8`; equity avg `-0.925` n `142`; fx avg `-0.1122` n `6`; index avg `-0.2538` n `26`; metal avg `-0.1358` n `20`; unknown avg `1.0011` n `911`
- 24h: commodity avg `-0.1722` n `13`; crypto_alt avg `-1.8171` n `234`; crypto_major avg `-0.157` n `8`; equity avg `-0.3544` n `142`; fx avg `-0.0337` n `6`; index avg `-0.1746` n `26`; metal avg `-0.1831` n `20`; unknown avg `3.1557` n `782`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
