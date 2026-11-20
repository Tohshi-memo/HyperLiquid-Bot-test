# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T11:52:40.670390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `13`; crypto_alt avg `-0.2701` n `239`; crypto_major avg `-0.2052` n `8`; equity avg `-0.1045` n `165`; fx avg `-0.014` n `6`; index avg `0.0138` n `27`; metal avg `-0.0313` n `20`; unknown avg `0.0843` n `1262`
- 1h: commodity avg `0.2217` n `13`; crypto_alt avg `-0.6895` n `239`; crypto_major avg `-0.7184` n `8`; equity avg `-0.5156` n `165`; fx avg `-0.0009` n `6`; index avg `-0.05` n `27`; metal avg `-0.1029` n `20`; unknown avg `222.3015` n `1258`
- 4h: commodity avg `-0.0845` n `13`; crypto_alt avg `-0.8841` n `239`; crypto_major avg `-1.0052` n `8`; equity avg `-0.9524` n `165`; fx avg `-0.0239` n `6`; index avg `-0.0851` n `27`; metal avg `0.0579` n `20`; unknown avg `45.9431` n `1194`
- 24h: commodity avg `-0.1933` n `13`; crypto_alt avg `-4.2356` n `239`; crypto_major avg `-3.773` n `8`; equity avg `-8.3701` n `165`; fx avg `-0.0752` n `6`; index avg `-0.8455` n `27`; metal avg `-1.2665` n `20`; unknown avg `58.8235` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
