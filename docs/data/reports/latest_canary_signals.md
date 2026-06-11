# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T22:07:30.590333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1451` n `12`; crypto_alt avg `-0.0173` n `228`; crypto_major avg `0.0969` n `8`; equity avg `0.1371` n `74`; fx avg `-0.0099` n `6`; index avg `0.0906` n `23`; metal avg `0.6343` n `18`; unknown avg `-0.0737` n `556`
- 1h: commodity avg `-0.3202` n `12`; crypto_alt avg `0.134` n `228`; crypto_major avg `0.3222` n `8`; equity avg `0.2361` n `74`; fx avg `0.0426` n `6`; index avg `0.167` n `23`; metal avg `0.5833` n `18`; unknown avg `-0.3558` n `556`
- 4h: commodity avg `-0.8904` n `12`; crypto_alt avg `0.3969` n `228`; crypto_major avg `0.5375` n `8`; equity avg `1.5565` n `74`; fx avg `0.0312` n `6`; index avg `0.8347` n `23`; metal avg `2.0223` n `18`; unknown avg `-0.1397` n `556`
- 24h: commodity avg `-2.795` n `12`; crypto_alt avg `5.7882` n `228`; crypto_major avg `5.07` n `8`; equity avg `4.7205` n `74`; fx avg `0.1077` n `6`; index avg `2.6533` n `23`; metal avg `4.5522` n `18`; unknown avg `2.3359` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
