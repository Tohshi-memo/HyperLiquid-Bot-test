# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T22:52:37.932062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `0.1159` n `235`; crypto_major avg `-0.0402` n `8`; equity avg `0.0026` n `144`; fx avg `-0.0012` n `6`; index avg `0.0024` n `26`; metal avg `-0.0151` n `20`; unknown avg `-0.1408` n `1079`
- 1h: commodity avg `0.0306` n `13`; crypto_alt avg `0.053` n `235`; crypto_major avg `0.0676` n `8`; equity avg `0.0366` n `144`; fx avg `0.0244` n `6`; index avg `-0.006` n `26`; metal avg `0.017` n `20`; unknown avg `-0.2574` n `1075`
- 4h: commodity avg `0.0583` n `13`; crypto_alt avg `1.0037` n `235`; crypto_major avg `0.6519` n `8`; equity avg `0.2381` n `144`; fx avg `0.0232` n `6`; index avg `0.0117` n `26`; metal avg `-0.0124` n `20`; unknown avg `-0.1997` n `979`
- 24h: commodity avg `-0.1959` n `13`; crypto_alt avg `0.7227` n `235`; crypto_major avg `0.1437` n `8`; equity avg `0.2626` n `144`; fx avg `-0.0807` n `6`; index avg `0.1081` n `26`; metal avg `0.111` n `20`; unknown avg `630.2844` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
