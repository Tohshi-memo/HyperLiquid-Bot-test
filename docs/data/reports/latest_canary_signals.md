# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T00:37:28.898998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `-0.3559` n `230`; crypto_major avg `-0.445` n `8`; equity avg `-0.3544` n `92`; fx avg `0.0222` n `6`; index avg `-0.0624` n `25`; metal avg `-0.0973` n `20`; unknown avg `0.2692` n `766`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `0.6636` n `230`; crypto_major avg `0.63` n `8`; equity avg `-0.1622` n `92`; fx avg `0.0567` n `6`; index avg `-0.0554` n `25`; metal avg `0.0137` n `20`; unknown avg `0.0041` n `766`
- 4h: commodity avg `-0.1717` n `12`; crypto_alt avg `-0.2534` n `230`; crypto_major avg `-0.2121` n `8`; equity avg `-0.5858` n `92`; fx avg `0.023` n `6`; index avg `-0.1433` n `25`; metal avg `-0.2324` n `20`; unknown avg `-0.085` n `765`
- 24h: commodity avg `-0.0524` n `12`; crypto_alt avg `0.3272` n `230`; crypto_major avg `0.9601` n `8`; equity avg `-0.5334` n `92`; fx avg `-0.0055` n `6`; index avg `-0.1247` n `25`; metal avg `-0.2944` n `20`; unknown avg `0.3937` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
