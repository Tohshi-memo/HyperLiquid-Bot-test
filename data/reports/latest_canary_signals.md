# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T06:37:32.278537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `-0.108` n `237`; crypto_major avg `-0.0915` n `8`; equity avg `-0.0262` n `152`; fx avg `0.0073` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.0761` n `1231`
- 1h: commodity avg `0.0491` n `13`; crypto_alt avg `-0.3639` n `237`; crypto_major avg `-0.3271` n `8`; equity avg `-0.1448` n `152`; fx avg `0.0056` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0385` n `20`; unknown avg `0.1839` n `1203`
- 4h: commodity avg `0.0075` n `13`; crypto_alt avg `-0.5906` n `237`; crypto_major avg `-0.5472` n `8`; equity avg `-0.1013` n `152`; fx avg `0.0251` n `6`; index avg `0.0089` n `26`; metal avg `-0.0192` n `20`; unknown avg `1.0119` n `1193`
- 24h: commodity avg `0.0949` n `13`; crypto_alt avg `-1.6495` n `237`; crypto_major avg `-0.3588` n `8`; equity avg `-0.0757` n `152`; fx avg `-0.0229` n `6`; index avg `0.0004` n `26`; metal avg `-0.102` n `20`; unknown avg `18.3374` n `1054`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
