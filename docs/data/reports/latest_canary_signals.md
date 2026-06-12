# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T15:07:34.843569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6451` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2951` n `12`; crypto_alt avg `0.4504` n `228`; crypto_major avg `0.5943` n `8`; equity avg `0.5591` n `74`; fx avg `-0.0067` n `6`; index avg `0.379` n `23`; metal avg `0.3093` n `18`; unknown avg `-0.1957` n `643`
- 1h: commodity avg `-0.699` n `12`; crypto_alt avg `1.0371` n `228`; crypto_major avg `1.284` n `8`; equity avg `0.5111` n `74`; fx avg `-0.006` n `6`; index avg `0.2864` n `23`; metal avg `0.2028` n `18`; unknown avg `3.2075` n `643`
- 4h: commodity avg `0.5766` n `12`; crypto_alt avg `0.5636` n `228`; crypto_major avg `1.4222` n `8`; equity avg `-0.0455` n `74`; fx avg `-0.028` n `6`; index avg `0.3739` n `23`; metal avg `-0.2229` n `18`; unknown avg `14.955` n `643`
- 24h: commodity avg `-1.7267` n `12`; crypto_alt avg `2.7529` n `228`; crypto_major avg `3.643` n `8`; equity avg `3.0791` n `74`; fx avg `0.0578` n `6`; index avg `2.0987` n `23`; metal avg `2.5903` n `18`; unknown avg `21.8401` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
