# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T12:07:40.211516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2417` n `12`; crypto_alt avg `0.2289` n `228`; crypto_major avg `0.193` n `8`; equity avg `-0.0158` n `77`; fx avg `-0.0129` n `6`; index avg `0.005` n `23`; metal avg `0.1119` n `18`; unknown avg `-0.0269` n `687`
- 1h: commodity avg `-0.2262` n `12`; crypto_alt avg `0.0051` n `228`; crypto_major avg `0.0418` n `8`; equity avg `-0.1974` n `77`; fx avg `-0.0291` n `6`; index avg `0.0347` n `23`; metal avg `0.1725` n `18`; unknown avg `-0.0036` n `687`
- 4h: commodity avg `-0.3764` n `12`; crypto_alt avg `0.5136` n `228`; crypto_major avg `0.788` n `8`; equity avg `0.153` n `77`; fx avg `0.0214` n `6`; index avg `0.1819` n `23`; metal avg `0.6341` n `18`; unknown avg `0.248` n `687`
- 24h: commodity avg `-0.3722` n `12`; crypto_alt avg `0.04` n `228`; crypto_major avg `1.8041` n `8`; equity avg `1.6011` n `76`; fx avg `-0.0861` n `6`; index avg `0.4732` n `23`; metal avg `0.0707` n `18`; unknown avg `0.3136` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
