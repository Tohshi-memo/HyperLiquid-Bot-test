# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T04:22:30.742206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.452` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0334` n `13`; crypto_alt avg `0.0045` n `237`; crypto_major avg `0.0377` n `8`; equity avg `-0.1044` n `151`; fx avg `0.0054` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0087` n `20`; unknown avg `3.9773` n `1201`
- 1h: commodity avg `0.0543` n `13`; crypto_alt avg `0.0127` n `237`; crypto_major avg `0.1187` n `8`; equity avg `-0.4754` n `151`; fx avg `-0.0152` n `6`; index avg `-0.1207` n `26`; metal avg `-0.1074` n `20`; unknown avg `-0.3352` n `1183`
- 4h: commodity avg `0.1906` n `13`; crypto_alt avg `-1.9168` n `237`; crypto_major avg `-1.6777` n `8`; equity avg `-1.556` n `151`; fx avg `-0.0541` n `6`; index avg `-0.2257` n `26`; metal avg `-0.5032` n `20`; unknown avg `6.4158` n `1177`
- 24h: commodity avg `-0.5235` n `13`; crypto_alt avg `-0.3737` n `237`; crypto_major avg `-0.319` n `8`; equity avg `-2.0723` n `151`; fx avg `-0.018` n `6`; index avg `-0.2861` n `26`; metal avg `-0.5753` n `20`; unknown avg `118.7915` n `930`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
