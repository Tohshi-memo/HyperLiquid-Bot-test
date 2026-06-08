# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T07:52:28.848550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0571` n `12`; crypto_alt avg `0.0891` n `228`; crypto_major avg `0.1111` n `8`; equity avg `0.0739` n `74`; fx avg `-0.0142` n `6`; index avg `0.0649` n `23`; metal avg `-0.203` n `18`; unknown avg `-0.0272` n `517`
- 1h: commodity avg `-0.0227` n `12`; crypto_alt avg `0.4506` n `228`; crypto_major avg `0.3638` n `8`; equity avg `0.7259` n `74`; fx avg `-0.0196` n `6`; index avg `0.2448` n `23`; metal avg `-0.091` n `18`; unknown avg `-0.0056` n `517`
- 4h: commodity avg `0.201` n `12`; crypto_alt avg `0.2101` n `228`; crypto_major avg `0.1696` n `8`; equity avg `-0.2148` n `74`; fx avg `-0.2118` n `6`; index avg `-0.0563` n `23`; metal avg `-0.3308` n `18`; unknown avg `-0.2178` n `507`
- 24h: commodity avg `0.8604` n `12`; crypto_alt avg `0.5199` n `228`; crypto_major avg `2.0882` n `8`; equity avg `0.7875` n `74`; fx avg `-0.2946` n `6`; index avg `0.2495` n `23`; metal avg `-0.7376` n `18`; unknown avg `-5.4293` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
