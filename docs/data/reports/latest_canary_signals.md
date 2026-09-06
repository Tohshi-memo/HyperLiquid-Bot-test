# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T13:07:24.964978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.012` n `232`; crypto_major avg `0.0066` n `8`; equity avg `-0.0658` n `134`; fx avg `0.0064` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0025` n `20`; unknown avg `1.1284` n `774`
- 1h: commodity avg `0.0373` n `12`; crypto_alt avg `-0.0947` n `232`; crypto_major avg `0.1781` n `8`; equity avg `-0.0137` n `134`; fx avg `0.0054` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0018` n `20`; unknown avg `63.472` n `768`
- 4h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.554` n `232`; crypto_major avg `0.4577` n `8`; equity avg `0.1449` n `134`; fx avg `0.0227` n `6`; index avg `0.0069` n `26`; metal avg `-0.0021` n `20`; unknown avg `63.5482` n `768`
- 24h: commodity avg `0.1366` n `12`; crypto_alt avg `1.7105` n `232`; crypto_major avg `1.5366` n `8`; equity avg `0.489` n `134`; fx avg `-0.012` n `6`; index avg `0.0507` n `26`; metal avg `0.0149` n `20`; unknown avg `0.3566` n `662`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
