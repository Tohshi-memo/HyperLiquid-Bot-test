# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T08:37:33.653892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0589` n `12`; crypto_alt avg `0.0625` n `234`; crypto_major avg `-0.0012` n `8`; equity avg `0.0688` n `141`; fx avg `-0.0111` n `6`; index avg `0.0149` n `26`; metal avg `0.0547` n `20`; unknown avg `-0.0098` n `946`
- 1h: commodity avg `-0.0696` n `12`; crypto_alt avg `1.2962` n `234`; crypto_major avg `0.8519` n `8`; equity avg `0.2452` n `141`; fx avg `-0.01` n `6`; index avg `0.0386` n `26`; metal avg `0.1344` n `20`; unknown avg `0.6077` n `926`
- 4h: commodity avg `-0.0658` n `12`; crypto_alt avg `1.1826` n `234`; crypto_major avg `0.5216` n `8`; equity avg `0.51` n `141`; fx avg `-0.0299` n `6`; index avg `0.1095` n `26`; metal avg `0.1427` n `20`; unknown avg `1.8445` n `904`
- 24h: commodity avg `-0.0834` n `12`; crypto_alt avg `3.7617` n `234`; crypto_major avg `1.5377` n `8`; equity avg `1.9644` n `141`; fx avg `-0.2063` n `6`; index avg `0.2944` n `26`; metal avg `0.0859` n `20`; unknown avg `13.9078` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
