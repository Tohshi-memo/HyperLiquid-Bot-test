# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T13:22:30.223056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `0.0961` n `239`; crypto_major avg `0.2204` n `8`; equity avg `0.232` n `161`; fx avg `-0.0119` n `6`; index avg `0.02` n `27`; metal avg `0.0354` n `20`; unknown avg `-0.1079` n `1261`
- 1h: commodity avg `0.0194` n `13`; crypto_alt avg `0.1122` n `239`; crypto_major avg `0.1957` n `8`; equity avg `0.0484` n `161`; fx avg `-0.0252` n `6`; index avg `0.0097` n `27`; metal avg `0.045` n `20`; unknown avg `-0.0505` n `1255`
- 4h: commodity avg `0.1932` n `13`; crypto_alt avg `0.6734` n `239`; crypto_major avg `0.4824` n `8`; equity avg `0.6854` n `161`; fx avg `-0.006` n `6`; index avg `0.0725` n `27`; metal avg `0.0492` n `20`; unknown avg `0.4563` n `1247`
- 24h: commodity avg `0.9951` n `13`; crypto_alt avg `-0.4717` n `239`; crypto_major avg `-1.0841` n `8`; equity avg `3.5651` n `161`; fx avg `-0.2267` n `6`; index avg `0.3061` n `27`; metal avg `0.2758` n `20`; unknown avg `1.2767` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.3057`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
