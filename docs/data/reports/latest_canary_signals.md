# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T00:52:25.985257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `0.0314` n `228`; crypto_major avg `0.001` n `8`; equity avg `-0.2745` n `86`; fx avg `-0.0046` n `6`; index avg `-0.0681` n `23`; metal avg `0.0361` n `20`; unknown avg `-0.0465` n `764`
- 1h: commodity avg `0.0425` n `12`; crypto_alt avg `-0.1785` n `228`; crypto_major avg `-0.1135` n `8`; equity avg `-0.7908` n `86`; fx avg `0.0456` n `6`; index avg `-0.1475` n `23`; metal avg `-0.1626` n `20`; unknown avg `-0.4485` n `764`
- 4h: commodity avg `0.0859` n `12`; crypto_alt avg `0.1918` n `228`; crypto_major avg `0.2147` n `8`; equity avg `-0.2787` n `86`; fx avg `0.044` n `6`; index avg `-0.0747` n `23`; metal avg `-0.0815` n `20`; unknown avg `-1.1603` n `748`
- 24h: commodity avg `-0.3875` n `12`; crypto_alt avg `-2.7339` n `228`; crypto_major avg `-2.2755` n `8`; equity avg `3.6017` n `86`; fx avg `0.0684` n `6`; index avg `0.3354` n `23`; metal avg `-1.6411` n `20`; unknown avg `-1.4573` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
