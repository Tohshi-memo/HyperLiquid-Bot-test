# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T16:07:24.344750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.0876` n `232`; crypto_major avg `0.042` n `8`; equity avg `0.009` n `134`; fx avg `-0.0229` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.1459` n `792`
- 1h: commodity avg `0.0286` n `12`; crypto_alt avg `-0.1247` n `232`; crypto_major avg `0.0501` n `8`; equity avg `0.0188` n `134`; fx avg `-0.0351` n `6`; index avg `-0.0066` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.3631` n `792`
- 4h: commodity avg `0.0573` n `12`; crypto_alt avg `0.1301` n `232`; crypto_major avg `0.7679` n `8`; equity avg `0.056` n `134`; fx avg `-0.0141` n `6`; index avg `0.0052` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.2448` n `729`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `2.3712` n `232`; crypto_major avg `1.8931` n `8`; equity avg `0.4373` n `134`; fx avg `-0.0315` n `6`; index avg `0.0285` n `26`; metal avg `0.0109` n `20`; unknown avg `0.0307` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
