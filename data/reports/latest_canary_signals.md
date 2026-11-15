# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T22:37:27.555510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `13`; crypto_alt avg `0.1425` n `239`; crypto_major avg `0.0627` n `8`; equity avg `0.0102` n `162`; fx avg `-0.0034` n `6`; index avg `-0.0014` n `27`; metal avg `0.0047` n `20`; unknown avg `-0.0052` n `1263`
- 1h: commodity avg `-0.0485` n `13`; crypto_alt avg `0.5378` n `239`; crypto_major avg `0.4707` n `8`; equity avg `0.047` n `162`; fx avg `-0.02` n `6`; index avg `-0.0042` n `27`; metal avg `0.0194` n `20`; unknown avg `-0.3405` n `1243`
- 4h: commodity avg `-0.0187` n `13`; crypto_alt avg `1.0226` n `239`; crypto_major avg `1.181` n `8`; equity avg `0.6451` n `162`; fx avg `0.0178` n `6`; index avg `0.0571` n `27`; metal avg `0.0721` n `20`; unknown avg `1.1065` n `1215`
- 24h: commodity avg `-0.062` n `13`; crypto_alt avg `3.8019` n `239`; crypto_major avg `4.6831` n `8`; equity avg `1.3397` n `162`; fx avg `0.0193` n `6`; index avg `0.1022` n `27`; metal avg `0.2653` n `20`; unknown avg `1.9832` n `1140`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
