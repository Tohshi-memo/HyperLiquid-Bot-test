# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T01:20:17.692337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.049` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `-0.0158` n `8`; equity avg `0.0075` n `102`; fx avg `-0.0023` n `6`; index avg `0.0065` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0904` n `781`
- 1h: commodity avg `-0.1278` n `12`; crypto_alt avg `0.2299` n `230`; crypto_major avg `0.1668` n `8`; equity avg `0.0229` n `102`; fx avg `0.0025` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.1225` n `781`
- 4h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.4247` n `230`; crypto_major avg `0.0304` n `8`; equity avg `-0.0691` n `102`; fx avg `-0.0108` n `6`; index avg `-0.0473` n `25`; metal avg `-0.0111` n `20`; unknown avg `2.0665` n `781`
- 24h: commodity avg `0.8558` n `12`; crypto_alt avg `-0.6006` n `230`; crypto_major avg `-2.3413` n `8`; equity avg `-2.8541` n `102`; fx avg `-0.1304` n `6`; index avg `-0.4091` n `25`; metal avg `-0.2529` n `20`; unknown avg `2.6297` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
