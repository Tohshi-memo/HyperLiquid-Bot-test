# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T17:07:28.954382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `13`; crypto_alt avg `-0.0273` n `235`; crypto_major avg `-0.1216` n `8`; equity avg `0.079` n `151`; fx avg `0.0015` n `6`; index avg `0.0028` n `26`; metal avg `0.0374` n `20`; unknown avg `-0.1116` n `1132`
- 1h: commodity avg `-0.0073` n `13`; crypto_alt avg `-0.7579` n `235`; crypto_major avg `-0.6919` n `8`; equity avg `-0.4182` n `151`; fx avg `-0.0061` n `6`; index avg `-0.061` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.292` n `1132`
- 4h: commodity avg `0.2239` n `13`; crypto_alt avg `-1.9391` n `235`; crypto_major avg `-1.074` n `8`; equity avg `-1.855` n `151`; fx avg `-0.0621` n `6`; index avg `-0.1308` n `26`; metal avg `-0.1208` n `20`; unknown avg `-0.3629` n `1074`
- 24h: commodity avg `0.5069` n `13`; crypto_alt avg `-3.1264` n `235`; crypto_major avg `-2.1082` n `8`; equity avg `-3.384` n `151`; fx avg `-0.1711` n `6`; index avg `-0.326` n `26`; metal avg `-0.1824` n `20`; unknown avg `0.0554` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2101`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1943`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1507`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0937`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
