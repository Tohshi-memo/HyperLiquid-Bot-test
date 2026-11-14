# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T14:22:36.452953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2265` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `-0.2038` n `239`; crypto_major avg `-0.0824` n `8`; equity avg `0.0501` n `162`; fx avg `0.0047` n `6`; index avg `0.0043` n `27`; metal avg `0.0052` n `20`; unknown avg `0.1918` n `1260`
- 1h: commodity avg `0.0219` n `13`; crypto_alt avg `-0.8818` n `239`; crypto_major avg `-0.5511` n `8`; equity avg `-0.081` n `162`; fx avg `0.0026` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0006` n `20`; unknown avg `158.4266` n `1260`
- 4h: commodity avg `-0.0141` n `13`; crypto_alt avg `-1.4013` n `239`; crypto_major avg `-1.24` n `8`; equity avg `-0.2407` n `162`; fx avg `0.0176` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0256` n `20`; unknown avg `80.9765` n `1246`
- 24h: commodity avg `-0.1999` n `13`; crypto_alt avg `-5.4606` n `239`; crypto_major avg `-5.1949` n `8`; equity avg `-3.3533` n `162`; fx avg `-0.1108` n `6`; index avg `-0.2623` n `27`; metal avg `-0.2536` n `20`; unknown avg `0.8466` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
