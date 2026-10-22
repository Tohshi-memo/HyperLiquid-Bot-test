# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T15:37:32.166241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8093` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0308` n `13`; crypto_alt avg `0.137` n `237`; crypto_major avg `0.1221` n `8`; equity avg `-0.7413` n `151`; fx avg `0.002` n `6`; index avg `-0.0314` n `26`; metal avg `-0.0142` n `20`; unknown avg `-0.0678` n `1233`
- 1h: commodity avg `-0.0763` n `13`; crypto_alt avg `-0.4634` n `237`; crypto_major avg `-0.1469` n `8`; equity avg `-0.9679` n `151`; fx avg `0.0175` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0168` n `20`; unknown avg `-0.1738` n `1179`
- 4h: commodity avg `-0.0961` n `13`; crypto_alt avg `-0.9802` n `237`; crypto_major avg `-0.2959` n `8`; equity avg `-2.1052` n `151`; fx avg `0.0389` n `6`; index avg `-0.1451` n `26`; metal avg `-0.0767` n `20`; unknown avg `-0.2014` n `1083`
- 24h: commodity avg `0.3128` n `13`; crypto_alt avg `-4.7075` n `237`; crypto_major avg `-3.384` n `8`; equity avg `-4.4699` n `151`; fx avg `-0.1652` n `6`; index avg `-0.5703` n `26`; metal avg `-0.8509` n `20`; unknown avg `2.133` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
