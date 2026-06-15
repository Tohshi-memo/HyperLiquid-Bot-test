# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T08:07:28.035522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.62` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.1995` n `228`; crypto_major avg `0.1303` n `8`; equity avg `-0.001` n `74`; fx avg `0.0016` n `6`; index avg `-0.0002` n `23`; metal avg `0.1119` n `18`; unknown avg `0.715` n `689`
- 1h: commodity avg `-0.0736` n `12`; crypto_alt avg `0.1389` n `228`; crypto_major avg `0.038` n `8`; equity avg `0.0767` n `74`; fx avg `0.0205` n `6`; index avg `0.0026` n `23`; metal avg `0.321` n `16`; unknown avg `1.0844` n `674`
- 4h: commodity avg `-0.2318` n `12`; crypto_alt avg `0.2101` n `228`; crypto_major avg `-0.0471` n `8`; equity avg `0.1031` n `74`; fx avg `0.0305` n `6`; index avg `0.1352` n `23`; metal avg `0.0121` n `18`; unknown avg `0.8405` n `529`
- 24h: commodity avg `-0.8574` n `12`; crypto_alt avg `3.1811` n `228`; crypto_major avg `3.1352` n `8`; equity avg `1.7513` n `74`; fx avg `0.0597` n `6`; index avg `0.9771` n `23`; metal avg `1.9765` n `18`; unknown avg `1.764` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
