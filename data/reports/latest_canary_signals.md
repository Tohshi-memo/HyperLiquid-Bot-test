# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T18:22:24.038316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7073` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.008` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0613` n `12`; crypto_alt avg `-0.4718` n `231`; crypto_major avg `-0.4288` n `8`; equity avg `-0.0312` n `127`; fx avg `0.006` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.193` n `793`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `-0.9672` n `231`; crypto_major avg `-0.9923` n `8`; equity avg `0.07` n `127`; fx avg `-0.0072` n `6`; index avg `0.0157` n `26`; metal avg `-0.1386` n `20`; unknown avg `-0.4422` n `793`
- 4h: commodity avg `0.0805` n `12`; crypto_alt avg `-1.9426` n `231`; crypto_major avg `-1.8889` n `8`; equity avg `-1.2716` n `127`; fx avg `0.0014` n `6`; index avg `-0.1816` n `26`; metal avg `-0.5872` n `20`; unknown avg `0.2046` n `793`
- 24h: commodity avg `-0.1977` n `12`; crypto_alt avg `-3.4387` n `231`; crypto_major avg `-3.252` n `8`; equity avg `-1.9209` n `127`; fx avg `-0.1047` n `6`; index avg `-0.0948` n `26`; metal avg `-0.2924` n `20`; unknown avg `-0.4428` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
