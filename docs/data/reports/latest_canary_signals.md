# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T17:22:21.748403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `0.1671` n `228`; crypto_major avg `0.1088` n `8`; equity avg `-0.1487` n `67`; fx avg `0.0016` n `6`; index avg `-0.0808` n `23`; metal avg `-0.0539` n `18`; unknown avg `0.0444` n `419`
- 1h: commodity avg `0.0514` n `12`; crypto_alt avg `0.5173` n `228`; crypto_major avg `0.4741` n `8`; equity avg `-0.0756` n `67`; fx avg `-0.0119` n `6`; index avg `0.0282` n `23`; metal avg `-0.0412` n `18`; unknown avg `-0.0685` n `419`
- 4h: commodity avg `0.1154` n `12`; crypto_alt avg `1.3208` n `228`; crypto_major avg `1.718` n `8`; equity avg `1.7324` n `67`; fx avg `-0.028` n `6`; index avg `1.2158` n `23`; metal avg `1.4868` n `18`; unknown avg `0.1628` n `419`
- 24h: commodity avg `0.522` n `12`; crypto_alt avg `-3.8091` n `228`; crypto_major avg `-1.334` n `8`; equity avg `1.4273` n `67`; fx avg `-0.0205` n `6`; index avg `1.0752` n `23`; metal avg `0.6861` n `18`; unknown avg `-1.0615` n `408`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
