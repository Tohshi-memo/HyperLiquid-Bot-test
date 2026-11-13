# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T22:52:30.114847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0008` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.1168` n `239`; crypto_major avg `0.1169` n `8`; equity avg `-0.0701` n `162`; fx avg `-0.0048` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0045` n `20`; unknown avg `-0.0747` n `1214`
- 1h: commodity avg `-0.0899` n `13`; crypto_alt avg `-0.2269` n `239`; crypto_major avg `-0.2292` n `8`; equity avg `-0.272` n `162`; fx avg `-0.0044` n `6`; index avg `-0.0343` n `27`; metal avg `0.0067` n `20`; unknown avg `0.1809` n `1204`
- 4h: commodity avg `-0.0249` n `13`; crypto_alt avg `-0.9643` n `239`; crypto_major avg `-1.0207` n `8`; equity avg `-0.614` n `162`; fx avg `-0.0124` n `6`; index avg `-0.0199` n `27`; metal avg `-0.0766` n `20`; unknown avg `2.0369` n `1160`
- 24h: commodity avg `-0.3194` n `13`; crypto_alt avg `-1.4024` n `239`; crypto_major avg `-2.5473` n `8`; equity avg `-3.2887` n `162`; fx avg `-0.0693` n `6`; index avg `-0.2359` n `27`; metal avg `-0.3063` n `20`; unknown avg `59.052` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
