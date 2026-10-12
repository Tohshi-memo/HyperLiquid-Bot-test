# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T13:37:29.120238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0174` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0733` n `13`; crypto_alt avg `-0.0863` n `235`; crypto_major avg `-0.1475` n `8`; equity avg `-0.7293` n `151`; fx avg `0.0085` n `6`; index avg `-0.0495` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.9122` n `1134`
- 1h: commodity avg `0.1526` n `13`; crypto_alt avg `-0.1797` n `235`; crypto_major avg `-0.1361` n `8`; equity avg `-0.679` n `151`; fx avg `0.0203` n `6`; index avg `-0.0401` n `26`; metal avg `0.0318` n `20`; unknown avg `0.4384` n `1132`
- 4h: commodity avg `0.2484` n `13`; crypto_alt avg `-1.2923` n `235`; crypto_major avg `-1.0956` n `8`; equity avg `-0.9831` n `151`; fx avg `-0.0008` n `6`; index avg `-0.0782` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.2521` n `1109`
- 24h: commodity avg `0.2636` n `13`; crypto_alt avg `0.1672` n `235`; crypto_major avg `-0.0522` n `8`; equity avg `-2.1723` n `151`; fx avg `-0.0951` n `6`; index avg `-0.2079` n `26`; metal avg `-0.0453` n `20`; unknown avg `0.1436` n `911`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2335`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
