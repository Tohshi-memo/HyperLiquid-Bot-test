# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T04:22:28.644374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0496` n `13`; crypto_alt avg `0.5654` n `239`; crypto_major avg `0.1708` n `8`; equity avg `0.2341` n `168`; fx avg `0.0104` n `6`; index avg `0.0318` n `27`; metal avg `0.1019` n `20`; unknown avg `158.4023` n `1263`
- 1h: commodity avg `0.0253` n `13`; crypto_alt avg `0.2714` n `239`; crypto_major avg `-0.3199` n `8`; equity avg `0.1113` n `168`; fx avg `-0.0227` n `6`; index avg `0.0286` n `27`; metal avg `-0.0438` n `20`; unknown avg `387.8389` n `1253`
- 4h: commodity avg `-0.2154` n `13`; crypto_alt avg `0.436` n `239`; crypto_major avg `-0.6138` n `8`; equity avg `-0.6174` n `168`; fx avg `-0.0755` n `6`; index avg `-0.0416` n `27`; metal avg `0.0103` n `20`; unknown avg `0.4239` n `1227`
- 24h: commodity avg `0.4957` n `13`; crypto_alt avg `-2.7483` n `239`; crypto_major avg `-2.9789` n `8`; equity avg `-4.8826` n `167`; fx avg `0.17` n `6`; index avg `-0.4802` n `27`; metal avg `-0.8882` n `20`; unknown avg `497.0654` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
