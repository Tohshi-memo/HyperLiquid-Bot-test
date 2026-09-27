# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T19:37:40.243824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.1171` n `234`; crypto_major avg `-0.0621` n `8`; equity avg `0.0128` n `141`; fx avg `0.0004` n `6`; index avg `0.0028` n `26`; metal avg `0.0017` n `20`; unknown avg `1.1201` n `962`
- 1h: commodity avg `-0.0434` n `12`; crypto_alt avg `0.042` n `234`; crypto_major avg `-0.0644` n `8`; equity avg `0.0137` n `141`; fx avg `0.0011` n `6`; index avg `-0.0002` n `26`; metal avg `0.0084` n `20`; unknown avg `0.8949` n `934`
- 4h: commodity avg `-0.0767` n `12`; crypto_alt avg `1.4899` n `234`; crypto_major avg `0.616` n `8`; equity avg `0.1805` n `141`; fx avg `0.0046` n `6`; index avg `0.0218` n `26`; metal avg `0.0149` n `20`; unknown avg `1.1165` n `928`
- 24h: commodity avg `-0.1507` n `12`; crypto_alt avg `0.8811` n `234`; crypto_major avg `0.6579` n `8`; equity avg `0.4157` n `141`; fx avg `-0.0204` n `6`; index avg `0.0386` n `26`; metal avg `-0.004` n `20`; unknown avg `119.0712` n `871`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
