# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T15:52:24.896596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0453` n `12`; crypto_alt avg `-0.229` n `228`; crypto_major avg `-0.2272` n `8`; equity avg `-0.0606` n `74`; fx avg `-0.0312` n `6`; index avg `0.0061` n `23`; metal avg `-0.0217` n `18`; unknown avg `-0.0373` n `516`
- 1h: commodity avg `0.143` n `12`; crypto_alt avg `-0.2295` n `228`; crypto_major avg `-0.0152` n `8`; equity avg `0.0123` n `74`; fx avg `-0.0305` n `6`; index avg `-0.1117` n `23`; metal avg `0.0328` n `18`; unknown avg `0.042` n `516`
- 4h: commodity avg `0.3345` n `12`; crypto_alt avg `-0.4502` n `228`; crypto_major avg `-0.3592` n `8`; equity avg `0.2016` n `74`; fx avg `-0.0273` n `6`; index avg `0.1044` n `23`; metal avg `-0.1311` n `18`; unknown avg `0.1652` n `516`
- 24h: commodity avg `0.3072` n `12`; crypto_alt avg `2.5287` n `228`; crypto_major avg `2.5425` n `8`; equity avg `1.8488` n `74`; fx avg `-0.0264` n `6`; index avg `0.4127` n `23`; metal avg `0.6344` n `18`; unknown avg `-4.5663` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
