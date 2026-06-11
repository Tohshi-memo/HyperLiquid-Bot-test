# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T01:37:26.520791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2102` n `12`; crypto_alt avg `0.0197` n `228`; crypto_major avg `-0.0535` n `8`; equity avg `-0.0062` n `74`; fx avg `0.0106` n `6`; index avg `0.006` n `23`; metal avg `0.3322` n `18`; unknown avg `-0.0375` n `550`
- 1h: commodity avg `-0.3463` n `12`; crypto_alt avg `0.7097` n `228`; crypto_major avg `0.6415` n `8`; equity avg `0.9769` n `74`; fx avg `0.0763` n `6`; index avg `0.5548` n `23`; metal avg `1.2925` n `18`; unknown avg `0.2343` n `550`
- 4h: commodity avg `-0.2721` n `12`; crypto_alt avg `1.5706` n `228`; crypto_major avg `1.0125` n `8`; equity avg `0.8778` n `74`; fx avg `0.1022` n `6`; index avg `0.4867` n `23`; metal avg `1.1186` n `18`; unknown avg `0.3592` n `550`
- 24h: commodity avg `1.2988` n `12`; crypto_alt avg `-0.807` n `228`; crypto_major avg `-1.0588` n `8`; equity avg `-1.2172` n `74`; fx avg `0.1128` n `6`; index avg `-1.1478` n `23`; metal avg `-0.6105` n `18`; unknown avg `-0.1168` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
