# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T06:37:32.783108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0134` n `230`; crypto_major avg `-0.0463` n `8`; equity avg `-0.0191` n `102`; fx avg `0.0088` n `6`; index avg `0.0058` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0047` n `781`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `-0.1315` n `230`; crypto_major avg `-0.0756` n `8`; equity avg `0.1401` n `102`; fx avg `-0.0037` n `6`; index avg `0.0278` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0158` n `765`
- 4h: commodity avg `-0.0719` n `12`; crypto_alt avg `0.0495` n `230`; crypto_major avg `-0.1668` n `8`; equity avg `0.022` n `102`; fx avg `0.0251` n `6`; index avg `-0.0163` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.0914` n `765`
- 24h: commodity avg `0.9107` n `12`; crypto_alt avg `0.1474` n `230`; crypto_major avg `-1.7605` n `8`; equity avg `-2.157` n `102`; fx avg `0.0062` n `6`; index avg `-0.2538` n `25`; metal avg `-0.2206` n `20`; unknown avg `4.6605` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
