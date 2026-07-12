# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T10:07:27.286004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.1017` n `230`; crypto_major avg `-0.1905` n `8`; equity avg `0.0056` n `92`; fx avg `0.0002` n `6`; index avg `-0.0105` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.0122` n `765`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.0645` n `230`; crypto_major avg `-0.1516` n `8`; equity avg `-0.0229` n `92`; fx avg `-0.0008` n `6`; index avg `-0.0209` n `25`; metal avg `0.0013` n `20`; unknown avg `1.1124` n `765`
- 4h: commodity avg `0.1591` n `12`; crypto_alt avg `0.1614` n `230`; crypto_major avg `0.1981` n `8`; equity avg `0.0081` n `92`; fx avg `0.004` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0168` n `20`; unknown avg `2.1335` n `763`
- 24h: commodity avg `0.5196` n `12`; crypto_alt avg `-0.7359` n `230`; crypto_major avg `-0.6373` n `8`; equity avg `-0.1748` n `92`; fx avg `0.0041` n `6`; index avg `-0.134` n `25`; metal avg `-0.1131` n `20`; unknown avg `-0.067` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
