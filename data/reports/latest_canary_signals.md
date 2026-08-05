# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T18:07:41.328892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0978` n `12`; crypto_alt avg `-0.0783` n `230`; crypto_major avg `-0.027` n `8`; equity avg `-0.0102` n `108`; fx avg `-0.0003` n `6`; index avg `-0.0051` n `25`; metal avg `0.0403` n `20`; unknown avg `0.0025` n `782`
- 1h: commodity avg `0.0688` n `12`; crypto_alt avg `0.1223` n `230`; crypto_major avg `0.3359` n `8`; equity avg `0.1338` n `108`; fx avg `-0.0009` n `6`; index avg `0.0148` n `25`; metal avg `0.1035` n `20`; unknown avg `-0.1165` n `782`
- 4h: commodity avg `0.1353` n `12`; crypto_alt avg `0.2164` n `230`; crypto_major avg `0.6189` n `8`; equity avg `-0.6956` n `108`; fx avg `-0.0058` n `6`; index avg `-0.1473` n `25`; metal avg `0.1267` n `20`; unknown avg `-0.1124` n `782`
- 24h: commodity avg `-0.0203` n `12`; crypto_alt avg `0.7472` n `230`; crypto_major avg `0.9771` n `8`; equity avg `-0.1641` n `108`; fx avg `-0.0053` n `6`; index avg `-0.0327` n `25`; metal avg `0.7661` n `20`; unknown avg `0.7799` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
