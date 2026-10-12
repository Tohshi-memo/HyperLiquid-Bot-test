# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T18:22:29.474161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0767` n `13`; crypto_alt avg `0.0041` n `235`; crypto_major avg `-0.0435` n `8`; equity avg `0.0088` n `151`; fx avg `0.0045` n `6`; index avg `-0.005` n `26`; metal avg `-0.0025` n `20`; unknown avg `1.2279` n `1134`
- 1h: commodity avg `0.1065` n `13`; crypto_alt avg `0.0682` n `235`; crypto_major avg `-0.1147` n `8`; equity avg `-0.0731` n `151`; fx avg `-0.0074` n `6`; index avg `-0.0229` n `26`; metal avg `0.014` n `20`; unknown avg `-0.4917` n `1132`
- 4h: commodity avg `0.1555` n `13`; crypto_alt avg `-1.1774` n `235`; crypto_major avg `-1.0008` n `8`; equity avg `-0.5085` n `151`; fx avg `-0.0484` n `6`; index avg `-0.0253` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.2126` n `1074`
- 24h: commodity avg `0.585` n `13`; crypto_alt avg `-3.0017` n `235`; crypto_major avg `-2.229` n `8`; equity avg `-3.4693` n `151`; fx avg `-0.1607` n `6`; index avg `-0.3522` n `26`; metal avg `-0.1508` n `20`; unknown avg `-0.1391` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2116`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1869`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1293`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1248`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0993`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0837`, n `666`, weak_sample_signal
