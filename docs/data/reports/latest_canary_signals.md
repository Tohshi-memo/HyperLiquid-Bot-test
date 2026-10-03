# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T17:54:36.112823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.083` n `13`; crypto_alt avg `-0.0508` n `235`; crypto_major avg `0.0457` n `8`; equity avg `0.0027` n `143`; fx avg `-0.0044` n `6`; index avg `0.0076` n `26`; metal avg `0.0022` n `20`; unknown avg `0.6526` n `1078`
- 1h: commodity avg `-0.1119` n `13`; crypto_alt avg `0.1917` n `235`; crypto_major avg `0.2777` n `8`; equity avg `0.0322` n `143`; fx avg `-0.0112` n `6`; index avg `0.0102` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.326` n `1076`
- 4h: commodity avg `0.021` n `13`; crypto_alt avg `0.7316` n `235`; crypto_major avg `0.5718` n `8`; equity avg `0.0947` n `143`; fx avg `-0.0131` n `6`; index avg `0.0243` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.2689` n `964`
- 24h: commodity avg `0.222` n `13`; crypto_alt avg `0.1595` n `235`; crypto_major avg `0.0701` n `8`; equity avg `0.1383` n `143`; fx avg `-0.052` n `6`; index avg `0.0582` n `26`; metal avg `0.0836` n `20`; unknown avg `0.0349` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
