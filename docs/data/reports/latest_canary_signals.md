# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T15:37:26.284503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5886` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.553` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2572` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0284` n `13`; crypto_alt avg `0.0331` n `237`; crypto_major avg `-0.0176` n `8`; equity avg `-0.1347` n `152`; fx avg `0.0087` n `6`; index avg `-0.0249` n `26`; metal avg `-0.0034` n `20`; unknown avg `1.6551` n `1230`
- 1h: commodity avg `0.0038` n `13`; crypto_alt avg `-1.1671` n `237`; crypto_major avg `-1.3016` n `8`; equity avg `-0.3857` n `152`; fx avg `0.0075` n `6`; index avg `-0.0444` n `26`; metal avg `-0.0587` n `20`; unknown avg `17.154` n `1230`
- 4h: commodity avg `0.0891` n `13`; crypto_alt avg `-2.0301` n `237`; crypto_major avg `-1.658` n `8`; equity avg `-0.4971` n `152`; fx avg `0.0012` n `6`; index avg `-0.0694` n `26`; metal avg `-0.105` n `20`; unknown avg `5.9613` n `1190`
- 24h: commodity avg `0.2888` n `13`; crypto_alt avg `-4.2691` n `237`; crypto_major avg `-3.619` n `8`; equity avg `-1.191` n `152`; fx avg `-0.0313` n `6`; index avg `-0.1632` n `26`; metal avg `-0.2845` n `20`; unknown avg `3.1953` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
