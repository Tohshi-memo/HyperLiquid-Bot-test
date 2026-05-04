# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T06:00:36.543934+00:00`
- Correlation status: `ready`
- Asset price records: `239`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `7`; crypto_alt avg `-0.015` n `223`; crypto_major avg `-0.1279` n `7`; equity avg `-0.0424` n `42`; fx avg `0.0029` n `4`; index avg `0.0248` n `9`; metal avg `-0.0554` n `7`; unknown avg `-0.1262` n `312`
- 1h: commodity avg `-0.2368` n `7`; crypto_alt avg `-0.1161` n `223`; crypto_major avg `-0.4415` n `7`; equity avg `-0.1231` n `42`; fx avg `0.0125` n `4`; index avg `0.0959` n `9`; metal avg `-0.1978` n `7`; unknown avg `-0.1501` n `312`
- 4h: commodity avg `-0.1276` n `7`; crypto_alt avg `1.0153` n `223`; crypto_major avg `0.7033` n `7`; equity avg `0.0981` n `42`; fx avg `-0.0294` n `4`; index avg `0.4131` n `9`; metal avg `-0.3722` n `7`; unknown avg `-0.2383` n `312`
- 24h: commodity avg `-0.1162` n `7`; crypto_alt avg `2.7608` n `223`; crypto_major avg `2.7862` n `7`; equity avg `0.9557` n `42`; fx avg `-0.0355` n `4`; index avg `0.9374` n `9`; metal avg `0.0107` n `7`; unknown avg `0.2769` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4035`, n `231`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3937`, n `231`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3617`, n `235`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3473`, n `235`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1915`, n `231`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `235`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1858`, n `231`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `235`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `235`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1445`, n `231`, weak_sample_signal
