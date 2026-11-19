# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T09:07:35.474420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `0.0792` n `239`; crypto_major avg `0.1798` n `8`; equity avg `0.1317` n `164`; fx avg `0.0314` n `6`; index avg `0.0118` n `27`; metal avg `0.0104` n `20`; unknown avg `272.8837` n `1258`
- 1h: commodity avg `0.0036` n `13`; crypto_alt avg `0.3432` n `239`; crypto_major avg `0.2217` n `8`; equity avg `0.2943` n `164`; fx avg `0.0347` n `6`; index avg `0.0424` n `27`; metal avg `0.0643` n `20`; unknown avg `382.9883` n `1258`
- 4h: commodity avg `-0.0726` n `13`; crypto_alt avg `0.482` n `239`; crypto_major avg `0.5456` n `8`; equity avg `1.1711` n `164`; fx avg `0.0745` n `6`; index avg `0.19` n `27`; metal avg `0.0198` n `20`; unknown avg `400.9898` n `1204`
- 24h: commodity avg `0.2101` n `13`; crypto_alt avg `0.2032` n `239`; crypto_major avg `-0.5342` n `8`; equity avg `0.1051` n `164`; fx avg `0.0953` n `6`; index avg `0.1615` n `27`; metal avg `-0.124` n `20`; unknown avg `3.532` n `1163`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
