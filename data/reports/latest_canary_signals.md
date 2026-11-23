# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T17:52:34.249338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.9248` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0587` n `13`; crypto_alt avg `-0.3546` n `239`; crypto_major avg `-0.2508` n `8`; equity avg `-0.3397` n `166`; fx avg `-0.0103` n `6`; index avg `-0.0493` n `27`; metal avg `-0.0898` n `20`; unknown avg `159.197` n `1266`
- 1h: commodity avg `0.1936` n `13`; crypto_alt avg `-0.6923` n `239`; crypto_major avg `-0.7143` n `8`; equity avg `-0.1248` n `166`; fx avg `-0.0133` n `6`; index avg `-0.0174` n `27`; metal avg `-0.079` n `20`; unknown avg `0.4784` n `1264`
- 4h: commodity avg `-0.0645` n `13`; crypto_alt avg `1.804` n `239`; crypto_major avg `1.7979` n `8`; equity avg `4.7227` n `166`; fx avg `-0.1274` n `6`; index avg `0.5768` n `27`; metal avg `0.5339` n `20`; unknown avg `9.4677` n `1254`
- 24h: commodity avg `-1.2924` n `13`; crypto_alt avg `2.0754` n `239`; crypto_major avg `2.4693` n `8`; equity avg `5.9813` n `166`; fx avg `-0.0834` n `6`; index avg `0.5348` n `27`; metal avg `0.6317` n `20`; unknown avg `9.3552` n `1057`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
