# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T11:36:39.292846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1537` n `12`; crypto_alt avg `-0.3096` n `230`; crypto_major avg `-0.644` n `8`; equity avg `0.0457` n `121`; fx avg `-0.0116` n `6`; index avg `0.0374` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0621` n `793`
- 1h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.3434` n `230`; crypto_major avg `-0.4945` n `8`; equity avg `0.0454` n `121`; fx avg `-0.0228` n `6`; index avg `0.0539` n `25`; metal avg `0.1197` n `20`; unknown avg `0.2244` n `793`
- 4h: commodity avg `-0.0457` n `12`; crypto_alt avg `1.8471` n `230`; crypto_major avg `0.8654` n `8`; equity avg `0.2298` n `121`; fx avg `-0.0104` n `6`; index avg `0.0208` n `25`; metal avg `0.241` n `20`; unknown avg `0.4344` n `793`
- 24h: commodity avg `-0.0802` n `12`; crypto_alt avg `6.5461` n `230`; crypto_major avg `5.3367` n `8`; equity avg `0.979` n `121`; fx avg `-0.1064` n `6`; index avg `0.1339` n `25`; metal avg `0.9397` n `20`; unknown avg `2.2011` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
