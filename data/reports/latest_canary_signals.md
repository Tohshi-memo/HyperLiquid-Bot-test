# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T19:07:24.988618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `13`; crypto_alt avg `0.1519` n `235`; crypto_major avg `0.0677` n `8`; equity avg `0.0167` n `150`; fx avg `-0.0075` n `6`; index avg `0.0006` n `26`; metal avg `0.0008` n `20`; unknown avg `0.2396` n `1130`
- 1h: commodity avg `0.0327` n `13`; crypto_alt avg `-0.226` n `235`; crypto_major avg `-0.3909` n `8`; equity avg `-0.052` n `150`; fx avg `0.0013` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.0807` n `1122`
- 4h: commodity avg `0.053` n `13`; crypto_alt avg `0.8924` n `235`; crypto_major avg `0.7161` n `8`; equity avg `0.1872` n `150`; fx avg `-0.0039` n `6`; index avg `0.0298` n `26`; metal avg `0.0426` n `20`; unknown avg `1.9908` n `1092`
- 24h: commodity avg `0.2775` n `13`; crypto_alt avg `1.8909` n `235`; crypto_major avg `0.694` n `8`; equity avg `0.2815` n `150`; fx avg `0.0181` n `6`; index avg `0.0402` n `26`; metal avg `0.0621` n `20`; unknown avg `0.8425` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
