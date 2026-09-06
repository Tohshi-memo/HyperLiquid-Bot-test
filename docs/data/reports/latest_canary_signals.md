# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T17:52:26.419879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0602` n `232`; crypto_major avg `-0.0012` n `8`; equity avg `0.0325` n `134`; fx avg `-0.0006` n `6`; index avg `-0.0006` n `26`; metal avg `0.0063` n `20`; unknown avg `1.1575` n `793`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.199` n `232`; crypto_major avg `-0.0188` n `8`; equity avg `0.0803` n `134`; fx avg `-0.0107` n `6`; index avg `0.0052` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.0877` n `783`
- 4h: commodity avg `0.0174` n `12`; crypto_alt avg `-0.3905` n `232`; crypto_major avg `-0.4804` n `8`; equity avg `-0.046` n `134`; fx avg `-0.0212` n `6`; index avg `-0.019` n `26`; metal avg `-0.0146` n `20`; unknown avg `1.1156` n `776`
- 24h: commodity avg `0.1003` n `12`; crypto_alt avg `1.11` n `232`; crypto_major avg `-0.0209` n `8`; equity avg `0.2328` n `134`; fx avg `-0.0196` n `6`; index avg `0.0162` n `26`; metal avg `-0.0481` n `20`; unknown avg `23.227` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
