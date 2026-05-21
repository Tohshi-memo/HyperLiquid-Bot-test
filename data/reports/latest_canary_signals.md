# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T05:37:17.142183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.101` n `12`; crypto_alt avg `-0.1697` n `228`; crypto_major avg `-0.0181` n `8`; equity avg `-0.0705` n `66`; fx avg `0.0105` n `6`; index avg `-0.0079` n `23`; metal avg `-0.192` n `18`; unknown avg `0.7679` n `384`
- 1h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.3206` n `228`; crypto_major avg `-0.0937` n `8`; equity avg `0.1296` n `66`; fx avg `0.0214` n `6`; index avg `0.0173` n `23`; metal avg `-0.3881` n `18`; unknown avg `0.188` n `384`
- 4h: commodity avg `0.1045` n `12`; crypto_alt avg `-0.1515` n `228`; crypto_major avg `0.1124` n `8`; equity avg `0.3131` n `66`; fx avg `0.0521` n `6`; index avg `0.207` n `23`; metal avg `-1.1397` n `18`; unknown avg `0.5395` n `384`
- 24h: commodity avg `-2.2031` n `12`; crypto_alt avg `2.4444` n `228`; crypto_major avg `3.0493` n `8`; equity avg `2.5316` n `66`; fx avg `0.0618` n `6`; index avg `1.7151` n `23`; metal avg `0.6301` n `18`; unknown avg `5.5325` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
