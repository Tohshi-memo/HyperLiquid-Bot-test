# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T13:22:28.958852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2523` n `12`; crypto_alt avg `-0.0674` n `230`; crypto_major avg `-0.0944` n `8`; equity avg `0.152` n `107`; fx avg `-0.0144` n `6`; index avg `0.0513` n `25`; metal avg `0.1114` n `20`; unknown avg `-0.0205` n `781`
- 1h: commodity avg `-0.2891` n `12`; crypto_alt avg `-0.0949` n `230`; crypto_major avg `-0.0326` n `8`; equity avg `-0.021` n `107`; fx avg `-0.009` n `6`; index avg `0.0415` n `25`; metal avg `0.0738` n `20`; unknown avg `-0.0668` n `781`
- 4h: commodity avg `-1.2752` n `12`; crypto_alt avg `-0.052` n `230`; crypto_major avg `0.5949` n `8`; equity avg `1.2401` n `107`; fx avg `-0.1069` n `6`; index avg `0.2723` n `25`; metal avg `0.5325` n `20`; unknown avg `0.0714` n `781`
- 24h: commodity avg `-0.8032` n `12`; crypto_alt avg `0.3675` n `230`; crypto_major avg `1.3111` n `8`; equity avg `5.2203` n `107`; fx avg `0.033` n `6`; index avg `0.6599` n `25`; metal avg `1.1239` n `20`; unknown avg `0.8273` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
