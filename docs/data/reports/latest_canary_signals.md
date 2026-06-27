# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T20:35:09.751645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4093` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0168` n `228`; crypto_major avg `-0.0332` n `8`; equity avg `0.0213` n `88`; fx avg `-0.0105` n `6`; index avg `0.006` n `23`; metal avg `0.0003` n `20`; unknown avg `-0.0991` n `764`
- 1h: commodity avg `0.0441` n `12`; crypto_alt avg `0.5631` n `228`; crypto_major avg `0.2523` n `8`; equity avg `0.0702` n `88`; fx avg `-0.0055` n `6`; index avg `0.0311` n `23`; metal avg `0.0123` n `20`; unknown avg `-0.0773` n `764`
- 4h: commodity avg `-0.01` n `12`; crypto_alt avg `-1.2223` n `228`; crypto_major avg `-1.4135` n `8`; equity avg `-0.1147` n `88`; fx avg `-0.0065` n `6`; index avg `-0.0042` n `23`; metal avg `-0.0572` n `20`; unknown avg `0.2728` n `764`
- 24h: commodity avg `0.1201` n `12`; crypto_alt avg `-0.2402` n `228`; crypto_major avg `-0.4004` n `8`; equity avg `0.5886` n `88`; fx avg `0.0777` n `6`; index avg `0.0348` n `23`; metal avg `0.1462` n `20`; unknown avg `-0.4384` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
