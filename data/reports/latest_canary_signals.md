# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T03:07:30.153394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `0.0147` n `230`; crypto_major avg `-0.0675` n `8`; equity avg `0.1564` n `108`; fx avg `-0.0229` n `6`; index avg `0.0271` n `25`; metal avg `0.0278` n `20`; unknown avg `0.2861` n `781`
- 1h: commodity avg `-0.1671` n `12`; crypto_alt avg `0.171` n `230`; crypto_major avg `0.0976` n `8`; equity avg `0.0531` n `108`; fx avg `-0.0367` n `6`; index avg `-0.0106` n `25`; metal avg `0.3176` n `20`; unknown avg `-0.1707` n `781`
- 4h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.287` n `230`; crypto_major avg `0.3003` n `8`; equity avg `0.6564` n `108`; fx avg `-0.1146` n `6`; index avg `0.0543` n `25`; metal avg `0.4412` n `20`; unknown avg `-0.3169` n `781`
- 24h: commodity avg `-1.5153` n `12`; crypto_alt avg `0.2982` n `230`; crypto_major avg `0.8332` n `8`; equity avg `4.0731` n `108`; fx avg `-0.0247` n `6`; index avg `0.8527` n `25`; metal avg `1.1232` n `20`; unknown avg `0.4064` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
