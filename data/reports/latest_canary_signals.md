# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T23:07:24.195068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6081` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5687` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0169` n `13`; crypto_alt avg `-0.36` n `239`; crypto_major avg `-0.4872` n `8`; equity avg `-0.1302` n `162`; fx avg `0.0117` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0145` n `20`; unknown avg `0.2278` n `1254`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.2884` n `239`; crypto_major avg `-0.2982` n `8`; equity avg `-0.3081` n `162`; fx avg `0.0141` n `6`; index avg `-0.0292` n `27`; metal avg `-0.0215` n `20`; unknown avg `-0.2459` n `1210`
- 4h: commodity avg `0.0886` n `13`; crypto_alt avg `-1.3753` n `239`; crypto_major avg `-1.6576` n `8`; equity avg `-0.9161` n `162`; fx avg `-0.0034` n `6`; index avg `-0.0495` n `27`; metal avg `-0.0889` n `20`; unknown avg `3.3821` n `1164`
- 24h: commodity avg `-0.3236` n `13`; crypto_alt avg `-1.8582` n `239`; crypto_major avg `-3.2692` n `8`; equity avg `-3.6597` n `162`; fx avg `-0.0676` n `6`; index avg `-0.2907` n `27`; metal avg `-0.3376` n `20`; unknown avg `59.2421` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
