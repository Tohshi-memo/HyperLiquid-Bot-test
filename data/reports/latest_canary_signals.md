# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T08:22:28.077340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0405` n `13`; crypto_alt avg `0.1046` n `239`; crypto_major avg `0.3863` n `8`; equity avg `0.1447` n `166`; fx avg `0.0008` n `6`; index avg `0.0269` n `27`; metal avg `-0.0077` n `20`; unknown avg `0.2132` n `1250`
- 1h: commodity avg `0.0041` n `13`; crypto_alt avg `-0.2636` n `239`; crypto_major avg `-0.0332` n `8`; equity avg `-0.0491` n `166`; fx avg `-0.0067` n `6`; index avg `-0.0128` n `27`; metal avg `-0.0387` n `20`; unknown avg `1.112` n `1236`
- 4h: commodity avg `0.1421` n `13`; crypto_alt avg `0.1275` n `239`; crypto_major avg `-0.1867` n `8`; equity avg `-0.2986` n `166`; fx avg `0.0319` n `6`; index avg `-0.0451` n `27`; metal avg `-0.1562` n `20`; unknown avg `0.0813` n `1200`
- 24h: commodity avg `-0.7369` n `13`; crypto_alt avg `0.3208` n `239`; crypto_major avg `0.0508` n `8`; equity avg `3.7641` n `166`; fx avg `-0.2265` n `6`; index avg `0.5989` n `27`; metal avg `-0.1483` n `20`; unknown avg `856.9733` n `1064`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
