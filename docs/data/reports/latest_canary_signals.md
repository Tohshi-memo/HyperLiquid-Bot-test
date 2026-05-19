# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T23:07:16.748928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.0082` n `228`; crypto_major avg `0.0409` n `8`; equity avg `-0.0375` n `66`; fx avg `0.0026` n `6`; index avg `0.0195` n `23`; metal avg `0.1053` n `18`; unknown avg `0.0151` n `383`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.2812` n `228`; crypto_major avg `-0.0451` n `8`; equity avg `-0.2115` n `66`; fx avg `-0.0064` n `6`; index avg `-0.0196` n `23`; metal avg `0.0671` n `18`; unknown avg `-0.2168` n `383`
- 4h: commodity avg `-0.1075` n `12`; crypto_alt avg `-0.5876` n `228`; crypto_major avg `-0.3974` n `8`; equity avg `-0.3152` n `66`; fx avg `-0.0044` n `6`; index avg `-0.2309` n `23`; metal avg `-0.0628` n `18`; unknown avg `-0.3407` n `383`
- 24h: commodity avg `1.1075` n `12`; crypto_alt avg `-1.4338` n `228`; crypto_major avg `-0.9216` n `8`; equity avg `-0.6025` n `66`; fx avg `0.065` n `6`; index avg `-0.8242` n `23`; metal avg `-3.0983` n `18`; unknown avg `0.833` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
