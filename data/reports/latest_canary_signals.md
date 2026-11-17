# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T19:07:26.835359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.1762` n `239`; crypto_major avg `-0.1033` n `8`; equity avg `0.1377` n `163`; fx avg `0.0108` n `6`; index avg `0.0056` n `27`; metal avg `-0.0313` n `20`; unknown avg `10.5651` n `1259`
- 1h: commodity avg `0.078` n `13`; crypto_alt avg `-0.0719` n `239`; crypto_major avg `0.0604` n `8`; equity avg `0.1545` n `163`; fx avg `0.0094` n `6`; index avg `-0.0022` n `27`; metal avg `-0.0508` n `20`; unknown avg `1.7585` n `1263`
- 4h: commodity avg `0.1386` n `13`; crypto_alt avg `-1.1411` n `239`; crypto_major avg `-0.664` n `8`; equity avg `-0.8057` n `163`; fx avg `0.0569` n `6`; index avg `-0.0822` n `27`; metal avg `-0.0865` n `20`; unknown avg `0.488` n `1245`
- 24h: commodity avg `0.3398` n `13`; crypto_alt avg `-0.7964` n `239`; crypto_major avg `-0.2221` n `8`; equity avg `-1.8751` n `163`; fx avg `0.0511` n `6`; index avg `-0.2175` n `27`; metal avg `-0.0444` n `20`; unknown avg `9.0561` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
