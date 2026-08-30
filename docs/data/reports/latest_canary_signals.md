# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T02:07:29.137161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0292` n `231`; crypto_major avg `-0.0262` n `8`; equity avg `0.012` n `128`; fx avg `-0.0001` n `6`; index avg `0.0093` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.1005` n `793`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.2049` n `231`; crypto_major avg `-0.0373` n `8`; equity avg `0.031` n `128`; fx avg `-0.0011` n `6`; index avg `0.0076` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.1933` n `793`
- 4h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.2489` n `231`; crypto_major avg `-0.0477` n `8`; equity avg `0.029` n `128`; fx avg `0.0153` n `6`; index avg `0.0275` n `26`; metal avg `-0.0047` n `20`; unknown avg `3.9169` n `779`
- 24h: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.0108` n `231`; crypto_major avg `0.6703` n `8`; equity avg `0.3674` n `128`; fx avg `-0.0083` n `6`; index avg `0.092` n `26`; metal avg `0.0987` n `20`; unknown avg `0.0272` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
