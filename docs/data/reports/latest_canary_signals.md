# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T23:58:53.584686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7426` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0374` n `12`; crypto_alt avg `-0.192` n `228`; crypto_major avg `-0.1928` n `8`; equity avg `0.0415` n `73`; fx avg `-0.0009` n `6`; index avg `-0.0295` n `23`; metal avg `0.076` n `18`; unknown avg `-0.2944` n `419`
- 1h: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.7903` n `228`; crypto_major avg `-0.7509` n `8`; equity avg `-0.3732` n `73`; fx avg `0.0212` n `6`; index avg `-0.0562` n `23`; metal avg `0.3542` n `18`; unknown avg `-0.644` n `419`
- 4h: commodity avg `-0.1356` n `12`; crypto_alt avg `-0.4058` n `228`; crypto_major avg `-0.2316` n `8`; equity avg `-1.9742` n `73`; fx avg `-0.0345` n `6`; index avg `-0.6297` n `23`; metal avg `0.1317` n `18`; unknown avg `0.1391` n `419`
- 24h: commodity avg `0.2904` n `12`; crypto_alt avg `2.0806` n `228`; crypto_major avg `-1.091` n `8`; equity avg `-3.6359` n `72`; fx avg `0.0736` n `6`; index avg `-1.0179` n `23`; metal avg `-1.6429` n `18`; unknown avg `0.8167` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
