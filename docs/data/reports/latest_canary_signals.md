# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T17:07:34.122937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1041` n `12`; crypto_alt avg `-0.0338` n `228`; crypto_major avg `-0.0102` n `8`; equity avg `0.0936` n `74`; fx avg `-0.0112` n `6`; index avg `0.0093` n `23`; metal avg `0.0081` n `18`; unknown avg `-0.0742` n `556`
- 1h: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.6355` n `228`; crypto_major avg `-0.4419` n `8`; equity avg `-0.4164` n `74`; fx avg `-0.0105` n `6`; index avg `-0.2163` n `23`; metal avg `-0.4023` n `18`; unknown avg `-0.628` n `556`
- 4h: commodity avg `-0.4768` n `12`; crypto_alt avg `-0.0496` n `228`; crypto_major avg `-0.2426` n `8`; equity avg `0.1175` n `74`; fx avg `-0.1067` n `6`; index avg `0.0534` n `23`; metal avg `0.1683` n `18`; unknown avg `-0.4244` n `556`
- 24h: commodity avg `-0.8667` n `12`; crypto_alt avg `0.5023` n `228`; crypto_major avg `0.2867` n `8`; equity avg `-0.1223` n `74`; fx avg `-0.0799` n `6`; index avg `0.1354` n `23`; metal avg `-0.7545` n `18`; unknown avg `1.4673` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
