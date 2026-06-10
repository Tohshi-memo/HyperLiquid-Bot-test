# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T13:54:42.217546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1502` n `12`; crypto_alt avg `0.0683` n `228`; crypto_major avg `0.0806` n `8`; equity avg `0.6267` n `74`; fx avg `0.0011` n `6`; index avg `0.2613` n `23`; metal avg `0.4319` n `18`; unknown avg `1.2168` n `547`
- 1h: commodity avg `-0.1306` n `12`; crypto_alt avg `1.0364` n `228`; crypto_major avg `1.0607` n `8`; equity avg `1.3848` n `74`; fx avg `0.0473` n `6`; index avg `0.3975` n `23`; metal avg `1.0804` n `18`; unknown avg `1.1229` n `547`
- 4h: commodity avg `0.8079` n `12`; crypto_alt avg `1.73` n `228`; crypto_major avg `1.8597` n `8`; equity avg `2.142` n `74`; fx avg `0.0058` n `6`; index avg `0.7499` n `23`; metal avg `1.2672` n `18`; unknown avg `1.4342` n `547`
- 24h: commodity avg `1.1373` n `12`; crypto_alt avg `-0.4254` n `228`; crypto_major avg `-1.641` n `8`; equity avg `-2.5982` n `74`; fx avg `-0.0268` n `6`; index avg `-1.6823` n `23`; metal avg `-2.4777` n `18`; unknown avg `1.4974` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
