# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T21:37:39.630582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.1062` n `230`; crypto_major avg `0.0587` n `8`; equity avg `-0.0426` n `113`; fx avg `-0.0002` n `6`; index avg `0.0203` n `25`; metal avg `0.0069` n `20`; unknown avg `0.0731` n `786`
- 1h: commodity avg `-0.0347` n `12`; crypto_alt avg `0.0422` n `230`; crypto_major avg `0.113` n `8`; equity avg `0.0365` n `113`; fx avg `-0.0028` n `6`; index avg `0.0055` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.0391` n `785`
- 4h: commodity avg `-0.0583` n `12`; crypto_alt avg `0.4364` n `230`; crypto_major avg `0.7988` n `8`; equity avg `0.6192` n `113`; fx avg `0.0025` n `6`; index avg `0.0422` n `25`; metal avg `-0.009` n `20`; unknown avg `0.6139` n `785`
- 24h: commodity avg `0.0535` n `12`; crypto_alt avg `-1.2486` n `230`; crypto_major avg `0.3414` n `8`; equity avg `1.1688` n `113`; fx avg `-0.0606` n `6`; index avg `0.1261` n `25`; metal avg `-0.2469` n `20`; unknown avg `-0.1995` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
