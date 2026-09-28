# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T12:52:29.799879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0797` n `12`; crypto_alt avg `0.1459` n `234`; crypto_major avg `0.2275` n `8`; equity avg `0.105` n `141`; fx avg `-0.0034` n `6`; index avg `0.0266` n `26`; metal avg `-0.0141` n `20`; unknown avg `0.9464` n `962`
- 1h: commodity avg `-0.3141` n `12`; crypto_alt avg `1.2851` n `234`; crypto_major avg `0.9532` n `8`; equity avg `0.2767` n `141`; fx avg `0.0083` n `6`; index avg `0.0703` n `26`; metal avg `-0.0259` n `20`; unknown avg `237.9726` n `954`
- 4h: commodity avg `-0.1659` n `12`; crypto_alt avg `1.4433` n `234`; crypto_major avg `1.2434` n `8`; equity avg `0.5126` n `141`; fx avg `-0.0011` n `6`; index avg `0.1068` n `26`; metal avg `0.0453` n `20`; unknown avg `45.6832` n `952`
- 24h: commodity avg `-0.3365` n `12`; crypto_alt avg `-2.558` n `234`; crypto_major avg `-2.0606` n `8`; equity avg `-2.3507` n `141`; fx avg `0.0239` n `6`; index avg `-0.1674` n `26`; metal avg `-0.9321` n `20`; unknown avg `4.1431` n `814`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
