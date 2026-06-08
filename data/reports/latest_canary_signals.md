# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T16:18:17.528713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1271` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0332` n `12`; crypto_alt avg `0.2726` n `228`; crypto_major avg `0.2058` n `8`; equity avg `0.2071` n `74`; fx avg `-0.002` n `6`; index avg `0.0672` n `23`; metal avg `-0.0681` n `18`; unknown avg `0.03` n `517`
- 1h: commodity avg `-0.0816` n `12`; crypto_alt avg `0.0492` n `228`; crypto_major avg `-0.0607` n `8`; equity avg `-0.049` n `74`; fx avg `-0.0217` n `6`; index avg `-0.0638` n `23`; metal avg `-0.1298` n `18`; unknown avg `0.0579` n `517`
- 4h: commodity avg `0.04` n `12`; crypto_alt avg `1.3228` n `228`; crypto_major avg `1.9292` n `8`; equity avg `1.0212` n `74`; fx avg `0.0017` n `6`; index avg `0.3485` n `23`; metal avg `-0.1979` n `18`; unknown avg `0.6006` n `517`
- 24h: commodity avg `-0.6267` n `12`; crypto_alt avg `2.6524` n `228`; crypto_major avg `3.8313` n `8`; equity avg `2.5559` n `74`; fx avg `-0.2744` n `6`; index avg `1.23` n `23`; metal avg `0.0973` n `18`; unknown avg `-2.989` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
