# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T17:06:14.936920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `13`; crypto_alt avg `-0.1324` n `237`; crypto_major avg `0.0498` n `8`; equity avg `0.0752` n `152`; fx avg `-0.0125` n `6`; index avg `0.0019` n `26`; metal avg `-0.0356` n `20`; unknown avg `-0.1186` n `1231`
- 1h: commodity avg `0.0596` n `13`; crypto_alt avg `-0.1526` n `237`; crypto_major avg `-0.024` n `8`; equity avg `-0.1892` n `152`; fx avg `-0.0083` n `6`; index avg `-0.0631` n `26`; metal avg `-0.0647` n `20`; unknown avg `-0.0906` n `1205`
- 4h: commodity avg `0.23` n `13`; crypto_alt avg `0.1114` n `237`; crypto_major avg `0.2795` n `8`; equity avg `0.5502` n `152`; fx avg `0.0246` n `6`; index avg `0.1088` n `26`; metal avg `-0.0443` n `20`; unknown avg `-0.3349` n `1151`
- 24h: commodity avg `0.381` n `13`; crypto_alt avg `1.4944` n `237`; crypto_major avg `1.3112` n `8`; equity avg `1.5541` n `152`; fx avg `-0.0984` n `6`; index avg `0.0898` n `26`; metal avg `-0.1438` n `20`; unknown avg `-0.5268` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
