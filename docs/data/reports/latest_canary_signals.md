# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T01:22:36.414430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.2108` n `228`; crypto_major avg `0.2178` n `8`; equity avg `0.0377` n `74`; fx avg `0.0084` n `6`; index avg `0.008` n `23`; metal avg `0.0088` n `18`; unknown avg `0.0436` n `645`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.0919` n `228`; crypto_major avg `0.3743` n `8`; equity avg `0.1079` n `74`; fx avg `0.0101` n `6`; index avg `0.0396` n `23`; metal avg `0.0351` n `18`; unknown avg `8.723` n `645`
- 4h: commodity avg `-0.3651` n `12`; crypto_alt avg `0.3371` n `228`; crypto_major avg `0.6501` n `8`; equity avg `0.1366` n `74`; fx avg `-0.0222` n `6`; index avg `-0.028` n `23`; metal avg `0.0787` n `18`; unknown avg `3.2533` n `644`
- 24h: commodity avg `-0.7456` n `12`; crypto_alt avg `1.6911` n `228`; crypto_major avg `1.6835` n `8`; equity avg `0.4946` n `74`; fx avg `0.0083` n `6`; index avg `0.4421` n `23`; metal avg `0.2374` n `18`; unknown avg `0.8033` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
