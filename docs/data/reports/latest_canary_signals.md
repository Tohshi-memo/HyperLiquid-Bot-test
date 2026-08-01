# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T05:52:25.213007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `-0.2774` n `230`; crypto_major avg `-0.218` n `8`; equity avg `0.0358` n `102`; fx avg `-0.011` n `6`; index avg `0.0011` n `25`; metal avg `0.0065` n `20`; unknown avg `0.4061` n `781`
- 1h: commodity avg `-0.0495` n `12`; crypto_alt avg `-0.2418` n `230`; crypto_major avg `-0.3264` n `8`; equity avg `-0.0534` n `102`; fx avg `-0.0019` n `6`; index avg `-0.0484` n `25`; metal avg `0.0202` n `20`; unknown avg `-0.0949` n `781`
- 4h: commodity avg `-0.128` n `12`; crypto_alt avg `-0.0602` n `230`; crypto_major avg `-0.213` n `8`; equity avg `-0.0121` n `102`; fx avg `0.0143` n `6`; index avg `-0.0674` n `25`; metal avg `-0.011` n `20`; unknown avg `0.2324` n `781`
- 24h: commodity avg `1.0092` n `12`; crypto_alt avg `0.1367` n `230`; crypto_major avg `-1.7044` n `8`; equity avg `-2.8413` n `102`; fx avg `-0.1404` n `6`; index avg `-0.3798` n `25`; metal avg `-0.158` n `20`; unknown avg `4.7477` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
