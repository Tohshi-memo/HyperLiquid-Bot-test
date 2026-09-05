# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T11:37:29.909776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `0.0561` n `232`; crypto_major avg `0.0026` n `8`; equity avg `0.017` n `134`; fx avg `0.0006` n `6`; index avg `0.0063` n `26`; metal avg `0.0002` n `20`; unknown avg `0.0583` n `791`
- 1h: commodity avg `0.0306` n `12`; crypto_alt avg `0.0225` n `232`; crypto_major avg `0.0131` n `8`; equity avg `0.0431` n `134`; fx avg `-0.0021` n `6`; index avg `0.0182` n `26`; metal avg `0.0027` n `20`; unknown avg `0.031` n `786`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `0.103` n `232`; crypto_major avg `0.2322` n `8`; equity avg `0.0901` n `134`; fx avg `-0.004` n `6`; index avg `0.0118` n `26`; metal avg `-0.0117` n `20`; unknown avg `-0.1165` n `780`
- 24h: commodity avg `0.1613` n `12`; crypto_alt avg `0.316` n `232`; crypto_major avg `-1.4176` n `8`; equity avg `0.836` n `134`; fx avg `-0.1112` n `6`; index avg `0.0556` n `26`; metal avg `-0.1092` n `20`; unknown avg `16.8486` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
