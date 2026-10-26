# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T10:22:29.058867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0691` n `13`; crypto_alt avg `-0.0532` n `237`; crypto_major avg `-0.074` n `8`; equity avg `-0.1519` n `152`; fx avg `-0.0003` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0094` n `20`; unknown avg `-0.0301` n `1240`
- 1h: commodity avg `0.0575` n `13`; crypto_alt avg `-0.0895` n `237`; crypto_major avg `0.0267` n `8`; equity avg `-0.0218` n `152`; fx avg `-0.0043` n `6`; index avg `-0.0333` n `26`; metal avg `0.0324` n `20`; unknown avg `0.2583` n `1240`
- 4h: commodity avg `0.1192` n `13`; crypto_alt avg `0.2927` n `237`; crypto_major avg `0.2541` n `8`; equity avg `0.1583` n `152`; fx avg `-0.0166` n `6`; index avg `0.0487` n `26`; metal avg `0.0943` n `20`; unknown avg `0.0177` n `1142`
- 24h: commodity avg `-0.4563` n `13`; crypto_alt avg `0.4463` n `237`; crypto_major avg `0.3516` n `8`; equity avg `-0.1585` n `152`; fx avg `0.0538` n `6`; index avg `0.029` n `26`; metal avg `0.2127` n `20`; unknown avg `-0.0978` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2648`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2276`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
