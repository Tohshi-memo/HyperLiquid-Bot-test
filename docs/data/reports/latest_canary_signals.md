# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T13:37:43.503363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.2499` n `237`; crypto_major avg `-0.1343` n `8`; equity avg `-0.5633` n `152`; fx avg `0.0058` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0269` n `20`; unknown avg `2.6439` n `1233`
- 1h: commodity avg `-0.0571` n `13`; crypto_alt avg `-0.4038` n `237`; crypto_major avg `-0.1518` n `8`; equity avg `-0.5658` n `152`; fx avg `0.0113` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0043` n `20`; unknown avg `4.2095` n `1231`
- 4h: commodity avg `-0.2091` n `13`; crypto_alt avg `-0.1984` n `237`; crypto_major avg `0.0293` n `8`; equity avg `-1.1883` n `152`; fx avg `-0.0024` n `6`; index avg `-0.0803` n `26`; metal avg `0.0308` n `20`; unknown avg `2.6122` n `1225`
- 24h: commodity avg `-0.0443` n `13`; crypto_alt avg `-0.0673` n `237`; crypto_major avg `0.0369` n `8`; equity avg `-2.5848` n `152`; fx avg `-0.1173` n `6`; index avg `-0.3399` n `26`; metal avg `-0.3045` n `20`; unknown avg `50.2051` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2201`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
