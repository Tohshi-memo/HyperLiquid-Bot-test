# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T14:07:23.070550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2417` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.5538` n `239`; crypto_major avg `-0.5173` n `8`; equity avg `-0.1247` n `162`; fx avg `-0.0065` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0281` n `20`; unknown avg `158.9155` n `1256`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `-0.6455` n `239`; crypto_major avg `-0.5321` n `8`; equity avg `-0.1293` n `162`; fx avg `0.0024` n `6`; index avg `-0.0082` n `27`; metal avg `-0.0145` n `20`; unknown avg `158.5303` n `1260`
- 4h: commodity avg `-0.0189` n `13`; crypto_alt avg `-1.5452` n `239`; crypto_major avg `-1.2655` n `8`; equity avg `-0.3016` n `162`; fx avg `0.0098` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0367` n `20`; unknown avg `80.6231` n `1238`
- 24h: commodity avg `-0.2282` n `13`; crypto_alt avg `-5.1807` n `239`; crypto_major avg `-5.0782` n `8`; equity avg `-3.2746` n `162`; fx avg `-0.1161` n `6`; index avg `-0.2572` n `27`; metal avg `-0.3174` n `20`; unknown avg `0.7892` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
