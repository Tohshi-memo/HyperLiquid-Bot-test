# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T20:52:28.244089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.054` n `230`; crypto_major avg `-0.0788` n `8`; equity avg `-0.0001` n `113`; fx avg `-0.0083` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0425` n `785`
- 1h: commodity avg `-0.0661` n `12`; crypto_alt avg `0.2065` n `230`; crypto_major avg `0.3393` n `8`; equity avg `0.4088` n `113`; fx avg `-0.017` n `6`; index avg `0.0371` n `25`; metal avg `0.0054` n `20`; unknown avg `0.1651` n `785`
- 4h: commodity avg `0.0348` n `12`; crypto_alt avg `0.358` n `230`; crypto_major avg `0.8048` n `8`; equity avg `0.5237` n `113`; fx avg `-0.0008` n `6`; index avg `0.011` n `25`; metal avg `-0.0348` n `20`; unknown avg `0.4483` n `785`
- 24h: commodity avg `0.0787` n `12`; crypto_alt avg `-1.5628` n `230`; crypto_major avg `0.087` n `8`; equity avg `1.0262` n `113`; fx avg `-0.0723` n `6`; index avg `0.112` n `25`; metal avg `-0.212` n `20`; unknown avg `-0.289` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2168`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.21`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
