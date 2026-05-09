# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T15:07:13.002581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1387` n `12`; crypto_alt avg `-0.0949` n `228`; crypto_major avg `-0.0838` n `8`; equity avg `-0.0198` n `65`; fx avg `0.011` n `5`; index avg `0.0391` n `23`; metal avg `-0.0034` n `18`; unknown avg `-0.1201` n `376`
- 1h: commodity avg `0.3326` n `12`; crypto_alt avg `-0.362` n `228`; crypto_major avg `-0.4253` n `8`; equity avg `-0.0115` n `65`; fx avg `0.0125` n `5`; index avg `-0.0168` n `23`; metal avg `-0.0655` n `18`; unknown avg `0.0809` n `376`
- 4h: commodity avg `0.424` n `12`; crypto_alt avg `-1.0973` n `228`; crypto_major avg `-0.6014` n `8`; equity avg `-0.0097` n `65`; fx avg `0.007` n `5`; index avg `0.028` n `23`; metal avg `-0.0574` n `18`; unknown avg `-0.0568` n `376`
- 24h: commodity avg `-0.0809` n `12`; crypto_alt avg `1.4759` n `228`; crypto_major avg `1.1589` n `8`; equity avg `1.5735` n `65`; fx avg `0.0419` n `5`; index avg `0.6521` n `23`; metal avg `-0.2221` n `18`; unknown avg `0.02` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
