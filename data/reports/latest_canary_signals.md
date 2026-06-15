# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T11:34:41.283862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.39` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9344` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0546` n `12`; crypto_alt avg `0.1118` n `228`; crypto_major avg `0.2197` n `8`; equity avg `0.0277` n `74`; fx avg `0.0145` n `6`; index avg `0.0036` n `23`; metal avg `0.2194` n `18`; unknown avg `0.2277` n `689`
- 1h: commodity avg `0.0443` n `12`; crypto_alt avg `1.2892` n `228`; crypto_major avg `1.4532` n `8`; equity avg `0.157` n `74`; fx avg `0.004` n `6`; index avg `0.1007` n `23`; metal avg `0.3073` n `18`; unknown avg `0.2654` n `689`
- 4h: commodity avg `0.1901` n `12`; crypto_alt avg `1.5753` n `228`; crypto_major avg `2.0635` n `8`; equity avg `0.1291` n `74`; fx avg `0.015` n `6`; index avg `0.113` n `23`; metal avg `0.9119` n `18`; unknown avg `1.0896` n `689`
- 24h: commodity avg `-1.081` n `12`; crypto_alt avg `4.5089` n `228`; crypto_major avg `4.66` n `8`; equity avg `1.5242` n `74`; fx avg `0.0555` n `6`; index avg `0.9608` n `23`; metal avg `2.7398` n `18`; unknown avg `1.4035` n `529`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
