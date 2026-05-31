# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T17:36:27.597929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1909` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `0.3195` n `228`; crypto_major avg `0.1942` n `8`; equity avg `0.0978` n `69`; fx avg `-0.0006` n `6`; index avg `0.0647` n `23`; metal avg `-0.024` n `18`; unknown avg `0.8715` n `421`
- 1h: commodity avg `0.0765` n `12`; crypto_alt avg `0.5215` n `228`; crypto_major avg `0.4485` n `8`; equity avg `0.0981` n `69`; fx avg `0.0025` n `6`; index avg `0.1647` n `23`; metal avg `-0.0012` n `18`; unknown avg `0.1858` n `421`
- 4h: commodity avg `0.1381` n `12`; crypto_alt avg `-1.2005` n `228`; crypto_major avg `-0.8937` n `8`; equity avg `0.0077` n `69`; fx avg `-0.0105` n `6`; index avg `0.2972` n `23`; metal avg `-0.0779` n `18`; unknown avg `0.6194` n `421`
- 24h: commodity avg `0.6652` n `12`; crypto_alt avg `-0.8278` n `228`; crypto_major avg `-0.1277` n `8`; equity avg `0.9653` n `69`; fx avg `-0.0116` n `6`; index avg `0.1905` n `23`; metal avg `-0.1432` n `18`; unknown avg `1.1474` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
