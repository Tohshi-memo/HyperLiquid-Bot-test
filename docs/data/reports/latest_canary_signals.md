# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T02:42:01.631296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `0.0473` n `239`; crypto_major avg `-0.0949` n `8`; equity avg `0.1722` n `162`; fx avg `-0.0152` n `6`; index avg `0.0343` n `27`; metal avg `0.0379` n `20`; unknown avg `0.0956` n `1266`
- 1h: commodity avg `-0.0426` n `13`; crypto_alt avg `0.1936` n `239`; crypto_major avg `-0.0933` n `8`; equity avg `0.0314` n `162`; fx avg `-0.01` n `6`; index avg `0.009` n `27`; metal avg `0.1026` n `20`; unknown avg `0.3503` n `1262`
- 4h: commodity avg `-0.1665` n `13`; crypto_alt avg `-0.4527` n `239`; crypto_major avg `-0.7626` n `8`; equity avg `0.1032` n `162`; fx avg `0.0278` n `6`; index avg `0.0251` n `27`; metal avg `0.1845` n `20`; unknown avg `0.5367` n `1226`
- 24h: commodity avg `-1.0298` n `13`; crypto_alt avg `-0.8325` n `239`; crypto_major avg `-0.4373` n `8`; equity avg `-3.3962` n `162`; fx avg `-0.0621` n `6`; index avg `-0.321` n `27`; metal avg `-0.1562` n `20`; unknown avg `560.6351` n `999`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
