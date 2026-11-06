# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T07:22:38.241113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `13`; crypto_alt avg `-0.0402` n `239`; crypto_major avg `-0.016` n `8`; equity avg `0.0185` n `158`; fx avg `-0.0128` n `6`; index avg `-0.0099` n `27`; metal avg `0.005` n `20`; unknown avg `-0.0289` n `1258`
- 1h: commodity avg `0.0125` n `13`; crypto_alt avg `-0.0253` n `239`; crypto_major avg `-0.2881` n `8`; equity avg `0.0483` n `158`; fx avg `-0.0669` n `6`; index avg `-0.0145` n `27`; metal avg `-0.0195` n `20`; unknown avg `-0.2731` n `1244`
- 4h: commodity avg `0.0843` n `13`; crypto_alt avg `-0.2863` n `239`; crypto_major avg `-0.8516` n `8`; equity avg `-0.4514` n `158`; fx avg `-0.1324` n `6`; index avg `-0.0969` n `27`; metal avg `-0.0836` n `20`; unknown avg `-0.6807` n `1218`
- 24h: commodity avg `1.2421` n `13`; crypto_alt avg `-4.209` n `239`; crypto_major avg `-6.1322` n `8`; equity avg `-6.2461` n `158`; fx avg `-0.0327` n `6`; index avg `-0.8219` n `27`; metal avg `-0.446` n `20`; unknown avg `234.178` n `1029`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
