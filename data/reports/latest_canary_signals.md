# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T23:52:26.409756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.059` n `232`; crypto_major avg `0.0808` n `8`; equity avg `0.0147` n `134`; fx avg `0.0` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0054` n `20`; unknown avg `-0.2434` n `794`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.0214` n `232`; crypto_major avg `-0.0931` n `8`; equity avg `0.0252` n `134`; fx avg `-0.0083` n `6`; index avg `0.0012` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.0361` n `792`
- 4h: commodity avg `-0.0113` n `12`; crypto_alt avg `0.4404` n `232`; crypto_major avg `-0.2512` n `8`; equity avg `0.1125` n `134`; fx avg `-0.0074` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.0345` n `770`
- 24h: commodity avg `0.1312` n `12`; crypto_alt avg `2.8694` n `232`; crypto_major avg `2.1594` n `8`; equity avg `0.2729` n `134`; fx avg `-0.0607` n `6`; index avg `0.0796` n `26`; metal avg `0.058` n `20`; unknown avg `13385.266` n `702`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
