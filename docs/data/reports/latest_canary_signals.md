# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T01:22:21.738429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0609` n `12`; crypto_alt avg `0.2016` n `228`; crypto_major avg `0.1198` n `8`; equity avg `0.0456` n `65`; fx avg `0.0` n `5`; index avg `-0.0147` n `23`; metal avg `0.0268` n `18`; unknown avg `0.235` n `375`
- 1h: commodity avg `-0.0403` n `12`; crypto_alt avg `0.5977` n `228`; crypto_major avg `0.2799` n `8`; equity avg `0.1145` n `65`; fx avg `-0.0072` n `5`; index avg `0.0322` n `23`; metal avg `0.1587` n `18`; unknown avg `0.2039` n `375`
- 4h: commodity avg `-0.3292` n `12`; crypto_alt avg `1.2622` n `228`; crypto_major avg `0.5192` n `8`; equity avg `0.3138` n `65`; fx avg `-0.0268` n `5`; index avg `0.1506` n `23`; metal avg `-0.0974` n `18`; unknown avg `0.0292` n `375`
- 24h: commodity avg `-0.5232` n `12`; crypto_alt avg `4.5697` n `228`; crypto_major avg `2.2758` n `8`; equity avg `3.6329` n `65`; fx avg `0.1073` n `5`; index avg `1.2713` n `23`; metal avg `0.2131` n `18`; unknown avg `1.3781` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
