# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T23:37:29.469640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `13`; crypto_alt avg `0.095` n `239`; crypto_major avg `0.1219` n `8`; equity avg `0.0644` n `160`; fx avg `0.0159` n `6`; index avg `0.0014` n `27`; metal avg `0.0052` n `20`; unknown avg `18.7791` n `1262`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `0.244` n `239`; crypto_major avg `0.0923` n `8`; equity avg `0.337` n `160`; fx avg `0.0171` n `6`; index avg `0.0471` n `27`; metal avg `0.0312` n `20`; unknown avg `18.8494` n `1256`
- 4h: commodity avg `0.0523` n `13`; crypto_alt avg `0.7939` n `239`; crypto_major avg `0.5509` n `8`; equity avg `1.314` n `160`; fx avg `0.0133` n `6`; index avg `0.0999` n `27`; metal avg `0.079` n `20`; unknown avg `20.6675` n `1226`
- 24h: commodity avg `0.1033` n `13`; crypto_alt avg `-0.6713` n `239`; crypto_major avg `-2.6611` n `8`; equity avg `-1.0292` n `160`; fx avg `-0.0948` n `6`; index avg `-0.1464` n `27`; metal avg `-0.608` n `20`; unknown avg `21.1061` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2583`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
