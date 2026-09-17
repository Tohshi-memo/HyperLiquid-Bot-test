# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T17:52:33.601372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0643` n `234`; crypto_major avg `-0.2681` n `8`; equity avg `0.0029` n `138`; fx avg `-0.009` n `6`; index avg `0.0075` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.4339` n `919`
- 1h: commodity avg `0.0404` n `12`; crypto_alt avg `0.2182` n `234`; crypto_major avg `0.106` n `8`; equity avg `-0.1564` n `138`; fx avg `0.0017` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0223` n `20`; unknown avg `0.1128` n `917`
- 4h: commodity avg `0.2783` n `12`; crypto_alt avg `1.1841` n `234`; crypto_major avg `0.377` n `8`; equity avg `-0.0104` n `138`; fx avg `-0.0244` n `6`; index avg `0.0155` n `26`; metal avg `-0.0854` n `20`; unknown avg `2.1953` n `895`
- 24h: commodity avg `0.0539` n `12`; crypto_alt avg `6.108` n `234`; crypto_major avg `3.3832` n `8`; equity avg `1.9904` n `138`; fx avg `0.0552` n `6`; index avg `0.2834` n `26`; metal avg `0.2176` n `20`; unknown avg `0.7821` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
