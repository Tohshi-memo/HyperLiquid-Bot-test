# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T14:52:31.970703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.3341` n `228`; crypto_major avg `0.2294` n `8`; equity avg `-0.2338` n `79`; fx avg `-0.0599` n `6`; index avg `-0.0265` n `23`; metal avg `0.0887` n `20`; unknown avg `-0.0356` n `722`
- 1h: commodity avg `0.0698` n `12`; crypto_alt avg `-0.6852` n `228`; crypto_major avg `-0.8821` n `8`; equity avg `-1.1391` n `79`; fx avg `-0.0735` n `6`; index avg `-0.0587` n `23`; metal avg `-0.184` n `20`; unknown avg `0.2978` n `722`
- 4h: commodity avg `-0.388` n `12`; crypto_alt avg `0.6758` n `228`; crypto_major avg `0.6753` n `8`; equity avg `-0.3251` n `79`; fx avg `-0.1006` n `6`; index avg `0.0567` n `23`; metal avg `-0.1171` n `20`; unknown avg `0.5604` n `722`
- 24h: commodity avg `-0.667` n `12`; crypto_alt avg `0.4786` n `228`; crypto_major avg `0.76` n `8`; equity avg `-0.3218` n `79`; fx avg `-0.0053` n `6`; index avg `0.139` n `23`; metal avg `0.4126` n `18`; unknown avg `0.8436` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
