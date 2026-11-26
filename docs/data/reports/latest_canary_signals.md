# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T15:37:33.601693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `13`; crypto_alt avg `0.1585` n `239`; crypto_major avg `0.3451` n `8`; equity avg `0.0508` n `168`; fx avg `-0.0007` n `6`; index avg `-0.0007` n `27`; metal avg `0.0249` n `20`; unknown avg `0.8175` n `1267`
- 1h: commodity avg `0.1051` n `13`; crypto_alt avg `-0.6964` n `239`; crypto_major avg `-0.7696` n `8`; equity avg `-0.1297` n `168`; fx avg `-0.0133` n `6`; index avg `-0.0074` n `27`; metal avg `-0.0301` n `20`; unknown avg `0.4684` n `1263`
- 4h: commodity avg `0.054` n `13`; crypto_alt avg `-0.7091` n `239`; crypto_major avg `-0.4878` n `8`; equity avg `-0.023` n `168`; fx avg `0.002` n `6`; index avg `-0.0046` n `27`; metal avg `0.0399` n `20`; unknown avg `0.8762` n `1251`
- 24h: commodity avg `0.2134` n `13`; crypto_alt avg `4.2153` n `239`; crypto_major avg `3.2765` n `8`; equity avg `5.5966` n `168`; fx avg `0.0443` n `6`; index avg `0.5069` n `27`; metal avg `1.3447` n `20`; unknown avg `18.4773` n `1060`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
