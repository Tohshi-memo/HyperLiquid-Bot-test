# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T15:22:40.908002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0842` n `12`; crypto_alt avg `-0.1954` n `228`; crypto_major avg `-0.2104` n `8`; equity avg `-0.4763` n `74`; fx avg `-0.003` n `6`; index avg `-0.0636` n `23`; metal avg `-0.0025` n `18`; unknown avg `1.9216` n `547`
- 1h: commodity avg `-0.2083` n `12`; crypto_alt avg `0.163` n `228`; crypto_major avg `-0.1647` n `8`; equity avg `-1.3315` n `74`; fx avg `-0.0035` n `6`; index avg `-0.6367` n `23`; metal avg `-0.8743` n `18`; unknown avg `1.8014` n `547`
- 4h: commodity avg `-0.6251` n `12`; crypto_alt avg `-0.4894` n `228`; crypto_major avg `-1.3844` n `8`; equity avg `-2.6833` n `74`; fx avg `-0.0004` n `6`; index avg `-1.4572` n `23`; metal avg `-1.5268` n `18`; unknown avg `0.9427` n `545`
- 24h: commodity avg `-1.0696` n `12`; crypto_alt avg `-2.8759` n `228`; crypto_major avg `-3.5376` n `8`; equity avg `-2.4634` n `74`; fx avg `0.1034` n `6`; index avg `-1.1877` n `23`; metal avg `-1.1872` n `18`; unknown avg `-1.2266` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
