# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T13:52:38.378858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2028` n `13`; crypto_alt avg `-0.4311` n `235`; crypto_major avg `-0.2695` n `8`; equity avg `0.2895` n `151`; fx avg `0.001` n `6`; index avg `0.0253` n `26`; metal avg `-0.1113` n `20`; unknown avg `1.0304` n `1135`
- 1h: commodity avg `0.43` n `13`; crypto_alt avg `0.0645` n `235`; crypto_major avg `0.1033` n `8`; equity avg `0.3489` n `151`; fx avg `0.0232` n `6`; index avg `0.0706` n `26`; metal avg `-0.0849` n `20`; unknown avg `4.8954` n `1125`
- 4h: commodity avg `0.591` n `13`; crypto_alt avg `-0.318` n `235`; crypto_major avg `-0.2344` n `8`; equity avg `-0.4621` n `151`; fx avg `0.0952` n `6`; index avg `-0.0224` n `26`; metal avg `-0.2369` n `20`; unknown avg `0.8137` n `1119`
- 24h: commodity avg `0.2664` n `13`; crypto_alt avg `-3.2166` n `235`; crypto_major avg `-1.486` n `8`; equity avg `-2.1158` n `151`; fx avg `0.113` n `6`; index avg `-0.259` n `26`; metal avg `-0.1544` n `20`; unknown avg `0.0974` n `986`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1676`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1513`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1499`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0866`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
