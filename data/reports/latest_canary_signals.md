# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T05:52:27.874503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.1164` n `230`; crypto_major avg `-0.1241` n `8`; equity avg `-0.0288` n `96`; fx avg `-0.0051` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.1999` n `769`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `-0.1525` n `230`; crypto_major avg `-0.1158` n `8`; equity avg `0.0003` n `96`; fx avg `-0.0088` n `6`; index avg `0.0004` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.223` n `769`
- 4h: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.4137` n `230`; crypto_major avg `-0.2462` n `8`; equity avg `-0.0763` n `96`; fx avg `-0.0081` n `6`; index avg `0.0428` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.4598` n `769`
- 24h: commodity avg `0.8465` n `12`; crypto_alt avg `0.0163` n `230`; crypto_major avg `0.6239` n `8`; equity avg `1.5348` n `96`; fx avg `0.0701` n `6`; index avg `0.2029` n `25`; metal avg `0.2038` n `20`; unknown avg `0.3264` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
