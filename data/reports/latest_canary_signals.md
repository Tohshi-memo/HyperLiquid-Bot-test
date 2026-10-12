# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T18:07:26.333679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2286` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0253` n `13`; crypto_alt avg `-0.1364` n `235`; crypto_major avg `-0.0425` n `8`; equity avg `-0.014` n `151`; fx avg `-0.0016` n `6`; index avg `-0.0081` n `26`; metal avg `0.012` n `20`; unknown avg `-0.1856` n `1132`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `-0.0305` n `235`; crypto_major avg `-0.1076` n `8`; equity avg `-0.1043` n `151`; fx avg `-0.0003` n `6`; index avg `-0.0173` n `26`; metal avg `0.0142` n `20`; unknown avg `0.0278` n `1132`
- 4h: commodity avg `0.1421` n `13`; crypto_alt avg `-1.6128` n `235`; crypto_major avg `-1.2507` n `8`; equity avg `-0.5067` n `151`; fx avg `-0.064` n `6`; index avg `-0.0221` n `26`; metal avg `-0.1021` n `20`; unknown avg `0.272` n `1074`
- 24h: commodity avg `0.5193` n `13`; crypto_alt avg `-3.1307` n `235`; crypto_major avg `-2.2853` n `8`; equity avg `-3.4865` n `151`; fx avg `-0.1638` n `6`; index avg `-0.3425` n `26`; metal avg `-0.1548` n `20`; unknown avg `-0.0786` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2103`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1892`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1309`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1255`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0977`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0834`, n `666`, weak_sample_signal
