# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T21:07:39.352025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0553` n `13`; crypto_alt avg `-0.603` n `239`; crypto_major avg `-0.5778` n `8`; equity avg `-0.8541` n `158`; fx avg `-0.0048` n `6`; index avg `-0.139` n `27`; metal avg `-0.144` n `20`; unknown avg `7.6583` n `1242`
- 1h: commodity avg `-0.0396` n `13`; crypto_alt avg `-0.6279` n `239`; crypto_major avg `-0.3521` n `8`; equity avg `-1.0911` n `158`; fx avg `-0.0177` n `6`; index avg `-0.2047` n `27`; metal avg `-0.1929` n `20`; unknown avg `7.0716` n `1216`
- 4h: commodity avg `0.2008` n `13`; crypto_alt avg `1.0494` n `239`; crypto_major avg `-0.2424` n `8`; equity avg `-0.719` n `158`; fx avg `-0.0157` n `6`; index avg `-0.2755` n `27`; metal avg `-0.3682` n `20`; unknown avg `5.0064` n `1194`
- 24h: commodity avg `0.7235` n `13`; crypto_alt avg `-4.3491` n `239`; crypto_major avg `-5.0435` n `8`; equity avg `-8.2879` n `158`; fx avg `0.0753` n `6`; index avg `-1.2415` n `27`; metal avg `0.018` n `20`; unknown avg `225.2134` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
