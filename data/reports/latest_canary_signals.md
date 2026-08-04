# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T07:22:51.677654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0698` n `12`; crypto_alt avg `-0.1232` n `230`; crypto_major avg `-0.1289` n `8`; equity avg `0.0382` n `107`; fx avg `0.0065` n `6`; index avg `-0.0023` n `25`; metal avg `0.0427` n `20`; unknown avg `0.3634` n `781`
- 1h: commodity avg `-0.0772` n `12`; crypto_alt avg `-0.5613` n `230`; crypto_major avg `-0.3603` n `8`; equity avg `0.1279` n `107`; fx avg `0.0162` n `6`; index avg `-0.0115` n `25`; metal avg `0.068` n `20`; unknown avg `0.3878` n `781`
- 4h: commodity avg `-0.0406` n `12`; crypto_alt avg `-0.3741` n `230`; crypto_major avg `-0.1706` n `8`; equity avg `1.046` n `107`; fx avg `0.0562` n `6`; index avg `0.1638` n `25`; metal avg `0.1302` n `20`; unknown avg `0.3807` n `765`
- 24h: commodity avg `0.2461` n `12`; crypto_alt avg `0.8845` n `230`; crypto_major avg `1.1798` n `8`; equity avg `2.7552` n `107`; fx avg `0.0645` n `6`; index avg `0.2863` n `25`; metal avg `0.2241` n `20`; unknown avg `0.5907` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
