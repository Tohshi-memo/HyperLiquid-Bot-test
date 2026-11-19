# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T08:07:37.535667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.02` n `13`; crypto_alt avg `-0.0448` n `239`; crypto_major avg `0.0222` n `8`; equity avg `-0.0152` n `164`; fx avg `0.0127` n `6`; index avg `-0.0023` n `27`; metal avg `0.0061` n `20`; unknown avg `0.152` n `1236`
- 1h: commodity avg `-0.0598` n `13`; crypto_alt avg `-0.1659` n `239`; crypto_major avg `-0.2392` n `8`; equity avg `-0.0826` n `164`; fx avg `0.0496` n `6`; index avg `0.0053` n `27`; metal avg `-0.1149` n `20`; unknown avg `2.3262` n `1226`
- 4h: commodity avg `-0.0188` n `13`; crypto_alt avg `-0.2294` n `239`; crypto_major avg `0.4512` n `8`; equity avg `0.5983` n `164`; fx avg `0.065` n `6`; index avg `0.1097` n `27`; metal avg `0.0336` n `20`; unknown avg `2.4041` n `1204`
- 24h: commodity avg `0.179` n `13`; crypto_alt avg `-0.1443` n `239`; crypto_major avg `-0.8504` n `8`; equity avg `0.0067` n `164`; fx avg `0.0116` n `6`; index avg `0.1496` n `27`; metal avg `-0.2513` n `20`; unknown avg `4.304` n `1101`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
