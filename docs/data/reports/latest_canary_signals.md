# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T20:07:26.741995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0627` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0194` n `13`; crypto_alt avg `-0.0714` n `239`; crypto_major avg `0.0128` n `8`; equity avg `0.0402` n `162`; fx avg `-0.0119` n `6`; index avg `0.0034` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.1087` n `1242`
- 1h: commodity avg `0.0366` n `13`; crypto_alt avg `-0.6411` n `239`; crypto_major avg `-0.2271` n `8`; equity avg `0.022` n `162`; fx avg `-0.0106` n `6`; index avg `-0.0` n `27`; metal avg `0.0075` n `20`; unknown avg `6.054` n `1246`
- 4h: commodity avg `-0.0141` n `13`; crypto_alt avg `-1.6892` n `239`; crypto_major avg `-1.0817` n `8`; equity avg `-0.2144` n `162`; fx avg `-0.0083` n `6`; index avg `-0.019` n `27`; metal avg `-0.0103` n `20`; unknown avg `0.61` n `1246`
- 24h: commodity avg `-0.0152` n `13`; crypto_alt avg `-7.8527` n `239`; crypto_major avg `-6.997` n `8`; equity avg `-1.9475` n `162`; fx avg `-0.0304` n `6`; index avg `-0.1673` n `27`; metal avg `-0.2456` n `20`; unknown avg `1.2324` n `1090`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
