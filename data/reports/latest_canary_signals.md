# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T15:07:34.816667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `-0.3205` n `228`; crypto_major avg `-0.2846` n `8`; equity avg `-0.4284` n `74`; fx avg `-0.0064` n `6`; index avg `-0.1029` n `23`; metal avg `0.0371` n `18`; unknown avg `0.3221` n `424`
- 1h: commodity avg `-0.0727` n `12`; crypto_alt avg `0.0651` n `228`; crypto_major avg `-0.1653` n `8`; equity avg `-0.1339` n `74`; fx avg `-0.0504` n `6`; index avg `-0.1156` n `23`; metal avg `-0.4068` n `18`; unknown avg `0.8315` n `424`
- 4h: commodity avg `-0.7929` n `12`; crypto_alt avg `-1.3459` n `228`; crypto_major avg `-2.0037` n `8`; equity avg `-2.6624` n `74`; fx avg `-0.1327` n `6`; index avg `-1.5093` n `23`; metal avg `-2.4871` n `18`; unknown avg `2.1847` n `424`
- 24h: commodity avg `-1.0102` n `12`; crypto_alt avg `-7.8646` n `228`; crypto_major avg `-6.6253` n `8`; equity avg `-4.2321` n `74`; fx avg `-0.0139` n `6`; index avg `-2.0057` n `23`; metal avg `-3.0219` n `18`; unknown avg `-0.7655` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
