# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T19:22:34.832485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2506` n `12`; crypto_alt avg `-0.0214` n `228`; crypto_major avg `-0.0145` n `8`; equity avg `-0.0791` n `74`; fx avg `-0.0039` n `6`; index avg `-0.065` n `23`; metal avg `-0.046` n `18`; unknown avg `0.2106` n `643`
- 1h: commodity avg `-0.293` n `12`; crypto_alt avg `0.2097` n `228`; crypto_major avg `-0.032` n `8`; equity avg `0.0454` n `74`; fx avg `-0.0024` n `6`; index avg `0.0521` n `23`; metal avg `-0.1968` n `18`; unknown avg `0.0414` n `643`
- 4h: commodity avg `0.009` n `12`; crypto_alt avg `-1.063` n `228`; crypto_major avg `-0.9228` n `8`; equity avg `-0.6763` n `74`; fx avg `0.0178` n `6`; index avg `-0.1794` n `23`; metal avg `0.203` n `18`; unknown avg `0.0809` n `643`
- 24h: commodity avg `-1.311` n `12`; crypto_alt avg `0.0134` n `228`; crypto_major avg `0.467` n `8`; equity avg `0.3046` n `74`; fx avg `0.0199` n `6`; index avg `0.8847` n `23`; metal avg `0.653` n `18`; unknown avg `40.4042` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
