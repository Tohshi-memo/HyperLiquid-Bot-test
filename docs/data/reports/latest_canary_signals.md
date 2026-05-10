# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T08:07:17.673934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `-0.0382` n `228`; crypto_major avg `-0.0141` n `8`; equity avg `-0.0179` n `65`; fx avg `0.0015` n `5`; index avg `-0.0118` n `23`; metal avg `-0.0129` n `18`; unknown avg `-0.0803` n `376`
- 1h: commodity avg `-0.0592` n `12`; crypto_alt avg `0.1766` n `228`; crypto_major avg `0.0159` n `8`; equity avg `-0.0124` n `65`; fx avg `0.0023` n `5`; index avg `0.0032` n `23`; metal avg `-0.0401` n `18`; unknown avg `-0.145` n `376`
- 4h: commodity avg `-0.0812` n `12`; crypto_alt avg `0.4312` n `228`; crypto_major avg `0.1384` n `8`; equity avg `0.0633` n `65`; fx avg `0.004` n `5`; index avg `-0.004` n `23`; metal avg `0.0062` n `18`; unknown avg `-0.0571` n `366`
- 24h: commodity avg `0.1184` n `12`; crypto_alt avg `-0.9102` n `228`; crypto_major avg `-0.4598` n `8`; equity avg `0.9089` n `65`; fx avg `-0.0231` n `5`; index avg `0.3074` n `23`; metal avg `0.3218` n `18`; unknown avg `-0.326` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
