# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T04:37:21.088895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.066` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.1725` n `228`; crypto_major avg `-0.0588` n `8`; equity avg `-0.0146` n `72`; fx avg `-0.0076` n `6`; index avg `0.0417` n `23`; metal avg `-0.1913` n `18`; unknown avg `0.3694` n `420`
- 1h: commodity avg `0.1275` n `12`; crypto_alt avg `0.5576` n `228`; crypto_major avg `0.5142` n `8`; equity avg `0.1734` n `72`; fx avg `-0.0004` n `6`; index avg `0.0298` n `23`; metal avg `-0.2256` n `18`; unknown avg `0.1505` n `420`
- 4h: commodity avg `0.0632` n `12`; crypto_alt avg `-0.2788` n `228`; crypto_major avg `-1.0437` n `8`; equity avg `0.1692` n `72`; fx avg `0.0326` n `6`; index avg `0.0223` n `23`; metal avg `-0.2088` n `18`; unknown avg `-0.915` n `419`
- 24h: commodity avg `0.8893` n `12`; crypto_alt avg `-4.4636` n `228`; crypto_major avg `-6.1547` n `8`; equity avg `1.2076` n `72`; fx avg `0.0142` n `6`; index avg `1.4937` n `23`; metal avg `-0.4416` n `18`; unknown avg `-0.7151` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
