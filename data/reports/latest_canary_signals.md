# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T21:07:33.667983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `-0.0475` n `230`; crypto_major avg `-0.0792` n `8`; equity avg `0.0851` n `108`; fx avg `0.0125` n `6`; index avg `-0.0046` n `25`; metal avg `0.0075` n `20`; unknown avg `0.2703` n `781`
- 1h: commodity avg `-0.039` n `12`; crypto_alt avg `0.1222` n `230`; crypto_major avg `-0.047` n `8`; equity avg `-0.638` n `108`; fx avg `0.0163` n `6`; index avg `-0.1037` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.2836` n `781`
- 4h: commodity avg `-0.1024` n `12`; crypto_alt avg `0.2819` n `230`; crypto_major avg `-0.0132` n `8`; equity avg `-0.3309` n `108`; fx avg `0.0627` n `6`; index avg `0.0174` n `25`; metal avg `-0.1644` n `20`; unknown avg `-0.1518` n `781`
- 24h: commodity avg `-1.2277` n `12`; crypto_alt avg `-0.011` n `230`; crypto_major avg `0.4604` n `8`; equity avg `3.0869` n `107`; fx avg `0.1379` n `6`; index avg `0.7297` n `25`; metal avg `0.8462` n `20`; unknown avg `0.4412` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
