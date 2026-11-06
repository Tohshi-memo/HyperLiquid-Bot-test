# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T14:37:28.463228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1865` n `13`; crypto_alt avg `0.4537` n `239`; crypto_major avg `0.1704` n `8`; equity avg `-0.8498` n `158`; fx avg `0.0341` n `6`; index avg `0.0086` n `27`; metal avg `0.0635` n `20`; unknown avg `10.1593` n `1257`
- 1h: commodity avg `-0.3871` n `13`; crypto_alt avg `0.2841` n `239`; crypto_major avg `0.0261` n `8`; equity avg `-0.4869` n `158`; fx avg `0.0333` n `6`; index avg `0.0151` n `27`; metal avg `-0.0297` n `20`; unknown avg `111.7741` n `1255`
- 4h: commodity avg `-0.2962` n `13`; crypto_alt avg `0.4905` n `239`; crypto_major avg `-0.1991` n `8`; equity avg `-0.4758` n `158`; fx avg `0.0715` n `6`; index avg `0.0083` n `27`; metal avg `-0.0881` n `20`; unknown avg `279.6157` n `1175`
- 24h: commodity avg `0.1505` n `13`; crypto_alt avg `-1.3047` n `239`; crypto_major avg `-3.9061` n `8`; equity avg `-2.3674` n `158`; fx avg `0.0141` n `6`; index avg `-0.3697` n `27`; metal avg `-0.6125` n `20`; unknown avg `85.6806` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
