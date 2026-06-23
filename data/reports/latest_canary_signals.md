# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T01:07:27.098608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0434` n `12`; crypto_alt avg `0.1655` n `228`; crypto_major avg `0.0764` n `8`; equity avg `-0.2149` n `86`; fx avg `-0.0198` n `6`; index avg `-0.0246` n `23`; metal avg `-0.0969` n `20`; unknown avg `-0.2312` n `716`
- 1h: commodity avg `-0.0597` n `12`; crypto_alt avg `0.3948` n `228`; crypto_major avg `0.1996` n `8`; equity avg `-0.4807` n `86`; fx avg `-0.0238` n `6`; index avg `-0.1036` n `23`; metal avg `-0.037` n `20`; unknown avg `-0.2773` n `716`
- 4h: commodity avg `-0.069` n `12`; crypto_alt avg `-0.4556` n `228`; crypto_major avg `-0.4234` n `8`; equity avg `-0.9083` n `86`; fx avg `0.0005` n `6`; index avg `-0.1826` n `23`; metal avg `-0.1369` n `20`; unknown avg `-0.5832` n `716`
- 24h: commodity avg `-0.6955` n `12`; crypto_alt avg `-0.7395` n `228`; crypto_major avg `-0.4183` n `8`; equity avg `-1.0938` n `85`; fx avg `0.0216` n `6`; index avg `-0.1256` n `23`; metal avg `-0.6063` n `18`; unknown avg `0.07` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
