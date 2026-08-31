# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T21:52:24.622813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `0.2033` n `232`; crypto_major avg `0.0464` n `8`; equity avg `0.0576` n `129`; fx avg `0.002` n `6`; index avg `0.0061` n `26`; metal avg `-0.0045` n `20`; unknown avg `0.2545` n `793`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.3821` n `232`; crypto_major avg `0.2273` n `8`; equity avg `0.0799` n `129`; fx avg `0.0156` n `6`; index avg `0.0051` n `26`; metal avg `0.0113` n `20`; unknown avg `0.465` n `785`
- 4h: commodity avg `0.0787` n `12`; crypto_alt avg `0.3349` n `232`; crypto_major avg `0.2101` n `8`; equity avg `0.433` n `129`; fx avg `0.0112` n `6`; index avg `0.0494` n `26`; metal avg `0.0476` n `20`; unknown avg `-0.1524` n `773`
- 24h: commodity avg `0.1723` n `12`; crypto_alt avg `0.1158` n `231`; crypto_major avg `0.2458` n `8`; equity avg `0.1752` n `129`; fx avg `-0.0938` n `6`; index avg `-0.1159` n `26`; metal avg `-0.3596` n `20`; unknown avg `0.0701` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
