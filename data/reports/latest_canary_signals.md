# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T18:22:20.500081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0434` n `12`; crypto_alt avg `0.1881` n `228`; crypto_major avg `0.1792` n `8`; equity avg `-0.0364` n `67`; fx avg `0.006` n `6`; index avg `-0.0242` n `23`; metal avg `0.0762` n `18`; unknown avg `0.3361` n `386`
- 1h: commodity avg `-0.2388` n `12`; crypto_alt avg `-0.118` n `228`; crypto_major avg `0.104` n `8`; equity avg `-0.0827` n `67`; fx avg `0.002` n `6`; index avg `0.0345` n `23`; metal avg `0.077` n `18`; unknown avg `0.582` n `386`
- 4h: commodity avg `-0.8413` n `12`; crypto_alt avg `-0.3286` n `228`; crypto_major avg `-0.3089` n `8`; equity avg `0.1344` n `67`; fx avg `0.0838` n `6`; index avg `0.3753` n `23`; metal avg `0.5972` n `18`; unknown avg `-0.1691` n `386`
- 24h: commodity avg `-0.7675` n `12`; crypto_alt avg `-0.6526` n `228`; crypto_major avg `-0.873` n `8`; equity avg `-0.2682` n `67`; fx avg `0.1684` n `6`; index avg `0.7499` n `23`; metal avg `-0.8672` n `18`; unknown avg `-0.3199` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0443`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0411`, n `668`, weak_sample_signal
