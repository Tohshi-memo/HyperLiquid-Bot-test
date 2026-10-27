# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T12:52:31.228185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `13`; crypto_alt avg `0.285` n `238`; crypto_major avg `0.2897` n `8`; equity avg `0.1338` n `154`; fx avg `0.0125` n `6`; index avg `0.0284` n `27`; metal avg `0.0074` n `20`; unknown avg `0.3958` n `1238`
- 1h: commodity avg `-0.0517` n `13`; crypto_alt avg `0.8756` n `238`; crypto_major avg `0.8526` n `8`; equity avg `0.3601` n `154`; fx avg `0.0328` n `6`; index avg `0.0693` n `27`; metal avg `0.1` n `20`; unknown avg `0.2996` n `1228`
- 4h: commodity avg `-0.3525` n `13`; crypto_alt avg `0.707` n `238`; crypto_major avg `1.0447` n `8`; equity avg `1.2513` n `154`; fx avg `0.02` n `6`; index avg `0.1694` n `27`; metal avg `0.2454` n `20`; unknown avg `14.6647` n `1182`
- 24h: commodity avg `-0.129` n `13`; crypto_alt avg `0.077` n `237`; crypto_major avg `0.555` n `8`; equity avg `1.1524` n `153`; fx avg `-0.0093` n `6`; index avg `0.3961` n `27`; metal avg `-0.1674` n `20`; unknown avg `1021.4419` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
