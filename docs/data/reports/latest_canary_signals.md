# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T18:52:27.860506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5593` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.599` n `239`; crypto_major avg `-0.6336` n `8`; equity avg `-0.169` n `162`; fx avg `-0.0169` n `6`; index avg `-0.015` n `27`; metal avg `-0.018` n `20`; unknown avg `0.7354` n `1262`
- 1h: commodity avg `-0.0189` n `13`; crypto_alt avg `-0.7605` n `239`; crypto_major avg `-0.6391` n `8`; equity avg `-0.1345` n `162`; fx avg `-0.0109` n `6`; index avg `-0.0141` n `27`; metal avg `-0.0312` n `20`; unknown avg `1.2952` n `1260`
- 4h: commodity avg `-0.0568` n `13`; crypto_alt avg `-1.9486` n `239`; crypto_major avg `-1.6056` n `8`; equity avg `-0.4934` n `162`; fx avg `-0.0085` n `6`; index avg `-0.0463` n `27`; metal avg `-0.1443` n `20`; unknown avg `0.7587` n `1250`
- 24h: commodity avg `-0.0903` n `13`; crypto_alt avg `-7.1923` n `239`; crypto_major avg `-6.7848` n `8`; equity avg `-1.8525` n `162`; fx avg `-0.0341` n `6`; index avg `-0.1434` n `27`; metal avg `-0.3104` n `20`; unknown avg `1.7897` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
