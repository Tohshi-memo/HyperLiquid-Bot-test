# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T05:22:33.512622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `13`; crypto_alt avg `0.0612` n `237`; crypto_major avg `0.0987` n `8`; equity avg `0.0446` n `152`; fx avg `0.0123` n `6`; index avg `0.0032` n `26`; metal avg `-0.0221` n `20`; unknown avg `0.0605` n `1240`
- 1h: commodity avg `0.0373` n `13`; crypto_alt avg `0.7428` n `237`; crypto_major avg `0.5601` n `8`; equity avg `0.3801` n `152`; fx avg `0.0106` n `6`; index avg `0.0371` n `26`; metal avg `0.0374` n `20`; unknown avg `1.3298` n `1238`
- 4h: commodity avg `-0.0271` n `13`; crypto_alt avg `-0.0077` n `237`; crypto_major avg `-0.0069` n `8`; equity avg `0.2059` n `152`; fx avg `-0.0029` n `6`; index avg `0.0785` n `26`; metal avg `0.0639` n `20`; unknown avg `0.8043` n `1222`
- 24h: commodity avg `-0.5369` n `13`; crypto_alt avg `-0.9591` n `237`; crypto_major avg `-0.8991` n `8`; equity avg `-0.3362` n `152`; fx avg `0.0562` n `6`; index avg `0.0523` n `26`; metal avg `0.177` n `20`; unknown avg `1.2695` n `985`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2536`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
