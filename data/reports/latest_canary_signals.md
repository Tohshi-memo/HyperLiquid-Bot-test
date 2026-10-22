# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T18:52:30.551942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0461` n `13`; crypto_alt avg `0.1522` n `237`; crypto_major avg `0.2106` n `8`; equity avg `-0.0052` n `151`; fx avg `-0.0137` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0316` n `20`; unknown avg `0.0018` n `1233`
- 1h: commodity avg `-0.1178` n `13`; crypto_alt avg `-0.0237` n `237`; crypto_major avg `0.1766` n `8`; equity avg `-0.1792` n `151`; fx avg `-0.0183` n `6`; index avg `-0.0323` n `26`; metal avg `-0.0764` n `20`; unknown avg `0.8545` n `1229`
- 4h: commodity avg `0.1471` n `13`; crypto_alt avg `-0.553` n `237`; crypto_major avg `-0.7219` n `8`; equity avg `-1.7` n `151`; fx avg `0.0487` n `6`; index avg `-0.0822` n `26`; metal avg `-0.2656` n `20`; unknown avg `-0.0746` n `1171`
- 24h: commodity avg `0.5932` n `13`; crypto_alt avg `-5.0081` n `237`; crypto_major avg `-3.8361` n `8`; equity avg `-5.3937` n `151`; fx avg `-0.1443` n `6`; index avg `-0.6728` n `26`; metal avg `-1.0131` n `20`; unknown avg `3.7024` n `906`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
