# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T23:07:22.444010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1173` n `12`; crypto_alt avg `-0.6665` n `228`; crypto_major avg `-0.5248` n `8`; equity avg `-0.2679` n `73`; fx avg `0.035` n `6`; index avg `0.0133` n `23`; metal avg `0.1324` n `18`; unknown avg `0.5512` n `419`
- 1h: commodity avg `-0.2264` n `12`; crypto_alt avg `-1.2101` n `228`; crypto_major avg `-1.0134` n `8`; equity avg `-0.6081` n `73`; fx avg `0.0244` n `6`; index avg `-0.0508` n `23`; metal avg `0.1595` n `18`; unknown avg `-0.0878` n `419`
- 4h: commodity avg `-0.2391` n `12`; crypto_alt avg `-1.1273` n `228`; crypto_major avg `-0.9027` n `8`; equity avg `-1.8565` n `73`; fx avg `-0.0079` n `6`; index avg `-0.5522` n `23`; metal avg `-0.1777` n `18`; unknown avg `1.148` n `419`
- 24h: commodity avg `0.2467` n `12`; crypto_alt avg `1.8514` n `228`; crypto_major avg `-0.8234` n `8`; equity avg `-3.7723` n `72`; fx avg `0.064` n `6`; index avg `-0.8901` n `23`; metal avg `-1.9341` n `18`; unknown avg `1.9194` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
