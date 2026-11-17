# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T08:52:32.037313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0424` n `13`; crypto_alt avg `0.0918` n `239`; crypto_major avg `0.1079` n `8`; equity avg `-0.0415` n `162`; fx avg `-0.0071` n `6`; index avg `0.0009` n `27`; metal avg `0.0487` n `20`; unknown avg `0.185` n `1266`
- 1h: commodity avg `-0.0348` n `13`; crypto_alt avg `-0.2543` n `239`; crypto_major avg `-0.3374` n `8`; equity avg `-0.1271` n `162`; fx avg `-0.0244` n `6`; index avg `-0.0163` n `27`; metal avg `-0.025` n `20`; unknown avg `-0.0281` n `1238`
- 4h: commodity avg `0.1451` n `13`; crypto_alt avg `-0.4563` n `239`; crypto_major avg `-0.6746` n `8`; equity avg `-0.7267` n `162`; fx avg `-0.0202` n `6`; index avg `-0.0557` n `27`; metal avg `-0.0761` n `20`; unknown avg `4.6787` n `1172`
- 24h: commodity avg `-0.951` n `13`; crypto_alt avg `0.7982` n `239`; crypto_major avg `0.9571` n `8`; equity avg `-2.7958` n `162`; fx avg `-0.0631` n `6`; index avg `-0.3135` n `27`; metal avg `-0.0701` n `20`; unknown avg `36.0015` n `1115`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
