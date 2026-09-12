# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T05:22:29.268147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.82` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.035` n `233`; crypto_major avg `0.0158` n `8`; equity avg `-0.0225` n `136`; fx avg `-0.0018` n `6`; index avg `-0.0002` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.1473` n `836`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.1048` n `233`; crypto_major avg `-0.061` n `8`; equity avg `0.0216` n `136`; fx avg `-0.0031` n `6`; index avg `-0.0036` n `26`; metal avg `0.0169` n `20`; unknown avg `-0.1936` n `828`
- 4h: commodity avg `-0.1288` n `12`; crypto_alt avg `-0.0414` n `233`; crypto_major avg `-0.1124` n `8`; equity avg `-0.0625` n `136`; fx avg `-0.0001` n `6`; index avg `-0.012` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.0614` n `814`
- 24h: commodity avg `-0.5773` n `12`; crypto_alt avg `0.7386` n `233`; crypto_major avg `0.8499` n `8`; equity avg `0.8058` n `136`; fx avg `-0.1255` n `6`; index avg `0.2441` n `26`; metal avg `0.1037` n `20`; unknown avg `1.5464` n `690`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
