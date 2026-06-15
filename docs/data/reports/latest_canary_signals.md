# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T09:22:38.092792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1207` n `12`; crypto_alt avg `0.1628` n `228`; crypto_major avg `0.0762` n `8`; equity avg `-0.1224` n `74`; fx avg `0.0085` n `6`; index avg `-0.0502` n `23`; metal avg `0.0163` n `18`; unknown avg `0.1706` n `689`
- 1h: commodity avg `-0.1999` n `12`; crypto_alt avg `0.2214` n `228`; crypto_major avg `0.2516` n `8`; equity avg `-0.0531` n `74`; fx avg `0.009` n `6`; index avg `-0.0224` n `23`; metal avg `0.353` n `18`; unknown avg `0.2325` n `689`
- 4h: commodity avg `-0.3828` n `12`; crypto_alt avg `0.1361` n `228`; crypto_major avg `0.1224` n `8`; equity avg `0.0203` n `74`; fx avg `0.0055` n `6`; index avg `0.0574` n `23`; metal avg `0.2553` n `18`; unknown avg `1.0237` n `529`
- 24h: commodity avg `-1.0913` n `12`; crypto_alt avg `3.324` n `228`; crypto_major avg `3.3805` n `8`; equity avg `1.7864` n `74`; fx avg `0.0604` n `6`; index avg `0.9592` n `23`; metal avg `2.3746` n `18`; unknown avg `1.7752` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
