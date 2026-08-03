# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T13:37:36.818356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1077` n `12`; crypto_alt avg `-0.0832` n `230`; crypto_major avg `-0.0801` n `8`; equity avg `0.1349` n `102`; fx avg `-0.0342` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0087` n `785`
- 1h: commodity avg `-0.1325` n `12`; crypto_alt avg `0.396` n `230`; crypto_major avg `0.2827` n `8`; equity avg `0.1785` n `102`; fx avg `-0.0415` n `6`; index avg `0.0184` n `25`; metal avg `-0.2151` n `20`; unknown avg `0.0927` n `785`
- 4h: commodity avg `-0.1802` n `12`; crypto_alt avg `0.3866` n `230`; crypto_major avg `0.3214` n `8`; equity avg `-0.7158` n `102`; fx avg `-0.0822` n `6`; index avg `-0.1309` n `25`; metal avg `-0.4563` n `20`; unknown avg `0.3117` n `784`
- 24h: commodity avg `-0.4977` n `12`; crypto_alt avg `-0.1833` n `230`; crypto_major avg `0.2173` n `8`; equity avg `-0.6432` n `102`; fx avg `-0.2169` n `6`; index avg `-0.1753` n `25`; metal avg `-0.6093` n `20`; unknown avg `1.3369` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
