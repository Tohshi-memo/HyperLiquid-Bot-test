# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T13:22:29.809303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `13`; crypto_alt avg `0.491` n `235`; crypto_major avg `0.246` n `8`; equity avg `-0.0032` n `151`; fx avg `0.0205` n `6`; index avg `0.0055` n `26`; metal avg `0.0454` n `20`; unknown avg `4.7522` n `1131`
- 1h: commodity avg `0.2472` n `13`; crypto_alt avg `1.1328` n `235`; crypto_major avg `0.5062` n `8`; equity avg `-0.1567` n `151`; fx avg `0.0334` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0308` n `20`; unknown avg `45.7201` n `1129`
- 4h: commodity avg `0.3783` n `13`; crypto_alt avg `-0.5518` n `235`; crypto_major avg `-0.3146` n `8`; equity avg `-1.0335` n `151`; fx avg `0.0722` n `6`; index avg `-0.1087` n `26`; metal avg `-0.1536` n `20`; unknown avg `0.2476` n `1123`
- 24h: commodity avg `0.1683` n `13`; crypto_alt avg `-3.1157` n `235`; crypto_major avg `-1.5167` n `8`; equity avg `-3.3818` n `151`; fx avg `0.1102` n `6`; index avg `-0.3913` n `26`; metal avg `-0.102` n `20`; unknown avg `0.3124` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1706`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1633`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.151`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1394`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0889`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
