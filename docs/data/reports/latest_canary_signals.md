# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T04:22:32.517893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0808` n `12`; crypto_alt avg `-0.3192` n `228`; crypto_major avg `-0.2479` n `8`; equity avg `0.0328` n `77`; fx avg `-0.0041` n `6`; index avg `0.0419` n `23`; metal avg `-0.0502` n `18`; unknown avg `0.0609` n `687`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.5284` n `228`; crypto_major avg `0.5269` n `8`; equity avg `0.2579` n `77`; fx avg `0.0243` n `6`; index avg `0.0218` n `23`; metal avg `0.2001` n `18`; unknown avg `4.1255` n `687`
- 4h: commodity avg `-0.4351` n `12`; crypto_alt avg `-0.4383` n `228`; crypto_major avg `-0.1272` n `8`; equity avg `0.1949` n `77`; fx avg `-0.0502` n `6`; index avg `0.0483` n `23`; metal avg `0.1217` n `18`; unknown avg `-0.0188` n `671`
- 24h: commodity avg `0.3938` n `12`; crypto_alt avg `0.0388` n `228`; crypto_major avg `1.6977` n `8`; equity avg `1.1368` n `76`; fx avg `-0.0674` n `6`; index avg `0.5479` n `23`; metal avg `-0.2437` n `18`; unknown avg `0.9214` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
