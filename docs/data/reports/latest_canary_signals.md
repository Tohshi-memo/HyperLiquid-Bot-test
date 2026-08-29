# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T18:37:25.031846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `0.052` n `231`; crypto_major avg `0.0816` n `8`; equity avg `0.0155` n `128`; fx avg `-0.0071` n `6`; index avg `0.0043` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.0375` n `792`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.2144` n `231`; crypto_major avg `0.2287` n `8`; equity avg `0.011` n `128`; fx avg `-0.0072` n `6`; index avg `-0.0062` n `26`; metal avg `0.0046` n `20`; unknown avg `-0.0438` n `792`
- 4h: commodity avg `0.0004` n `12`; crypto_alt avg `0.1274` n `231`; crypto_major avg `0.4306` n `8`; equity avg `0.0235` n `128`; fx avg `-0.0059` n `6`; index avg `0.0025` n `26`; metal avg `0.0659` n `20`; unknown avg `-0.1122` n `778`
- 24h: commodity avg `0.0525` n `12`; crypto_alt avg `1.5029` n `231`; crypto_major avg `1.528` n `8`; equity avg `0.241` n `128`; fx avg `-0.0461` n `6`; index avg `0.025` n `26`; metal avg `0.1458` n `20`; unknown avg `0.1321` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
