# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T10:52:34.045296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `13`; crypto_alt avg `-0.1029` n `239`; crypto_major avg `-0.0824` n `8`; equity avg `-0.0491` n `158`; fx avg `0.0033` n `6`; index avg `-0.016` n `27`; metal avg `0.0146` n `20`; unknown avg `0.28` n `1251`
- 1h: commodity avg `0.0468` n `13`; crypto_alt avg `-0.4861` n `239`; crypto_major avg `-0.2125` n `8`; equity avg `-0.1698` n `158`; fx avg `0.0268` n `6`; index avg `-0.0197` n `27`; metal avg `0.0624` n `20`; unknown avg `-0.2104` n `1233`
- 4h: commodity avg `0.4581` n `13`; crypto_alt avg `-0.4051` n `239`; crypto_major avg `-0.1` n `8`; equity avg `0.1221` n `158`; fx avg `-0.0148` n `6`; index avg `0.0477` n `27`; metal avg `0.0158` n `20`; unknown avg `0.4428` n `1135`
- 24h: commodity avg `-1.2707` n `13`; crypto_alt avg `0.2925` n `239`; crypto_major avg `1.3226` n `8`; equity avg `-3.4652` n `158`; fx avg `-0.0158` n `6`; index avg `-0.3005` n `27`; metal avg `0.5676` n `20`; unknown avg `0.4233` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2476`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
