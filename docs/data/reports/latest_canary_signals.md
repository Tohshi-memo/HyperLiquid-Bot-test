# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T14:52:28.201622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2042` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.3703` n `230`; crypto_major avg `-0.2477` n `8`; equity avg `-0.0348` n `121`; fx avg `-0.0017` n `6`; index avg `0.0031` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0388` n `794`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `-1.0886` n `230`; crypto_major avg `-1.2062` n `8`; equity avg `-0.0579` n `121`; fx avg `-0.0174` n `6`; index avg `-0.002` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.1267` n `794`
- 4h: commodity avg `-0.058` n `12`; crypto_alt avg `-0.2563` n `230`; crypto_major avg `-0.203` n `8`; equity avg `-0.0015` n `121`; fx avg `-0.0222` n `6`; index avg `0.0083` n `25`; metal avg `0.0252` n `20`; unknown avg `0.2067` n `794`
- 24h: commodity avg `-0.0558` n `12`; crypto_alt avg `-0.3776` n `230`; crypto_major avg `1.7325` n `8`; equity avg `-0.3185` n `121`; fx avg `0.0547` n `6`; index avg `-0.0194` n `25`; metal avg `-0.0056` n `20`; unknown avg `1.1944` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
