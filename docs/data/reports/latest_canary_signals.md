# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T17:50:09.526154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.187` n `234`; crypto_major avg `0.1407` n `8`; equity avg `0.023` n `141`; fx avg `0.0006` n `6`; index avg `0.002` n `26`; metal avg `-0.003` n `20`; unknown avg `0.8298` n `962`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.4693` n `234`; crypto_major avg `0.2525` n `8`; equity avg `0.0911` n `141`; fx avg `-0.0052` n `6`; index avg `0.0162` n `26`; metal avg `0.0008` n `20`; unknown avg `1.3741` n `960`
- 4h: commodity avg `-0.1308` n `12`; crypto_alt avg `0.2947` n `234`; crypto_major avg `-0.381` n `8`; equity avg `0.0657` n `141`; fx avg `0.0008` n `6`; index avg `0.0144` n `26`; metal avg `-0.0028` n `20`; unknown avg `5.8584` n `954`
- 24h: commodity avg `-0.1324` n `12`; crypto_alt avg `-0.1475` n `234`; crypto_major avg `0.0399` n `8`; equity avg `0.323` n `141`; fx avg `-0.0228` n `6`; index avg `0.0244` n `26`; metal avg `-0.0127` n `20`; unknown avg `3.3838` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
