# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T02:07:31.036801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0205` n `13`; crypto_alt avg `0.0266` n `238`; crypto_major avg `-0.0956` n `8`; equity avg `-0.1446` n `154`; fx avg `-0.0055` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0533` n `20`; unknown avg `-0.0443` n `1232`
- 1h: commodity avg `0.0386` n `13`; crypto_alt avg `0.4603` n `238`; crypto_major avg `0.2531` n `8`; equity avg `0.2666` n `154`; fx avg `0.0363` n `6`; index avg `0.0346` n `27`; metal avg `-0.063` n `20`; unknown avg `-0.3284` n `1232`
- 4h: commodity avg `0.2197` n `13`; crypto_alt avg `0.5628` n `238`; crypto_major avg `0.2739` n `8`; equity avg `0.8272` n `154`; fx avg `0.0912` n `6`; index avg `0.1545` n `27`; metal avg `-0.1041` n `20`; unknown avg `0.7515` n `1212`
- 24h: commodity avg `0.0681` n `13`; crypto_alt avg `1.9623` n `237`; crypto_major avg `1.5937` n `8`; equity avg `1.9761` n `154`; fx avg `0.0656` n `6`; index avg `0.4427` n `27`; metal avg `0.2023` n `20`; unknown avg `237.984` n `1028`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
