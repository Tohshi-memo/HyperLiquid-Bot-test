# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T02:07:55.161528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `-0.0461` n `230`; crypto_major avg `-0.0085` n `8`; equity avg `0.1354` n `113`; fx avg `0.0119` n `6`; index avg `0.0203` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.2233` n `786`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.0672` n `230`; crypto_major avg `-0.036` n `8`; equity avg `0.2168` n `113`; fx avg `0.0168` n `6`; index avg `0.0171` n `25`; metal avg `-0.1659` n `20`; unknown avg `-0.2834` n `786`
- 4h: commodity avg `-0.129` n `12`; crypto_alt avg `0.4649` n `230`; crypto_major avg `0.1847` n `8`; equity avg `0.5831` n `113`; fx avg `-0.0295` n `6`; index avg `0.0537` n `25`; metal avg `0.0288` n `20`; unknown avg `-0.2407` n `786`
- 24h: commodity avg `-0.237` n `12`; crypto_alt avg `-1.544` n `230`; crypto_major avg `-0.7513` n `8`; equity avg `2.909` n `113`; fx avg `-0.0482` n `6`; index avg `0.3865` n `25`; metal avg `0.034` n `20`; unknown avg `-0.042` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2025`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
