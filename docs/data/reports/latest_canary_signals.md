# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T23:37:30.153216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.93` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0692` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.2716` n `230`; crypto_major avg `-0.3086` n `8`; equity avg `-0.0861` n `92`; fx avg `0.0088` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.138` n `765`
- 1h: commodity avg `0.1356` n `12`; crypto_alt avg `-1.0783` n `230`; crypto_major avg `-1.0253` n `8`; equity avg `-0.236` n `92`; fx avg `0.0157` n `6`; index avg `-0.089` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.6423` n `765`
- 4h: commodity avg `0.3158` n `12`; crypto_alt avg `-1.5496` n `230`; crypto_major avg `-1.1781` n `8`; equity avg `-0.2376` n `92`; fx avg `0.026` n `6`; index avg `-0.1089` n `25`; metal avg `-0.0231` n `20`; unknown avg `0.3156` n `765`
- 24h: commodity avg `0.3335` n `12`; crypto_alt avg `-0.877` n `229`; crypto_major avg `-0.5481` n `8`; equity avg `0.0797` n `92`; fx avg `0.0332` n `6`; index avg `-0.07` n `25`; metal avg `-0.0468` n `20`; unknown avg `1.9995` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
