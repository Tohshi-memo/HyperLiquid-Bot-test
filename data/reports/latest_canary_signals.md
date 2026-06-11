# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T06:22:25.822474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1108` n `12`; crypto_alt avg `0.4713` n `228`; crypto_major avg `0.5531` n `8`; equity avg `0.3001` n `74`; fx avg `0.0079` n `6`; index avg `0.1851` n `23`; metal avg `0.2702` n `18`; unknown avg `0.0016` n `556`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `-0.0696` n `228`; crypto_major avg `0.4464` n `8`; equity avg `0.098` n `74`; fx avg `0.0262` n `6`; index avg `0.1022` n `23`; metal avg `0.1404` n `18`; unknown avg `-0.0398` n `540`
- 4h: commodity avg `-0.3069` n `12`; crypto_alt avg `1.4999` n `228`; crypto_major avg `1.4572` n `8`; equity avg `0.9148` n `74`; fx avg `-0.001` n `6`; index avg `0.4276` n `23`; metal avg `0.1235` n `18`; unknown avg `3.2293` n `540`
- 24h: commodity avg `1.9285` n `12`; crypto_alt avg `1.4292` n `228`; crypto_major avg `1.4201` n `8`; equity avg `-0.3746` n `74`; fx avg `0.0234` n `6`; index avg `-0.4524` n `23`; metal avg `-1.0493` n `18`; unknown avg `3.7657` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
