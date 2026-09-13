# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T04:40:30.318170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.0082` n `233`; crypto_major avg `-0.0328` n `8`; equity avg `-0.0127` n `136`; fx avg `0.0033` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0057` n `20`; unknown avg `50.6464` n `832`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `0.0048` n `233`; crypto_major avg `-0.0841` n `8`; equity avg `-0.036` n `136`; fx avg `-0.0082` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0033` n `20`; unknown avg `50.828` n `830`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.2042` n `233`; crypto_major avg `-0.1436` n `8`; equity avg `-0.1727` n `136`; fx avg `0.0086` n `6`; index avg `-0.0342` n `26`; metal avg `-0.0021` n `20`; unknown avg `2.8706` n `806`
- 24h: commodity avg `0.0625` n `12`; crypto_alt avg `0.9075` n `233`; crypto_major avg `-0.1089` n `8`; equity avg `-0.5146` n `136`; fx avg `-0.0034` n `6`; index avg `-0.0626` n `26`; metal avg `0.0308` n `20`; unknown avg `-0.1947` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
