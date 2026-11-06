# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T16:52:29.871440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `13`; crypto_alt avg `0.2242` n `239`; crypto_major avg `0.2286` n `8`; equity avg `0.0453` n `158`; fx avg `-0.0111` n `6`; index avg `0.001` n `27`; metal avg `0.0336` n `20`; unknown avg `69.8721` n `1257`
- 1h: commodity avg `0.1919` n `13`; crypto_alt avg `0.1077` n `239`; crypto_major avg `0.1852` n `8`; equity avg `0.103` n `158`; fx avg `-0.002` n `6`; index avg `-0.0008` n `27`; metal avg `0.0415` n `20`; unknown avg `87.0402` n `1247`
- 4h: commodity avg `-0.0992` n `13`; crypto_alt avg `0.3179` n `239`; crypto_major avg `0.2818` n `8`; equity avg `-0.52` n `158`; fx avg `-0.0275` n `6`; index avg `0.0683` n `27`; metal avg `0.046` n `20`; unknown avg `157.1959` n `1245`
- 24h: commodity avg `0.1343` n `13`; crypto_alt avg `1.8033` n `239`; crypto_major avg `-1.0438` n `8`; equity avg `0.5548` n `158`; fx avg `-0.0967` n `6`; index avg `0.0174` n `27`; metal avg `-0.327` n `20`; unknown avg `55.3074` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
