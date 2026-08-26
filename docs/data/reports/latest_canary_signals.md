# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T14:37:29.848764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1603` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0699` n `12`; crypto_alt avg `-0.4072` n `231`; crypto_major avg `-0.4652` n `8`; equity avg `0.088` n `122`; fx avg `0.0032` n `6`; index avg `0.01` n `25`; metal avg `-0.083` n `20`; unknown avg `-0.1145` n `797`
- 1h: commodity avg `0.1861` n `12`; crypto_alt avg `-0.251` n `231`; crypto_major avg `-0.4401` n `8`; equity avg `-0.3048` n `122`; fx avg `-0.0083` n `6`; index avg `-0.0489` n `25`; metal avg `-0.0583` n `20`; unknown avg `-0.1299` n `797`
- 4h: commodity avg `0.4168` n `12`; crypto_alt avg `-0.8558` n `231`; crypto_major avg `-1.1755` n `8`; equity avg `-0.3069` n `122`; fx avg `0.0055` n `6`; index avg `-0.0152` n `25`; metal avg `-0.1567` n `20`; unknown avg `-0.1997` n `797`
- 24h: commodity avg `0.1554` n `12`; crypto_alt avg `-1.9411` n `231`; crypto_major avg `-1.8975` n `8`; equity avg `-0.2311` n `122`; fx avg `-0.0502` n `6`; index avg `0.0343` n `25`; metal avg `-0.0519` n `20`; unknown avg `0.4293` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
