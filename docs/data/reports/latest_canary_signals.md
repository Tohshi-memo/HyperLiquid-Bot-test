# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T00:07:25.544672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.587` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0643` n `12`; crypto_alt avg `0.451` n `228`; crypto_major avg `0.2864` n `8`; equity avg `0.2258` n `73`; fx avg `-0.002` n `6`; index avg `0.0103` n `23`; metal avg `-0.0659` n `18`; unknown avg `-0.0231` n `419`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `0.3252` n `228`; crypto_major avg `0.0594` n `8`; equity avg `0.125` n `73`; fx avg `-0.0159` n `6`; index avg `-0.0588` n `23`; metal avg `0.1553` n `18`; unknown avg `-0.5774` n `419`
- 4h: commodity avg `-0.2415` n `12`; crypto_alt avg `0.1279` n `228`; crypto_major avg `0.0795` n `8`; equity avg `-1.5075` n `73`; fx avg `-0.04` n `6`; index avg `-0.5041` n `23`; metal avg `0.2315` n `18`; unknown avg `0.0936` n `419`
- 24h: commodity avg `0.367` n `12`; crypto_alt avg `2.29` n `228`; crypto_major avg `-0.9705` n `8`; equity avg `-3.6041` n `72`; fx avg `0.0567` n `6`; index avg `-1.0691` n `23`; metal avg `-1.8143` n `18`; unknown avg `0.7534` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
