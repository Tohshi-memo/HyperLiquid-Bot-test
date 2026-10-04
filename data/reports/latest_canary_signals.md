# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T13:37:30.767854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `-0.1093` n `235`; crypto_major avg `0.0966` n `8`; equity avg `0.0119` n `144`; fx avg `0.001` n `6`; index avg `0.0027` n `26`; metal avg `0.0052` n `20`; unknown avg `0.1915` n `1078`
- 1h: commodity avg `0.0314` n `13`; crypto_alt avg `0.0581` n `235`; crypto_major avg `0.0639` n `8`; equity avg `0.0079` n `144`; fx avg `-0.0021` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.4263` n `1076`
- 4h: commodity avg `0.0499` n `13`; crypto_alt avg `-0.1509` n `235`; crypto_major avg `0.0977` n `8`; equity avg `0.0414` n `144`; fx avg `0.0238` n `6`; index avg `0.0031` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.056` n `1070`
- 24h: commodity avg `0.14` n `13`; crypto_alt avg `1.5274` n `235`; crypto_major avg `1.2253` n `8`; equity avg `0.2711` n `144`; fx avg `0.0076` n `6`; index avg `0.0306` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0291` n `901`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
