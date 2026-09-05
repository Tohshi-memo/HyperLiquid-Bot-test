# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T01:07:25.108043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0134` n `232`; crypto_major avg `-0.0805` n `8`; equity avg `-0.0032` n `134`; fx avg `0.0057` n `6`; index avg `0.0022` n `26`; metal avg `0.0119` n `20`; unknown avg `2.6959` n `788`
- 1h: commodity avg `0.0302` n `12`; crypto_alt avg `0.2627` n `232`; crypto_major avg `-0.0095` n `8`; equity avg `-0.0353` n `134`; fx avg `0.0152` n `6`; index avg `0.0008` n `26`; metal avg `0.0091` n `20`; unknown avg `3.5755` n `778`
- 4h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.4405` n `232`; crypto_major avg `0.0001` n `8`; equity avg `-0.0423` n `134`; fx avg `0.0339` n `6`; index avg `-0.0371` n `26`; metal avg `0.0158` n `20`; unknown avg `0.4995` n `758`
- 24h: commodity avg `0.042` n `12`; crypto_alt avg `-0.4586` n `232`; crypto_major avg `-1.8607` n `8`; equity avg `1.2134` n `134`; fx avg `-0.1237` n `6`; index avg `0.158` n `26`; metal avg `-0.1757` n `20`; unknown avg `0.8177` n `652`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
