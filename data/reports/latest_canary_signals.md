# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T20:07:29.952958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `0.036` n `228`; crypto_major avg `0.0378` n `8`; equity avg `-0.0091` n `74`; fx avg `0.0024` n `6`; index avg `0.1163` n `23`; metal avg `0.1218` n `18`; unknown avg `-0.0371` n `643`
- 1h: commodity avg `0.0211` n `12`; crypto_alt avg `-0.0833` n `228`; crypto_major avg `-0.2289` n `8`; equity avg `-0.2822` n `74`; fx avg `-0.0242` n `6`; index avg `-0.0552` n `23`; metal avg `-0.0464` n `18`; unknown avg `-0.144` n `643`
- 4h: commodity avg `0.0429` n `12`; crypto_alt avg `-0.1083` n `228`; crypto_major avg `0.0318` n `8`; equity avg `0.4166` n `74`; fx avg `-0.0207` n `6`; index avg `0.2648` n `23`; metal avg `0.4131` n `18`; unknown avg `-0.5019` n `643`
- 24h: commodity avg `-0.4315` n `12`; crypto_alt avg `-0.1725` n `228`; crypto_major avg `0.2965` n `8`; equity avg `-0.391` n `74`; fx avg `0.022` n `6`; index avg `0.4381` n `23`; metal avg `0.3541` n `18`; unknown avg `39.7398` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
