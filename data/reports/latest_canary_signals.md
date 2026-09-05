# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T00:52:28.042836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.0816` n `232`; crypto_major avg `0.095` n `8`; equity avg `-0.0343` n `134`; fx avg `0.0155` n `6`; index avg `0.007` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.0915` n `790`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.1846` n `232`; crypto_major avg `0.0155` n `8`; equity avg `-0.0827` n `134`; fx avg `0.0111` n `6`; index avg `0.0138` n `26`; metal avg `0.0025` n `20`; unknown avg `-0.0009` n `758`
- 4h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.4534` n `232`; crypto_major avg `0.0906` n `8`; equity avg `-0.0197` n `134`; fx avg `0.0353` n `6`; index avg `-0.031` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.2983` n `758`
- 24h: commodity avg `0.0425` n `12`; crypto_alt avg `-0.7395` n `232`; crypto_major avg `-1.959` n `8`; equity avg `1.1905` n `134`; fx avg `-0.101` n `6`; index avg `0.1472` n `26`; metal avg `-0.2725` n `20`; unknown avg `0.7711` n `652`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
