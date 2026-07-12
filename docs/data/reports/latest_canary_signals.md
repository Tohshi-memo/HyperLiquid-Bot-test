# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T02:07:27.651479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0772` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0193` n `230`; crypto_major avg `-0.0756` n `8`; equity avg `0.0024` n `92`; fx avg `0.0007` n `6`; index avg `0.0011` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.1917` n `765`
- 1h: commodity avg `-0.054` n `12`; crypto_alt avg `0.5105` n `230`; crypto_major avg `0.4057` n `8`; equity avg `0.1525` n `92`; fx avg `0.0037` n `6`; index avg `0.0107` n `25`; metal avg `0.0128` n `20`; unknown avg `0.1551` n `765`
- 4h: commodity avg `0.473` n `12`; crypto_alt avg `-1.1468` n `230`; crypto_major avg `-1.1987` n `8`; equity avg `-0.2512` n `92`; fx avg `0.0138` n `6`; index avg `-0.1215` n `25`; metal avg `-0.0405` n `20`; unknown avg `0.6705` n `765`
- 24h: commodity avg `0.5494` n `12`; crypto_alt avg `-0.5999` n `229`; crypto_major avg `-0.207` n `8`; equity avg `0.1518` n `92`; fx avg `0.0208` n `6`; index avg `-0.0681` n `25`; metal avg `-0.0698` n `20`; unknown avg `-0.1894` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
