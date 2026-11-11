# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T07:37:28.680613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `13`; crypto_alt avg `-0.1834` n `239`; crypto_major avg `-0.1007` n `8`; equity avg `-0.1263` n `161`; fx avg `-0.0074` n `6`; index avg `-0.0163` n `27`; metal avg `-0.0063` n `20`; unknown avg `0.1925` n `1259`
- 1h: commodity avg `-0.1154` n `13`; crypto_alt avg `-0.3004` n `239`; crypto_major avg `-0.2555` n `8`; equity avg `-0.3986` n `161`; fx avg `0.0212` n `6`; index avg `-0.0637` n `27`; metal avg `0.0253` n `20`; unknown avg `6.9577` n `1251`
- 4h: commodity avg `-0.0324` n `13`; crypto_alt avg `-0.9184` n `239`; crypto_major avg `-0.3347` n `8`; equity avg `0.4426` n `161`; fx avg `-0.0413` n `6`; index avg `0.0462` n `27`; metal avg `0.1961` n `20`; unknown avg `0.7117` n `1211`
- 24h: commodity avg `0.4189` n `13`; crypto_alt avg `-1.5022` n `239`; crypto_major avg `-2.6808` n `8`; equity avg `1.5625` n `161`; fx avg `-0.1785` n `6`; index avg `0.1844` n `27`; metal avg `0.0542` n `20`; unknown avg `1.3878` n `1158`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
