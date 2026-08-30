# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T15:22:27.229066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.1237` n `231`; crypto_major avg `-0.0603` n `8`; equity avg `-0.0157` n `128`; fx avg `0.0027` n `6`; index avg `-0.0095` n `26`; metal avg `-0.019` n `20`; unknown avg `0.1589` n `793`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1803` n `231`; crypto_major avg `-0.1782` n `8`; equity avg `-0.0312` n `128`; fx avg `0.0085` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0366` n `20`; unknown avg `-0.077` n `793`
- 4h: commodity avg `0.0188` n `12`; crypto_alt avg `0.3408` n `231`; crypto_major avg `0.5723` n `8`; equity avg `-0.0152` n `128`; fx avg `0.0009` n `6`; index avg `-0.0062` n `26`; metal avg `0.0407` n `20`; unknown avg `0.0292` n `793`
- 24h: commodity avg `0.0012` n `12`; crypto_alt avg `1.0072` n `231`; crypto_major avg `0.7722` n `8`; equity avg `0.284` n `128`; fx avg `0.0169` n `6`; index avg `0.0645` n `26`; metal avg `0.0898` n `20`; unknown avg `-0.351` n `740`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
