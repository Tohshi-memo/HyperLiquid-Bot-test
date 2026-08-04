# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T18:22:44.214061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `0.0994` n `230`; crypto_major avg `0.1106` n `8`; equity avg `0.1132` n `107`; fx avg `0.0125` n `6`; index avg `0.0262` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.0234` n `782`
- 1h: commodity avg `-0.0597` n `12`; crypto_alt avg `0.2073` n `230`; crypto_major avg `0.1956` n `8`; equity avg `0.2982` n `107`; fx avg `0.0204` n `6`; index avg `0.0978` n `25`; metal avg `-0.0636` n `20`; unknown avg `-0.1146` n `782`
- 4h: commodity avg `-0.1304` n `12`; crypto_alt avg `0.7525` n `230`; crypto_major avg `0.7565` n `8`; equity avg `1.7189` n `107`; fx avg `0.0476` n `6`; index avg `0.3553` n `25`; metal avg `0.2031` n `20`; unknown avg `-0.0545` n `782`
- 24h: commodity avg `-1.1771` n `12`; crypto_alt avg `-0.232` n `230`; crypto_major avg `0.3451` n `8`; equity avg `3.9638` n `107`; fx avg `0.1284` n `6`; index avg `0.8351` n `25`; metal avg `1.1308` n `20`; unknown avg `0.4438` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
