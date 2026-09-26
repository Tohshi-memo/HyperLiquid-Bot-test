# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T16:22:32.276689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.0408` n `234`; crypto_major avg `-0.0977` n `8`; equity avg `0.0106` n `141`; fx avg `0.0029` n `6`; index avg `0.0021` n `26`; metal avg `0.0001` n `20`; unknown avg `0.1136` n `961`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `0.3049` n `234`; crypto_major avg `0.0715` n `8`; equity avg `0.0143` n `141`; fx avg `-0.0017` n `6`; index avg `0.0045` n `26`; metal avg `-0.0098` n `20`; unknown avg `-0.0938` n `945`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `0.9621` n `234`; crypto_major avg `0.1705` n `8`; equity avg `0.0944` n `141`; fx avg `-0.002` n `6`; index avg `0.0146` n `26`; metal avg `-0.0044` n `20`; unknown avg `5.3684` n `945`
- 24h: commodity avg `0.463` n `12`; crypto_alt avg `3.2938` n `234`; crypto_major avg `0.1091` n `8`; equity avg `-0.0845` n `141`; fx avg `0.0316` n `6`; index avg `0.005` n `26`; metal avg `-0.0321` n `20`; unknown avg `0.5883` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
