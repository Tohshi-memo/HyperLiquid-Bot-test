# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T15:22:31.132222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5994` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5415` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.1579` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0323` n `13`; crypto_alt avg `-0.5061` n `237`; crypto_major avg `-0.4331` n `8`; equity avg `-0.0576` n `152`; fx avg `-0.0065` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0308` n `20`; unknown avg `4.5739` n `1230`
- 1h: commodity avg `-0.0324` n `13`; crypto_alt avg `-1.0409` n `237`; crypto_major avg `-1.1643` n `8`; equity avg `-0.1169` n `152`; fx avg `-0.004` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0624` n `20`; unknown avg `0.4374` n `1228`
- 4h: commodity avg `0.0609` n `13`; crypto_alt avg `-2.1058` n `237`; crypto_major avg `-1.6522` n `8`; equity avg `-0.3781` n `152`; fx avg `-0.0218` n `6`; index avg `-0.0528` n `26`; metal avg `-0.1107` n `20`; unknown avg `6.1853` n `1192`
- 24h: commodity avg `0.364` n `13`; crypto_alt avg `-4.4717` n `237`; crypto_major avg `-3.6844` n `8`; equity avg `-0.996` n `152`; fx avg `-0.023` n `6`; index avg `-0.124` n `26`; metal avg `-0.3053` n `20`; unknown avg `2.1992` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
