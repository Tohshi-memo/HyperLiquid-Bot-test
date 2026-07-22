# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T15:22:35.749354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.2004` n `230`; crypto_major avg `0.2898` n `8`; equity avg `0.1329` n `98`; fx avg `0.0096` n `6`; index avg `0.0243` n `25`; metal avg `0.0305` n `20`; unknown avg `-0.0627` n `773`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.2871` n `230`; crypto_major avg `0.5592` n `8`; equity avg `0.3526` n `98`; fx avg `-0.0105` n `6`; index avg `0.0369` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0281` n `773`
- 4h: commodity avg `-0.0133` n `12`; crypto_alt avg `0.3502` n `230`; crypto_major avg `0.3872` n `8`; equity avg `1.1037` n `98`; fx avg `-0.0195` n `6`; index avg `0.1858` n `25`; metal avg `0.1496` n `20`; unknown avg `10.9918` n `773`
- 24h: commodity avg `0.553` n `12`; crypto_alt avg `-0.1371` n `230`; crypto_major avg `-0.7503` n `8`; equity avg `0.3969` n `98`; fx avg `-0.0265` n `6`; index avg `-0.0332` n `25`; metal avg `0.4501` n `20`; unknown avg `0.9536` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1068`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0891`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0723`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0715`, n `666`, weak_sample_signal
