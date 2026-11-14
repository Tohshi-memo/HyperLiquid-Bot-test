# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T15:07:24.968917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8542` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7989` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `0.205` n `239`; crypto_major avg `0.3125` n `8`; equity avg `0.1181` n `162`; fx avg `-0.0036` n `6`; index avg `0.0153` n `27`; metal avg `-0.005` n `20`; unknown avg `1.0347` n `1256`
- 1h: commodity avg `-0.0424` n `13`; crypto_alt avg `-0.9181` n `239`; crypto_major avg `-0.8145` n `8`; equity avg `-0.1303` n `162`; fx avg `0.0054` n `6`; index avg `-0.0144` n `27`; metal avg `-0.0537` n `20`; unknown avg `1.0004` n `1256`
- 4h: commodity avg `-0.0599` n `13`; crypto_alt avg `-1.8919` n `239`; crypto_major avg `-1.8808` n `8`; equity avg `-0.3909` n `162`; fx avg `0.0162` n `6`; index avg `-0.0266` n `27`; metal avg `-0.0819` n `20`; unknown avg `0.5997` n `1250`
- 24h: commodity avg `-0.2547` n `13`; crypto_alt avg `-5.6458` n `239`; crypto_major avg `-5.4333` n `8`; equity avg `-1.1125` n `162`; fx avg `-0.1233` n `6`; index avg `-0.0707` n `27`; metal avg `-0.3847` n `20`; unknown avg `0.6516` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
