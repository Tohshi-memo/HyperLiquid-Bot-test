# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T04:37:27.349977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `-0.0528` n `228`; crypto_major avg `-0.071` n `8`; equity avg `-0.0411` n `86`; fx avg `-0.0102` n `6`; index avg `0.0088` n `23`; metal avg `0.001` n `20`; unknown avg `-0.1291` n `716`
- 1h: commodity avg `0.0326` n `12`; crypto_alt avg `0.1642` n `228`; crypto_major avg `-0.23` n `8`; equity avg `0.1571` n `86`; fx avg `-0.0253` n `6`; index avg `0.0443` n `23`; metal avg `0.0239` n `20`; unknown avg `6.0004` n `716`
- 4h: commodity avg `-0.0429` n `12`; crypto_alt avg `0.4119` n `228`; crypto_major avg `-0.1368` n `8`; equity avg `-1.4183` n `86`; fx avg `-0.0669` n `6`; index avg `-0.2699` n `23`; metal avg `-0.6151` n `20`; unknown avg `-0.186` n `708`
- 24h: commodity avg `-0.4999` n `12`; crypto_alt avg `-0.5942` n `228`; crypto_major avg `-0.4672` n `8`; equity avg `-2.4249` n `85`; fx avg `-0.0527` n `6`; index avg `-0.3523` n `23`; metal avg `-0.7133` n `18`; unknown avg `0.5965` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
