# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T17:37:38.219860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0339` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `-0.1372` n `235`; crypto_major avg `-0.2699` n `8`; equity avg `-0.1048` n `151`; fx avg `-0.0075` n `6`; index avg `-0.0161` n `26`; metal avg `0.0102` n `20`; unknown avg `-0.1388` n `1134`
- 1h: commodity avg `-0.0206` n `13`; crypto_alt avg `-0.8779` n `235`; crypto_major avg `-0.8185` n `8`; equity avg `-0.2933` n `151`; fx avg `0.0047` n `6`; index avg `-0.048` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.298` n `1132`
- 4h: commodity avg `0.1611` n `13`; crypto_alt avg `-1.7869` n `235`; crypto_major avg `-1.1207` n `8`; equity avg `-1.1405` n `151`; fx avg `-0.0533` n `6`; index avg `-0.0868` n `26`; metal avg `-0.065` n `20`; unknown avg `0.2974` n `1074`
- 24h: commodity avg `0.4927` n `13`; crypto_alt avg `-3.5966` n `235`; crypto_major avg `-2.7916` n `8`; equity avg `-3.5433` n `151`; fx avg `-0.1644` n `6`; index avg `-0.346` n `26`; metal avg `-0.1782` n `20`; unknown avg `0.2059` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2096`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1929`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1431`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1292`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1136`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0947`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.086`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0853`, n `666`, weak_sample_signal
