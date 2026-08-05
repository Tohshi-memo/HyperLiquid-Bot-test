# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T08:37:30.944575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `0.058` n `230`; crypto_major avg `0.0114` n `8`; equity avg `-0.0905` n `108`; fx avg `0.0079` n `6`; index avg `-0.004` n `25`; metal avg `-0.0166` n `20`; unknown avg `0.0129` n `781`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.1776` n `230`; crypto_major avg `0.4262` n `8`; equity avg `-0.5306` n `108`; fx avg `0.0302` n `6`; index avg `-0.0551` n `25`; metal avg `-0.1048` n `20`; unknown avg `0.127` n `781`
- 4h: commodity avg `0.2729` n `12`; crypto_alt avg `0.1735` n `230`; crypto_major avg `0.4202` n `8`; equity avg `-0.7337` n `108`; fx avg `0.0723` n `6`; index avg `-0.0927` n `25`; metal avg `0.1746` n `20`; unknown avg `0.1399` n `749`
- 24h: commodity avg `-1.2595` n `12`; crypto_alt avg `0.7255` n `230`; crypto_major avg `1.1109` n `8`; equity avg `2.306` n `108`; fx avg `0.0044` n `6`; index avg `0.6076` n `25`; metal avg `1.1142` n `20`; unknown avg `0.1643` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
