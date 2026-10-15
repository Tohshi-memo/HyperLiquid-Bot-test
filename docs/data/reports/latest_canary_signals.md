# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T02:38:00.268445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1665` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0217` n `13`; crypto_alt avg `-0.4325` n `236`; crypto_major avg `0.1236` n `8`; equity avg `-0.196` n `151`; fx avg `0.0066` n `6`; index avg `-0.0591` n `26`; metal avg `-0.0319` n `20`; unknown avg `0.7851` n `1136`
- 1h: commodity avg `-0.0775` n `13`; crypto_alt avg `-2.4664` n `236`; crypto_major avg `-1.2429` n `8`; equity avg `-0.3598` n `151`; fx avg `-0.0196` n `6`; index avg `-0.0764` n `26`; metal avg `-0.0958` n `20`; unknown avg `2.1894` n `1134`
- 4h: commodity avg `-0.2866` n `13`; crypto_alt avg `-2.6857` n `236`; crypto_major avg `-1.05` n `8`; equity avg `-0.6568` n `151`; fx avg `0.227` n `6`; index avg `-0.3228` n `26`; metal avg `0.1327` n `20`; unknown avg `2.8293` n `1128`
- 24h: commodity avg `-0.4867` n `13`; crypto_alt avg `-5.1577` n `236`; crypto_major avg `-3.4146` n `8`; equity avg `-6.1047` n `151`; fx avg `0.0907` n `6`; index avg `-1.0322` n `26`; metal avg `-0.7082` n `20`; unknown avg `1396.1464` n `890`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1228`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1012`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0787`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0755`, n `666`, weak_sample_signal
