# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T23:22:23.653495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2119` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0231` n `13`; crypto_alt avg `0.3521` n `235`; crypto_major avg `0.1882` n `8`; equity avg `-0.0423` n `151`; fx avg `0.0037` n `6`; index avg `0.0018` n `26`; metal avg `0.0369` n `20`; unknown avg `0.1754` n `1135`
- 1h: commodity avg `0.0044` n `13`; crypto_alt avg `-0.548` n `235`; crypto_major avg `-0.6459` n `8`; equity avg `-0.3125` n `151`; fx avg `-0.0061` n `6`; index avg `-0.0311` n `26`; metal avg `-0.0113` n `20`; unknown avg `1.8338` n `1133`
- 4h: commodity avg `-0.0521` n `13`; crypto_alt avg `-1.6491` n `235`; crypto_major avg `-1.2358` n `8`; equity avg `-0.2605` n `151`; fx avg `-0.0128` n `6`; index avg `-0.0239` n `26`; metal avg `0.0755` n `20`; unknown avg `2.1422` n `1060`
- 24h: commodity avg `0.4242` n `13`; crypto_alt avg `-4.7502` n `235`; crypto_major avg `-3.1286` n `8`; equity avg `-3.8318` n `151`; fx avg `-0.1552` n `6`; index avg `-0.3972` n `26`; metal avg `-0.1247` n `20`; unknown avg `0.0647` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2037`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1773`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `666`, weak_sample_signal
