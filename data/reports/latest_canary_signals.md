# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T16:37:39.460787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0423` n `12`; crypto_alt avg `-0.061` n `230`; crypto_major avg `-0.1552` n `8`; equity avg `-0.1681` n `103`; fx avg `-0.0027` n `6`; index avg `-0.0205` n `25`; metal avg `0.074` n `20`; unknown avg `0.0447` n `784`
- 1h: commodity avg `0.0508` n `12`; crypto_alt avg `0.0605` n `230`; crypto_major avg `0.0874` n `8`; equity avg `0.4435` n `103`; fx avg `0.0207` n `6`; index avg `0.0506` n `25`; metal avg `0.0763` n `20`; unknown avg `-0.0158` n `784`
- 4h: commodity avg `0.0701` n `12`; crypto_alt avg `1.0031` n `230`; crypto_major avg `1.4667` n `8`; equity avg `2.543` n `103`; fx avg `-0.0218` n `6`; index avg `0.218` n `25`; metal avg `0.011` n `20`; unknown avg `0.0772` n `784`
- 24h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.2343` n `230`; crypto_major avg `1.0033` n `8`; equity avg `1.5605` n `102`; fx avg `-0.171` n `6`; index avg `-0.0067` n `25`; metal avg `-0.4237` n `20`; unknown avg `0.0917` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
