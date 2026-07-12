# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T01:37:29.138426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1945` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1142` n `230`; crypto_major avg `0.1182` n `8`; equity avg `0.0239` n `92`; fx avg `-0.0025` n `6`; index avg `-0.0125` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0304` n `765`
- 1h: commodity avg `-0.0868` n `12`; crypto_alt avg `0.5955` n `230`; crypto_major avg `0.5672` n `8`; equity avg `0.013` n `92`; fx avg `-0.0054` n `6`; index avg `-0.0241` n `25`; metal avg `-0.0049` n `20`; unknown avg `0.2129` n `765`
- 4h: commodity avg `0.4571` n `12`; crypto_alt avg `-1.4032` n `230`; crypto_major avg `-1.321` n `8`; equity avg `-0.2314` n `92`; fx avg `0.009` n `6`; index avg `-0.1265` n `25`; metal avg `-0.0446` n `20`; unknown avg `0.6806` n `765`
- 24h: commodity avg `0.4744` n `12`; crypto_alt avg `-0.8569` n `229`; crypto_major avg `-0.586` n `8`; equity avg `0.039` n `92`; fx avg `0.0214` n `6`; index avg `-0.0977` n `25`; metal avg `-0.0823` n `20`; unknown avg `-0.4295` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
