# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T14:22:32.871660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `12`; crypto_alt avg `-0.5091` n `229`; crypto_major avg `-0.609` n `8`; equity avg `-0.2671` n `91`; fx avg `0.0164` n `6`; index avg `-0.0194` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0073` n `766`
- 1h: commodity avg `-0.2348` n `12`; crypto_alt avg `-0.4418` n `229`; crypto_major avg `-0.63` n `8`; equity avg `-0.7046` n `91`; fx avg `-0.0325` n `6`; index avg `0.0344` n `25`; metal avg `0.0977` n `20`; unknown avg `-0.0462` n `766`
- 4h: commodity avg `-0.2843` n `12`; crypto_alt avg `-0.5578` n `229`; crypto_major avg `-0.9417` n `8`; equity avg `-0.6362` n `91`; fx avg `-0.0543` n `6`; index avg `0.0167` n `25`; metal avg `0.0835` n `20`; unknown avg `-0.0966` n `766`
- 24h: commodity avg `-0.7818` n `12`; crypto_alt avg `0.6252` n `229`; crypto_major avg `1.0273` n `8`; equity avg `-0.3033` n `91`; fx avg `-0.1547` n `6`; index avg `0.1248` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.2055` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
