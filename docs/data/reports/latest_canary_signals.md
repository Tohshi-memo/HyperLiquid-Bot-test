# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T23:52:28.087786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `13`; crypto_alt avg `0.047` n `239`; crypto_major avg `0.0141` n `8`; equity avg `0.0525` n `168`; fx avg `-0.0009` n `6`; index avg `0.0035` n `27`; metal avg `-0.0095` n `20`; unknown avg `0.8715` n `1265`
- 1h: commodity avg `-0.0083` n `13`; crypto_alt avg `0.2827` n `239`; crypto_major avg `0.0833` n `8`; equity avg `0.0822` n `168`; fx avg `-0.0106` n `6`; index avg `0.0071` n `27`; metal avg `-0.0043` n `20`; unknown avg `1.9105` n `1245`
- 4h: commodity avg `0.0207` n `13`; crypto_alt avg `0.3457` n `239`; crypto_major avg `-0.2559` n `8`; equity avg `0.1148` n `168`; fx avg `-0.019` n `6`; index avg `0.0177` n `27`; metal avg `0.079` n `20`; unknown avg `0.4617` n `1159`
- 24h: commodity avg `-0.5258` n `13`; crypto_alt avg `0.6818` n `239`; crypto_major avg `0.3647` n `8`; equity avg `3.5377` n `168`; fx avg `-0.1905` n `6`; index avg `0.3302` n `27`; metal avg `1.0363` n `20`; unknown avg `211.8634` n `987`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
