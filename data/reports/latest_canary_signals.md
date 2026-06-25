# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T01:07:33.325162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0659` n `12`; crypto_alt avg `-0.1014` n `228`; crypto_major avg `-0.2453` n `8`; equity avg `-0.1062` n `86`; fx avg `0.0024` n `6`; index avg `-0.0057` n `23`; metal avg `0.0058` n `20`; unknown avg `0.0417` n `764`
- 1h: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.4189` n `228`; crypto_major avg `-0.473` n `8`; equity avg `-0.6648` n `86`; fx avg `0.0136` n `6`; index avg `-0.0607` n `23`; metal avg `-0.139` n `20`; unknown avg `0.1081` n `764`
- 4h: commodity avg `-0.007` n `12`; crypto_alt avg `0.5231` n `228`; crypto_major avg `0.4939` n `8`; equity avg `-0.2838` n `86`; fx avg `0.0413` n `6`; index avg `-0.0828` n `23`; metal avg `-0.0749` n `20`; unknown avg `-0.9089` n `748`
- 24h: commodity avg `-0.3936` n `12`; crypto_alt avg `-2.5559` n `228`; crypto_major avg `-2.3167` n `8`; equity avg `3.7887` n `86`; fx avg `0.0783` n `6`; index avg `0.363` n `23`; metal avg `-1.4184` n `20`; unknown avg `-1.3215` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
