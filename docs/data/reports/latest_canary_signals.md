# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T17:07:27.372851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.1738` n `232`; crypto_major avg `-0.2058` n `8`; equity avg `-0.1602` n `133`; fx avg `-0.0049` n `6`; index avg `-0.025` n `26`; metal avg `-0.042` n `20`; unknown avg `-0.0953` n `791`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `0.3579` n `232`; crypto_major avg `0.1992` n `8`; equity avg `0.1784` n `133`; fx avg `-0.0131` n `6`; index avg `0.0246` n `26`; metal avg `-0.0421` n `20`; unknown avg `0.1247` n `785`
- 4h: commodity avg `0.1678` n `12`; crypto_alt avg `0.8986` n `232`; crypto_major avg `0.1496` n `8`; equity avg `1.6015` n `133`; fx avg `0.0122` n `6`; index avg `0.205` n `26`; metal avg `0.2151` n `20`; unknown avg `0.2303` n `739`
- 24h: commodity avg `-0.0631` n `12`; crypto_alt avg `-0.9816` n `232`; crypto_major avg `-1.7383` n `8`; equity avg `1.6099` n `133`; fx avg `-0.1128` n `6`; index avg `0.2029` n `26`; metal avg `-0.3463` n `20`; unknown avg `0.6759` n `686`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
