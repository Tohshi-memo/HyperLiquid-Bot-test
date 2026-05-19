# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T15:07:22.442190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.2189` n `228`; crypto_major avg `0.2966` n `8`; equity avg `0.28` n `66`; fx avg `-0.0187` n `6`; index avg `0.0774` n `23`; metal avg `-0.1026` n `18`; unknown avg `0.1845` n `383`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.4426` n `228`; crypto_major avg `-0.2057` n `8`; equity avg `0.2605` n `66`; fx avg `0.0117` n `6`; index avg `0.0161` n `23`; metal avg `-0.3894` n `18`; unknown avg `0.0467` n `383`
- 4h: commodity avg `0.0538` n `12`; crypto_alt avg `-0.5692` n `228`; crypto_major avg `-0.5234` n `8`; equity avg `-0.637` n `66`; fx avg `-0.0226` n `6`; index avg `-0.7382` n `23`; metal avg `-1.6987` n `18`; unknown avg `-0.5623` n `383`
- 24h: commodity avg `0.6669` n `12`; crypto_alt avg `0.9981` n `228`; crypto_major avg `1.1503` n `8`; equity avg `-1.0246` n `66`; fx avg `0.2072` n `6`; index avg `-1.1767` n `23`; metal avg `-1.8712` n `18`; unknown avg `-0.4398` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
