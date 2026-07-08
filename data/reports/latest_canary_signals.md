# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T20:17:55.100746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0641` n `12`; crypto_alt avg `-0.1497` n `229`; crypto_major avg `-0.1731` n `8`; equity avg `-0.1322` n `91`; fx avg `0.015` n `6`; index avg `-0.0306` n `25`; metal avg `-0.0416` n `20`; unknown avg `-0.0656` n `764`
- 1h: commodity avg `0.227` n `12`; crypto_alt avg `-0.0509` n `229`; crypto_major avg `0.0589` n `8`; equity avg `0.2105` n `91`; fx avg `0.0121` n `6`; index avg `-0.0055` n `25`; metal avg `-0.1093` n `20`; unknown avg `-0.085` n `764`
- 4h: commodity avg `-0.1692` n `12`; crypto_alt avg `0.3324` n `229`; crypto_major avg `0.3539` n `8`; equity avg `0.9203` n `91`; fx avg `-0.0073` n `6`; index avg `0.123` n `25`; metal avg `0.3463` n `20`; unknown avg `1.3189` n `764`
- 24h: commodity avg `0.5027` n `12`; crypto_alt avg `-2.3357` n `229`; crypto_major avg `-2.8923` n `8`; equity avg `0.9002` n `91`; fx avg `0.0043` n `6`; index avg `-0.0548` n `25`; metal avg `-0.8381` n `20`; unknown avg `0.0461` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
