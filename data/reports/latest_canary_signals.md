# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T21:06:37.553531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.07` n `12`; crypto_alt avg `-0.0626` n `228`; crypto_major avg `0.026` n `8`; equity avg `0.0506` n `66`; fx avg `0.0077` n `6`; index avg `0.0055` n `23`; metal avg `0.0204` n `18`; unknown avg `-0.0472` n `383`
- 1h: commodity avg `-0.1818` n `12`; crypto_alt avg `0.0714` n `228`; crypto_major avg `0.0369` n `8`; equity avg `0.0339` n `66`; fx avg `-0.0253` n `6`; index avg `-0.121` n `23`; metal avg `0.0263` n `18`; unknown avg `-0.1264` n `383`
- 4h: commodity avg `0.0346` n `12`; crypto_alt avg `-0.2927` n `228`; crypto_major avg `-0.2511` n `8`; equity avg `-0.422` n `66`; fx avg `0.0227` n `6`; index avg `-0.3143` n `23`; metal avg `-0.5553` n `18`; unknown avg `1.1912` n `383`
- 24h: commodity avg `0.8867` n `12`; crypto_alt avg `0.1381` n `228`; crypto_major avg `0.2032` n `8`; equity avg `0.1979` n `66`; fx avg `0.0543` n `6`; index avg `-0.5556` n `23`; metal avg `-2.7228` n `18`; unknown avg `0.8717` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
