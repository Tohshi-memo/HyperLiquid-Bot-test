# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T13:37:19.062187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0486` n `12`; crypto_alt avg `-0.5686` n `228`; crypto_major avg `-0.8462` n `8`; equity avg `-0.7555` n `66`; fx avg `-0.0024` n `5`; index avg `-0.2988` n `23`; metal avg `0.1079` n `18`; unknown avg `0.1131` n `383`
- 1h: commodity avg `-0.4699` n `12`; crypto_alt avg `-0.8027` n `228`; crypto_major avg `-0.8906` n `8`; equity avg `-0.3308` n `66`; fx avg `-0.0227` n `5`; index avg `0.0293` n `23`; metal avg `0.388` n `18`; unknown avg `0.4216` n `383`
- 4h: commodity avg `-0.8728` n `12`; crypto_alt avg `0.158` n `228`; crypto_major avg `0.0143` n `8`; equity avg `-0.1948` n `66`; fx avg `-0.0158` n `5`; index avg `0.1041` n `23`; metal avg `0.9177` n `18`; unknown avg `0.3214` n `383`
- 24h: commodity avg `-0.246` n `12`; crypto_alt avg `-2.4871` n `228`; crypto_major avg `-1.5929` n `8`; equity avg `0.0572` n `65`; fx avg `0.0627` n `5`; index avg `0.3169` n `23`; metal avg `0.989` n `18`; unknown avg `-0.2618` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
