# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T05:22:28.710914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.1317` n `228`; crypto_major avg `-0.1122` n `8`; equity avg `0.0068` n `74`; fx avg `-0.0171` n `6`; index avg `0.0133` n `23`; metal avg `-0.0388` n `18`; unknown avg `0.0281` n `557`
- 1h: commodity avg `0.1628` n `12`; crypto_alt avg `-0.1924` n `228`; crypto_major avg `-0.2171` n `8`; equity avg `0.0116` n `74`; fx avg `-0.0197` n `6`; index avg `0.0013` n `23`; metal avg `-0.0919` n `18`; unknown avg `-0.2459` n `557`
- 4h: commodity avg `-0.0792` n `12`; crypto_alt avg `0.2579` n `228`; crypto_major avg `0.2369` n `8`; equity avg `0.1196` n `74`; fx avg `0.0482` n `6`; index avg `0.0659` n `23`; metal avg `0.2103` n `18`; unknown avg `2.6168` n `556`
- 24h: commodity avg `-2.1935` n `12`; crypto_alt avg `1.4167` n `228`; crypto_major avg `2.1907` n `8`; equity avg `3.6275` n `74`; fx avg `0.0092` n `6`; index avg `1.9889` n `23`; metal avg `2.9462` n `18`; unknown avg `1.725` n `530`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
