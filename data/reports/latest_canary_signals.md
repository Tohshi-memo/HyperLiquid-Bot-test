# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T19:52:36.271627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.1758` n `234`; crypto_major avg `-0.0974` n `8`; equity avg `-0.1776` n `140`; fx avg `0.0002` n `6`; index avg `-0.0256` n `26`; metal avg `-0.0387` n `20`; unknown avg `9.1731` n `942`
- 1h: commodity avg `-0.0574` n `12`; crypto_alt avg `0.1221` n `234`; crypto_major avg `-0.1751` n `8`; equity avg `-0.1274` n `140`; fx avg `0.0042` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0097` n `20`; unknown avg `22.0758` n `936`
- 4h: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.4275` n `234`; crypto_major avg `-0.1256` n `8`; equity avg `0.2403` n `140`; fx avg `0.001` n `6`; index avg `0.0959` n `26`; metal avg `0.0304` n `20`; unknown avg `14.6059` n `924`
- 24h: commodity avg `-1.06` n `12`; crypto_alt avg `3.7463` n `234`; crypto_major avg `4.9532` n `8`; equity avg `2.8428` n `140`; fx avg `-0.0691` n `6`; index avg `0.6476` n `26`; metal avg `0.0519` n `20`; unknown avg `11.3603` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
