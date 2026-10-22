# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T15:52:37.989537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.755` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0095` n `13`; crypto_alt avg `-0.165` n `237`; crypto_major avg `-0.0612` n `8`; equity avg `0.0838` n `151`; fx avg `0.003` n `6`; index avg `0.0196` n `26`; metal avg `0.0004` n `20`; unknown avg `0.307` n `1233`
- 1h: commodity avg `-0.1172` n `13`; crypto_alt avg `-0.4017` n `237`; crypto_major avg `-0.3125` n `8`; equity avg `-0.6363` n `151`; fx avg `0.0308` n `6`; index avg `0.0429` n `26`; metal avg `-0.0983` n `20`; unknown avg `-0.1764` n `1179`
- 4h: commodity avg `-0.1392` n `13`; crypto_alt avg `-1.0438` n `237`; crypto_major avg `-0.244` n `8`; equity avg `-1.999` n `151`; fx avg `0.0571` n `6`; index avg `-0.1207` n `26`; metal avg `-0.0493` n `20`; unknown avg `-0.2888` n `1083`
- 24h: commodity avg `0.3226` n `13`; crypto_alt avg `-4.861` n `237`; crypto_major avg `-3.4428` n `8`; equity avg `-4.3885` n `151`; fx avg `-0.1623` n `6`; index avg `-0.5509` n `26`; metal avg `-0.8504` n `20`; unknown avg `1.8155` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
