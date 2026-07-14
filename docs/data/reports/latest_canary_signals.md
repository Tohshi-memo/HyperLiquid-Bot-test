# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T20:37:28.836446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0457` n `12`; crypto_alt avg `-0.0039` n `230`; crypto_major avg `-0.0082` n `8`; equity avg `0.0464` n `92`; fx avg `-0.0034` n `6`; index avg `0.0019` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.0615` n `768`
- 1h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.0228` n `230`; crypto_major avg `-0.0944` n `8`; equity avg `0.1025` n `92`; fx avg `0.0037` n `6`; index avg `0.0009` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.0325` n `768`
- 4h: commodity avg `0.2249` n `12`; crypto_alt avg `-0.5262` n `230`; crypto_major avg `-0.2201` n `8`; equity avg `0.1838` n `92`; fx avg `-0.0145` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0309` n `20`; unknown avg `0.0831` n `766`
- 24h: commodity avg `0.3582` n `12`; crypto_alt avg `1.727` n `230`; crypto_major avg `3.267` n `8`; equity avg `1.4333` n `92`; fx avg `0.0074` n `6`; index avg `0.4196` n `25`; metal avg `0.5903` n `20`; unknown avg `0.1291` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
