# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T02:52:24.043059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0971` n `12`; crypto_alt avg `0.0446` n `230`; crypto_major avg `-0.0288` n `8`; equity avg `-0.0099` n `92`; fx avg `0.0006` n `6`; index avg `0.0037` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0277` n `765`
- 1h: commodity avg `-0.0984` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `-0.0464` n `8`; equity avg `0.006` n `92`; fx avg `-0.001` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.1943` n `765`
- 4h: commodity avg `0.1528` n `12`; crypto_alt avg `-0.6291` n `230`; crypto_major avg `-0.797` n `8`; equity avg `-0.1196` n `92`; fx avg `0.0066` n `6`; index avg `-0.1015` n `25`; metal avg `-0.0497` n `20`; unknown avg `0.3234` n `765`
- 24h: commodity avg `0.4763` n `12`; crypto_alt avg `-0.693` n `229`; crypto_major avg `-0.3809` n `8`; equity avg `0.0568` n `92`; fx avg `0.0199` n `6`; index avg `-0.0917` n `25`; metal avg `-0.0802` n `20`; unknown avg `0.072` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
