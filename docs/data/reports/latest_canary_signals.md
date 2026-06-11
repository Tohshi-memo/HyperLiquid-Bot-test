# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T21:52:37.292690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0828` n `12`; crypto_alt avg `-0.0351` n `228`; crypto_major avg `0.0783` n `8`; equity avg `0.0466` n `74`; fx avg `-0.0005` n `6`; index avg `0.0295` n `23`; metal avg `-0.0214` n `18`; unknown avg `7.1231` n `556`
- 1h: commodity avg `-0.2634` n `12`; crypto_alt avg `0.4307` n `228`; crypto_major avg `0.4513` n `8`; equity avg `0.1768` n `74`; fx avg `0.0222` n `6`; index avg `0.0957` n `23`; metal avg `0.0183` n `18`; unknown avg `0.3604` n `556`
- 4h: commodity avg `-0.6376` n `12`; crypto_alt avg `0.1019` n `228`; crypto_major avg `0.0039` n `8`; equity avg `1.2156` n `74`; fx avg `0.0399` n `6`; index avg `0.6908` n `23`; metal avg `0.8303` n `18`; unknown avg `0.3522` n `556`
- 24h: commodity avg `-2.6919` n `12`; crypto_alt avg `5.5919` n `228`; crypto_major avg `4.9795` n `8`; equity avg `4.2651` n `74`; fx avg `0.0762` n `6`; index avg `2.4262` n `23`; metal avg `3.4913` n `18`; unknown avg `2.4992` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
