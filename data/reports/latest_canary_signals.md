# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T18:37:24.477850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0361` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `0.5011` n `239`; crypto_major avg `0.459` n `8`; equity avg `0.16` n `162`; fx avg `0.0021` n `6`; index avg `0.0179` n `27`; metal avg `0.0071` n `20`; unknown avg `0.9471` n `1262`
- 1h: commodity avg `0.0012` n `13`; crypto_alt avg `-0.6901` n `239`; crypto_major avg `-0.3935` n `8`; equity avg `-0.1115` n `162`; fx avg `0.0058` n `6`; index avg `-0.0126` n `27`; metal avg `-0.0331` n `20`; unknown avg `0.8437` n `1260`
- 4h: commodity avg `-0.0373` n `13`; crypto_alt avg `-1.4303` n `239`; crypto_major avg `-1.0751` n `8`; equity avg `-0.3327` n `162`; fx avg `0.016` n `6`; index avg `-0.039` n `27`; metal avg `-0.1382` n `20`; unknown avg `0.6402` n `1252`
- 24h: commodity avg `-0.0658` n `13`; crypto_alt avg `-6.6218` n `239`; crypto_major avg `-6.1814` n `8`; equity avg `-1.6195` n `162`; fx avg `-0.0182` n `6`; index avg `-0.1104` n `27`; metal avg `-0.3103` n `20`; unknown avg `1.6111` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
