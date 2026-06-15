# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T12:37:36.745574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.28` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.1479` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5354` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `0.1509` n `228`; crypto_major avg `0.1646` n `8`; equity avg `0.0073` n `74`; fx avg `-0.0111` n `6`; index avg `0.0212` n `23`; metal avg `0.2572` n `18`; unknown avg `0.0475` n `689`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.0233` n `228`; crypto_major avg `0.1529` n `8`; equity avg `-0.1775` n `74`; fx avg `-0.0292` n `6`; index avg `-0.0362` n `23`; metal avg `-0.0359` n `18`; unknown avg `0.0802` n `689`
- 4h: commodity avg `0.2174` n `12`; crypto_alt avg `1.3081` n `228`; crypto_major avg `1.8276` n `8`; equity avg `-0.3203` n `74`; fx avg `0.002` n `6`; index avg `-0.0149` n `23`; metal avg `0.2922` n `18`; unknown avg `0.2484` n `689`
- 24h: commodity avg `-1.0908` n `12`; crypto_alt avg `4.8312` n `228`; crypto_major avg `5.2522` n `8`; equity avg `1.4481` n `74`; fx avg `0.0077` n `6`; index avg `0.8917` n `23`; metal avg `2.6395` n `18`; unknown avg `1.4181` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
