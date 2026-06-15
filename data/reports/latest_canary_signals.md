# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T11:37:31.872764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.38` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9273` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.099` n `12`; crypto_alt avg `0.0649` n `228`; crypto_major avg `0.1422` n `8`; equity avg `-0.0441` n `74`; fx avg `0.0125` n `6`; index avg `-0.0097` n `23`; metal avg `0.1816` n `18`; unknown avg `0.0132` n `689`
- 1h: commodity avg `0.0887` n `12`; crypto_alt avg `1.242` n `228`; crypto_major avg `1.3743` n `8`; equity avg `0.0851` n `74`; fx avg `0.0019` n `6`; index avg `0.0873` n `23`; metal avg `0.2694` n `18`; unknown avg `0.1146` n `689`
- 4h: commodity avg `0.2347` n `12`; crypto_alt avg `1.5288` n `228`; crypto_major avg `1.9847` n `8`; equity avg `0.0574` n `74`; fx avg `0.0129` n `6`; index avg `0.0997` n `23`; metal avg `0.8738` n `18`; unknown avg `0.9732` n `689`
- 24h: commodity avg `-1.0377` n `12`; crypto_alt avg `4.4623` n `228`; crypto_major avg `4.5795` n `8`; equity avg `1.451` n `74`; fx avg `0.0534` n `6`; index avg `0.9472` n `23`; metal avg `2.7008` n `18`; unknown avg `1.3614` n `529`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
