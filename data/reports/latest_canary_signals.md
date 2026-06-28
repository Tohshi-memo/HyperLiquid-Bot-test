# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T00:52:34.978916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0972` n `12`; crypto_alt avg `-0.0343` n `228`; crypto_major avg `-0.0203` n `8`; equity avg `-0.0369` n `88`; fx avg `-0.0021` n `6`; index avg `-0.0167` n `23`; metal avg `-0.0097` n `20`; unknown avg `-0.1651` n `764`
- 1h: commodity avg `0.1466` n `12`; crypto_alt avg `0.1611` n `228`; crypto_major avg `0.071` n `8`; equity avg `0.0031` n `88`; fx avg `-0.0173` n `6`; index avg `-0.0085` n `23`; metal avg `0.0247` n `20`; unknown avg `-0.3747` n `764`
- 4h: commodity avg `0.2854` n `12`; crypto_alt avg `-0.137` n `228`; crypto_major avg `-0.46` n `8`; equity avg `-0.0537` n `88`; fx avg `-0.0213` n `6`; index avg `-0.082` n `23`; metal avg `0.0195` n `20`; unknown avg `-0.5544` n `764`
- 24h: commodity avg `0.2951` n `12`; crypto_alt avg `-0.6324` n `228`; crypto_major avg `-0.9303` n `8`; equity avg `0.3303` n `88`; fx avg `0.0032` n `6`; index avg `-0.0799` n `23`; metal avg `-0.0394` n `20`; unknown avg `-0.6595` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
