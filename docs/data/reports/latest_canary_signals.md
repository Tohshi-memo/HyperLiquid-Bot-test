# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T16:37:32.548424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `0.0569` n `234`; crypto_major avg `0.0734` n `8`; equity avg `0.0127` n `141`; fx avg `0.0004` n `6`; index avg `0.0014` n `26`; metal avg `0.0036` n `20`; unknown avg `0.1434` n `961`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `0.1002` n `234`; crypto_major avg `-0.1199` n `8`; equity avg `0.0146` n `141`; fx avg `0.0007` n `6`; index avg `0.0065` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.0653` n `945`
- 4h: commodity avg `-0.0158` n `12`; crypto_alt avg `1.3357` n `234`; crypto_major avg `0.3416` n `8`; equity avg `0.1207` n `141`; fx avg `-0.0013` n `6`; index avg `0.0191` n `26`; metal avg `0.003` n `20`; unknown avg `3.5399` n `945`
- 24h: commodity avg `0.3523` n `12`; crypto_alt avg `3.0557` n `234`; crypto_major avg `0.0207` n `8`; equity avg `-0.1686` n `141`; fx avg `0.0029` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0297` n `20`; unknown avg `0.7603` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
