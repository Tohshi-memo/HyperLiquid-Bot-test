# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T22:37:26.876154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `-0.0623` n `239`; crypto_major avg `-0.2321` n `8`; equity avg `-0.0505` n `158`; fx avg `-0.0104` n `6`; index avg `0.0046` n `27`; metal avg `-0.0124` n `20`; unknown avg `-0.2475` n `1256`
- 1h: commodity avg `0.0933` n `13`; crypto_alt avg `-0.6391` n `239`; crypto_major avg `-0.4998` n `8`; equity avg `-0.6662` n `158`; fx avg `0.0099` n `6`; index avg `-0.0289` n `27`; metal avg `-0.0337` n `20`; unknown avg `-1.3081` n `1254`
- 4h: commodity avg `0.1799` n `13`; crypto_alt avg `-0.2512` n `239`; crypto_major avg `-0.4129` n `8`; equity avg `-0.493` n `158`; fx avg `-0.0314` n `6`; index avg `-0.2368` n `27`; metal avg `-0.2372` n `20`; unknown avg `3.0423` n `1194`
- 24h: commodity avg `1.0326` n `13`; crypto_alt avg `-5.7293` n `239`; crypto_major avg `-5.9448` n `8`; equity avg `-8.7375` n `158`; fx avg `0.0817` n `6`; index avg `-1.3557` n `27`; metal avg `0.0257` n `20`; unknown avg `229.2385` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
