# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T08:07:36.439092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `-0.0526` n `228`; crypto_major avg `-0.0957` n `8`; equity avg `0.05` n `74`; fx avg `0.004` n `6`; index avg `-0.0008` n `23`; metal avg `0.0148` n `18`; unknown avg `-0.0015` n `645`
- 1h: commodity avg `-0.2228` n `12`; crypto_alt avg `0.0659` n `228`; crypto_major avg `-0.0481` n `8`; equity avg `0.1406` n `74`; fx avg `0.0` n `6`; index avg `0.0045` n `23`; metal avg `0.0176` n `18`; unknown avg `0.0719` n `645`
- 4h: commodity avg `-0.2982` n `12`; crypto_alt avg `-0.4819` n `228`; crypto_major avg `-0.5749` n `8`; equity avg `0.11` n `74`; fx avg `-0.0113` n `6`; index avg `-0.0164` n `23`; metal avg `0.0272` n `18`; unknown avg `2.7719` n `625`
- 24h: commodity avg `-0.9153` n `12`; crypto_alt avg `0.2194` n `228`; crypto_major avg `0.7632` n `8`; equity avg `0.6807` n `74`; fx avg `-0.02` n `6`; index avg `0.2419` n `23`; metal avg `0.2519` n `18`; unknown avg `-0.6972` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
