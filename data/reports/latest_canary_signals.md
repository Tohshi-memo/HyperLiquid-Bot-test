# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T13:22:26.084349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.2695` n `232`; crypto_major avg `-0.3487` n `8`; equity avg `-0.0758` n `134`; fx avg `-0.0102` n `6`; index avg `0.0058` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.3499` n `760`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.4539` n `232`; crypto_major avg `-0.3855` n `8`; equity avg `-0.1428` n `134`; fx avg `-0.0009` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.2434` n `736`
- 4h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.062` n `232`; crypto_major avg `-0.1378` n `8`; equity avg `0.0356` n `134`; fx avg `0.0113` n `6`; index avg `0.0074` n `26`; metal avg `-0.0275` n `20`; unknown avg `65.9153` n `736`
- 24h: commodity avg `0.1341` n `12`; crypto_alt avg `1.4846` n `232`; crypto_major avg `1.0521` n `8`; equity avg `0.4139` n `134`; fx avg `-0.0337` n `6`; index avg `0.0601` n `26`; metal avg `0.0118` n `20`; unknown avg `0.7063` n `630`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
