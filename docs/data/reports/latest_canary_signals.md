# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T09:07:16.174429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1097` n `12`; crypto_alt avg `-0.0197` n `228`; crypto_major avg `-0.0467` n `8`; equity avg `0.0381` n `66`; fx avg `0.0037` n `5`; index avg `-0.0431` n `23`; metal avg `-0.1575` n `18`; unknown avg `-0.2583` n `383`
- 1h: commodity avg `0.1698` n `12`; crypto_alt avg `-0.0794` n `228`; crypto_major avg `-0.125` n `8`; equity avg `0.417` n `66`; fx avg `0.0043` n `5`; index avg `0.1516` n `23`; metal avg `0.0866` n `18`; unknown avg `-0.0588` n `383`
- 4h: commodity avg `-0.1883` n `12`; crypto_alt avg `-0.8999` n `228`; crypto_major avg `-0.6807` n `8`; equity avg `0.7806` n `66`; fx avg `-0.0658` n `5`; index avg `0.2611` n `23`; metal avg `0.5287` n `18`; unknown avg `-0.2448` n `363`
- 24h: commodity avg `0.6809` n `12`; crypto_alt avg `-2.8005` n `228`; crypto_major avg `-1.3404` n `8`; equity avg `0.6485` n `65`; fx avg `0.0401` n `5`; index avg `0.3282` n `23`; metal avg `0.1293` n `18`; unknown avg `-0.4326` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
