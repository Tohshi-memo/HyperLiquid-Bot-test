# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T00:56:02.577213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2827` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0363` n `13`; crypto_alt avg `0.0881` n `239`; crypto_major avg `-0.0461` n `8`; equity avg `-0.0494` n `162`; fx avg `-0.0111` n `6`; index avg `0.0018` n `27`; metal avg `0.0058` n `20`; unknown avg `-0.0536` n `1260`
- 1h: commodity avg `0.0855` n `13`; crypto_alt avg `-0.0688` n `239`; crypto_major avg `0.0253` n `8`; equity avg `-0.0283` n `162`; fx avg `-0.0114` n `6`; index avg `-0.0913` n `27`; metal avg `0.0005` n `20`; unknown avg `0.2689` n `1252`
- 4h: commodity avg `0.1031` n `13`; crypto_alt avg `-0.8636` n `239`; crypto_major avg `-1.3578` n `8`; equity avg `-1.2237` n `162`; fx avg `-0.0378` n `6`; index avg `-0.0751` n `27`; metal avg `-0.0285` n `20`; unknown avg `2.8597` n `1166`
- 24h: commodity avg `-0.1683` n `13`; crypto_alt avg `-1.4932` n `239`; crypto_major avg `-2.9214` n `8`; equity avg `-3.9247` n `162`; fx avg `-0.1229` n `6`; index avg `-0.3194` n `27`; metal avg `-0.3582` n `20`; unknown avg `59.9193` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
