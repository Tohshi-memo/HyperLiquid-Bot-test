# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T15:39:18.062177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.5991` n `228`; crypto_major avg `0.4733` n `8`; equity avg `-0.0148` n `74`; fx avg `-0.007` n `6`; index avg `0.0306` n `23`; metal avg `0.0159` n `18`; unknown avg `-0.1601` n `515`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `-0.5506` n `228`; crypto_major avg `-0.5778` n `8`; equity avg `-0.2322` n `74`; fx avg `-0.007` n `6`; index avg `-0.0288` n `23`; metal avg `-0.0207` n `18`; unknown avg `-2.81` n `515`
- 4h: commodity avg `0.1053` n `12`; crypto_alt avg `0.3226` n `228`; crypto_major avg `-0.0268` n `8`; equity avg `0.3386` n `74`; fx avg `-0.0063` n `6`; index avg `0.5302` n `23`; metal avg `-0.1537` n `18`; unknown avg `-0.4601` n `411`
- 24h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.5116` n `228`; crypto_major avg `-0.4073` n `8`; equity avg `-3.0983` n `74`; fx avg `-0.1061` n `6`; index avg `-1.9993` n `23`; metal avg `-1.3403` n `18`; unknown avg `-0.2497` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
