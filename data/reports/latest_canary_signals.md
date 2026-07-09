# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T01:22:29.594856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0986` n `12`; crypto_alt avg `0.5429` n `229`; crypto_major avg `0.3253` n `8`; equity avg `0.1464` n `91`; fx avg `0.0112` n `6`; index avg `0.034` n `25`; metal avg `0.0483` n `20`; unknown avg `0.2404` n `764`
- 1h: commodity avg `0.0908` n `12`; crypto_alt avg `0.5227` n `229`; crypto_major avg `0.6172` n `8`; equity avg `0.1913` n `91`; fx avg `0.0368` n `6`; index avg `0.0259` n `25`; metal avg `-0.0713` n `20`; unknown avg `0.4722` n `764`
- 4h: commodity avg `-0.0812` n `12`; crypto_alt avg `1.2199` n `229`; crypto_major avg `1.0266` n `8`; equity avg `0.8518` n `91`; fx avg `-0.0013` n `6`; index avg `0.1217` n `25`; metal avg `0.0054` n `20`; unknown avg `0.9244` n `764`
- 24h: commodity avg `0.5167` n `12`; crypto_alt avg `-1.0645` n `229`; crypto_major avg `-1.5328` n `8`; equity avg `1.0626` n `91`; fx avg `-0.0326` n `6`; index avg `-0.0697` n `25`; metal avg `-0.7716` n `20`; unknown avg `0.0037` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
