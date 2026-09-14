# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T06:37:29.802275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.2208` n `233`; crypto_major avg `-0.2618` n `8`; equity avg `-0.0204` n `136`; fx avg `0.0177` n `6`; index avg `-0.0322` n `27`; metal avg `-0.0` n `20`; unknown avg `0.2285` n `884`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0653` n `233`; crypto_major avg `-0.0466` n `8`; equity avg `-0.009` n `136`; fx avg `0.0195` n `6`; index avg `-0.0216` n `27`; metal avg `-0.0245` n `20`; unknown avg `-0.0484` n `840`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `0.174` n `233`; crypto_major avg `0.3901` n `8`; equity avg `-0.2971` n `136`; fx avg `-0.0075` n `6`; index avg `-0.0823` n `27`; metal avg `-0.1245` n `20`; unknown avg `0.14` n `828`
- 24h: commodity avg `0.5273` n `12`; crypto_alt avg `-0.461` n `233`; crypto_major avg `0.1551` n `8`; equity avg `-1.2518` n `136`; fx avg `0.068` n `6`; index avg `-0.3026` n `26`; metal avg `-0.1539` n `20`; unknown avg `1.0983` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
