# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T14:17:30.322982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `-0.2301` n `228`; crypto_major avg `-0.2165` n `8`; equity avg `-0.0431` n `65`; fx avg `0.0` n `5`; index avg `-0.0629` n `23`; metal avg `-0.0126` n `18`; unknown avg `0.0204` n `383`
- 1h: commodity avg `-0.2755` n `12`; crypto_alt avg `-0.2865` n `228`; crypto_major avg `-0.2596` n `8`; equity avg `-0.0211` n `65`; fx avg `0.0` n `5`; index avg `0.012` n `23`; metal avg `-0.0063` n `18`; unknown avg `-0.0386` n `383`
- 4h: commodity avg `-0.2485` n `12`; crypto_alt avg `-1.1169` n `228`; crypto_major avg `-0.6675` n `8`; equity avg `0.0906` n `65`; fx avg `-0.0175` n `5`; index avg `0.0712` n `23`; metal avg `0.0095` n `18`; unknown avg `-0.228` n `383`
- 24h: commodity avg `1.5437` n `12`; crypto_alt avg `-9.5862` n `228`; crypto_major avg `-2.7868` n `8`; equity avg `-2.5849` n `65`; fx avg `-0.1861` n `5`; index avg `-1.6219` n `23`; metal avg `-5.8369` n `18`; unknown avg `549.9064` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
