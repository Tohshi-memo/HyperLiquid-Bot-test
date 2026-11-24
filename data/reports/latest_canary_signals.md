# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T06:07:38.455980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `13`; crypto_alt avg `-0.3517` n `239`; crypto_major avg `-0.3787` n `8`; equity avg `-0.3769` n `166`; fx avg `0.0009` n `6`; index avg `-0.0571` n `27`; metal avg `-0.1352` n `20`; unknown avg `165.0442` n `1228`
- 1h: commodity avg `0.0331` n `13`; crypto_alt avg `0.4097` n `239`; crypto_major avg `0.0347` n `8`; equity avg `-0.4806` n `166`; fx avg `0.0318` n `6`; index avg `-0.0523` n `27`; metal avg `-0.2051` n `20`; unknown avg `164.5824` n `1230`
- 4h: commodity avg `-0.099` n `13`; crypto_alt avg `0.5181` n `239`; crypto_major avg `-0.1494` n `8`; equity avg `-0.3191` n `166`; fx avg `-0.0099` n `6`; index avg `0.0085` n `27`; metal avg `-0.4347` n `20`; unknown avg `165.9468` n `1214`
- 24h: commodity avg `-1.2086` n `13`; crypto_alt avg `0.6822` n `239`; crypto_major avg `-0.1539` n `8`; equity avg `3.8608` n `166`; fx avg `-0.2667` n `6`; index avg `0.6004` n `27`; metal avg `-0.3632` n `20`; unknown avg `258.4987` n `1030`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
