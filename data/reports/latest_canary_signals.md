# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T21:56:56.810326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `0.0905` n `237`; crypto_major avg `0.063` n `8`; equity avg `-0.0275` n `151`; fx avg `0.0062` n `6`; index avg `0.012` n `26`; metal avg `0.008` n `20`; unknown avg `-0.0392` n `1199`
- 1h: commodity avg `0.0102` n `13`; crypto_alt avg `0.2629` n `237`; crypto_major avg `0.188` n `8`; equity avg `0.5551` n `151`; fx avg `0.0126` n `6`; index avg `0.0552` n `26`; metal avg `0.0221` n `20`; unknown avg `0.9162` n `1157`
- 4h: commodity avg `0.1574` n `13`; crypto_alt avg `0.2105` n `237`; crypto_major avg `0.359` n `8`; equity avg `1.0` n `151`; fx avg `0.0079` n `6`; index avg `0.1122` n `26`; metal avg `0.0049` n `20`; unknown avg `-0.0076` n `1099`
- 24h: commodity avg `-0.0007` n `13`; crypto_alt avg `3.0929` n `237`; crypto_major avg `1.9397` n `8`; equity avg `1.2676` n `151`; fx avg `0.0237` n `6`; index avg `0.143` n `26`; metal avg `0.0703` n `20`; unknown avg `4.3115` n `1054`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
