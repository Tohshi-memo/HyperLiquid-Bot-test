# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T13:37:29.674073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6629` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5414` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5308` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.2943` n `228`; crypto_major avg `-0.3512` n `8`; equity avg `0.3459` n `88`; fx avg `0.0026` n `6`; index avg `0.0647` n `23`; metal avg `-0.1075` n `20`; unknown avg `-0.0332` n `765`
- 1h: commodity avg `-0.1559` n `12`; crypto_alt avg `-0.1972` n `228`; crypto_major avg `-0.3116` n `8`; equity avg `0.2429` n `88`; fx avg `0.0302` n `6`; index avg `0.0717` n `23`; metal avg `-0.0028` n `20`; unknown avg `-0.0322` n `765`
- 4h: commodity avg `0.1581` n `12`; crypto_alt avg `-1.5488` n `228`; crypto_major avg `-1.5418` n `8`; equity avg `-0.0004` n `88`; fx avg `0.0048` n `6`; index avg `0.1211` n `23`; metal avg `-0.011` n `20`; unknown avg `-0.1153` n `765`
- 24h: commodity avg `0.3571` n `12`; crypto_alt avg `-2.3028` n `228`; crypto_major avg `-1.6196` n `8`; equity avg `1.3574` n `88`; fx avg `0.0884` n `6`; index avg `0.2728` n `23`; metal avg `0.0607` n `20`; unknown avg `8.3621` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
