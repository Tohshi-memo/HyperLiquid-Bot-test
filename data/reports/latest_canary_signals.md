# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T21:07:29.438536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `0.079` n `228`; crypto_major avg `0.088` n `8`; equity avg `0.0101` n `74`; fx avg `0.0081` n `6`; index avg `0.0045` n `23`; metal avg `-0.2674` n `18`; unknown avg `5.329` n `644`
- 1h: commodity avg `0.0564` n `12`; crypto_alt avg `-0.0145` n `228`; crypto_major avg `0.0822` n `8`; equity avg `0.0121` n `74`; fx avg `0.0171` n `6`; index avg `0.0221` n `23`; metal avg `-0.2365` n `18`; unknown avg `4.709` n `644`
- 4h: commodity avg `0.0213` n `12`; crypto_alt avg `0.0019` n `228`; crypto_major avg `0.2309` n `8`; equity avg `0.2663` n `74`; fx avg `0.0512` n `6`; index avg `0.011` n `23`; metal avg `-0.0483` n `18`; unknown avg `1.4467` n `644`
- 24h: commodity avg `-0.4973` n `12`; crypto_alt avg `2.1611` n `228`; crypto_major avg `0.7258` n `8`; equity avg `0.5288` n `74`; fx avg `0.0952` n `6`; index avg `0.6039` n `23`; metal avg `0.0025` n `18`; unknown avg `-0.2797` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
