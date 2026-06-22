# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T15:52:28.697663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.4425` n `228`; crypto_major avg `-0.4883` n `8`; equity avg `-0.0122` n `85`; fx avg `0.0023` n `6`; index avg `0.0084` n `23`; metal avg `-0.1523` n `20`; unknown avg `0.1671` n `716`
- 1h: commodity avg `-0.1209` n `12`; crypto_alt avg `-0.5417` n `228`; crypto_major avg `-0.6262` n `8`; equity avg `-0.0309` n `85`; fx avg `0.039` n `6`; index avg `-0.0301` n `23`; metal avg `-0.2786` n `20`; unknown avg `0.127` n `716`
- 4h: commodity avg `-0.4156` n `12`; crypto_alt avg `-0.6007` n `228`; crypto_major avg `-0.6604` n `8`; equity avg `-0.5513` n `85`; fx avg `-0.0382` n `6`; index avg `-0.0267` n `23`; metal avg `-0.3203` n `20`; unknown avg `0.301` n `716`
- 24h: commodity avg `-0.7882` n `12`; crypto_alt avg `-0.3268` n `228`; crypto_major avg `-0.09` n `8`; equity avg `-0.4864` n `85`; fx avg `-0.0314` n `6`; index avg `0.1119` n `23`; metal avg `0.0768` n `18`; unknown avg `0.7508` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
