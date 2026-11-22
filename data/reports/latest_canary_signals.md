# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T09:07:26.462704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `0.059` n `239`; crypto_major avg `0.1128` n `8`; equity avg `0.0166` n `166`; fx avg `0.0037` n `6`; index avg `-0.0047` n `27`; metal avg `0.0133` n `20`; unknown avg `40.238` n `1253`
- 1h: commodity avg `-0.0199` n `13`; crypto_alt avg `0.6781` n `239`; crypto_major avg `0.9024` n `8`; equity avg `0.5779` n `166`; fx avg `-0.0031` n `6`; index avg `0.0476` n `27`; metal avg `0.0586` n `20`; unknown avg `242.6206` n `1239`
- 4h: commodity avg `-0.0004` n `13`; crypto_alt avg `0.9885` n `239`; crypto_major avg `1.0446` n `8`; equity avg `0.6349` n `166`; fx avg `-0.0163` n `6`; index avg `0.0637` n `27`; metal avg `0.0873` n `20`; unknown avg `206.5484` n `1213`
- 24h: commodity avg `0.0084` n `13`; crypto_alt avg `2.4791` n `239`; crypto_major avg `3.1404` n `8`; equity avg `1.4052` n `166`; fx avg `0.0161` n `6`; index avg `0.1803` n `27`; metal avg `0.104` n `20`; unknown avg `236.1247` n `1070`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
