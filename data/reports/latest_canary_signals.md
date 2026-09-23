# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T05:07:32.570111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0778` n `12`; crypto_alt avg `-0.1121` n `234`; crypto_major avg `-0.4005` n `8`; equity avg `-0.0998` n `140`; fx avg `0.0085` n `6`; index avg `-0.0094` n `26`; metal avg `0.0026` n `20`; unknown avg `1.5118` n `943`
- 1h: commodity avg `0.0352` n `12`; crypto_alt avg `0.0289` n `234`; crypto_major avg `0.0505` n `8`; equity avg `0.0474` n `140`; fx avg `-0.0182` n `6`; index avg `0.0074` n `26`; metal avg `0.0141` n `20`; unknown avg `1.048` n `943`
- 4h: commodity avg `-0.17` n `12`; crypto_alt avg `0.6895` n `234`; crypto_major avg `0.5394` n `8`; equity avg `-0.0898` n `140`; fx avg `-0.0549` n `6`; index avg `-0.0181` n `26`; metal avg `-0.1097` n `20`; unknown avg `0.5163` n `937`
- 24h: commodity avg `-0.1701` n `12`; crypto_alt avg `4.0778` n `234`; crypto_major avg `2.6019` n `8`; equity avg `1.0192` n `140`; fx avg `-0.167` n `6`; index avg `0.0933` n `26`; metal avg `0.1272` n `20`; unknown avg `2.3529` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
