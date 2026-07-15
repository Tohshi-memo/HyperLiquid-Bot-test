# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T13:22:32.691443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0848` n `12`; crypto_alt avg `0.0641` n `230`; crypto_major avg `0.1454` n `8`; equity avg `-0.0669` n `93`; fx avg `0.0035` n `6`; index avg `-0.0291` n `25`; metal avg `-0.069` n `20`; unknown avg `-0.0303` n `768`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `1.1913` n `230`; crypto_major avg `1.5674` n `8`; equity avg `0.3104` n `93`; fx avg `0.008` n `6`; index avg `0.0664` n `25`; metal avg `0.2613` n `20`; unknown avg `0.5891` n `768`
- 4h: commodity avg `-0.0774` n `12`; crypto_alt avg `1.1868` n `230`; crypto_major avg `1.2511` n `8`; equity avg `-0.0536` n `93`; fx avg `0.0192` n `6`; index avg `-0.0296` n `25`; metal avg `0.1585` n `20`; unknown avg `0.2641` n `767`
- 24h: commodity avg `-0.0409` n `12`; crypto_alt avg `1.2398` n `230`; crypto_major avg `2.2387` n `8`; equity avg `0.5619` n `92`; fx avg `0.06` n `6`; index avg `0.1744` n `25`; metal avg `0.0596` n `20`; unknown avg `0.2239` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
