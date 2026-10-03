# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T16:37:32.771544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `13`; crypto_alt avg `0.1423` n `235`; crypto_major avg `0.0949` n `8`; equity avg `0.001` n `143`; fx avg `0.0025` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.1371` n `1078`
- 1h: commodity avg `-0.1449` n `13`; crypto_alt avg `0.2752` n `235`; crypto_major avg `0.0691` n `8`; equity avg `0.0288` n `143`; fx avg `0.005` n `6`; index avg `0.0089` n `26`; metal avg `0.0088` n `20`; unknown avg `-0.0512` n `1070`
- 4h: commodity avg `0.0586` n `13`; crypto_alt avg `1.0125` n `235`; crypto_major avg `0.365` n `8`; equity avg `0.0467` n `143`; fx avg `-0.0003` n `6`; index avg `0.0237` n `26`; metal avg `0.0033` n `20`; unknown avg `0.0068` n `950`
- 24h: commodity avg `0.4194` n `13`; crypto_alt avg `-0.7684` n `235`; crypto_major avg `-0.514` n `8`; equity avg `0.043` n `143`; fx avg `-0.0229` n `6`; index avg `0.0363` n `26`; metal avg `0.1037` n `20`; unknown avg `0.0896` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
