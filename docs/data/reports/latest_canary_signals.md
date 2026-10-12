# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T19:37:24.970539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `0.2741` n `235`; crypto_major avg `0.2663` n `8`; equity avg `0.1697` n `151`; fx avg `-0.0078` n `6`; index avg `0.0191` n `26`; metal avg `0.024` n `20`; unknown avg `22.2473` n `1134`
- 1h: commodity avg `-0.1125` n `13`; crypto_alt avg `0.3398` n `235`; crypto_major avg `0.4018` n `8`; equity avg `0.1639` n `151`; fx avg `-0.0009` n `6`; index avg `0.0171` n `26`; metal avg `-0.0087` n `20`; unknown avg `14.2269` n `1132`
- 4h: commodity avg `-0.1313` n `13`; crypto_alt avg `-0.4512` n `235`; crypto_major avg `-0.3726` n `8`; equity avg `-0.1246` n `151`; fx avg `-0.0242` n `6`; index avg `-0.0295` n `26`; metal avg `-0.0067` n `20`; unknown avg `8.1904` n `1126`
- 24h: commodity avg `0.3901` n `13`; crypto_alt avg `-2.7996` n `235`; crypto_major avg `-1.7283` n `8`; equity avg `-3.3362` n `151`; fx avg `-0.1691` n `6`; index avg `-0.3345` n `26`; metal avg `-0.1701` n `20`; unknown avg `5.1287` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2084`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1777`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0972`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
