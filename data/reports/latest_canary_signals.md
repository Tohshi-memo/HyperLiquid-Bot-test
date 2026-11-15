# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T21:22:32.850215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `-0.5785` n `239`; crypto_major avg `-0.3239` n `8`; equity avg `-0.0562` n `162`; fx avg `-0.0006` n `6`; index avg `-0.018` n `27`; metal avg `-0.0365` n `20`; unknown avg `4.2103` n `1263`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.2465` n `239`; crypto_major avg `0.0398` n `8`; equity avg `0.1121` n `162`; fx avg `0.0055` n `6`; index avg `0.0098` n `27`; metal avg `-0.0061` n `20`; unknown avg `2.7137` n `1247`
- 4h: commodity avg `0.0545` n `13`; crypto_alt avg `0.1394` n `239`; crypto_major avg `0.3065` n `8`; equity avg `0.3648` n `162`; fx avg `0.0636` n `6`; index avg `0.0491` n `27`; metal avg `0.0839` n `20`; unknown avg `3.7357` n `1235`
- 24h: commodity avg `0.1024` n `13`; crypto_alt avg `2.7008` n `239`; crypto_major avg `2.9214` n `8`; equity avg `1.3281` n `162`; fx avg `0.0433` n `6`; index avg `0.1176` n `27`; metal avg `0.2738` n `20`; unknown avg `5.2086` n `1156`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
