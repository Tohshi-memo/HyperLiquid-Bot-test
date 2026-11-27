# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T22:52:32.924117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `13`; crypto_alt avg `0.107` n `239`; crypto_major avg `0.1697` n `8`; equity avg `0.0587` n `168`; fx avg `-0.0025` n `6`; index avg `0.0054` n `27`; metal avg `0.0027` n `20`; unknown avg `2.3374` n `1265`
- 1h: commodity avg `0.0199` n `13`; crypto_alt avg `-0.106` n `239`; crypto_major avg `-0.2296` n `8`; equity avg `-0.0507` n `168`; fx avg `-0.0082` n `6`; index avg `-0.022` n `27`; metal avg `0.0226` n `20`; unknown avg `0.8218` n `1251`
- 4h: commodity avg `0.1247` n `13`; crypto_alt avg `0.1663` n `239`; crypto_major avg `-0.2121` n `8`; equity avg `0.0897` n `168`; fx avg `-0.0019` n `6`; index avg `0.0108` n `27`; metal avg `0.2081` n `20`; unknown avg `172.2314` n `1173`
- 24h: commodity avg `-0.5028` n `13`; crypto_alt avg `0.0877` n `239`; crypto_major avg `-0.0336` n `8`; equity avg `3.2097` n `168`; fx avg `-0.1661` n `6`; index avg `0.3208` n `27`; metal avg `0.9958` n `20`; unknown avg `273.2416` n `1003`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
