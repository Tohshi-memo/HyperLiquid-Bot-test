# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T19:22:42.886708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.0166` n `230`; crypto_major avg `0.0218` n `8`; equity avg `-0.0349` n `107`; fx avg `0.0031` n `6`; index avg `0.0161` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0205` n `782`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `0.0597` n `230`; crypto_major avg `-0.0906` n `8`; equity avg `0.0522` n `107`; fx avg `0.0372` n `6`; index avg `0.0321` n `25`; metal avg `-0.0486` n `20`; unknown avg `-0.0417` n `782`
- 4h: commodity avg `-0.1352` n `12`; crypto_alt avg `0.6277` n `230`; crypto_major avg `0.3` n `8`; equity avg `0.8487` n `107`; fx avg `0.0761` n `6`; index avg `0.2535` n `25`; metal avg `0.1096` n `20`; unknown avg `-0.2184` n `782`
- 24h: commodity avg `-1.2198` n `12`; crypto_alt avg `-0.1107` n `230`; crypto_major avg `0.3855` n `8`; equity avg `4.0379` n `107`; fx avg `0.1596` n `6`; index avg `0.8708` n `25`; metal avg `0.9907` n `20`; unknown avg `0.4913` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
