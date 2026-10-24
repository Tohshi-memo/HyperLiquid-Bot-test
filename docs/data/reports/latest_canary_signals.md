# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T10:22:24.402605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.0404` n `237`; crypto_major avg `0.03` n `8`; equity avg `0.0303` n `152`; fx avg `0.0` n `6`; index avg `-0.0004` n `26`; metal avg `0.0121` n `20`; unknown avg `0.5523` n `1228`
- 1h: commodity avg `0.0122` n `13`; crypto_alt avg `0.112` n `237`; crypto_major avg `0.0395` n `8`; equity avg `0.0498` n `152`; fx avg `0.0078` n `6`; index avg `-0.0042` n `26`; metal avg `0.0015` n `20`; unknown avg `12.2615` n `1224`
- 4h: commodity avg `0.0486` n `13`; crypto_alt avg `-0.7757` n `237`; crypto_major avg `-0.8908` n `8`; equity avg `-0.2788` n `152`; fx avg `0.0037` n `6`; index avg `-0.0386` n `26`; metal avg `-0.0256` n `20`; unknown avg `11.9806` n `1194`
- 24h: commodity avg `0.178` n `13`; crypto_alt avg `-2.8501` n `237`; crypto_major avg `-2.4009` n `8`; equity avg `-0.8663` n `152`; fx avg `0.0027` n `6`; index avg `-0.0301` n `26`; metal avg `-0.1604` n `20`; unknown avg `193.6671` n `1053`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
