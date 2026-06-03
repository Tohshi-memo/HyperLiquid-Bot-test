# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T03:07:19.718010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0712` n `12`; crypto_alt avg `0.1432` n `228`; crypto_major avg `0.018` n `8`; equity avg `0.0031` n `72`; fx avg `-0.0072` n `6`; index avg `0.0421` n `23`; metal avg `0.2297` n `18`; unknown avg `-0.1775` n `420`
- 1h: commodity avg `-0.1006` n `12`; crypto_alt avg `0.013` n `228`; crypto_major avg `0.0006` n `8`; equity avg `-0.0891` n `72`; fx avg `0.0311` n `6`; index avg `-0.059` n `23`; metal avg `0.3112` n `18`; unknown avg `-0.46` n `419`
- 4h: commodity avg `-0.0914` n `12`; crypto_alt avg `0.8513` n `228`; crypto_major avg `0.2857` n `8`; equity avg `-0.1378` n `72`; fx avg `0.0393` n `6`; index avg `0.2473` n `23`; metal avg `0.1701` n `18`; unknown avg `-0.3048` n `419`
- 24h: commodity avg `0.5236` n `12`; crypto_alt avg `-3.9325` n `228`; crypto_major avg `-6.0321` n `8`; equity avg `1.4159` n `72`; fx avg `0.0495` n `6`; index avg `1.4816` n `23`; metal avg `0.083` n `18`; unknown avg `-1.0504` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
