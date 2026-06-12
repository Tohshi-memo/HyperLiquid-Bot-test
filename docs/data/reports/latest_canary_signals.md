# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T02:52:26.601199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0905` n `12`; crypto_alt avg `-0.114` n `228`; crypto_major avg `0.0342` n `8`; equity avg `0.0903` n `74`; fx avg `0.0008` n `6`; index avg `0.0617` n `23`; metal avg `0.133` n `18`; unknown avg `-0.0609` n `557`
- 1h: commodity avg `-0.0787` n `12`; crypto_alt avg `0.3642` n `228`; crypto_major avg `0.644` n `8`; equity avg `0.1784` n `74`; fx avg `0.0043` n `6`; index avg `0.0595` n `23`; metal avg `0.0986` n `18`; unknown avg `-0.053` n `557`
- 4h: commodity avg `0.4066` n `12`; crypto_alt avg `0.2673` n `228`; crypto_major avg `0.2283` n `8`; equity avg `0.1395` n `74`; fx avg `0.0133` n `6`; index avg `-0.1266` n `23`; metal avg `-0.2538` n `18`; unknown avg `-0.0105` n `556`
- 24h: commodity avg `-2.2989` n `12`; crypto_alt avg `3.3757` n `228`; crypto_major avg `3.5198` n `8`; equity avg `4.4441` n `74`; fx avg `-0.0137` n `6`; index avg `2.2782` n `23`; metal avg `3.6779` n `18`; unknown avg `2.3075` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
