# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T04:52:28.523703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.0629` n `239`; crypto_major avg `-0.0361` n `8`; equity avg `-0.028` n `158`; fx avg `0.0143` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0015` n `20`; unknown avg `180.7105` n `1256`
- 1h: commodity avg `-0.1108` n `13`; crypto_alt avg `0.1401` n `239`; crypto_major avg `-0.0528` n `8`; equity avg `0.0966` n `158`; fx avg `-0.0077` n `6`; index avg `0.018` n `27`; metal avg `0.012` n `20`; unknown avg `61.7295` n `1246`
- 4h: commodity avg `0.2584` n `13`; crypto_alt avg `0.4173` n `239`; crypto_major avg `-0.5084` n `8`; equity avg `0.7209` n `158`; fx avg `-0.036` n `6`; index avg `0.16` n `27`; metal avg `-0.2725` n `20`; unknown avg `2.7082` n `1244`
- 24h: commodity avg `1.4717` n `13`; crypto_alt avg `-4.3813` n `239`; crypto_major avg `-5.7204` n `8`; equity avg `-5.9177` n `158`; fx avg `0.027` n `6`; index avg `-0.7605` n `27`; metal avg `-0.5957` n `20`; unknown avg `230.6776` n `1033`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
