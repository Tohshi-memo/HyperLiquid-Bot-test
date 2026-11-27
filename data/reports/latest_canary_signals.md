# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T17:22:27.118893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.9526` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8784` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.513` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `0.0769` n `239`; crypto_major avg `0.0416` n `8`; equity avg `0.1752` n `168`; fx avg `0.0108` n `6`; index avg `0.0218` n `27`; metal avg `0.0094` n `20`; unknown avg `1.0258` n `1262`
- 1h: commodity avg `-0.0395` n `13`; crypto_alt avg `0.122` n `239`; crypto_major avg `-0.1007` n `8`; equity avg `0.2797` n `168`; fx avg `-0.0076` n `6`; index avg `0.0368` n `27`; metal avg `0.0738` n `20`; unknown avg `4.2061` n `1252`
- 4h: commodity avg `-0.2174` n `13`; crypto_alt avg `-1.5602` n `239`; crypto_major avg `-1.979` n `8`; equity avg `-0.466` n `168`; fx avg `-0.0415` n `6`; index avg `-0.0264` n `27`; metal avg `-0.1006` n `20`; unknown avg `3.4538` n `1248`
- 24h: commodity avg `-0.453` n `13`; crypto_alt avg `0.5476` n `239`; crypto_major avg `0.9309` n `8`; equity avg `3.0892` n `168`; fx avg `-0.1405` n `6`; index avg `0.3051` n `27`; metal avg `0.7386` n `20`; unknown avg `70.551` n `1033`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
