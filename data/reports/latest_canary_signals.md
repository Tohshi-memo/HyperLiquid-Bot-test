# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T19:52:26.755279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0549` n `12`; crypto_alt avg `-0.2889` n `228`; crypto_major avg `-0.1847` n `8`; equity avg `-0.2783` n `74`; fx avg `-0.0079` n `6`; index avg `-0.0989` n `23`; metal avg `-0.0592` n `18`; unknown avg `-0.0833` n `424`
- 1h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.4826` n `228`; crypto_major avg `-0.5602` n `8`; equity avg `-0.3969` n `74`; fx avg `-0.033` n `6`; index avg `-0.1034` n `23`; metal avg `-0.0595` n `18`; unknown avg `-0.1441` n `424`
- 4h: commodity avg `0.0461` n `12`; crypto_alt avg `-0.3741` n `228`; crypto_major avg `-0.2268` n `8`; equity avg `0.0348` n `74`; fx avg `-0.0568` n `6`; index avg `0.317` n `23`; metal avg `0.0515` n `18`; unknown avg `0.7097` n `424`
- 24h: commodity avg `-0.6084` n `12`; crypto_alt avg `-4.9028` n `228`; crypto_major avg `-3.2615` n `8`; equity avg `-1.2595` n `73`; fx avg `0.008` n `6`; index avg `-0.0864` n `23`; metal avg `0.7892` n `18`; unknown avg `-0.1149` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
