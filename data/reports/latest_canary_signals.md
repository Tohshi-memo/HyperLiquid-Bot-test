# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T21:52:43.989352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0661` n `12`; crypto_alt avg `0.1043` n `229`; crypto_major avg `0.1432` n `8`; equity avg `0.0807` n `91`; fx avg `-0.0025` n `6`; index avg `0.0018` n `25`; metal avg `0.0278` n `20`; unknown avg `0.0748` n `764`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `0.0853` n `229`; crypto_major avg `0.0317` n `8`; equity avg `0.2153` n `91`; fx avg `0.0163` n `6`; index avg `0.0022` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0827` n `764`
- 4h: commodity avg `0.2386` n `12`; crypto_alt avg `-0.1704` n `229`; crypto_major avg `-0.1325` n `8`; equity avg `0.6955` n `91`; fx avg `-0.0152` n `6`; index avg `0.0354` n `25`; metal avg `0.0248` n `20`; unknown avg `0.9501` n `764`
- 24h: commodity avg `0.4154` n `12`; crypto_alt avg `-1.727` n `229`; crypto_major avg `-2.258` n `8`; equity avg `1.4168` n `91`; fx avg `0.0257` n `6`; index avg `-0.0347` n `25`; metal avg `-0.8397` n `20`; unknown avg `0.0652` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
