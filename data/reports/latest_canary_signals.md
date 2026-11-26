# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T04:22:26.051147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `0.0347` n `239`; crypto_major avg `0.0297` n `8`; equity avg `-0.0377` n `168`; fx avg `0.0019` n `6`; index avg `0.0154` n `27`; metal avg `0.0366` n `20`; unknown avg `0.038` n `1261`
- 1h: commodity avg `0.048` n `13`; crypto_alt avg `-0.0165` n `239`; crypto_major avg `0.1437` n `8`; equity avg `0.2382` n `168`; fx avg `-0.0296` n `6`; index avg `0.0395` n `27`; metal avg `0.0674` n `20`; unknown avg `4.0683` n `1249`
- 4h: commodity avg `0.1128` n `13`; crypto_alt avg `0.2588` n `239`; crypto_major avg `0.2131` n `8`; equity avg `0.2043` n `168`; fx avg `-0.021` n `6`; index avg `0.0211` n `27`; metal avg `0.2022` n `20`; unknown avg `1.5063` n `1247`
- 24h: commodity avg `0.7312` n `13`; crypto_alt avg `3.3315` n `239`; crypto_major avg `3.0614` n `8`; equity avg `2.2547` n `168`; fx avg `-0.0074` n `6`; index avg `0.1715` n `27`; metal avg `0.5565` n `20`; unknown avg `770.6447` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.205`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
