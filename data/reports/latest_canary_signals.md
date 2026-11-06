# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T05:52:27.977006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `13`; crypto_alt avg `0.0271` n `239`; crypto_major avg `-0.0191` n `8`; equity avg `-0.1647` n `158`; fx avg `0.014` n `6`; index avg `-0.0399` n `27`; metal avg `-0.0295` n `20`; unknown avg `0.2887` n `1258`
- 1h: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.1563` n `239`; crypto_major avg `-0.2159` n `8`; equity avg `-0.2363` n `158`; fx avg `0.0292` n `6`; index avg `-0.0134` n `27`; metal avg `-0.039` n `20`; unknown avg `36.4358` n `1248`
- 4h: commodity avg `0.1578` n `13`; crypto_alt avg `0.1624` n `239`; crypto_major avg `-0.6757` n `8`; equity avg `0.0947` n `158`; fx avg `0.014` n `6`; index avg `0.0637` n `27`; metal avg `-0.2242` n `20`; unknown avg `1.4055` n `1242`
- 24h: commodity avg `1.3152` n `13`; crypto_alt avg `-3.9555` n `239`; crypto_major avg `-5.5705` n `8`; equity avg `-5.5381` n `158`; fx avg `0.0539` n `6`; index avg `-0.6871` n `27`; metal avg `-0.3922` n `20`; unknown avg `230.3386` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2403`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
