# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T11:07:33.930712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.039` n `228`; crypto_major avg `-0.0662` n `8`; equity avg `-0.0677` n `78`; fx avg `0.005` n `6`; index avg `0.0088` n `23`; metal avg `-0.0051` n `18`; unknown avg `-0.0233` n `687`
- 1h: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.3037` n `228`; crypto_major avg `-0.2328` n `8`; equity avg `-0.1255` n `78`; fx avg `0.0129` n `6`; index avg `-0.0121` n `23`; metal avg `0.0034` n `18`; unknown avg `-0.2148` n `687`
- 4h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.2574` n `228`; crypto_major avg `0.1642` n `8`; equity avg `-0.1547` n `78`; fx avg `0.0351` n `6`; index avg `-0.0144` n `23`; metal avg `-0.0191` n `18`; unknown avg `-0.158` n `687`
- 24h: commodity avg `0.4709` n `12`; crypto_alt avg `-3.0279` n `228`; crypto_major avg `-3.4006` n `8`; equity avg `1.111` n `78`; fx avg `-0.0759` n `6`; index avg `0.2938` n `23`; metal avg `-4.1056` n `18`; unknown avg `-0.0498` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
