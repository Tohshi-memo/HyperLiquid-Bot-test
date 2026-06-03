# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T22:52:28.855941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0521` n `12`; crypto_alt avg `0.0964` n `228`; crypto_major avg `0.002` n `8`; equity avg `-0.1463` n `73`; fx avg `-0.025` n `6`; index avg `-0.0605` n `23`; metal avg `0.0074` n `18`; unknown avg `0.1722` n `419`
- 1h: commodity avg `-0.3569` n `12`; crypto_alt avg `-0.6277` n `228`; crypto_major avg `-0.5616` n `8`; equity avg `-0.2863` n `73`; fx avg `-0.0253` n `6`; index avg `-0.0795` n `23`; metal avg `-0.1193` n `18`; unknown avg `0.1471` n `419`
- 4h: commodity avg `-0.1486` n `12`; crypto_alt avg `-0.2552` n `228`; crypto_major avg `-0.4587` n `8`; equity avg `-1.7526` n `73`; fx avg `0.0077` n `6`; index avg `-0.5341` n `23`; metal avg `-0.2594` n `18`; unknown avg `0.3596` n `419`
- 24h: commodity avg `0.5398` n `12`; crypto_alt avg `2.9562` n `228`; crypto_major avg `0.3466` n `8`; equity avg `-3.5221` n `72`; fx avg `0.0334` n `6`; index avg `-0.9308` n `23`; metal avg `-2.1876` n `18`; unknown avg `0.9758` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
