# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T13:07:27.018968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0772` n `12`; crypto_alt avg `0.0271` n `230`; crypto_major avg `-0.0215` n `8`; equity avg `-0.0386` n `102`; fx avg `0.0182` n `6`; index avg `0.0065` n `25`; metal avg `-0.1067` n `20`; unknown avg `0.0114` n `785`
- 1h: commodity avg `0.0055` n `12`; crypto_alt avg `0.1314` n `230`; crypto_major avg `0.2248` n `8`; equity avg `0.2709` n `102`; fx avg `0.0214` n `6`; index avg `0.05` n `25`; metal avg `-0.2927` n `20`; unknown avg `0.0634` n `785`
- 4h: commodity avg `-0.2281` n `12`; crypto_alt avg `0.2049` n `230`; crypto_major avg `0.217` n `8`; equity avg `-1.1275` n `102`; fx avg `-0.022` n `6`; index avg `-0.1533` n `25`; metal avg `-0.4552` n `20`; unknown avg `0.2762` n `784`
- 24h: commodity avg `-0.4266` n `12`; crypto_alt avg `-0.6707` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `-0.8344` n `102`; fx avg `-0.1741` n `6`; index avg `-0.1797` n `25`; metal avg `-0.5363` n `20`; unknown avg `1.3191` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
