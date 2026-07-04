# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T22:15:56.588663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.1589` n `229`; crypto_major avg `-0.0224` n `8`; equity avg `-0.0084` n `88`; fx avg `0.0` n `6`; index avg `0.0011` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0318` n `765`
- 1h: commodity avg `0.0265` n `12`; crypto_alt avg `-0.4132` n `229`; crypto_major avg `-0.2014` n `8`; equity avg `0.0004` n `88`; fx avg `0.0012` n `6`; index avg `0.0145` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.3791` n `765`
- 4h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.6547` n `229`; crypto_major avg `-0.4359` n `8`; equity avg `0.083` n `88`; fx avg `-0.0238` n `6`; index avg `0.0233` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.6188` n `765`
- 24h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0892` n `229`; crypto_major avg `0.595` n `8`; equity avg `0.2641` n `88`; fx avg `-0.0256` n `6`; index avg `-0.0002` n `25`; metal avg `0.0955` n `20`; unknown avg `-0.1063` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
