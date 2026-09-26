# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T18:22:36.168437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0673` n `234`; crypto_major avg `-0.046` n `8`; equity avg `-0.0252` n `141`; fx avg `-0.0054` n `6`; index avg `-0.0171` n `26`; metal avg `-0.0053` n `20`; unknown avg `1.666` n `961`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.1338` n `234`; crypto_major avg `-0.1173` n `8`; equity avg `-0.0239` n `141`; fx avg `0.0034` n `6`; index avg `-0.0239` n `26`; metal avg `-0.0061` n `20`; unknown avg `2.9096` n `959`
- 4h: commodity avg `-0.0115` n `12`; crypto_alt avg `0.4708` n `234`; crypto_major avg `-0.046` n `8`; equity avg `0.0416` n `141`; fx avg `-0.0111` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0065` n `20`; unknown avg `12.6419` n `945`
- 24h: commodity avg `0.3379` n `12`; crypto_alt avg `2.0884` n `234`; crypto_major avg `-0.5196` n `8`; equity avg `-0.1001` n `141`; fx avg `0.0128` n `6`; index avg `-0.0442` n `26`; metal avg `-0.0308` n `20`; unknown avg `3.7576` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
