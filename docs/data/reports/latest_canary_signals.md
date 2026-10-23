# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T07:52:28.555481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0577` n `13`; crypto_alt avg `-0.1572` n `237`; crypto_major avg `-0.23` n `8`; equity avg `-0.1946` n `152`; fx avg `-0.0019` n `6`; index avg `-0.0167` n `26`; metal avg `-0.042` n `20`; unknown avg `0.1713` n `1233`
- 1h: commodity avg `0.0643` n `13`; crypto_alt avg `-0.1014` n `237`; crypto_major avg `-0.2344` n `8`; equity avg `-0.2549` n `152`; fx avg `-0.0436` n `6`; index avg `-0.0436` n `26`; metal avg `-0.0608` n `20`; unknown avg `0.7713` n `1231`
- 4h: commodity avg `0.0995` n `13`; crypto_alt avg `0.1254` n `237`; crypto_major avg `-0.0349` n `8`; equity avg `0.9128` n `152`; fx avg `-0.0088` n `6`; index avg `0.033` n `26`; metal avg `-0.0365` n `20`; unknown avg `0.1599` n `1204`
- 24h: commodity avg `0.1755` n `13`; crypto_alt avg `-0.2553` n `237`; crypto_major avg `-0.2774` n `8`; equity avg `-1.1057` n `152`; fx avg `-0.0777` n `6`; index avg `-0.0891` n `26`; metal avg `-0.4471` n `20`; unknown avg `51.8204` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
