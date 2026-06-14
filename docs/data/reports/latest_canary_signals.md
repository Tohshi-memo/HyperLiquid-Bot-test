# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T00:52:33.047346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.052` n `12`; crypto_alt avg `-0.217` n `228`; crypto_major avg `-0.1504` n `8`; equity avg `-0.0235` n `74`; fx avg `0.0036` n `6`; index avg `0.059` n `23`; metal avg `0.1927` n `18`; unknown avg `0.1271` n `645`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.1529` n `228`; crypto_major avg `-0.0307` n `8`; equity avg `0.0185` n `74`; fx avg `0.0061` n `6`; index avg `0.0234` n `23`; metal avg `0.0256` n `18`; unknown avg `-0.511` n `645`
- 4h: commodity avg `-0.1959` n `12`; crypto_alt avg `-0.0337` n `228`; crypto_major avg `0.4305` n `8`; equity avg `0.0931` n `74`; fx avg `-0.0302` n `6`; index avg `-0.0125` n `23`; metal avg `-0.0123` n `18`; unknown avg `6.6736` n `644`
- 24h: commodity avg `-0.7037` n `12`; crypto_alt avg `1.8005` n `228`; crypto_major avg `1.4217` n `8`; equity avg `0.2609` n `74`; fx avg `0.019` n `6`; index avg `0.3549` n `23`; metal avg `0.2431` n `18`; unknown avg `0.789` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
