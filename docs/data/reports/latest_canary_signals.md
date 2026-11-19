# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T16:22:31.499350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `13`; crypto_alt avg `-0.0053` n `239`; crypto_major avg `0.0329` n `8`; equity avg `0.0781` n `165`; fx avg `-0.0021` n `6`; index avg `0.0013` n `27`; metal avg `0.0417` n `20`; unknown avg `3.4677` n `1263`
- 1h: commodity avg `0.0505` n `13`; crypto_alt avg `-0.7191` n `239`; crypto_major avg `-0.6919` n `8`; equity avg `-0.4051` n `165`; fx avg `0.0433` n `6`; index avg `-0.0745` n `27`; metal avg `-0.1471` n `20`; unknown avg `3.9908` n `1257`
- 4h: commodity avg `0.0192` n `13`; crypto_alt avg `-1.3249` n `239`; crypto_major avg `-1.1056` n `8`; equity avg `-1.4521` n `165`; fx avg `0.0012` n `6`; index avg `-0.2574` n `27`; metal avg `-0.3516` n `20`; unknown avg `1.4254` n `1257`
- 24h: commodity avg `0.2496` n `13`; crypto_alt avg `0.6301` n `239`; crypto_major avg `1.1256` n `8`; equity avg `1.6828` n `165`; fx avg `0.0653` n `6`; index avg `0.2526` n `27`; metal avg `-0.3673` n `20`; unknown avg `3.5701` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
