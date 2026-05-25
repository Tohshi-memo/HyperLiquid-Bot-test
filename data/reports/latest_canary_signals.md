# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T08:22:16.848414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.168` n `12`; crypto_alt avg `-0.0771` n `228`; crypto_major avg `-0.061` n `8`; equity avg `-0.0375` n `67`; fx avg `0.0014` n `6`; index avg `0.0155` n `23`; metal avg `-0.0575` n `18`; unknown avg `-0.2238` n `397`
- 1h: commodity avg `-0.0996` n `12`; crypto_alt avg `0.1897` n `228`; crypto_major avg `0.3853` n `8`; equity avg `0.1088` n `67`; fx avg `0.0188` n `6`; index avg `0.065` n `23`; metal avg `0.2019` n `18`; unknown avg `0.0546` n `397`
- 4h: commodity avg `0.403` n `12`; crypto_alt avg `1.1138` n `228`; crypto_major avg `0.9517` n `8`; equity avg `0.0954` n `67`; fx avg `0.0731` n `6`; index avg `-0.005` n `23`; metal avg `-0.0881` n `18`; unknown avg `0.4051` n `387`
- 24h: commodity avg `0.3463` n `12`; crypto_alt avg `0.1779` n `228`; crypto_major avg `0.3117` n `8`; equity avg `0.4561` n `67`; fx avg `0.0101` n `6`; index avg `-0.0794` n `23`; metal avg `0.3607` n `18`; unknown avg `-0.204` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
