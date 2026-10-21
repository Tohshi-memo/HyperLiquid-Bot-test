# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T07:07:30.074984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `13`; crypto_alt avg `0.031` n `237`; crypto_major avg `-0.023` n `8`; equity avg `-0.1348` n `151`; fx avg `0.0009` n `6`; index avg `-0.0122` n `26`; metal avg `0.0237` n `20`; unknown avg `0.4012` n `1196`
- 1h: commodity avg `-0.0231` n `13`; crypto_alt avg `0.2373` n `237`; crypto_major avg `0.072` n `8`; equity avg `-0.2451` n `151`; fx avg `0.0142` n `6`; index avg `-0.0395` n `26`; metal avg `-0.0466` n `20`; unknown avg `0.2316` n `1192`
- 4h: commodity avg `-0.0935` n `13`; crypto_alt avg `0.0145` n `237`; crypto_major avg `-0.1473` n `8`; equity avg `-0.4198` n `151`; fx avg `-0.0614` n `6`; index avg `-0.1138` n `26`; metal avg `-0.1221` n `20`; unknown avg `0.7364` n `1168`
- 24h: commodity avg `-0.0575` n `13`; crypto_alt avg `2.6164` n `237`; crypto_major avg `1.7843` n `8`; equity avg `2.1491` n `151`; fx avg `0.0064` n `6`; index avg `0.2481` n `26`; metal avg `-0.2598` n `20`; unknown avg `5292.8166` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
