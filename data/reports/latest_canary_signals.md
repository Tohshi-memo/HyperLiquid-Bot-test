# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T06:22:29.386313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2124` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `0.5732` n `230`; crypto_major avg `0.5411` n `8`; equity avg `0.0376` n `121`; fx avg `0.0237` n `6`; index avg `-0.0044` n `25`; metal avg `0.0028` n `20`; unknown avg `0.3031` n `794`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `0.0461` n `230`; crypto_major avg `-0.1411` n `8`; equity avg `-0.107` n `121`; fx avg `-0.0076` n `6`; index avg `-0.0295` n `25`; metal avg `-0.0171` n `20`; unknown avg `0.377` n `778`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `-1.3829` n `230`; crypto_major avg `-1.2394` n `8`; equity avg `-0.2644` n `121`; fx avg `0.0047` n `6`; index avg `-0.027` n `25`; metal avg `-0.0272` n `20`; unknown avg `0.3565` n `778`
- 24h: commodity avg `-0.0345` n `12`; crypto_alt avg `-4.0024` n `230`; crypto_major avg `-2.0083` n `8`; equity avg `-0.0689` n `121`; fx avg `0.0965` n `6`; index avg `-0.014` n `25`; metal avg `0.0655` n `20`; unknown avg `3.5633` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
