# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T08:22:30.304854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.0421` n `232`; crypto_major avg `-0.0173` n `8`; equity avg `0.0129` n `134`; fx avg `-0.0106` n `6`; index avg `0.0016` n `26`; metal avg `-0.003` n `20`; unknown avg `-0.0509` n `794`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `0.1912` n `232`; crypto_major avg `-0.0366` n `8`; equity avg `0.0113` n `134`; fx avg `0.0177` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0106` n `20`; unknown avg `-0.1428` n `792`
- 4h: commodity avg `0.0094` n `12`; crypto_alt avg `0.018` n `232`; crypto_major avg `-0.0976` n `8`; equity avg `0.0753` n `134`; fx avg `0.0184` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0116` n `20`; unknown avg `0.1331` n `758`
- 24h: commodity avg `0.1551` n `12`; crypto_alt avg `1.7652` n `232`; crypto_major avg `1.9604` n `8`; equity avg `0.4481` n `134`; fx avg `-0.0348` n `6`; index avg `0.0843` n `26`; metal avg `-0.0093` n `20`; unknown avg `493.285` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
