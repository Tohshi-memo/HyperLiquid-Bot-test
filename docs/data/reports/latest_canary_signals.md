# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T07:52:29.061899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `0.0567` n `228`; crypto_major avg `0.0952` n `8`; equity avg `0.0334` n `88`; fx avg `-0.0548` n `6`; index avg `0.0041` n `23`; metal avg `0.0021` n `20`; unknown avg `-0.018` n `764`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `0.0386` n `228`; crypto_major avg `0.0839` n `8`; equity avg `0.0287` n `88`; fx avg `-0.025` n `6`; index avg `-0.0018` n `23`; metal avg `-0.0275` n `20`; unknown avg `-0.0864` n `748`
- 4h: commodity avg `0.0341` n `12`; crypto_alt avg `0.0071` n `228`; crypto_major avg `-0.0192` n `8`; equity avg `0.1828` n `88`; fx avg `-0.0215` n `6`; index avg `0.0179` n `23`; metal avg `-0.016` n `20`; unknown avg `-0.2947` n `716`
- 24h: commodity avg `0.0052` n `12`; crypto_alt avg `0.823` n `228`; crypto_major avg `0.259` n `8`; equity avg `1.3645` n `87`; fx avg `0.0197` n `6`; index avg `0.0032` n `23`; metal avg `0.6553` n `20`; unknown avg `-0.2501` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
