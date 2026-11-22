# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T06:52:25.403089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `13`; crypto_alt avg `-0.0959` n `239`; crypto_major avg `-0.1644` n `8`; equity avg `-0.03` n `166`; fx avg `-0.0052` n `6`; index avg `-0.0045` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.0922` n `1263`
- 1h: commodity avg `-0.0001` n `13`; crypto_alt avg `0.0836` n `239`; crypto_major avg `0.1607` n `8`; equity avg `0.0228` n `166`; fx avg `-0.0041` n `6`; index avg `0.0046` n `27`; metal avg `0.0014` n `20`; unknown avg `272.8886` n `1231`
- 4h: commodity avg `-0.0427` n `13`; crypto_alt avg `-0.0581` n `239`; crypto_major avg `-0.7352` n `8`; equity avg `-0.1785` n `166`; fx avg `0.003` n `6`; index avg `-0.0146` n `27`; metal avg `-0.0492` n `20`; unknown avg `0.336` n `1223`
- 24h: commodity avg `-0.0318` n `13`; crypto_alt avg `0.7128` n `239`; crypto_major avg `1.2954` n `8`; equity avg `0.5127` n `166`; fx avg `0.0725` n `6`; index avg `0.0987` n `27`; metal avg `-0.0015` n `20`; unknown avg `236.1465` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
