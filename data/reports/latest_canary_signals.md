# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T06:37:30.283141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0443` n `12`; crypto_alt avg `0.0809` n `230`; crypto_major avg `0.0726` n `8`; equity avg `-0.0214` n `92`; fx avg `0.0007` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0219` n `765`
- 1h: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.35` n `230`; crypto_major avg `-0.3261` n `8`; equity avg `-0.1431` n `92`; fx avg `-0.0015` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0109` n `20`; unknown avg `-0.1536` n `749`
- 4h: commodity avg `-0.115` n `12`; crypto_alt avg `-0.3031` n `230`; crypto_major avg `-0.5328` n `8`; equity avg `-0.1597` n `92`; fx avg `-0.0003` n `6`; index avg `-0.0286` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.2771` n `749`
- 24h: commodity avg `0.4373` n `12`; crypto_alt avg `-0.9303` n `230`; crypto_major avg `-0.9954` n `8`; equity avg `-0.1149` n `92`; fx avg `-0.0096` n `6`; index avg `-0.1246` n `25`; metal avg `-0.1012` n `20`; unknown avg `-0.1063` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
