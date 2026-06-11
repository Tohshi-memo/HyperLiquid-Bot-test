# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T23:07:28.982575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.1442` n `228`; crypto_major avg `-0.1886` n `8`; equity avg `-0.1493` n `74`; fx avg `0.0222` n `6`; index avg `-0.0657` n `23`; metal avg `-0.0214` n `18`; unknown avg `0.1304` n `556`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.4578` n `228`; crypto_major avg `-0.3373` n `8`; equity avg `0.1212` n `74`; fx avg `0.038` n `6`; index avg `0.1189` n `23`; metal avg `-0.1931` n `18`; unknown avg `0.8779` n `556`
- 4h: commodity avg `-1.0835` n `12`; crypto_alt avg `0.0521` n `228`; crypto_major avg `0.0681` n `8`; equity avg `1.2116` n `74`; fx avg `0.0534` n `6`; index avg `0.662` n `23`; metal avg `0.9797` n `18`; unknown avg `0.6586` n `556`
- 24h: commodity avg `-3.1132` n `12`; crypto_alt avg `4.676` n `228`; crypto_major avg `4.5087` n `8`; equity avg `5.2168` n `74`; fx avg `0.1618` n `6`; index avg `2.8315` n `23`; metal avg `4.4668` n `18`; unknown avg `2.5108` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
