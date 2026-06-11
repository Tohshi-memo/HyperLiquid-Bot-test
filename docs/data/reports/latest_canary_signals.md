# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T11:22:32.078880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1205` n `12`; crypto_alt avg `-0.0305` n `228`; crypto_major avg `0.0093` n `8`; equity avg `-0.0255` n `74`; fx avg `-0.0` n `6`; index avg `-0.0318` n `23`; metal avg `-0.1769` n `18`; unknown avg `0.2419` n `556`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.1685` n `228`; crypto_major avg `0.4075` n `8`; equity avg `-0.2087` n `74`; fx avg `0.0204` n `6`; index avg `-0.0918` n `23`; metal avg `-0.1124` n `18`; unknown avg `-1.4425` n `556`
- 4h: commodity avg `-0.5056` n `12`; crypto_alt avg `0.2513` n `228`; crypto_major avg `0.4781` n `8`; equity avg `0.2545` n `74`; fx avg `-0.0701` n `6`; index avg `0.0634` n `23`; metal avg `-0.5812` n `18`; unknown avg `0.9496` n `556`
- 24h: commodity avg `-0.3548` n `12`; crypto_alt avg `2.1239` n `228`; crypto_major avg `1.937` n `8`; equity avg `0.9411` n `74`; fx avg `0.0213` n `6`; index avg `0.1718` n `23`; metal avg `-0.7398` n `18`; unknown avg `4.4998` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
