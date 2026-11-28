# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T02:07:27.934918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `-0.1195` n `239`; crypto_major avg `-0.065` n `8`; equity avg `0.0967` n `168`; fx avg `-0.0021` n `6`; index avg `0.0091` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.0204` n `1251`
- 1h: commodity avg `0.0171` n `13`; crypto_alt avg `0.1151` n `239`; crypto_major avg `0.4029` n `8`; equity avg `0.2535` n `168`; fx avg `-0.017` n `6`; index avg `0.0243` n `27`; metal avg `0.0112` n `20`; unknown avg `2.198` n `1257`
- 4h: commodity avg `-0.0929` n `13`; crypto_alt avg `0.3389` n `239`; crypto_major avg `0.8182` n `8`; equity avg `0.2546` n `168`; fx avg `-0.0115` n `6`; index avg `0.0171` n `27`; metal avg `0.024` n `20`; unknown avg `21.1517` n `1239`
- 24h: commodity avg `-0.7922` n `13`; crypto_alt avg `-0.343` n `239`; crypto_major avg `-0.3347` n `8`; equity avg `2.0559` n `168`; fx avg `-0.1706` n `6`; index avg `0.1951` n `27`; metal avg `0.2044` n `20`; unknown avg `285.7597` n `987`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
