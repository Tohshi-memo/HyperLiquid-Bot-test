# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T07:52:36.961897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0949` n `12`; crypto_alt avg `-0.0343` n `228`; crypto_major avg `0.0256` n `8`; equity avg `0.0579` n `74`; fx avg `0.0086` n `6`; index avg `0.0088` n `23`; metal avg `0.1176` n `18`; unknown avg `0.0176` n `689`
- 1h: commodity avg `-0.2967` n `12`; crypto_alt avg `-0.2073` n `228`; crypto_major avg `-0.169` n `8`; equity avg `0.0629` n `74`; fx avg `0.0153` n `6`; index avg `0.0346` n `23`; metal avg `0.2214` n `18`; unknown avg `0.3489` n `689`
- 4h: commodity avg `-0.2105` n `12`; crypto_alt avg `0.0201` n `228`; crypto_major avg `-0.2057` n `8`; equity avg `0.047` n `74`; fx avg `0.0324` n `6`; index avg `0.0486` n `23`; metal avg `-0.1417` n `18`; unknown avg `-0.0745` n `529`
- 24h: commodity avg `-0.8978` n `12`; crypto_alt avg `2.9153` n `228`; crypto_major avg `2.8942` n `8`; equity avg `1.8026` n `74`; fx avg `0.0621` n `6`; index avg `0.9753` n `23`; metal avg `1.8774` n `18`; unknown avg `1.5777` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
