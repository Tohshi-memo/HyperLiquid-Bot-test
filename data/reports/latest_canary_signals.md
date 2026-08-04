# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T22:52:25.414247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `12`; crypto_alt avg `0.0099` n `230`; crypto_major avg `-0.0334` n `8`; equity avg `-0.0562` n `108`; fx avg `-0.0012` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0221` n `20`; unknown avg `0.0449` n `781`
- 1h: commodity avg `0.0119` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `-0.0336` n `8`; equity avg `0.1166` n `108`; fx avg `-0.0082` n `6`; index avg `-0.0068` n `25`; metal avg `0.0279` n `20`; unknown avg `0.0371` n `781`
- 4h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.0367` n `230`; crypto_major avg `-0.1987` n `8`; equity avg `-0.5006` n `108`; fx avg `0.0156` n `6`; index avg `-0.0544` n `25`; metal avg `-0.0243` n `20`; unknown avg `0.0589` n `781`
- 24h: commodity avg `-1.1584` n `12`; crypto_alt avg `0.1413` n `230`; crypto_major avg `0.6484` n `8`; equity avg `2.9069` n `107`; fx avg `0.1047` n `6`; index avg `0.682` n `25`; metal avg `0.9234` n `20`; unknown avg `0.4431` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
