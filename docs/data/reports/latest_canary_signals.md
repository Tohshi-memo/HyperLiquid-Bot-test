# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T19:52:29.116243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `13`; crypto_alt avg `-0.0181` n `239`; crypto_major avg `0.0485` n `8`; equity avg `-0.002` n `168`; fx avg `-0.0134` n `6`; index avg `-0.0051` n `27`; metal avg `-0.0118` n `20`; unknown avg `-0.3949` n `1263`
- 1h: commodity avg `-0.1416` n `13`; crypto_alt avg `-0.3067` n `239`; crypto_major avg `-0.2744` n `8`; equity avg `-0.1161` n `168`; fx avg `-0.0202` n `6`; index avg `-0.0099` n `27`; metal avg `0.0333` n `20`; unknown avg `1.9248` n `1255`
- 4h: commodity avg `0.4561` n `13`; crypto_alt avg `0.0818` n `239`; crypto_major avg `-0.1086` n `8`; equity avg `0.4984` n `168`; fx avg `-0.0041` n `6`; index avg `0.0932` n `27`; metal avg `-0.1186` n `20`; unknown avg `385.6412` n `1225`
- 24h: commodity avg `0.7384` n `13`; crypto_alt avg `-3.2429` n `239`; crypto_major avg `-3.1167` n `8`; equity avg `-3.5869` n `167`; fx avg `0.2395` n `6`; index avg `-0.1879` n `27`; metal avg `-1.0574` n `20`; unknown avg `421.5191` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
