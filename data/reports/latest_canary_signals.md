# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T23:52:24.755804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.08` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0233` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `0.037` n `230`; crypto_major avg `0.0585` n `8`; equity avg `0.046` n `92`; fx avg `-0.0087` n `6`; index avg `0.0025` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.1111` n `765`
- 1h: commodity avg `0.0862` n `12`; crypto_alt avg `-0.8899` n `230`; crypto_major avg `-0.8013` n `8`; equity avg `-0.118` n `92`; fx avg `0.0081` n `6`; index avg `-0.073` n `25`; metal avg `-0.016` n `20`; unknown avg `0.4346` n `765`
- 4h: commodity avg `0.335` n `12`; crypto_alt avg `-1.5491` n `230`; crypto_major avg `-1.132` n `8`; equity avg `-0.2029` n `92`; fx avg `0.0157` n `6`; index avg `-0.1087` n `25`; metal avg `-0.0211` n `20`; unknown avg `0.566` n `765`
- 24h: commodity avg `0.3444` n `12`; crypto_alt avg `-0.7736` n `229`; crypto_major avg `-0.4565` n `8`; equity avg `0.0828` n `92`; fx avg `0.0238` n `6`; index avg `-0.0671` n `25`; metal avg `-0.0424` n `20`; unknown avg `2.0051` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
