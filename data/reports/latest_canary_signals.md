# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T13:22:28.329494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0758` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0571` n `13`; crypto_alt avg `-0.1499` n `236`; crypto_major avg `-0.2272` n `8`; equity avg `-0.0617` n `151`; fx avg `-0.0097` n `6`; index avg `-0.0082` n `26`; metal avg `0.0394` n `20`; unknown avg `-0.2261` n `1136`
- 1h: commodity avg `-0.0517` n `13`; crypto_alt avg `-0.5926` n `236`; crypto_major avg `-0.8018` n `8`; equity avg `-0.2645` n `151`; fx avg `-0.0306` n `6`; index avg `-0.0206` n `26`; metal avg `0.0522` n `20`; unknown avg `0.3822` n `1134`
- 4h: commodity avg `-0.0119` n `13`; crypto_alt avg `-1.0325` n `236`; crypto_major avg `-1.129` n `8`; equity avg `-0.7702` n `151`; fx avg `-0.0345` n `6`; index avg `-0.0532` n `26`; metal avg `0.025` n `20`; unknown avg `0.0502` n `1048`
- 24h: commodity avg `-0.2237` n `13`; crypto_alt avg `-3.5134` n `236`; crypto_major avg `-2.9472` n `8`; equity avg `-5.0502` n `151`; fx avg `0.1307` n `6`; index avg `-0.7475` n `26`; metal avg `0.091` n `20`; unknown avg `0.4485` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0898`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0783`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
