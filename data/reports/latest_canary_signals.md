# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T10:52:32.284293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0565` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.3712` n `228`; crypto_major avg `-0.2655` n `8`; equity avg `0.0005` n `86`; fx avg `0.0037` n `6`; index avg `0.0069` n `23`; metal avg `0.0146` n `20`; unknown avg `-0.0027` n `765`
- 1h: commodity avg `0.0691` n `12`; crypto_alt avg `-0.4269` n `228`; crypto_major avg `-0.4667` n `8`; equity avg `-0.125` n `86`; fx avg `0.0102` n `6`; index avg `-0.0087` n `23`; metal avg `0.0638` n `20`; unknown avg `-0.1112` n `765`
- 4h: commodity avg `-0.2087` n `12`; crypto_alt avg `-0.8727` n `228`; crypto_major avg `-1.1232` n `8`; equity avg `-0.4522` n `86`; fx avg `0.0404` n `6`; index avg `-0.0667` n `23`; metal avg `0.3043` n `20`; unknown avg `-0.1844` n `757`
- 24h: commodity avg `0.0496` n `12`; crypto_alt avg `-2.1798` n `228`; crypto_major avg `-2.2528` n `8`; equity avg `-4.2923` n `86`; fx avg `0.0539` n `6`; index avg `-0.6474` n `23`; metal avg `0.7034` n `20`; unknown avg `0.6789` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2759`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
