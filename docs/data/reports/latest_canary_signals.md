# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T05:22:28.084078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6966` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6764` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.53` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `0.4231` n `239`; crypto_major avg `0.3258` n `8`; equity avg `0.0835` n `162`; fx avg `-0.0019` n `6`; index avg `0.0069` n `27`; metal avg `0.0151` n `20`; unknown avg `6.2253` n `1258`
- 1h: commodity avg `-0.0004` n `13`; crypto_alt avg `0.3519` n `239`; crypto_major avg `0.4001` n `8`; equity avg `0.0507` n `162`; fx avg `-0.0027` n `6`; index avg `0.006` n `27`; metal avg `0.0215` n `20`; unknown avg `0.6463` n `1252`
- 4h: commodity avg `-0.0424` n `13`; crypto_alt avg `-1.0872` n `239`; crypto_major avg `-1.7228` n `8`; equity avg `-0.1928` n `162`; fx avg `-0.0072` n `6`; index avg `-0.0262` n `27`; metal avg `-0.0464` n `20`; unknown avg `7.5621` n `1242`
- 24h: commodity avg `-0.1307` n `13`; crypto_alt avg `-0.3709` n `239`; crypto_major avg `-2.0713` n `8`; equity avg `-2.5619` n `162`; fx avg `-0.1047` n `6`; index avg `-0.2026` n `27`; metal avg `-0.5832` n `20`; unknown avg `64.2393` n `1024`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
