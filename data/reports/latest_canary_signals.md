# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T22:42:07.435827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.0375` n `230`; crypto_major avg `0.0228` n `8`; equity avg `0.0` n `108`; fx avg `0.0007` n `6`; index avg `-0.0028` n `25`; metal avg `0.0158` n `20`; unknown avg `0.0511` n `781`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.001` n `230`; crypto_major avg `-0.0172` n `8`; equity avg `0.1302` n `108`; fx avg `-0.0091` n `6`; index avg `0.0023` n `25`; metal avg `0.0475` n `20`; unknown avg `0.0016` n `781`
- 4h: commodity avg `-0.1267` n `12`; crypto_alt avg `0.0799` n `230`; crypto_major avg `-0.1707` n `8`; equity avg `-0.4092` n `108`; fx avg `0.0239` n `6`; index avg `-0.0428` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.0165` n `781`
- 24h: commodity avg `-1.2413` n `12`; crypto_alt avg `0.1777` n `230`; crypto_major avg `0.7941` n `8`; equity avg `3.0195` n `107`; fx avg `0.1076` n `6`; index avg `0.7067` n `25`; metal avg `0.943` n `20`; unknown avg `0.4162` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
