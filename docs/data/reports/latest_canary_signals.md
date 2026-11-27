# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T12:52:26.166122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0422` n `13`; crypto_alt avg `-0.0982` n `239`; crypto_major avg `-0.0976` n `8`; equity avg `0.0784` n `168`; fx avg `0.003` n `6`; index avg `0.0105` n `27`; metal avg `-0.0375` n `20`; unknown avg `5.3764` n `1261`
- 1h: commodity avg `-0.1719` n `13`; crypto_alt avg `0.0664` n `239`; crypto_major avg `-0.2042` n `8`; equity avg `0.218` n `168`; fx avg `0.0259` n `6`; index avg `0.0514` n `27`; metal avg `-0.1253` n `20`; unknown avg `1.0127` n `1245`
- 4h: commodity avg `-0.3568` n `13`; crypto_alt avg `-0.0913` n `239`; crypto_major avg `-0.2799` n `8`; equity avg `-0.556` n `168`; fx avg `0.026` n `6`; index avg `-0.0491` n `27`; metal avg `-0.348` n `20`; unknown avg `441.004` n `1231`
- 24h: commodity avg `-0.1562` n `13`; crypto_alt avg `1.7055` n `239`; crypto_major avg `2.3504` n `8`; equity avg `3.2175` n `168`; fx avg `-0.0752` n `6`; index avg `0.2621` n `27`; metal avg `0.9979` n `20`; unknown avg `69.8932` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
