# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T14:52:26.351139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `12`; crypto_alt avg `-0.0975` n `232`; crypto_major avg `-0.0365` n `8`; equity avg `0.0026` n `134`; fx avg `-0.0044` n `6`; index avg `0.0105` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.1929` n `794`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `0.1692` n `232`; crypto_major avg `0.3556` n `8`; equity avg `0.0321` n `134`; fx avg `0.0031` n `6`; index avg `0.0049` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.0699` n `788`
- 4h: commodity avg `0.0634` n `12`; crypto_alt avg `0.2012` n `232`; crypto_major avg `0.7918` n `8`; equity avg `0.0266` n `134`; fx avg `0.0163` n `6`; index avg `0.0092` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.2493` n `728`
- 24h: commodity avg `0.0383` n `12`; crypto_alt avg `3.3921` n `232`; crypto_major avg `2.4749` n `8`; equity avg `0.7263` n `134`; fx avg `-0.0024` n `6`; index avg `0.0807` n `26`; metal avg `0.0969` n `20`; unknown avg `0.4206` n `656`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
