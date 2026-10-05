# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T23:37:29.850957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.052` n `235`; crypto_major avg `-0.1131` n `8`; equity avg `-0.0038` n `144`; fx avg `0.0025` n `6`; index avg `-0.0098` n `26`; metal avg `-0.011` n `20`; unknown avg `0.418` n `1079`
- 1h: commodity avg `-0.0127` n `13`; crypto_alt avg `-0.2287` n `235`; crypto_major avg `-0.2504` n `8`; equity avg `0.0351` n `144`; fx avg `-0.0043` n `6`; index avg `0.0089` n `26`; metal avg `-0.0529` n `20`; unknown avg `0.2265` n `1077`
- 4h: commodity avg `0.0286` n `13`; crypto_alt avg `0.5528` n `235`; crypto_major avg `0.4515` n `8`; equity avg `0.216` n `144`; fx avg `0.0118` n `6`; index avg `0.0031` n `26`; metal avg `-0.0504` n `20`; unknown avg `0.1967` n `979`
- 24h: commodity avg `-0.2148` n `13`; crypto_alt avg `0.2585` n `235`; crypto_major avg `-0.0422` n `8`; equity avg `0.2239` n `144`; fx avg `-0.0641` n `6`; index avg `0.1142` n `26`; metal avg `0.0722` n `20`; unknown avg `630.3283` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
