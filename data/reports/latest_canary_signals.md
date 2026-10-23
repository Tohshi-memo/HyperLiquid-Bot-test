# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T04:37:28.513350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `13`; crypto_alt avg `-0.1305` n `237`; crypto_major avg `0.0034` n `8`; equity avg `0.0227` n `151`; fx avg `0.0007` n `6`; index avg `0.008` n `26`; metal avg `0.0047` n `20`; unknown avg `0.0636` n `1231`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.1906` n `237`; crypto_major avg `-0.0602` n `8`; equity avg `0.0464` n `151`; fx avg `-0.0066` n `6`; index avg `0.018` n `26`; metal avg `-0.1157` n `20`; unknown avg `-0.1625` n `1223`
- 4h: commodity avg `0.1231` n `13`; crypto_alt avg `0.956` n `237`; crypto_major avg `0.5504` n `8`; equity avg `0.9285` n `151`; fx avg `0.061` n `6`; index avg `0.1148` n `26`; metal avg `-0.0609` n `20`; unknown avg `0.1732` n `1221`
- 24h: commodity avg `0.406` n `13`; crypto_alt avg `-1.7171` n `237`; crypto_major avg `-0.99` n `8`; equity avg `-2.5954` n `151`; fx avg `-0.1301` n `6`; index avg `-0.2446` n `26`; metal avg `-0.6074` n `20`; unknown avg `53.3528` n `901`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
