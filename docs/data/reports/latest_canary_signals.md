# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T18:52:26.542866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `13`; crypto_alt avg `0.2539` n `239`; crypto_major avg `-0.0164` n `8`; equity avg `-0.0147` n `166`; fx avg `-0.0064` n `6`; index avg `0.009` n `27`; metal avg `-0.0198` n `20`; unknown avg `2.1663` n `1264`
- 1h: commodity avg `0.0067` n `13`; crypto_alt avg `-0.3418` n `239`; crypto_major avg `-0.1341` n `8`; equity avg `0.0239` n `166`; fx avg `-0.0032` n `6`; index avg `0.0138` n `27`; metal avg `-0.0447` n `20`; unknown avg `42.2479` n `1251`
- 4h: commodity avg `-0.0101` n `13`; crypto_alt avg `-0.1671` n `239`; crypto_major avg `0.1589` n `8`; equity avg `0.1651` n `166`; fx avg `0.0094` n `6`; index avg `0.033` n `27`; metal avg `-0.0079` n `20`; unknown avg `2.5339` n `1229`
- 24h: commodity avg `-0.0647` n `13`; crypto_alt avg `0.5165` n `239`; crypto_major avg `0.8018` n `8`; equity avg `1.006` n `166`; fx avg `-0.0114` n `6`; index avg `0.1728` n `27`; metal avg `-0.0583` n `20`; unknown avg `191.1337` n `1058`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
