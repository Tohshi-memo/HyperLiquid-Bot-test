# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T04:22:20.184944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1228` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0458` n `12`; crypto_alt avg `0.1263` n `228`; crypto_major avg `0.0862` n `8`; equity avg `0.0646` n `72`; fx avg `-0.0014` n `6`; index avg `-0.0589` n `23`; metal avg `-0.0946` n `18`; unknown avg `-0.735` n `420`
- 1h: commodity avg `0.122` n `12`; crypto_alt avg `-0.2377` n `228`; crypto_major avg `0.0233` n `8`; equity avg `0.2607` n `72`; fx avg `0.0077` n `6`; index avg `0.0023` n `23`; metal avg `-0.062` n `18`; unknown avg `-0.0122` n `420`
- 4h: commodity avg `0.1052` n `12`; crypto_alt avg `-0.2616` n `228`; crypto_major avg `-0.9494` n `8`; equity avg `0.1908` n `72`; fx avg `0.0373` n `6`; index avg `0.1734` n `23`; metal avg `0.0688` n `18`; unknown avg `-0.027` n `419`
- 24h: commodity avg `0.9232` n `12`; crypto_alt avg `-4.4864` n `228`; crypto_major avg `-6.0687` n `8`; equity avg `1.3042` n `72`; fx avg `0.0235` n `6`; index avg `1.4608` n `23`; metal avg `-0.1752` n `18`; unknown avg `-1.5139` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
