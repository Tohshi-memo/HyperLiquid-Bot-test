# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T10:37:25.460463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `-0.0616` n `232`; crypto_major avg `0.0326` n `8`; equity avg `-0.0017` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0244` n `790`
- 1h: commodity avg `-0.0376` n `12`; crypto_alt avg `-0.0446` n `232`; crypto_major avg `-0.0471` n `8`; equity avg `0.0097` n `134`; fx avg `-0.0016` n `6`; index avg `0.0093` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.2292` n `788`
- 4h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.3306` n `232`; crypto_major avg `0.7201` n `8`; equity avg `0.0436` n `134`; fx avg `-0.0103` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0128` n `20`; unknown avg `0.6677` n `780`
- 24h: commodity avg `0.1206` n `12`; crypto_alt avg `0.7338` n `232`; crypto_major avg `-1.1672` n `8`; equity avg `0.7961` n `134`; fx avg `-0.1103` n `6`; index avg `0.0511` n `26`; metal avg `-0.1147` n `20`; unknown avg `16.3625` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
