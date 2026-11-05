# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T02:52:28.224262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1143` n `13`; crypto_alt avg `0.1757` n `239`; crypto_major avg `0.0289` n `8`; equity avg `-0.1688` n `158`; fx avg `-0.0248` n `6`; index avg `-0.0455` n `27`; metal avg `0.1137` n `20`; unknown avg `-0.4389` n `1265`
- 1h: commodity avg `-0.002` n `13`; crypto_alt avg `0.0872` n `239`; crypto_major avg `-0.2059` n `8`; equity avg `0.0923` n `158`; fx avg `-0.0048` n `6`; index avg `0.0245` n `27`; metal avg `0.0756` n `20`; unknown avg `-0.2786` n `1256`
- 4h: commodity avg `-0.2648` n `13`; crypto_alt avg `-0.2558` n `239`; crypto_major avg `-0.2275` n `8`; equity avg `-0.8776` n `158`; fx avg `0.0306` n `6`; index avg `-0.2411` n `27`; metal avg `0.5159` n `20`; unknown avg `0.5622` n `1196`
- 24h: commodity avg `-1.6406` n `13`; crypto_alt avg `3.9655` n `239`; crypto_major avg `4.2229` n `8`; equity avg `0.9391` n `158`; fx avg `0.1096` n `6`; index avg `0.5049` n `27`; metal avg `1.9663` n `20`; unknown avg `31.7225` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2536`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
