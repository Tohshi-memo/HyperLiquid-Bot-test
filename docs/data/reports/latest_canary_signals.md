# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T19:52:28.922144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `13`; crypto_alt avg `0.0232` n `235`; crypto_major avg `0.0237` n `8`; equity avg `-0.0465` n `151`; fx avg `0.0011` n `6`; index avg `-0.006` n `26`; metal avg `0.0022` n `20`; unknown avg `52.1307` n `1134`
- 1h: commodity avg `-0.079` n `13`; crypto_alt avg `0.3819` n `235`; crypto_major avg `0.4397` n `8`; equity avg `0.2268` n `151`; fx avg `-0.0023` n `6`; index avg `0.0237` n `26`; metal avg `0.0068` n `20`; unknown avg `40.4635` n `1132`
- 4h: commodity avg `-0.0977` n `13`; crypto_alt avg `-0.3104` n `235`; crypto_major avg `-0.3143` n `8`; equity avg `-0.2808` n `151`; fx avg `-0.0096` n `6`; index avg `-0.0471` n `26`; metal avg `-0.0121` n `20`; unknown avg `7.7997` n `1126`
- 24h: commodity avg `0.361` n `13`; crypto_alt avg `-2.8512` n `235`; crypto_major avg `-1.6677` n `8`; equity avg `-3.3829` n `151`; fx avg `-0.1688` n `6`; index avg `-0.3391` n `26`; metal avg `-0.1736` n `20`; unknown avg `5.0622` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2059`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1758`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0965`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0873`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
