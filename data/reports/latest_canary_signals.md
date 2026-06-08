# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T06:07:24.212192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `0.4787` n `228`; crypto_major avg `0.5115` n `8`; equity avg `0.116` n `74`; fx avg `-0.0483` n `6`; index avg `-0.1223` n `23`; metal avg `0.2014` n `18`; unknown avg `0.1031` n `507`
- 1h: commodity avg `0.0915` n `12`; crypto_alt avg `0.4395` n `228`; crypto_major avg `0.5768` n `8`; equity avg `-0.5027` n `74`; fx avg `-0.1525` n `6`; index avg `-0.2144` n `23`; metal avg `-0.318` n `18`; unknown avg `-0.0303` n `507`
- 4h: commodity avg `0.4328` n `12`; crypto_alt avg `-0.5526` n `228`; crypto_major avg `-0.4282` n `8`; equity avg `-0.7101` n `74`; fx avg `-0.1355` n `6`; index avg `-0.0877` n `23`; metal avg `-0.624` n `18`; unknown avg `-0.0609` n `507`
- 24h: commodity avg `0.8016` n `12`; crypto_alt avg `0.377` n `228`; crypto_major avg `2.1749` n `8`; equity avg `0.2276` n `74`; fx avg `-0.2273` n `6`; index avg `-0.2368` n `23`; metal avg `-0.7963` n `18`; unknown avg `-4.323` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
