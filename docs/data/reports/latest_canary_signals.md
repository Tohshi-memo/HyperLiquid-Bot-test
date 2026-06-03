# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T04:07:22.502868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0578` n `12`; crypto_alt avg `0.8556` n `228`; crypto_major avg `0.7925` n `8`; equity avg `0.1679` n `72`; fx avg `0.0083` n `6`; index avg `0.0418` n `23`; metal avg `0.0678` n `18`; unknown avg `0.1561` n `420`
- 1h: commodity avg `0.0879` n `12`; crypto_alt avg `-0.5423` n `228`; crypto_major avg `-0.4508` n `8`; equity avg `0.1962` n `72`; fx avg `0.0065` n `6`; index avg `0.0861` n `23`; metal avg `0.0512` n `18`; unknown avg `2.8646` n `420`
- 4h: commodity avg `0.0831` n `12`; crypto_alt avg `0.3936` n `228`; crypto_major avg `-0.3855` n `8`; equity avg `0.1169` n `72`; fx avg `0.055` n `6`; index avg `0.214` n `23`; metal avg `0.1875` n `18`; unknown avg `-0.4584` n `419`
- 24h: commodity avg `0.8017` n `12`; crypto_alt avg `-4.7379` n `228`; crypto_major avg `-6.2807` n `8`; equity avg `1.1561` n `72`; fx avg `0.0459` n `6`; index avg `1.6016` n `23`; metal avg `-0.0245` n `18`; unknown avg `-0.5439` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
