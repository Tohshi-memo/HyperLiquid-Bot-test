# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T18:37:33.652079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1496` n `12`; crypto_alt avg `-0.0946` n `234`; crypto_major avg `0.1392` n `8`; equity avg `-0.0333` n `141`; fx avg `-0.0037` n `6`; index avg `-0.0155` n `26`; metal avg `0.0015` n `20`; unknown avg `1.7426` n `943`
- 1h: commodity avg `0.1454` n `12`; crypto_alt avg `-0.6312` n `234`; crypto_major avg `-0.1712` n `8`; equity avg `0.1293` n `141`; fx avg `-0.0332` n `6`; index avg `0.0255` n `26`; metal avg `0.0987` n `20`; unknown avg `3.5118` n `941`
- 4h: commodity avg `0.29` n `12`; crypto_alt avg `-1.7996` n `234`; crypto_major avg `-1.0382` n `8`; equity avg `0.0158` n `141`; fx avg `-0.0375` n `6`; index avg `-0.0383` n `26`; metal avg `-0.0435` n `20`; unknown avg `2.8502` n `919`
- 24h: commodity avg `0.559` n `12`; crypto_alt avg `-3.1111` n `234`; crypto_major avg `-3.5636` n `8`; equity avg `-1.2623` n `140`; fx avg `-0.0233` n `6`; index avg `-0.3442` n `26`; metal avg `-0.7656` n `20`; unknown avg `12.9334` n `878`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
