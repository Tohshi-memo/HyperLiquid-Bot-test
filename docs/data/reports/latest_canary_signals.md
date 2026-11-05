# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T22:52:26.739591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0527` n `13`; crypto_alt avg `-0.0645` n `239`; crypto_major avg `-0.2078` n `8`; equity avg `-0.0544` n `158`; fx avg `-0.0001` n `6`; index avg `0.0002` n `27`; metal avg `-0.0014` n `20`; unknown avg `1.5825` n `1256`
- 1h: commodity avg `0.0103` n `13`; crypto_alt avg `-0.4185` n `239`; crypto_major avg `-0.3472` n `8`; equity avg `-0.4048` n `158`; fx avg `-0.0051` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0092` n `20`; unknown avg `-0.8173` n `1252`
- 4h: commodity avg `0.272` n `13`; crypto_alt avg `-0.3893` n `239`; crypto_major avg `-0.6376` n `8`; equity avg `-0.4205` n `158`; fx avg `-0.0107` n `6`; index avg `-0.2214` n `27`; metal avg `-0.2026` n `20`; unknown avg `2.4019` n `1194`
- 24h: commodity avg `0.9357` n `13`; crypto_alt avg `-5.8979` n `239`; crypto_major avg `-6.2185` n `8`; equity avg `-8.7703` n `158`; fx avg `0.0844` n `6`; index avg `-1.3528` n `27`; metal avg `0.0382` n `20`; unknown avg `229.013` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
