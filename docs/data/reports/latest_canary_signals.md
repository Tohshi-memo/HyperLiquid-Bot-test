# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T06:37:14.080273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1732` n `12`; crypto_alt avg `0.0222` n `228`; crypto_major avg `-0.0063` n `8`; equity avg `0.0262` n `66`; fx avg `-0.01` n `6`; index avg `0.0027` n `23`; metal avg `-0.1185` n `18`; unknown avg `0.0389` n `383`
- 1h: commodity avg `0.1632` n `12`; crypto_alt avg `0.1084` n `228`; crypto_major avg `0.0399` n `8`; equity avg `0.1393` n `66`; fx avg `0.0069` n `6`; index avg `0.0391` n `23`; metal avg `0.2236` n `18`; unknown avg `0.1437` n `363`
- 4h: commodity avg `0.2483` n `12`; crypto_alt avg `0.5501` n `228`; crypto_major avg `0.2442` n `8`; equity avg `0.243` n `66`; fx avg `0.0556` n `6`; index avg `0.1279` n `23`; metal avg `-0.0431` n `18`; unknown avg `0.2905` n `363`
- 24h: commodity avg `0.3468` n `12`; crypto_alt avg `1.7732` n `228`; crypto_major avg `0.9382` n `8`; equity avg `-0.7413` n `66`; fx avg `0.3131` n `6`; index avg `-0.2658` n `23`; metal avg `0.4954` n `18`; unknown avg `0.778` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
