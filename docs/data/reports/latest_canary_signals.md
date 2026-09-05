# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T11:52:26.347625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `0.0324` n `232`; crypto_major avg `0.0124` n `8`; equity avg `-0.0069` n `134`; fx avg `0.0004` n `6`; index avg `-0.0034` n `26`; metal avg `0.0007` n `20`; unknown avg `0.1894` n `791`
- 1h: commodity avg `0.0353` n `12`; crypto_alt avg `-0.0071` n `232`; crypto_major avg `0.0141` n `8`; equity avg `0.0244` n `134`; fx avg `0.0021` n `6`; index avg `0.0079` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0343` n `786`
- 4h: commodity avg `0.0293` n `12`; crypto_alt avg `0.2597` n `232`; crypto_major avg `0.3147` n `8`; equity avg `0.0854` n `134`; fx avg `-0.0128` n `6`; index avg `0.0302` n `26`; metal avg `-0.0143` n `20`; unknown avg `-0.178` n `780`
- 24h: commodity avg `0.1652` n `12`; crypto_alt avg `0.4346` n `232`; crypto_major avg `-1.3832` n `8`; equity avg `0.8334` n `134`; fx avg `-0.1056` n `6`; index avg `0.0637` n `26`; metal avg `-0.1468` n `20`; unknown avg `16.8966` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
