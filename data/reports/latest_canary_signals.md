# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T19:07:26.200622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0986` n `231`; crypto_major avg `-0.0833` n `8`; equity avg `-0.0134` n `128`; fx avg `-0.0069` n `6`; index avg `-0.0024` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.0041` n `793`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `0.2975` n `231`; crypto_major avg `0.238` n `8`; equity avg `0.0045` n `128`; fx avg `-0.0027` n `6`; index avg `-0.004` n `26`; metal avg `0.0072` n `20`; unknown avg `0.0513` n `793`
- 4h: commodity avg `0.0782` n `12`; crypto_alt avg `0.6475` n `231`; crypto_major avg `0.5309` n `8`; equity avg `0.1019` n `128`; fx avg `0.0049` n `6`; index avg `0.0106` n `26`; metal avg `0.0416` n `20`; unknown avg `0.6975` n `793`
- 24h: commodity avg `0.049` n `12`; crypto_alt avg `1.7121` n `231`; crypto_major avg `1.0814` n `8`; equity avg `0.3435` n `128`; fx avg `0.0341` n `6`; index avg `0.074` n `26`; metal avg `0.1071` n `20`; unknown avg `0.0283` n `740`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
