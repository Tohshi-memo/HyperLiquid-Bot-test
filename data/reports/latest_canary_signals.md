# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T10:52:28.223149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0935` n `13`; crypto_alt avg `-0.0195` n `239`; crypto_major avg `-0.0953` n `8`; equity avg `-0.1425` n `158`; fx avg `0.0256` n `6`; index avg `-0.0226` n `27`; metal avg `-0.0305` n `20`; unknown avg `0.1034` n `1257`
- 1h: commodity avg `0.4083` n `13`; crypto_alt avg `0.2368` n `239`; crypto_major avg `0.0714` n `8`; equity avg `-0.233` n `158`; fx avg `0.0369` n `6`; index avg `-0.0345` n `27`; metal avg `-0.0816` n `20`; unknown avg `0.2302` n `1252`
- 4h: commodity avg `-0.0845` n `13`; crypto_alt avg `0.751` n `239`; crypto_major avg `0.5767` n `8`; equity avg `1.3756` n `158`; fx avg `-0.0381` n `6`; index avg `0.1968` n `27`; metal avg `0.1131` n `20`; unknown avg `0.8482` n `1192`
- 24h: commodity avg `0.8812` n `13`; crypto_alt avg `-3.2162` n `239`; crypto_major avg `-5.3184` n `8`; equity avg `-4.9793` n `158`; fx avg `-0.0228` n `6`; index avg `-0.6343` n `27`; metal avg `-0.4035` n `20`; unknown avg `195.9041` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
