# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T07:23:02.579932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.0839` n `234`; crypto_major avg `-0.0052` n `8`; equity avg `0.0017` n `141`; fx avg `0.0032` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.0095` n `961`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `0.4688` n `234`; crypto_major avg `0.1409` n `8`; equity avg `0.0257` n `141`; fx avg `0.0138` n `6`; index avg `-0.002` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0235` n `959`
- 4h: commodity avg `-0.0468` n `12`; crypto_alt avg `0.9823` n `234`; crypto_major avg `-0.1947` n `8`; equity avg `0.0235` n `141`; fx avg `-0.0038` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.9842` n `929`
- 24h: commodity avg `-0.0582` n `12`; crypto_alt avg `3.4668` n `234`; crypto_major avg `0.8764` n `8`; equity avg `-0.6781` n `141`; fx avg `-0.0776` n `6`; index avg `0.0444` n `26`; metal avg `0.236` n `20`; unknown avg `1127.3464` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
