# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T01:07:34.681292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.121` n `13`; crypto_alt avg `-0.0547` n `237`; crypto_major avg `-0.162` n `8`; equity avg `-0.0442` n `151`; fx avg `-0.0224` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0873` n `20`; unknown avg `0.0792` n `1231`
- 1h: commodity avg `0.0703` n `13`; crypto_alt avg `0.1945` n `237`; crypto_major avg `0.097` n `8`; equity avg `0.9066` n `151`; fx avg `-0.045` n `6`; index avg `0.1308` n `26`; metal avg `-0.0457` n `20`; unknown avg `1.1645` n `1231`
- 4h: commodity avg `0.0872` n `13`; crypto_alt avg `0.1247` n `237`; crypto_major avg `0.1121` n `8`; equity avg `0.4975` n `151`; fx avg `-0.0711` n `6`; index avg `0.0475` n `26`; metal avg `-0.0805` n `20`; unknown avg `0.2503` n `1185`
- 24h: commodity avg `0.4651` n `13`; crypto_alt avg `-4.581` n `237`; crypto_major avg `-3.0094` n `8`; equity avg `-4.4568` n `151`; fx avg `-0.2418` n `6`; index avg `-0.5154` n `26`; metal avg `-0.8698` n `20`; unknown avg `53.1116` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
