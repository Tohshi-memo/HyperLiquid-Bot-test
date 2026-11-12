# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T18:22:37.970982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.1057` n `239`; crypto_major avg `-0.0603` n `8`; equity avg `0.0605` n `162`; fx avg `0.0032` n `6`; index avg `0.0052` n `27`; metal avg `-0.006` n `20`; unknown avg `0.2263` n `1259`
- 1h: commodity avg `0.2056` n `13`; crypto_alt avg `0.2187` n `239`; crypto_major avg `0.1858` n `8`; equity avg `0.2884` n `162`; fx avg `-0.0089` n `6`; index avg `0.0222` n `27`; metal avg `0.0381` n `20`; unknown avg `0.4965` n `1253`
- 4h: commodity avg `0.4265` n `13`; crypto_alt avg `0.7012` n `239`; crypto_major avg `0.8944` n `8`; equity avg `2.0871` n `162`; fx avg `-0.0654` n `6`; index avg `0.1989` n `27`; metal avg `-0.1464` n `20`; unknown avg `59.6995` n `1229`
- 24h: commodity avg `0.4933` n `13`; crypto_alt avg `-3.3586` n `239`; crypto_major avg `-3.501` n `8`; equity avg `-3.0378` n `162`; fx avg `-0.1535` n `6`; index avg `-0.1669` n `27`; metal avg `-0.8002` n `20`; unknown avg `17.3009` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
