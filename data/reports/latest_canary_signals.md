# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T20:22:26.285565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.32` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `-0.0133` n `8`; equity avg `-0.0168` n `92`; fx avg `0.0077` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0173` n `20`; unknown avg `-0.0124` n `768`
- 1h: commodity avg `0.0636` n `12`; crypto_alt avg `-0.2098` n `230`; crypto_major avg `-0.3301` n `8`; equity avg `-0.0037` n `92`; fx avg `0.0036` n `6`; index avg `0.0064` n `25`; metal avg `0.0062` n `20`; unknown avg `0.2311` n `768`
- 4h: commodity avg `0.1261` n `12`; crypto_alt avg `-0.4739` n `230`; crypto_major avg `-0.1096` n `8`; equity avg `0.2005` n `92`; fx avg `-0.0006` n `6`; index avg `0.0438` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0361` n `766`
- 24h: commodity avg `0.3117` n `12`; crypto_alt avg `1.7681` n `230`; crypto_major avg `3.3489` n `8`; equity avg `1.3915` n `92`; fx avg `-0.0047` n `6`; index avg `0.3926` n `25`; metal avg `0.6191` n `20`; unknown avg `0.1472` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
