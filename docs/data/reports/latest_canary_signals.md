# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T03:07:22.380266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.1452` n `228`; crypto_major avg `0.221` n `8`; equity avg `0.0427` n `74`; fx avg `0.0001` n `6`; index avg `0.1456` n `23`; metal avg `0.1144` n `18`; unknown avg `-0.1336` n `516`
- 1h: commodity avg `-0.0809` n `12`; crypto_alt avg `-0.4268` n `228`; crypto_major avg `0.0206` n `8`; equity avg `-0.0497` n `74`; fx avg `-0.0027` n `6`; index avg `0.1508` n `23`; metal avg `0.1688` n `18`; unknown avg `-0.3556` n `516`
- 4h: commodity avg `-0.034` n `12`; crypto_alt avg `1.8661` n `228`; crypto_major avg `1.774` n `8`; equity avg `0.6296` n `74`; fx avg `-0.0045` n `6`; index avg `0.239` n `23`; metal avg `0.4686` n `18`; unknown avg `0.8465` n `515`
- 24h: commodity avg `0.0347` n `12`; crypto_alt avg `1.6882` n `228`; crypto_major avg `0.8477` n `8`; equity avg `1.6367` n `74`; fx avg `0.0427` n `6`; index avg `0.839` n `23`; metal avg `0.4176` n `18`; unknown avg `0.0564` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
