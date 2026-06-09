# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T21:07:28.236507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1309` n `12`; crypto_alt avg `0.1638` n `228`; crypto_major avg `0.1142` n `8`; equity avg `-0.0674` n `74`; fx avg `-0.0146` n `6`; index avg `-0.0328` n `23`; metal avg `0.0336` n `18`; unknown avg `0.0468` n `547`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `0.2729` n `228`; crypto_major avg `0.3176` n `8`; equity avg `-0.0095` n `74`; fx avg `-0.0163` n `6`; index avg `0.2172` n `23`; metal avg `0.0784` n `18`; unknown avg `0.0618` n `547`
- 4h: commodity avg `-0.0273` n `12`; crypto_alt avg `1.5027` n `228`; crypto_major avg `0.9247` n `8`; equity avg `1.995` n `74`; fx avg `-0.0658` n `6`; index avg `1.4828` n `23`; metal avg `0.3458` n `18`; unknown avg `0.5985` n `547`
- 24h: commodity avg `-0.9241` n `12`; crypto_alt avg `-1.8534` n `228`; crypto_major avg `-2.9536` n `8`; equity avg `-1.8157` n `74`; fx avg `-0.0031` n `6`; index avg `-0.8936` n `23`; metal avg `-1.4586` n `18`; unknown avg `-1.0634` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0409`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0406`, n `668`, weak_sample_signal
