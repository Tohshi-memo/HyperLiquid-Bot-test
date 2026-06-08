# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T16:07:29.088637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.948` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.077` n `228`; crypto_major avg `-0.1506` n `8`; equity avg `-0.2014` n `74`; fx avg `-0.0169` n `6`; index avg `-0.1099` n `23`; metal avg `-0.0402` n `18`; unknown avg `0.0069` n `517`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0666` n `228`; crypto_major avg `-0.0174` n `8`; equity avg `-0.3104` n `74`; fx avg `-0.0122` n `6`; index avg `-0.1941` n `23`; metal avg `0.1267` n `18`; unknown avg `0.0066` n `517`
- 4h: commodity avg `0.0716` n `12`; crypto_alt avg `1.2012` n `228`; crypto_major avg `1.7456` n `8`; equity avg `0.915` n `74`; fx avg `-0.0119` n `6`; index avg `0.3224` n `23`; metal avg `-0.2024` n `18`; unknown avg `-1.9453` n `517`
- 24h: commodity avg `-0.5447` n `12`; crypto_alt avg `2.4678` n `228`; crypto_major avg `3.8775` n `8`; equity avg `2.5559` n `74`; fx avg `-0.2742` n `6`; index avg `1.2104` n `23`; metal avg `0.2168` n `18`; unknown avg `-1.2838` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
