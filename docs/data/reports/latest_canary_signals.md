# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T14:22:33.563538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.2344` n `230`; crypto_major avg `-0.1869` n `8`; equity avg `-0.2127` n `107`; fx avg `0.0278` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0788` n `20`; unknown avg `0.0273` n `782`
- 1h: commodity avg `-0.1776` n `12`; crypto_alt avg `-0.3882` n `230`; crypto_major avg `-0.4468` n `8`; equity avg `0.2443` n `107`; fx avg `0.0096` n `6`; index avg `0.1142` n `25`; metal avg `0.0264` n `20`; unknown avg `-0.1108` n `781`
- 4h: commodity avg `-1.3535` n `12`; crypto_alt avg `-0.4842` n `230`; crypto_major avg `0.0327` n `8`; equity avg `0.8058` n `107`; fx avg `-0.0777` n `6`; index avg `0.2998` n `25`; metal avg `0.52` n `20`; unknown avg `-0.1915` n `781`
- 24h: commodity avg `-0.8968` n `12`; crypto_alt avg `-0.2492` n `230`; crypto_major avg `0.5431` n `8`; equity avg `4.0504` n `107`; fx avg `0.0892` n `6`; index avg `0.7446` n `25`; metal avg `1.0458` n `20`; unknown avg `0.5412` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
