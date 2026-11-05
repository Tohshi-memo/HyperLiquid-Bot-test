# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T22:22:33.950766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.006` n `239`; crypto_major avg `0.1943` n `8`; equity avg `-0.0427` n `158`; fx avg `-0.0044` n `6`; index avg `0.013` n `27`; metal avg `0.0146` n `20`; unknown avg `0.0951` n `1256`
- 1h: commodity avg `0.1309` n `13`; crypto_alt avg `-0.0928` n `239`; crypto_major avg `0.1879` n `8`; equity avg `0.1541` n `158`; fx avg `0.0127` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0147` n `20`; unknown avg `0.042` n `1252`
- 4h: commodity avg `0.1788` n `13`; crypto_alt avg `0.1835` n `239`; crypto_major avg `-0.159` n `8`; equity avg `-0.426` n `158`; fx avg `-0.0228` n `6`; index avg `-0.2341` n `27`; metal avg `-0.1739` n `20`; unknown avg `3.6475` n `1194`
- 24h: commodity avg `1.0179` n `13`; crypto_alt avg `-5.4635` n `239`; crypto_major avg `-5.5382` n `8`; equity avg `-8.7094` n `158`; fx avg `0.0962` n `6`; index avg `-1.3149` n `27`; metal avg `0.0477` n `20`; unknown avg `229.1962` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
