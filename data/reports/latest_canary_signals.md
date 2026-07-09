# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T11:38:42.119303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `12`; crypto_alt avg `0.0167` n `229`; crypto_major avg `0.012` n `8`; equity avg `0.2148` n `91`; fx avg `0.0015` n `6`; index avg `0.0508` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.0161` n `764`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `-0.0727` n `229`; crypto_major avg `-0.3116` n `8`; equity avg `0.0559` n `91`; fx avg `-0.0005` n `6`; index avg `0.0408` n `25`; metal avg `0.0191` n `20`; unknown avg `0.0138` n `764`
- 4h: commodity avg `0.1931` n `12`; crypto_alt avg `-0.1512` n `229`; crypto_major avg `-0.509` n `8`; equity avg `0.0568` n `91`; fx avg `0.0028` n `6`; index avg `0.0188` n `25`; metal avg `-0.0415` n `20`; unknown avg `0.0224` n `764`
- 24h: commodity avg `-0.3931` n `12`; crypto_alt avg `1.3336` n `229`; crypto_major avg `0.3484` n `8`; equity avg `3.4426` n `91`; fx avg `0.1396` n `6`; index avg `0.5342` n `25`; metal avg `0.7555` n `20`; unknown avg `0.7473` n `741`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
