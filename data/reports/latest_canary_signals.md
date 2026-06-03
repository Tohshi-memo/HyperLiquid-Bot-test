# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T03:22:24.607860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.1804` n `228`; crypto_major avg `-0.3877` n `8`; equity avg `0.0013` n `72`; fx avg `-0.0026` n `6`; index avg `0.0248` n `23`; metal avg `0.0185` n `18`; unknown avg `2.4155` n `420`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `0.123` n `228`; crypto_major avg `-0.2231` n `8`; equity avg `0.0498` n `72`; fx avg `0.0236` n `6`; index avg `-0.0234` n `23`; metal avg `0.3169` n `18`; unknown avg `-0.3149` n `420`
- 4h: commodity avg `-0.3412` n `12`; crypto_alt avg `0.8815` n `228`; crypto_major avg `0.0474` n `8`; equity avg `0.2422` n `72`; fx avg `0.0529` n `6`; index avg `0.421` n `23`; metal avg `0.4764` n `18`; unknown avg `-0.5857` n `419`
- 24h: commodity avg `0.5884` n `12`; crypto_alt avg `-4.1505` n `228`; crypto_major avg `-6.3385` n `8`; equity avg `1.423` n `72`; fx avg `0.0444` n `6`; index avg `1.5763` n `23`; metal avg `0.2125` n `18`; unknown avg `-0.5797` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
