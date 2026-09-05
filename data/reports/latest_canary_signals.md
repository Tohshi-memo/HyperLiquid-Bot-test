# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T03:37:28.041276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `0.1029` n `232`; crypto_major avg `0.1112` n `8`; equity avg `-0.0051` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0086` n `26`; metal avg `0.0049` n `20`; unknown avg `0.067` n `790`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `0.1054` n `232`; crypto_major avg `0.0675` n `8`; equity avg `-0.0287` n `134`; fx avg `0.0028` n `6`; index avg `-0.0151` n `26`; metal avg `0.0096` n `20`; unknown avg `-0.1344` n `788`
- 4h: commodity avg `0.0015` n `12`; crypto_alt avg `0.6668` n `232`; crypto_major avg `-0.0274` n `8`; equity avg `-0.1101` n `134`; fx avg `-0.0069` n `6`; index avg `0.0088` n `26`; metal avg `0.0257` n `20`; unknown avg `1.0447` n `758`
- 24h: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.0066` n `232`; crypto_major avg `-1.9646` n `8`; equity avg `1.128` n `134`; fx avg `-0.1329` n `6`; index avg `0.1417` n `26`; metal avg `-0.1428` n `20`; unknown avg `0.8884` n `652`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
