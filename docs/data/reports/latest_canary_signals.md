# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T05:52:30.249114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.716` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6691` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5885` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0075` n `13`; crypto_alt avg `0.2487` n `239`; crypto_major avg `0.1367` n `8`; equity avg `0.0413` n `162`; fx avg `0.0032` n `6`; index avg `0.0013` n `27`; metal avg `0.0007` n `20`; unknown avg `0.2433` n `1262`
- 1h: commodity avg `-0.0027` n `13`; crypto_alt avg `0.2569` n `239`; crypto_major avg `0.1143` n `8`; equity avg `0.1154` n `162`; fx avg `0.005` n `6`; index avg `0.0114` n `27`; metal avg `0.0072` n `20`; unknown avg `11.0506` n `1258`
- 4h: commodity avg `-0.0483` n `13`; crypto_alt avg `-0.8488` n `239`; crypto_major avg `-1.7395` n `8`; equity avg `-0.151` n `162`; fx avg `-0.0082` n `6`; index avg `-0.0235` n `27`; metal avg `-0.0704` n `20`; unknown avg `7.6666` n `1242`
- 24h: commodity avg `-0.0984` n `13`; crypto_alt avg `-0.462` n `239`; crypto_major avg `-2.0156` n `8`; equity avg `-2.3586` n `162`; fx avg `-0.0961` n `6`; index avg `-0.1931` n `27`; metal avg `-0.4142` n `20`; unknown avg `60.0549` n `1024`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
