# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T07:22:33.104075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2603` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `0.082` n `239`; crypto_major avg `0.1873` n `8`; equity avg `0.0478` n `162`; fx avg `-0.0043` n `6`; index avg `0.0025` n `27`; metal avg `0.0236` n `20`; unknown avg `0.1701` n `1261`
- 1h: commodity avg `-0.0116` n `13`; crypto_alt avg `-0.1169` n `239`; crypto_major avg `-0.0434` n `8`; equity avg `0.0509` n `162`; fx avg `-0.0082` n `6`; index avg `0.0009` n `27`; metal avg `0.0814` n `20`; unknown avg `0.163` n `1259`
- 4h: commodity avg `0.0184` n `13`; crypto_alt avg `-0.7184` n `239`; crypto_major avg `-1.2879` n `8`; equity avg `-0.2368` n `162`; fx avg `0.0072` n `6`; index avg `-0.0276` n `27`; metal avg `-0.0125` n `20`; unknown avg `0.6533` n `1227`
- 24h: commodity avg `0.0236` n `13`; crypto_alt avg `-4.8265` n `239`; crypto_major avg `-4.4395` n `8`; equity avg `-0.9027` n `162`; fx avg `0.0426` n `6`; index avg `-0.094` n `27`; metal avg `-0.4063` n `20`; unknown avg `46.8308` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
